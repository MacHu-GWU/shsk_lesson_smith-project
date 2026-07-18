# -*- coding: utf-8 -*-

"""``lesson-smith`` command line interface, powered by Python Fire.

Usage::

    lesson-smith sync [--project_root=PATH] [--quiet]
    lesson-smith check [--project_root=PATH] [--quiet]
"""

import sys

import fire

from .linter import make_linter
from .repo import StandardRepo
from .repo_types import resolve_repo
from .sync import sync_repo


def _resolve(project_root: "str | None") -> StandardRepo:
    try:
        return resolve_repo(project_root)
    except FileNotFoundError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)


class Command:
    """Maintain and validate a lesson-smith teaching repository."""

    def sync(
        self,
        project_root: "str | None" = None,
        quiet: bool = False,
    ):
        """Snapshot current branch task files and regenerate the syllabus.

        :param project_root: any directory inside the teaching repo
            (default: current working directory).
        :param quiet: suppress normal output.
        """
        repo = _resolve(project_root)
        exit_code = sync_repo(repo, quiet=quiet)
        if exit_code:
            raise SystemExit(exit_code)

    def check(
        self,
        project_root: "str | None" = None,
        quiet: bool = False,
    ):
        """Read-only lint of repo structure, language completeness, descriptions.

        :param project_root: any directory inside the teaching repo
            (default: current working directory).
        :param quiet: suppress normal output.
        """
        repo = _resolve(project_root)
        problems = make_linter(repo).lint()
        if problems:
            for problem in problems:
                print(f"FAIL: {problem}", file=sys.stderr)
            print(f"{len(problems)} problem(s) found.", file=sys.stderr)
            raise SystemExit(1)
        if not quiet:
            print("OK: repo structure, language versions and descriptions are consistent.")


def main():
    """Console script entry point (``lesson-smith``)."""
    fire.Fire(Command)
