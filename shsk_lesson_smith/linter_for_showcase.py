# -*- coding: utf-8 -*-

"""Showcase-specific lint rules.

The showcase layout matches upskill (examples/ mini tasks under a single
``01-showcase`` branch) plus two showcase-only things: a demo mini task
(``NN-how-i-build-this``, the last example) and a publish step. The forge step
produces five docs and four child skills (upskill produces three and two).

Reuses the shared rules and the examples-based helpers from ``linter.py`` and
adds the showcase-only ones. ``RULES`` is the composed rule list that
:func:`linter.lint` runs for a showcase repo.

Spec source of truth: the showcase-only rules here enforce the specs in
``.claude/skills/lesson-smith/skills/lesson-smith/ref/showcase/*.md``
(showcase-repo-layout, showcase-readme-spec, showcase-ticket-spec,
showcase-examples-readme-spec, showcase-examples-quiz-*-spec,
showcase-examples-demo-*-spec, docs-showcase-*-spec). The shared, type-agnostic
checks come from ``linter.py`` and its top-level ``ref/*.md`` specs. Those specs
are authoritative; keep these rules in sync with them.
"""

import re

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
from .linter_utils import check_file_exists
from .repo import Repo, get_variant_filename

# Files the forge step produces for a finished showcase repo (existence only;
# their content is AI-facing and not linted). Five docs, four child skills.
DOCS_SHOWCASE_FILES = (
    "01-showcase-learn.md",
    "02-showcase-runbook.md",
    "03-showcase-quiz.md",
    "04-showcase-demo.md",
    "05-showcase-publish.md",
)
FORGE_SKILLS = ("showcase-learn", "showcase-quiz", "showcase-demo", "showcase-publish")
QUIZ_TASK_SUFFIX = "prove-i-get-it"
DEMO_TASK_SUFFIX = "how-i-build-this"


def rule_single_branch(repo: Repo) -> "list[CheckResult]":
    """Showcase has exactly one task branch, and it must be ``01-showcase``.

    The mini tasks live under ``examples/``; ``docs/tasks/`` holds the snapshot
    of that single branch, so it must contain exactly one dir whose name is
    :attr:`Repo.single_task_branch`.
    """

    def _check() -> None:
        expected = repo.single_task_branch
        names = [d.name for d in repo.iter_dir_tasks()]
        if names != [expected]:
            raise LintError(
                f"A showcase repo must have exactly one task branch named "
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
            "A showcase repo must have exactly one quiz mini task named "
            f"NN-{QUIZ_TASK_SUFFIX} under examples/; found {quiz}."
        )


def _check_demo_task_present(example_dirs: "list") -> None:
    """Exactly one mini task is the demo, named NN-how-i-build-this, and it is last.

    The demo story is the last example (highest number), so it comes after the
    teaching tasks and the quiz.
    """
    demo = [
        d.name
        for d in example_dirs
        if re.match(r"^\d\d-" + re.escape(DEMO_TASK_SUFFIX) + r"$", d.name)
    ]
    if len(demo) != 1:
        raise LintError(
            "A showcase repo must have exactly one demo mini task named "
            f"NN-{DEMO_TASK_SUFFIX} under examples/; found {demo}."
        )
    if example_dirs and example_dirs[-1].name != demo[0]:
        raise LintError(
            f"The demo mini task NN-{DEMO_TASK_SUFFIX} must be the last example "
            f"(highest number); the last example is {example_dirs[-1].name!r}."
        )


def rule_examples(repo: Repo) -> "list[CheckResult]":
    """The ``examples/`` tree: the dir, its index README, and each mini task.

    Beyond consecutive numbering, showcase requires exactly one quiz task
    (``NN-prove-i-get-it``) and exactly one demo task (``NN-how-i-build-this``,
    last).
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
    out.append(run_check(dir_examples, _check_quiz_task_present, example_dirs))
    out.append(run_check(dir_examples, _check_demo_task_present, example_dirs))
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
    """The forge step's outputs must exist: the docs/showcase/ docs and the skills.

    Existence only; these files are AI-facing (English meta files and skill
    definitions), so their content is not linted here. A finished showcase repo
    has run ``/lesson-smith-showcase-forge``, so these are expected to be present.
    """
    root = repo.dir_project_root
    out: "list[CheckResult]" = []
    for name in DOCS_SHOWCASE_FILES:
        path = root / "docs" / "showcase" / name
        out.append(run_check(path, check_file_exists, path))
    for skill in FORGE_SKILLS:
        path = root / ".claude" / "skills" / skill / "SKILL.md"
        out.append(run_check(path, check_file_exists, path))
    return out


# Rule list run by linter.lint() for a showcase repo, in report order.
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
