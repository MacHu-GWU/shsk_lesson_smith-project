# -*- coding: utf-8 -*-

"""Shared constants and enums for the lesson-smith teaching repo standard."""

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


# Name-body of the per-task special files (snapshotted into docs/tasks/<branch>/
# for evolve repos, or living in examples/NN-title/ for showcase/upskill repos).
TASK_FILE_BASES = ("README", "TICKET")

# Name-body of the repo-level special files that live at the project root.
REPO_FILE_BASES = ("README", "TICKET", "README-ORIGINAL")

SYLLABUS_BASE = "SYLLABUS"

# Frontmatter description constraints: one line, capped length, no quote-like
# characters (the description gets embedded into other strings verbatim).
MAX_DESCRIPTION_CHARS = 400
DESCRIPTION_FORBIDDEN_CHARS = "\"'`“”‘’"

# Strict form of a task branch / task dir name: NN-lowercase-hyphen-words.
TASK_DIR_PATTERN = re.compile(r"^\d{2}-[a-z0-9]+(-[a-z0-9]+)*$")

# Loose form used to discover task dirs (so the linter can still flag dirs
# that have the NN- prefix but violate the strict pattern).
TASK_DIR_PREFIX_PATTERN = re.compile(r"^\d{2}-")
