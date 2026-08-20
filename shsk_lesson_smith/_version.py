# -*- coding: utf-8 -*-

"""
Where the running package reads its own version from.

The literal lives in the ``version`` field of ``pyproject.toml`` and nowhere else.
This module reads it back out of the installed distribution's metadata, the same
way ``docs/source/conf.py`` does, so there is no second copy to keep in sync.

One caveat worth knowing: an editable install bakes the version into its
``.dist-info`` at install time, so between bumping ``pyproject.toml`` and the next
``uv sync`` this reports the previous number. ``tests/test_version.py`` fails in
that window rather than letting a stale value pass unnoticed, and ``mise run inst``
(which ``mise run cov`` already depends on) closes it.
"""

from importlib.metadata import PackageNotFoundError, version as _get_version

try:
    __version__ = _get_version("shsk_lesson_smith")
except PackageNotFoundError:  # pragma: no cover
    # A source checkout that was never installed has no distribution metadata to
    # read from. Degrade rather than raise: a package that cannot be imported at
    # all is a worse outcome than one that cannot name its own version.
    __version__ = "unknown"
