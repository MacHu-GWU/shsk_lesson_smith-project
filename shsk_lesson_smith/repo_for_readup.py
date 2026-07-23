# -*- coding: utf-8 -*-

"""Readup-specific repo and metadata.

A readup repo has the same ``examples/NN-title/`` layout as upskill but is a
pure-reading course: no AI learning toolchain (no learn / quiz child skills, no
docs/ learning docs, no quiz mini task). Both the :class:`Repo` and
:class:`Metadata` bases are subclassed so future readup-only fields have a home.
"""

import dataclasses
from functools import cached_property

from .repo import Metadata, Repo


@dataclasses.dataclass
class ReadupMetadata(Metadata):
    """``lm.json`` metadata for a readup repo. Add readup-only fields here."""


@dataclasses.dataclass(frozen=True)
class ReadupRepo(Repo):
    """A readup teaching repo (examples/ layout, pure reading, no toolchain)."""

    @cached_property
    def metadata(self) -> "ReadupMetadata | None":
        return ReadupMetadata.load_or_none(self.path_lm_json)
