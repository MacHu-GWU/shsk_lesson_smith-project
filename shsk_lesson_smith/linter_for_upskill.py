# -*- coding: utf-8 -*-

"""Upskill-specific lint rules.

Reuses the shared rules from ``linter.py`` and adds the two upskill-only ones:
the repo-root overview files, and the ``examples/`` mini tasks. ``RULES`` is the
composed rule list that :func:`linter.lint` runs for an upskill repo.
"""

from .constants import README_BASE
from .exc import LintError
from .linter import (
    CheckResult,
    lint_file_group,
    lint_task_dir,
    rule_manifest,
    rule_readme_original,
    rule_syllabus,
    rule_task_snapshots,
    run_check,
)
from .repo import Repo, get_variant_filename


#: The single task branch an upskill repo is allowed to have.
UPSKILL_BRANCH = "01-upskill"


def rule_single_branch(repo: Repo) -> "list[CheckResult]":
    """Upskill has exactly one task branch, and it must be ``01-upskill``.

    The mini tasks live under ``examples/``; ``docs/tasks/`` holds the snapshot
    of that single branch, so it must contain exactly one dir with this name.
    """

    def _check() -> None:
        names = [d.name for d in repo.iter_dir_tasks()]
        if names != [UPSKILL_BRANCH]:
            raise LintError(
                f"An upskill repo must have exactly one task branch named "
                f"{UPSKILL_BRANCH!r} under docs/tasks/; found {names}."
            )

    return [run_check(repo.dir_docs_tasks, _check)]


def rule_root_overview(repo: Repo) -> "list[CheckResult]":
    """Repo-root README (course overview) and optional TICKET.

    The root README here is the repo overview, not a teaching README, so it is
    only checked for existence and language completeness (no description / H1
    rules). The root TICKET is optional for upskill (each mini task carries its
    own), but if present it must be language-complete.
    """
    out = lint_file_group(repo.get_path_readme, required=True)
    out += lint_file_group(repo.get_path_ticket, required=False)
    return out


def rule_examples(repo: Repo) -> "list[CheckResult]":
    """The ``examples/`` tree: the dir, its index README, and each mini task."""
    dir_examples = repo.dir_examples
    if dir_examples is None or not dir_examples.exists():
        target = dir_examples or (repo.dir_project_root / "examples")

        def _missing() -> None:
            raise LintError("examples/ directory is missing.")

        return [run_check(target, _missing)]

    # examples/README is a series index, not a teaching README: existence only.
    out = lint_file_group(
        lambda lang: dir_examples / get_variant_filename(README_BASE, lang),
        required=True,
    )
    for dir_example in repo.iter_dir_examples():
        name = dir_example.name
        out.extend(
            lint_task_dir(
                dir_example,
                lambda lang, n=name: repo.get_path_example_readme(n, lang),
                lambda lang, n=name: repo.get_path_example_ticket(n, lang),
            )
        )
    return out


# Rule list run by linter.lint() for an upskill repo, in report order.
RULES = [
    rule_manifest,
    rule_readme_original,
    rule_root_overview,
    rule_examples,
    rule_single_branch,
    rule_syllabus,
    rule_task_snapshots,
]
