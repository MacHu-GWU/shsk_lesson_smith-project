# -*- coding: utf-8 -*-

"""``lesson-smith`` command line interface, powered by Python Fire.

This module only maps CLI flags onto the library. All lint logic lives in
``linter.py`` (:func:`lint_project`, :meth:`LintReport.render`,
:meth:`LintReport.to_json`); the methods below just parse arguments, pick an
output form, and set the exit code.

Usage::

    lesson-smith lint [--project-root PATH] [--json] [--quiet]
    lesson-smith sync [--project-root PATH] [--json] [--quiet]
    lesson-smith version
    lesson-smith --version
"""

import sys

import fire

from . import __version__
from .linter import lint_project
from .sync import sync_project

#: Top-level flags handled before Fire sees them. Fire consumes ``-v`` itself as
#: an alias of ``--verbose``, so the short form here is the capital ``-V``.
VERSION_FLAGS = ("--version", "-V")


class Command:
    """Maintain and validate a lesson-smith teaching repository."""

    def lint(
        self,
        project_root: "str | None" = None,
        json: bool = False,
        quiet: bool = False,
    ):
        """Lint a teaching repo. Exits non-zero when linting does not pass.

        :param project_root: the repo root (default: resolve upward from the
            current working directory until ``.git`` + ``mise.toml`` are found).
        :param json: print the report as JSON, one entry per check point,
            instead of the human-readable markdown form.
        :param quiet: print nothing; only set the exit code.
        """
        try:
            report = lint_project(project_root)
        except FileNotFoundError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            raise SystemExit(1)

        if not quiet:
            print(report.to_json() if json else report.render())

        if not report.passed:
            raise SystemExit(1)

    def sync(
        self,
        project_root: "str | None" = None,
        json: bool = False,
        quiet: bool = False,
    ):
        """Snapshot the current branch's task files and regenerate the syllabus.

        :param project_root: the repo root (default: resolve upward from the
            current working directory until ``.git`` + ``mise.toml`` are found).
        :param json: print what was written as JSON instead of the
            human-readable form.
        :param quiet: print nothing; only set the exit code.
        """
        try:
            report = sync_project(project_root)
        except FileNotFoundError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            raise SystemExit(1)
        except NotImplementedError as error:
            print(f"ERROR: {error}", file=sys.stderr)
            raise SystemExit(1)

        if not quiet:
            print(report.to_json() if json else report.render())

    def version(self):
        """Print the installed ``shsk-lesson-smith`` version, then exit.

        Worth running whenever a repo is linted through a pinned
        ``uvx --from shsk-lesson-smith==X.Y.Z``: it is the only way to confirm
        which ruleset actually ran.
        """
        print(__version__)


def main():
    """Console script entry point (``lesson-smith``)."""
    # Fire has no notion of a top-level flag: it tries to consume ``--version``
    # as an argument to a command and fails with "Could not consume arg". So the
    # conventional spelling is intercepted here, and ``version`` also exists as a
    # real subcommand so that it shows up in Fire's own usage listing.
    if len(sys.argv) == 2 and sys.argv[1] in VERSION_FLAGS:
        print(__version__)
        return
    fire.Fire(Command)
