# -*- coding: utf-8 -*-

"""Upskill-specific lint rules.

Reuses the shared rules from ``linter.py`` and adds the two upskill-only ones:
the repo-root overview files, and the ``examples/`` mini tasks. ``RULES`` is the
composed rule list that :func:`linter.lint` runs for an upskill repo.

Spec source of truth: the upskill-only rules here enforce the specs in
``.claude/skills/lesson-smith/skills/lesson-smith/ref/upskill/*.md`` (upskill-repo-layout,
upskill-readme-spec, upskill-ticket-spec, upskill-examples-readme-spec, upskill-examples-quiz-*-spec,
docs-upskill-*-spec). The shared, type-agnostic checks come from ``linter.py`` and
its top-level ``ref/*.md`` specs. Those specs are authoritative; keep these rules in
sync with them.
"""

import re

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
from .linter import (  # re-exported: shared helpers now live in linter.py
    _check_examples_numbering,
    rule_root_overview,
)
from .linter_utils import check_file_exists
from .repo import Repo, get_variant_filename

# Files the forge step produces for a finished upskill repo (checked for
# existence only; their content is AI-facing and not linted).
DOCS_UPSKILL_FILES = (
    "01-upskill-learn.md",
    "02-upskill-runbook.md",
    "03-upskill-quiz.md",
)
FORGE_SKILLS = ("upskill-learn", "upskill-quiz")
QUIZ_TASK_SUFFIX = "prove-i-get-it"


def rule_single_branch(repo: Repo) -> "list[CheckResult]":
    """Upskill has exactly one task branch, and it must be ``01-upskill``.

    The mini tasks live under ``examples/``; ``docs/tasks/`` holds the snapshot
    of that single branch, so it must contain exactly one dir whose name is
    :attr:`Repo.single_task_branch`.
    """

    def _check() -> None:
        expected = repo.single_task_branch
        names = [d.name for d in repo.iter_dir_tasks()]
        if names != [expected]:
            raise LintError(
                f"An upskill repo must have exactly one task branch named "
                f"{expected!r} under docs/tasks/; found {names}."
            )

    return [run_check(repo.dir_docs_tasks, _check)]


def _check_quiz_task_present(example_dirs: "list") -> None:
    """Exactly one examples mini task must be the quiz, named NN-prove-i-get-it."""
    quiz = [
        d.name
        for d in example_dirs
        if re.match(r"^\d\d-" + re.escape(QUIZ_TASK_SUFFIX) + r"$", d.name)
    ]
    if len(quiz) != 1:
        raise LintError(
            "An upskill repo must have exactly one quiz mini task named "
            f"NN-{QUIZ_TASK_SUFFIX} under examples/; found {quiz}."
        )


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
    example_dirs = list(repo.iter_dir_examples())
    out.append(run_check(dir_examples, _check_examples_numbering, example_dirs))
    out.append(run_check(dir_examples, _check_quiz_task_present, example_dirs))
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


def rule_forge_outputs(repo: Repo) -> "list[CheckResult]":
    """The forge step's outputs must exist: the docs/upskill/ docs and the skills.

    Existence only; these files are AI-facing (English meta files and skill
    definitions), so their content is not linted here. A finished upskill repo
    has run ``/lesson-smith-upskill-forge``, so these are expected to be present.
    """
    root = repo.dir_project_root
    out: "list[CheckResult]" = []
    for name in DOCS_UPSKILL_FILES:
        path = root / "docs" / "upskill" / name
        out.append(run_check(path, check_file_exists, path))
    for skill in FORGE_SKILLS:
        path = root / ".claude" / "skills" / skill / "SKILL.md"
        out.append(run_check(path, check_file_exists, path))
    return out


# Rule list run by linter.lint() for an upskill repo, in report order.
RULES = [
    rule_manifest,
    rule_readme_original,
    rule_root_overview,
    rule_examples,
    rule_forge_outputs,
    rule_single_branch,
    rule_syllabus,
    rule_task_snapshots,
]
