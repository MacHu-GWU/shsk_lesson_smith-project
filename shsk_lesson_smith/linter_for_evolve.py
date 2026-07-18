# -*- coding: utf-8 -*-

"""Evolve-specific lint rules.

STRUCTURE STUB. In an evolve repo the root README / TICKET are the current
task's files and get snapshotted into docs/tasks/<branch>/. Only the shared
rules are wired up so far; the evolve-specific rules (root task files, current
branch is a task branch) are TODO. ``RULES`` is the composed list that
:func:`linter.lint` runs for an evolve repo.
"""

from .linter import (
    rule_manifest,
    rule_readme_original,
    rule_syllabus,
    rule_task_snapshots,
)

# TODO: add a rule for the root README/TICKET as the current task's files, and
# any evolve-only structural checks.
RULES = [
    rule_manifest,
    rule_readme_original,
    rule_syllabus,
    rule_task_snapshots,
]
