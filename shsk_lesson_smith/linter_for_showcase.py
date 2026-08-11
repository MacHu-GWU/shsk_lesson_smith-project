# -*- coding: utf-8 -*-

"""Showcase-specific lint rules.

The showcase layout matches upskill (examples/ tasks under a single
``01-showcase`` branch) plus two showcase-only things: a demo task
(``NN-how-i-build-this``, sitting between the quiz and the wrap-up) and a
publish step. The forge step produces five docs and four child skills (upskill
produces three and two).

Reuses the shared rules and the examples-based helpers from ``linter.py`` and
adds the showcase-only ones. ``RULES`` is the composed rule list that
:func:`linter.lint` runs for a showcase repo.

Spec source of truth: the showcase-only rules here enforce the specs under
``.claude/skills/lesson-smith/skills/lesson-smith/ref/03-showcase/``
(showcase-repo-layout, showcase-readme-spec, showcase-ticket-spec,
showcase-demo-readme-spec, showcase-demo-ticket-spec, forge/) plus the shared
ones under ``ref/00-common/`` that showcase takes part in (11-quiz-readme-spec,
12-quiz-ticket-spec, 13-forge-shared). The shared, type-agnostic checks come
from ``linter.py`` and the rest of ``ref/00-common/``. Those specs are
authoritative; keep these rules in sync with them.
"""

import re

from .exc import LintError
from .linter import (
    CheckResult,
    _check_examples_numbering,
    lint_file_group,
    lint_task_dir,
    linted_langs,
    rule_manifest,
    rule_readme_original,
    rule_root_overview,
    rule_syllabus,
    rule_task_snapshots,
    run_check,
)
from .linter_utils import check_file_exists
from .repo import Repo, get_variant_filename, get_variant_name

# What the forge step produces for a finished showcase repo, as language-free
# bases: five docs and four child skills (upskill has three and two). Forge
# emits one variant per language, so the ``-<lang>`` suffix is appended at check
# time: ``01-showcase-learn-cn.md`` and the child skill dir
# ``showcase-learn-cn/``. English carries no suffix.
DOCS_SHOWCASE_FILE_BASES = (
    "01-showcase-learn",
    "02-showcase-runbook",
    "03-showcase-quiz",
    "04-showcase-demo",
    "05-showcase-publish",
)
FORGE_SKILL_BASES = (
    "showcase-learn",
    "showcase-quiz",
    "showcase-demo",
    "showcase-publish",
)
QUIZ_TASK_SUFFIX = "prove-i-get-it"
DEMO_TASK_SUFFIX = "how-i-build-this"


def rule_single_branch(repo: Repo) -> "list[CheckResult]":
    """Showcase has exactly one task branch, and it must be ``01-showcase``.

    The tasks live under ``examples/``; ``docs/tasks/`` holds the snapshot
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
    """Exactly one examples task must be the quiz, named NN-prove-i-get-it."""
    quiz = [
        d.name
        for d in example_dirs
        if re.match(r"^\d\d-" + re.escape(QUIZ_TASK_SUFFIX) + r"$", d.name)
    ]
    if len(quiz) != 1:
        raise LintError(
            "A showcase repo must have exactly one quiz task named "
            f"NN-{QUIZ_TASK_SUFFIX} under examples/; found {quiz}."
        )


def _check_demo_task_present(example_dirs: "list") -> None:
    """Exactly one demo task, NN-how-i-build-this, sitting between quiz and wrap-up.

    Two position rules, both from section 4.2 of ``01-repo-layout.md``: the demo
    comes directly after the quiz, and the wrap-up task comes after every
    special task, so the demo is never the last example.

    lint cannot recognize the wrap-up by name (its directory name is up to the
    course), but "something follows the demo" is that check by another route,
    and it falls out for free from the two names that *are* fixed. This is why
    showcase catches a missing wrap-up while upskill and readup do not; see the
    hardness table in section 4.3.
    """
    names = [d.name for d in example_dirs]
    demo = [
        n for n in names if re.match(r"^\d\d-" + re.escape(DEMO_TASK_SUFFIX) + r"$", n)
    ]
    if len(demo) != 1:
        raise LintError(
            "A showcase repo must have exactly one demo task named "
            f"NN-{DEMO_TASK_SUFFIX} under examples/; found {demo}."
        )
    index_demo = names.index(demo[0])

    # The quiz's own existence is _check_quiz_task_present's job; only check
    # adjacency when there is exactly one quiz to be adjacent to.
    quiz = [
        n for n in names if re.match(r"^\d\d-" + re.escape(QUIZ_TASK_SUFFIX) + r"$", n)
    ]
    if len(quiz) == 1 and names.index(quiz[0]) != index_demo - 1:
        raise LintError(
            f"The demo task {demo[0]!r} must come directly after the quiz task "
            f"{quiz[0]!r}; the examples are ordered {names}."
        )

    if index_demo == len(names) - 1:
        raise LintError(
            f"The demo task {demo[0]!r} is the last example, but the wrap-up "
            "task must come after every special task, so one more example has "
            "to follow it."
        )


def rule_examples(repo: Repo) -> "list[CheckResult]":
    """The ``examples/`` tree: the dir and each task.

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

    # No examples/README: the series index is a normal first task under
    # examples/, indistinguishable from a teaching task as far as lint can tell.
    out: "list[CheckResult]" = []
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

    Existence only; these files are AI-facing (meta docs and skill definitions),
    so their content is not linted here. A finished showcase repo has run
    ``/lesson-smith-showcase-forge``, so these are expected to be present.

    Forge produces one variant per language, so this walks
    :func:`linted_langs` the same way every other rule does: a language that is
    switched off is skipped whole, and its variants are not required to exist.
    That matters right now, because forge emits the ``-cn`` set only while the
    English variants wait for the multi-language module.
    """
    root = repo.dir_project_root
    out: "list[CheckResult]" = []
    for lang in linted_langs():
        for base in DOCS_SHOWCASE_FILE_BASES:
            path = root / "docs" / "showcase" / get_variant_filename(base, lang)
            out.append(run_check(path, check_file_exists, path))
        for base in FORGE_SKILL_BASES:
            skill = get_variant_name(base, lang)
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
