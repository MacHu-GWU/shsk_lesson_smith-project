# -*- coding: utf-8 -*-

"""Showcase-specific lint rules.

STRUCTURE STUB. The showcase layout matches upskill (examples/ mini tasks) plus
a publish step. Only the shared rules are wired up so far; the showcase-specific
rules (examples/ tree, publish readiness) are TODO. ``RULES`` is the composed
list that :func:`linter.lint` runs for a showcase repo.
"""

from .linter import (
    rule_manifest,
    rule_readme_original,
    rule_syllabus,
    rule_task_snapshots,
)

# TODO: add rule_root_overview + rule_examples (shareable with upskill) and any
# publish-readiness rule specific to showcase.
RULES = [
    rule_manifest,
    rule_readme_original,
    rule_syllabus,
    rule_task_snapshots,
]
