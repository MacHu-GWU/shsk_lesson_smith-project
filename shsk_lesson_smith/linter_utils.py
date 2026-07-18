# -*- coding: utf-8 -*-

"""Repo-agnostic, single-file lint utilities.

Nothing here knows about repo types or directory layout. There are two kinds of
building block:

- :class:`MarkdownFile`: turn a path into a parsed document (frontmatter split
  from body, with convenient accessors for the description and H1 title).
- ``check_*`` functions: each inspects one thing and either returns quietly or
  raises :class:`LintError` with a friendly message.

The repo-aware linters in ``linter.py`` compose these into full lint runs.
"""

import dataclasses
from pathlib import Path

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
class MarkdownFile:
    """A parsed markdown file: raw text split into frontmatter and body.

    Build one with :meth:`from_path` (the file must already exist; use
    :func:`check_file_exists` first when existence is itself in question).
    """

    path: Path
    text: str
    frontmatter_lines: "list[str] | None"
    body: str

    @classmethod
    def from_path(cls, path: "Path | str") -> "MarkdownFile":
        """Read and parse the markdown file at ``path``."""
        path = Path(path)
        text = path.read_text(encoding="utf-8")
        frontmatter_lines, body = _split_frontmatter(text)
        return cls(
            path=path,
            text=text,
            frontmatter_lines=frontmatter_lines,
            body=body,
        )

    @property
    def has_frontmatter(self) -> bool:
        """Whether the file opens with a well-formed ``---`` frontmatter block."""
        return self.frontmatter_lines is not None

    @property
    def description(self) -> "str | None":
        """The one-line ``description`` value from the frontmatter, if present."""
        if not self.frontmatter_lines:
            return None
        for line in self.frontmatter_lines:
            if line.startswith(_DESCRIPTION_KEY):
                return _unquote(line[len(_DESCRIPTION_KEY) :].strip())
        return None

    @property
    def h1_titles(self) -> "list[str]":
        """Every H1 title in the body (text of each line starting with ``# ``)."""
        return [
            line[2:].strip()
            for line in self.body.splitlines()
            if line.startswith("# ")
        ]

    @property
    def h1(self) -> "str | None":
        """The first H1 title, or None when the document has none."""
        titles = self.h1_titles
        return titles[0] if titles else None


# --------------------------------------------------------------------------- #
# Check functions. Each raises LintError with a friendly message on failure.
# --------------------------------------------------------------------------- #
def check_file_exists(path: "Path | str") -> None:
    """The file must exist on disk."""
    path = Path(path)
    if not path.exists():
        raise LintError(f"File is missing: expected it to exist at {path}.")


def check_description(md: MarkdownFile) -> None:
    """The file must carry a valid one-line frontmatter ``description``.

    Valid means: frontmatter is present, has a non-empty ``description`` key,
    within the character limit, and free of quote / backtick characters.
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


def check_h1(md: MarkdownFile) -> None:
    """The file must have exactly one H1 that uses only the allowed charset.

    Allowed: letters, digits, text, and the punctuation , : . Banned: dashes,
    quotes, brackets, and emoji. (README-ORIGINAL is exempt; use
    :func:`check_h1_matches` for it instead.)
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
    """The file's H1 must exactly equal ``expected`` (used for README-ORIGINAL)."""
    title = md.h1
    if title is None:
        raise LintError(
            "The document has no H1 title, but it must exactly match the repo "
            f"name {expected!r}."
        )
    if title != expected:
        raise LintError(
            f"The H1 title is {title!r}, but it must exactly match the repo "
            f"name {expected!r}."
        )
