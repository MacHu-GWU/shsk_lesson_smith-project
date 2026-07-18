# -*- coding: utf-8 -*-

"""Evolve-specific repo and metadata.

An evolve repo is multi-branch, one task per branch; the current branch's
README / TICKET live at the repo root and get snapshotted into
``docs/tasks/<branch>/``. Structure is defined here; evolve-specific rules are
still TODO (see linter_for_evolve.py).
"""

import dataclasses
from functools import cached_property

from .repo import Metadata, Repo


@dataclasses.dataclass
class EvolveMetadata(Metadata):
    """``lm.json`` metadata for an evolve repo. Add evolve-only fields here."""


@dataclasses.dataclass(frozen=True)
class EvolveRepo(Repo):
    """An evolve teaching repo (root task files, snapshotted per branch)."""

    @cached_property
    def metadata(self) -> "EvolveMetadata | None":
        return EvolveMetadata.load_or_none(self.path_lm_json)
