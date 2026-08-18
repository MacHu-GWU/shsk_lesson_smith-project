# -*- coding: utf-8 -*-

"""Shared constants and enums for the lesson-smith teaching repo standard.

This is the bottom of the dependency stack: it imports nothing from the rest of
the package, so every other module can safely import from here.
"""

import enum
import re


class LangEnum(str, enum.Enum):
    """Non-English language codes that have a translated variant of each special file.

    English is the default language: its files carry no suffix (``README.md``).
    Every other language gets a ``-<lang>`` suffix (``README-cn.md``).
    """

    cn = "cn"


class RepoTypeEnum(str, enum.Enum):
    """The four kinds of teaching repositories, declared in ``lm.json``."""

    evolve = "evolve"
    showcase = "showcase"
    upskill = "upskill"
    readup = "readup"


# --------------------------------------------------------------------------- #
# Special file base names (the "name body", before the -<lang> suffix and .md).
# Spelled out one per constant so references read clearly and typos surface as
# NameError instead of silent string mismatches.
# --------------------------------------------------------------------------- #
README_BASE = "README"
TICKET_BASE = "TICKET"
README_ORIGINAL_BASE = "README-ORIGINAL"
SYLLABUS_BASE = "SYLLABUS"

# Per-task special files (snapshotted into docs/tasks/<branch>/ for evolve
# repos, or living in examples/NN-title/ for showcase / upskill repos).
TASK_FILE_BASES = (README_BASE, TICKET_BASE)

# Repo-level special files that live at the project root.
REPO_FILE_BASES = (README_BASE, TICKET_BASE, README_ORIGINAL_BASE)


# --------------------------------------------------------------------------- #
# Frontmatter description constraints.
# One line, capped length, no quote-like characters (the description is embedded
# verbatim into other strings, so quotes and backticks would need escaping).
#
# The length cap is per language, because a character carries very different
# amounts of information depending on the script. 400 characters of Chinese
# rewritten into English lands somewhere around 700 to 900 characters, so a
# single global cap would either fail every English variant or force the Chinese
# ones to stay far under-used. The English text is a rewrite of the Chinese, not
# a compression of it, and the budget has to say so.
# --------------------------------------------------------------------------- #
DEFAULT_MAX_DESCRIPTION_CHARS = 800
MAX_DESCRIPTION_CHARS_BY_LANG = {LangEnum.cn: 400}

# The README-ORIGINAL-only ``github_about`` field: a compressed tagline that also
# fits GitHub's About box. Its cap is not a style budget like the description's,
# it is an external limit: GitHub truncates that box around 350 characters
# whatever the script. So English gets modest headroom here rather than the
# doubling the description gets.
DEFAULT_MAX_GITHUB_ABOUT_CHARS = 300
MAX_GITHUB_ABOUT_CHARS_BY_LANG = {LangEnum.cn: 150}


def lang_from_filename(name: str) -> "LangEnum | None":
    """The language a special file's name declares. ``None`` means English.

    English variants carry no suffix (``README.md``, ``README-ORIGINAL.md``);
    every other language appends ``-<lang>`` before ``.md``. Derived from the
    name rather than passed in, so a check on a single file is correct on its
    own without the caller having to know which variant it handed over.
    """
    stem = name[:-3] if name.endswith(".md") else name
    for lang in LangEnum:
        if stem.endswith(f"-{lang.value}"):
            return lang
    return None


# --------------------------------------------------------------------------- #
# Per-language lint switch.
#
# A teaching repo keeps every language variant of every special file in place, so
# the layout never changes, but a variant that has not been written yet is an
# empty placeholder. Linting one of those would fail on every content check for a
# reason that says nothing about the repo's quality, so each language carries a
# flag saying whether it takes part in linting at all. A disabled language is
# skipped whole: no existence check, no frontmatter check, no H1 check.
#
# English is currently disabled: the authoring workflow writes Chinese only, and
# the English variants exist as empty files until the multi-language module picks
# them up. Flipping English back on is a one-word change here, not a rewrite of
# the linter.
#
# A language absent from the mapping defaults to enabled, so adding a language to
# ``LangEnum`` starts it out linted; turning it off has to be deliberate.
# --------------------------------------------------------------------------- #
LINT_ENABLED_BY_LANG: "dict[LangEnum | None, bool]" = {
    None: False,  # English: placeholder files, left empty on purpose
    LangEnum.cn: True,
}


