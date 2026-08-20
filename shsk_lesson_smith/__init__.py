# -*- coding: utf-8 -*-

"""
Maintain and validate lesson-smith teaching repositories.
"""

from importlib.metadata import PackageNotFoundError, version as _get_version

try:
    __version__ = _get_version("shsk_lesson_smith")
except PackageNotFoundError:  # pragma: no cover
    # Running straight from a source checkout that was never installed. There is
    # no second place to read the version from: ``pyproject.toml`` is the single
    # source of truth and it is only visible through the installed distribution.
    __version__ = "unknown"
