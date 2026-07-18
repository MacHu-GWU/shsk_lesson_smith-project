# -*- coding: utf-8 -*-

"""``lesson-smith`` command line interface, powered by Python Fire.

This module only maps CLI flags onto the library. All lint logic lives in
``linter.py`` (:func:`lint_project`, :meth:`LintReport.render`,
:meth:`LintReport.to_json`); the methods below just parse arguments, pick an
output form, and set the exit code.

Usage::

    lesson-smith lint [--project-root PATH] [--json] [--quiet]
    lesson-smith sync [--project-root PATH] [--json] [--quiet]
"""

import sys

import fire

from .linter import lint_project
from .sync import sync_project


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


def main():
    """Console script entry point (``lesson-smith``)."""
    fire.Fire(Command)