def is_lint_enabled(lang: "LangEnum | None") -> bool:
    """Whether the variant written in ``lang`` takes part in linting.

    ``None`` means English. Languages not listed in
    :data:`LINT_ENABLED_BY_LANG` default to enabled.
    """
    return LINT_ENABLED_BY_LANG.get(lang, True)


def max_description_chars(lang: "LangEnum | None") -> int:
    """The ``description`` budget for one language. ``None`` means English."""
    return MAX_DESCRIPTION_CHARS_BY_LANG.get(lang, DEFAULT_MAX_DESCRIPTION_CHARS)


def max_github_about_chars(lang: "LangEnum | None") -> int:
    """The ``github_about`` budget for one language. ``None`` means English."""
    return MAX_GITHUB_ABOUT_CHARS_BY_LANG.get(
        lang, DEFAULT_MAX_GITHUB_ABOUT_CHARS
    )


# --------------------------------------------------------------------------- #
# description / github_about charset.
#
# The value is always wrapped in double quotes and gets embedded verbatim into
# other strings (a SYLLABUS bullet, a table cell, GitHub's About box), so any
# character that could close the wrapper or start a code span is out.
#
# The ASCII apostrophe is deliberately NOT here. It cannot be confused with the
# wrapping quote, and English prose needs it constantly ("it's", "GitHub's").
# Note that H1_FORBIDDEN_CHARS below still bans it: an H1 travels around as a
# bare unwrapped string, so the reasoning there is a different one.
# --------------------------------------------------------------------------- #
DESCRIPTION_FORBIDDEN_CHARS = (
    '"'  # straight double quote
    "`"  # backtick
    "“"  # left double quotation mark
    "”"  # right double quotation mark
    "‘"  # left single quotation mark
    "’"  # right single quotation mark
)


# --------------------------------------------------------------------------- #
# H1 title charset.
# A general H1 may use only letters, digits, text, and the punctuation , : .
# The characters below are banned: the three dash characters, straight and curly
# quotes, and square brackets (an H1 often ends up as a bare string elsewhere,
# where quotes and brackets would need escaping). README-ORIGINAL is exempt: its
# H1 must equal the repo name, which may itself contain hyphens or underscores.
# --------------------------------------------------------------------------- #
H1_FORBIDDEN_CHARS = (
    "—"  # em dash
    "–"  # en dash
    "-"  # hyphen
    '"'  # straight double quote
    "'"  # straight single quote
    "“"  # left double quotation mark
    "”"  # right double quotation mark
    "‘"  # left single quotation mark
    "’"  # right single quotation mark
    "["
    "]"
)


# --------------------------------------------------------------------------- #
# Estimated time.
#
# Every TICKET closes its "what to do" section with one line giving the task's
# estimated time as a minute range picked from a fixed six-tier ladder (3-5,
# 5-15, 15-30, 30-60, 60-90, 90-120). The repo-level total in ``lm.json`` is the
# straight sum of every branch's range, converted to decimal hours once at the
# end and rounded to :data:`ESTIMATED_HOURS_DIGITS` places, so the stored value
# is exactly reproducible and can be compared for equality rather than within a
# tolerance.
#
# The label is Chinese because courses are authored in Chinese only; when the
# multi-language module lands this becomes a per-language mapping like the
# description caps above.
# --------------------------------------------------------------------------- #
ESTIMATED_TIME_LABEL = "**预计用时:**"
ESTIMATED_TIME_PATTERN = re.compile(
    r"^\*\*预计用时:\*\*\s*(\d+)\s*到\s*(\d+)\s*分钟"
)
ESTIMATED_HOURS_DIGITS = 2

# lm.json field names for the repo-level total.
ESTIMATED_HOURS_LOWER_FIELD = "estimated_hours_lower"
ESTIMATED_HOURS_UPPER_FIELD = "estimated_hours_upper"


def minutes_to_hours(minutes: int) -> float:
    """Convert a minute count to decimal hours, rounded for storage in lm.json."""
    return round(minutes / 60, ESTIMATED_HOURS_DIGITS)


# --------------------------------------------------------------------------- #
# Task branch / task dir naming.
# --------------------------------------------------------------------------- #
# Strict form: NN-lowercase-hyphen-words.
TASK_DIR_PATTERN = re.compile(r"^\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")

# Loose form used to discover task dirs (so the linter can still flag dirs that
# have the NN- prefix but violate the strict pattern).
TASK_DIR_PREFIX_PATTERN = re.compile(r"^\d{2}-")
