# -*- coding: utf-8 -*-

import re

from shsk_lesson_smith import __version__
from shsk_lesson_smith._version import __version__ as _version_py_version
from shsk_lesson_smith.paths import path_enum


def read_pyproject_version() -> str:
    """Pull the ``version`` field out of the ``[project]`` table.

    Done with a regex rather than ``tomllib`` so the test also runs on Python
    3.10, which the ``requires-python`` field still supports.
    """
    text = path_enum.path_pyproject_toml.read_text(encoding="utf-8")
    # Anchored at line start: the string "[project]" also shows up in the comment
    # block above the real table header.
    header = re.search(r"^\[project\]$", text, re.MULTILINE)
    assert header is not None, "no [project] table found in pyproject.toml"
    project_table = re.split(
        r"^\[", text[header.end() :], maxsplit=1, flags=re.MULTILINE
    )[0]
    match = re.search(r'^version\s*=\s*"([^"]+)"', project_table, re.MULTILINE)
    assert match is not None, "no version field found in the [project] table"
    return match.group(1)


class TestVersion:
    def test_package_reexports_version_py(self):
        assert __version__ == _version_py_version

    def test_is_a_real_version_not_the_fallback(self):
        # Also guards the ``importlib.metadata`` lookup: a renamed distribution
        # would silently degrade to "unknown" rather than raise.
        assert re.fullmatch(r"\d+\.\d+\.\d+.*", __version__), __version__

    def test_installed_metadata_matches_pyproject_toml(self):
        # ``pyproject.toml`` is the single source of truth, but an editable
        # install freezes its version into ``.dist-info`` at install time. So this
        # is really a staleness check on the virtualenv, and it is what makes
        # reading the version out of metadata safe to rely on.
        assert __version__ == read_pyproject_version(), (
            f"the installed distribution reports {__version__!r} but "
            f"pyproject.toml declares {read_pyproject_version()!r} — the venv is "
            f"stale, run `mise run inst`"
        )


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith._version",
        preview=False,
    )
