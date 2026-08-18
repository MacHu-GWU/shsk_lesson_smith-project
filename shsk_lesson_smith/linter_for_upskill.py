# -*- coding: utf-8 -*-

"""Upskill-specific lint rules.

Reuses the shared rules from ``linter.py`` and adds the two upskill-only ones:
the repo-root overview files, and the ``examples/`` tasks. ``RULES`` is the
composed rule list that :func:`linter.lint` runs for an upskill repo.

Spec source of truth: the upskill-only rules here enforce the specs under
``.claude/skills/lesson-smith/skills/lesson-smith/ref/02-upskill/``
(upskill-repo-layout, upskill-readme-spec, upskill-ticket-spec) plus the shared
ones under ``ref/00-common/`` that upskill takes part in (11-quiz-readme-spec,
12-quiz-ticket-spec, 13-forge-shared). The shared, type-agnostic checks come
from ``linter.py`` and the rest of ``ref/00-common/``. Those specs are
authoritative; keep these rules in sync with them.
"""

import re

from .exc import LintError
from .linter import (
    CheckResult,
    lint_file_group,
    lint_task_dir,
    rule_estimated_hours,
    rule_manifest,
    rule_readme_original,
    rule_syllabus,
    rule_task_snapshots,
    run_check,
)
from .linter import (  # re-exported: shared helpers now live in linter.py
    _check_examples_numbering,
    linted_langs,
    rule_root_overview,
)
from .linter_utils import check_file_exists
from .repo import Repo, get_variant_filename, get_variant_name

# What the forge step produces for a finished upskill repo, as language-free
# bases. Forge emits one variant per language, so the ``-<lang>`` suffix is
# appended at check time: ``01-upskill-learn-cn.md`` and the child skill dir
# ``upskill-learn-cn/``. English carries no suffix.
DOCS_UPSKILL_FILE_BASES = (
    "01-upskill-learn",
    "02-upskill-runbook",
    "03-upskill-quiz",
)
FORGE_SKILL_BASES = ("upskill-learn", "upskill-quiz")
QUIZ_TASK_SUFFIX = "prove-i-get-it"


def rule_single_branch(repo: Repo) -> "list[CheckResult]":
    """Upskill has exactly one task branch, and it must be ``01-upskill``.

    The tasks live under ``examples/``; ``docs/tasks/`` holds the snapshot
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
    """Exactly one examples task must be the quiz, named NN-prove-i-get-it."""
    quiz = [
        d.name
        for d in example_dirs
        if re.match(r"^\d\d-" + re.escape(QUIZ_TASK_SUFFIX) + r"$", d.name)
    ]
    if len(quiz) != 1:
        raise LintError(
            "An upskill repo must have exactly one quiz task named "
            f"NN-{QUIZ_TASK_SUFFIX} under examples/; found {quiz}."
        )


def rule_examples(repo: Repo) -> "list[CheckResult]":
    """The ``examples/`` tree: the dir and each task."""
    dir_examples = repo.dir_examples
    if dir_examples is None or not dir_examples.exists():
        target = dir_examples or (repo.dir_project_root / "examples")

        def _missing() -> None:
            raise LintError("examples/ directory is missing.")

        return [run_check(target, _missing)]

    # No examples/README: the series index is a normal first task under
    # examples/, indistinguishable from a teaching task as far as lint can tell.
    out: "list[CheckResult]" = []
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

    Existence only; these files are AI-facing (meta docs and skill definitions),
    so their content is not linted here. A finished upskill repo has run
    ``/lesson-smith-upskill-forge``, so these are expected to be present.

    Forge produces one variant per language, so this walks
    :func:`linted_langs` the same way every other rule does: a language that is
    switched off is skipped whole, and its variants are not required to exist.
    That matters right now, because forge emits the ``-cn`` set only while the
    English variants wait for the multi-language module.
    """
    root = repo.dir_project_root
    out: "list[CheckResult]" = []
    for lang in linted_langs():
        for base in DOCS_UPSKILL_FILE_BASES:
            path = root / "docs" / "upskill" / get_variant_filename(base, lang)
            out.append(run_check(path, check_file_exists, path))
        for base in FORGE_SKILL_BASES:
            skill = get_variant_name(base, lang)
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
    rule_estimated_hours,
]
