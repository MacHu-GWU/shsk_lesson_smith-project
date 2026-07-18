# -*- coding: utf-8 -*-

"""Type-specific teaching repo models, all subclassing :class:`StandardRepo`.

- :class:`EvolveRepo`: multi-branch, one task per branch; the task's
  README / TICKET live at the repo root of that branch.
- :class:`ShowcaseRepo`: single ``showcase`` branch; each mini task lives in
  ``examples/NN-title/``; the repo is publishable as the student's own work.
- :class:`UpskillRepo`: same layout as showcase, minus the publish step.

Use :func:`resolve_repo` to get the right subclass from ``lm.json``.
"""

import dataclasses
from functools import cached_property
from pathlib import Path

from .constants import TASK_DIR_PREFIX_PATTERN, RepoTypeEnum
from .repo import StandardRepo


@dataclasses.dataclass
class EvolveRepo(StandardRepo):
    """Evolve repo: the root-level README / TICKET belong to the current task."""


@dataclasses.dataclass
class ShowcaseRepo(StandardRepo):
    """Showcase repo: mini tasks live under ``examples/NN-title/``."""

    @cached_property
    def dir_examples(self) -> Path:
        return self.dir_project_root / "examples"

    def get_dir_example(self, example_dir_name: str) -> Path:
        """One mini task directory: ``examples/<NN-title>/``."""
        return self.dir_examples / example_dir_name

    def iter_example_dirs(self) -> "list[Path]":
        """Mini task dirs under examples/, sorted by number."""
        if not self.dir_examples.exists():
            return []
        return sorted(
            d
            for d in self.dir_examples.iterdir()
            if d.is_dir() and TASK_DIR_PREFIX_PATTERN.match(d.name)
        )


@dataclasses.dataclass
class UpskillRepo(ShowcaseRepo):
    """Upskill repo: identical layout to showcase, no external publish step."""


REPO_TYPE_TO_CLASS: "dict[RepoTypeEnum, type[StandardRepo]]" = {
    RepoTypeEnum.evolve: EvolveRepo,
    RepoTypeEnum.showcase: ShowcaseRepo,
    RepoTypeEnum.upskill: UpskillRepo,
}


def resolve_repo(dir_cwd: "Path | str | None" = None) -> StandardRepo:
    """Build the right repo model for the teaching repo containing ``dir_cwd``.

    Reads the ``type`` field of ``lm.json`` and returns the matching subclass.
    Falls back to the plain :class:`StandardRepo` when lm.json is missing or
    invalid, so the linter can still run and report the manifest problem.
    """
    if dir_cwd is None:
        base = StandardRepo()
    else:
        base = StandardRepo(dir_cwd=Path(dir_cwd))
    klass = REPO_TYPE_TO_CLASS.get(base.repo_type, StandardRepo)
    if klass is StandardRepo:
        return base
    return klass(dir_cwd=base.dir_cwd)
