# -*- coding: utf-8 -*-

"""Readup-specific lint rules.

A readup repo has the same ``examples/`` layout as upskill (mini tasks under a
single ``01-readup`` branch) but is a pure-reading course: it strips the entire
AI toolchain. So compared with upskill it drops two rules:

- no ``rule_forge_outputs`` (there is no ``docs/upskill``-style learning doc and
  no child skill to check for),
- no quiz mini task check (there is no ``NN-prove-i-get-it`` task; self-checking
  is done through each mini task's own TICKET).

What remains is the shared rules plus the examples tree and the single-branch
check. ``RULES`` is the composed rule list that :func:`linter.lint` runs for a
readup repo.

Spec source of truth: the readup-only rules here enforce the specs in
``.claude/skills/lesson-smith/skills/lesson-smith/ref/readup/*.md`` (readup-repo-layout,
readup-readme-spec, readup-ticket-spec, readup-examples-readme-spec). The shared,
type-agnostic checks come from ``linter.py`` and its top-level ``ref/*.md`` specs.
Those specs are authoritative; keep these rules in sync with them.
"""

from .constants import README_BASE
from .exc import LintError
from .linter import (
    CheckResult,
    _check_examples_numbering,
    lint_file_group,
    lint_task_dir,
    rule_manifest,
    rule_readme_original,
    rule_root_overview,
    rule_syllabus,
    rule_task_snapshots,
    run_check,
)
from .repo import Repo, get_variant_filename


def rule_single_branch(repo: Repo) -> "list[CheckResult]":
    """Readup has exactly one task branch, and it must be ``01-readup``.

    The mini tasks live under ``examples/``; ``docs/tasks/`` holds the snapshot
    of that single branch, so it must contain exactly one dir whose name is
    :attr:`Repo.single_task_branch`.
    """

    def _check() -> None:
        expected = repo.single_task_branch
        names = [d.name for d in repo.iter_dir_tasks()]
        if names != [expected]:
            raise LintError(
                f"A readup repo must have exactly one task branch named "
                f"{expected!r} under docs/tasks/; found {names}."
            )

    return [run_check(repo.dir_docs_tasks, _check)]


def rule_examples(repo: Repo) -> "list[CheckResult]":
    """The ``examples/`` tree: the dir, its index README, and each mini task.

    Readup only requires consecutive numbering from 01; unlike upskill it has no
    quiz mini task, so there is no ``NN-prove-i-get-it`` check.
    """
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
    example_dirs = list(repo.iter_dir_examples())
    out.append(run_check(dir_examples, _check_examples_numbering, example_dirs))
    for dir_example in example_dirs:
        name = dir_example.name
        out.extend(
            lint_task_dir(
                dir_example,
                lambda lang, n=name: repo.get_path_example_readme(n, lang),
                lambda lang, n=name: repo.get_path_example_ticket(n, lang),
            )
        )
    return out


# Rule list run by linter.lint() for a readup repo, in report order. Note the
# absence of a forge-outputs rule: a readup repo ships no learning docs or skills.
RULES = [
    rule_manifest,
    rule_readme_original,
    rule_root_overview,
    rule_examples,
    rule_single_branch,
    rule_syllabus,
    rule_task_snapshots,
]
