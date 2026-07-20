# -*- coding: utf-8 -*-

"""Repo-agnostic, single-file lint utilities.

Nothing here knows about repo types or directory layout. There are two kinds of
building block:

- :class:`MarkdownFile`: turn a path into a parsed document. It stores only the
  ``path``; the raw ``text`` and everything derived from it (the frontmatter,
  the body, the H1 titles) is a lazily computed, cached property.
- ``check_*`` functions: each inspects one thing and either returns quietly or
  raises :class:`LintError` with a friendly message.

The repo-aware linters in ``linter.py`` compose these into full lint runs.

Spec source of truth: the constraints these primitives enforce (frontmatter
description, H1 charset, and so on) are defined in the top-level spec files under
``.claude/skills/lesson-smith/skills/lesson-smith/ref/*.md`` (that directory's own
``.md`` files, not its subfolders). Those specs are authoritative; when they
change, update these checks to match, and when adding a check, anchor it to the
spec clause it enforces.
"""

import re
import typing as T
import dataclasses
from pathlib import Path
from functools import cached_property

from .constants import (
    DESCRIPTION_FORBIDDEN_CHARS,
    H1_FORBIDDEN_CHARS,
    MAX_DESCRIPTION_CHARS,
    MAX_GITHUB_ABOUT_CHARS,
)
from .exc import LintError

# Unicode ranges covering the common emoji / pictograph blocks. Kept
# deliberately narrow (no arrows, no lone symbols like the trademark sign) so
# ordinary punctuation is never flagged as an emoji.
_EMOJI_RANGES = (
    (0x1F300, 0x1FAFF),  # symbols & pictographs, emoticons, transport, faces
    (0x1F000, 0x1F0FF),  # mahjong / dominoes / playing cards
    (0x2600, 0x26FF),  # miscellaneous symbols
    (0x2700, 0x27BF),  # dingbats (checkmarks, scissors, ...)
    (0xFE00, 0xFE0F),  # variation selectors (emoji presentation)
)

_FRONTMATTER_FENCE = "---"
_DESCRIPTION_KEY = "description:"
_GITHUB_ABOUT_KEY = "github_about:"

# Inline markdown link target: the "..." in [text](...). A target is allowed in a
# TICKET only when it is an absolute URL or an in-page anchor; anything else is a
# relative path, which does not resolve once the TICKET is pasted into an Issue.
_MD_LINK_TARGET = re.compile(r"\]\(\s*([^)]+?)\s*\)")
_ALLOWED_LINK_TARGET = re.compile(r"^(?:https?://|mailto:|#)", re.IGNORECASE)


def find_emoji(text: str) -> "str | None":
    """Return the first emoji-like character in ``text``, or None if there is none."""
    for char in text:
        code = ord(char)
        for low, high in _EMOJI_RANGES:
            if low <= code <= high:
                return char
    return None


