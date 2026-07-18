# -*- coding: utf-8 -*-

"""Upskill-specific repo and metadata.

An upskill repo has the same layout as showcase (mini tasks under
``examples/NN-title/``) but no external publish step. Both the :class:`Repo`
and :class:`Metadata` bases are subclassed so future upskill-only fields have a
home.
"""

import dataclasses
from functools import cached_property

from .repo import Metadata, Repo


@dataclasses.dataclass
class UpskillMetadata(Metadata):
    """``lm.json`` metadata for an upskill repo. Add upskill-only fields here."""


@dataclasses.dataclass(frozen=True)
class UpskillRepo(Repo):
    """An upskill teaching repo (examples/ layout, no publish)."""

    @cached_property
    def metadata(self) -> "UpskillMetadata | None":
        return UpskillMetadata.load_or_none(self.path_lm_json)
