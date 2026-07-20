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
"""

import typing as T
import dataclasses
from pathlib import Path
from functools import cached_property

from .constants import (
    DESCRIPTION_FORBIDDEN_CHARS,
    H1_FORBIDDEN_CHARS,
    MAX_DESCRIPTION_CHARS,
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

    @classmethod
    def from_lines(cls, lines: "list[str]") -> "T.Self":
        """Parse the inner lines of a ``---`` block into the tracked fields.

        ``description`` is the usable value (surrounding quotes stripped, if any);
        ``description_raw`` keeps the value exactly as written, so a check can tell
        whether the standard double-quote wrapping is present.
        """
        description = None
        description_raw = None
        for line in lines:
            if line.startswith(_DESCRIPTION_KEY):
                description_raw = line[len(_DESCRIPTION_KEY) :].strip()
                description = _unquote(description_raw)
                break
        return cls(description=description, description_raw=description_raw)


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
    desc = md.description
    if desc is None:
        raise LintError(
            "The frontmatter has no 'description' key. Add a one-line "
            "'description:' entry."
        )
    raw = md.description_raw or ""
    if not (len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"'):
        raise LintError(
            "The description value must be wrapped in double quotes, like "
            'description: "your text here". The value is one line and never '
            "contains a quote, so wrapping it keeps it unambiguous for YAML "
            "editors."
        )
    if not desc.strip():
        raise LintError("The frontmatter 'description' is empty.")
    if len(desc) > MAX_DESCRIPTION_CHARS:
        raise LintError(
            f"The description is {len(desc)} characters long, over the "
            f"{MAX_DESCRIPTION_CHARS}-character limit. Tighten it to one short line."
        )
    forbidden = _forbidden_in(desc, DESCRIPTION_FORBIDDEN_CHARS)
    if forbidden:
        raise LintError(
            f"The description contains forbidden character(s): {forbidden}. "
            "Quotes and backticks are not allowed, because the description is "
            "embedded verbatim into other strings."
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