def _split_frontmatter(text: str) -> "tuple[list[str] | None, str]":
    """Split raw markdown into (frontmatter_lines, body).

    Returns ``(None, text)`` when there is no well-formed ``---`` frontmatter
    block at the very top; otherwise the frontmatter's inner lines and the body
    that follows the closing fence.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != _FRONTMATTER_FENCE:
        return None, text
    for index in range(1, len(lines)):
        if lines[index].strip() == _FRONTMATTER_FENCE:
            return lines[1:index], "\n".join(lines[index + 1 :])
    # Opening fence but no closing fence: not a valid frontmatter block.
    return None, text


def _unquote(value: str) -> str:
    """Strip a single pair of matching surrounding quotes, if present."""
    if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
        return value[1:-1]
    return value


def _forbidden_in(text: str, forbidden_chars: str) -> str:
    """Space-joined, de-duplicated, sorted list of forbidden chars found in text."""
    return " ".join(sorted({char for char in text if char in forbidden_chars}))


@dataclasses.dataclass
class Frontmatter:
    """The frontmatter key-value pairs lesson-smith actually cares about.

    A dedicated dataclass rather than a raw dict: only the keys the standard
    uses become typed fields, so callers get autocomplete and a clear contract,
    and adding a new tracked key is a one-line change here. An instance always
    means "a frontmatter block was present"; a missing block is modeled as
    :attr:`MarkdownFile.frontmatter` being None.
    """

    description: "str | None" = None
    description_raw: "str | None" = None
    github_about: "str | None" = None
    github_about_raw: "str | None" = None

    @classmethod
    def from_lines(cls, lines: "list[str]") -> "T.Self":
        """Parse the inner lines of a ``---`` block into the tracked fields.

        For each tracked key the ``*_raw`` field keeps the value exactly as
        written, while the plain field is the usable value (surrounding quotes
        stripped, if any), so a check can tell whether the standard double-quote
        wrapping is present.
        """
        fields: "dict[str, str]" = {}
        for line in lines:
            if line.startswith(_DESCRIPTION_KEY):
                fields.setdefault("description", line[len(_DESCRIPTION_KEY) :].strip())
            elif line.startswith(_GITHUB_ABOUT_KEY):
                fields.setdefault(
                    "github_about", line[len(_GITHUB_ABOUT_KEY) :].strip()
                )
        desc_raw = fields.get("description")
        about_raw = fields.get("github_about")
        return cls(
            description=None if desc_raw is None else _unquote(desc_raw),
            description_raw=desc_raw,
            github_about=None if about_raw is None else _unquote(about_raw),
            github_about_raw=about_raw,
        )


@dataclasses.dataclass
class MarkdownFile:
    """A parsed markdown file. Stores only ``path``.

    Build one with :meth:`from_path` or directly from a path. Nothing is read
    from disk until a derived view is accessed: ``text`` reads the file on first
    access, and everything else (frontmatter, body, H1 titles) is a cached
    property on top of it, so a file is read and parsed at most once. Use
    :func:`check_file_exists` first when the file's existence is itself in
    question, since accessing ``text`` on a missing file raises.
    """

    path: Path

    def __post_init__(self):
        self.path = Path(self.path)

    @classmethod
    def from_path(cls, path: "Path | str") -> "T.Self":
        """Wrap ``path`` in a :class:`MarkdownFile` (contents read lazily)."""
        return cls(path=Path(path))

    @cached_property
    def text(self) -> str:
        """Raw file contents, read from ``path`` on first access."""
        return self.path.read_text(encoding="utf-8")

    @cached_property
    def _frontmatter_lines_and_body(self) -> "tuple[list[str] | None, str]":
        return _split_frontmatter(self.text)

    @cached_property
    def frontmatter(self) -> "Frontmatter | None":
        """Parsed frontmatter, or None when the file has no ``---`` block."""
        lines, _ = self._frontmatter_lines_and_body
        if lines is None:
            return None
        return Frontmatter.from_lines(lines)

    @cached_property
    def body(self) -> str:
        """Everything after the frontmatter block (the whole text if none)."""
        _, body = self._frontmatter_lines_and_body
        return body

    @property
    def has_frontmatter(self) -> bool:
        """Whether the file opens with a well-formed ``---`` frontmatter block."""
        return self.frontmatter is not None

    @cached_property
    def description(self) -> "str | None":
        """The one-line ``description`` value from the frontmatter, if present.

        Surrounding quotes are stripped, so this is the usable value that flows
        into the SYLLABUS and index.
        """
        return self.frontmatter.description if self.frontmatter else None

    @cached_property
    def description_raw(self) -> "str | None":
        """The ``description`` value exactly as written (quotes not stripped)."""
        return self.frontmatter.description_raw if self.frontmatter else None

    @cached_property
    def github_about(self) -> "str | None":
        """The ``github_about`` value (surrounding quotes stripped), if present."""
        return self.frontmatter.github_about if self.frontmatter else None

    @cached_property
    def github_about_raw(self) -> "str | None":
        """The ``github_about`` value exactly as written (quotes not stripped)."""
        return self.frontmatter.github_about_raw if self.frontmatter else None

    @cached_property
    def h1_titles(self) -> "list[str]":
        """Every H1 title in the body (text of each line starting with ``# ``).

        A well-formed document has exactly one; the full list is kept so
        :func:`check_h1_charset` can flag documents that have none or several.
        """
        return [
            line[2:].strip()
            for line in self.body.splitlines()
            if line.startswith("# ")
        ]

    @cached_property
    def h1(self) -> "str | None":
        """The first H1 title, or None when the document has none."""
        return self.h1_titles[0] if self.h1_titles else None


# --------------------------------------------------------------------------- #
# Check functions. Each raises LintError with a friendly message on failure.
# --------------------------------------------------------------------------- #
def check_file_exists(path: "Path | str") -> None:
    """The file must exist on disk."""
    path = Path(path)
    if not path.exists():
        raise LintError(f"File is missing: expected it to exist at {path}.")


def _validate_quoted_oneliner(
    raw: "str | None", value: "str | None", *, field: str, max_chars: int
) -> None:
    """Shared rules for a one-line frontmatter field (description, github_about).

    ``value`` is the usable (unquoted) value and ``raw`` the value as written.
    The field must be present, wrapped in double quotes, non-empty, within
    ``max_chars``, and free of quote / backtick characters inside the quotes.
    Presence of the frontmatter block itself is the caller's responsibility.
    """
    if value is None:
        raise LintError(
            f"The frontmatter has no '{field}' key. Add a one-line "
            f"'{field}:' entry."
        )
    text = raw or ""
    if not (len(text) >= 2 and text[0] == '"' and text[-1] == '"'):
        raise LintError(
            f"The {field} value must be wrapped in double quotes, like "
            f'{field}: "your text here". The value is one line and never '
            "contains a quote, so wrapping it keeps it unambiguous for YAML "
            "editors."
        )
    if not value.strip():
        raise LintError(f"The frontmatter '{field}' is empty.")
    if len(value) > max_chars:
        raise LintError(
            f"The {field} is {len(value)} characters long, over the "
            f"{max_chars}-character limit. Tighten it to one short line."
        )
    forbidden = _forbidden_in(value, DESCRIPTION_FORBIDDEN_CHARS)
    if forbidden:
        raise LintError(
            f"The {field} contains forbidden character(s): {forbidden}. "
            f"Quotes and backticks are not allowed, because the {field} is "
            "embedded verbatim into other strings."
        )


def check_frontmatter_description(md: MarkdownFile) -> None:
    """The markdown file's frontmatter ``description`` field must be valid.

    Valid means: frontmatter is present, has a ``description`` key whose value is
    wrapped in double quotes, non-empty, within the character limit, and free of
    quote / backtick characters inside the quotes.
    """
    if not md.has_frontmatter:
        raise LintError(
            "The file has no YAML frontmatter, so it is missing the required "
            "one-line 'description'. Add a '---' block at the top with a "
            "'description:' entry."
        )
    _validate_quoted_oneliner(
        md.description_raw, md.description,
        field="description", max_chars=MAX_DESCRIPTION_CHARS,
    )


def check_frontmatter_github_about(md: MarkdownFile) -> None:
    """The frontmatter ``github_about`` field must be valid (README-ORIGINAL only).

    A compressed tagline that also fits GitHub's About box: same wrapping and
    charset rules as ``description``, but capped at ``MAX_GITHUB_ABOUT_CHARS``.
    """
    if not md.has_frontmatter:
        raise LintError(
            "The file has no YAML frontmatter, so it is missing the required "
            "'github_about' tagline. Add a '---' block at the top with a "
            "'github_about:' entry."
        )
    _validate_quoted_oneliner(
        md.github_about_raw, md.github_about,
        field="github_about", max_chars=MAX_GITHUB_ABOUT_CHARS,
    )


def check_h1_charset(md: MarkdownFile) -> None:
    """The markdown H1 title must use only the allowed character set.

    The file must have exactly one H1, and that title may use only letters,
    digits, text, and the punctuation , : . Banned: dashes, quotes, brackets,
    and emoji. (README-ORIGINAL is exempt; use :func:`check_h1_matches` for it
    instead.)
    """
    titles = md.h1_titles
    if not titles:
        raise LintError(
            "The document has no H1 title (a line starting with '# ')."
        )
    if len(titles) > 1:
        raise LintError(
            f"The document has {len(titles)} H1 titles, but exactly one is allowed."
        )
    title = titles[0]
    forbidden = _forbidden_in(title, H1_FORBIDDEN_CHARS)
    if forbidden:
        raise LintError(
            f"The H1 title {title!r} contains forbidden character(s): {forbidden}. "
            "An H1 may use only letters, digits, text, and the punctuation , : ."
        )
    emoji = find_emoji(title)
    if emoji is not None:
        raise LintError(
            f"The H1 title {title!r} contains an emoji ({emoji}). "
            "Emoji are not allowed in an H1 title."
        )


def check_h1_matches(md: MarkdownFile, expected: str) -> None:
    """The file's H1 must exactly equal ``expected``.

    Used where the title is fixed by convention: README-ORIGINAL (the repo name)
    and SYLLABUS (the literal ``Syllabus``).
    """
    title = md.h1
    if title is None:
        raise LintError(
            f"The document has no H1 title, but it must be exactly {expected!r}."
        )
    if title != expected:
        raise LintError(
            f"The H1 title is {title!r}, but it must be exactly {expected!r}."
        )


def check_no_relative_links(md: MarkdownFile) -> None:
    """The markdown body must not contain relative-path links.

    Used for TICKET files: a TICKET body is embedded verbatim into a GitHub Issue,
    where relative links do not resolve. Absolute ``http(s)://`` / ``mailto:`` URLs
    and in-page ``#anchor`` links are fine; a link whose target is anything else
    (``./x``, ``../x``, ``x/y.md``) is a relative path and is flagged.
    """
    relative = []
    for target in _MD_LINK_TARGET.findall(md.body):
        cleaned = target.strip()
        if cleaned.startswith("<") and cleaned.endswith(">"):
            cleaned = cleaned[1:-1].strip()
        if not _ALLOWED_LINK_TARGET.match(cleaned):
            relative.append(target.strip())
    if relative:
        joined = ", ".join(relative)
        raise LintError(
            f"The TICKET body has relative-path link(s): {joined}. A TICKET is "
            "embedded into a GitHub Issue, where relative links do not resolve. "
            "Refer to files in plain text, or use an absolute http(s):// URL."
        )
