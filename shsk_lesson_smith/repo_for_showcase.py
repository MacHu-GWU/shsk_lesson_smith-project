# -*- coding: utf-8 -*-

"""Showcase-specific repo and metadata.

A showcase repo keeps mini tasks under ``examples/NN-title/`` and is publishable
as the student's own work. Structure is defined here; showcase-specific rules
are still TODO (see linter_for_showcase.py).
"""

import dataclasses
from functools import cached_property

from .repo import Metadata, Repo


@dataclasses.dataclass
class ShowcaseMetadata(Metadata):
    """``lm.json`` metadata for a showcase repo. Add showcase-only fields here."""


@dataclasses.dataclass(frozen=True)
class ShowcaseRepo(Repo):
    """A showcase teaching repo (examples/ layout, publishable)."""

    @cached_property
    def metadata(self) -> "ShowcaseMetadata | None":
        return ShowcaseMetadata.load_or_none(self.path_lm_json)
