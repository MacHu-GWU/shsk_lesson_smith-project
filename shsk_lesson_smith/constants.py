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
    """The three kinds of teaching repositories, declared in ``lm.json``."""

    evolve = "evolve"
    showcase = "showcase"
    upskill = "upskill"


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
# --------------------------------------------------------------------------- #
MAX_DESCRIPTION_CHARS = 400
# The README-ORIGINAL-only ``github_about`` field: a compressed tagline that also
# fits GitHub's About box, so it is capped tighter than the full description.
MAX_GITHUB_ABOUT_CHARS = 200
DESCRIPTION_FORBIDDEN_CHARS = (
    '"'  # straight double quote
    "'"  # straight single quote
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
# Task branch / task dir naming.
# --------------------------------------------------------------------------- #
# Strict form: NN-lowercase-hyphen-words.
TASK_DIR_PATTERN = re.compile(r"^\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")

# Loose form used to discover task dirs (so the linter can still flag dirs that
# have the NN- prefix but violate the strict pattern).
TASK_DIR_PREFIX_PATTERN = re.compile(r"^\d{2}-")
