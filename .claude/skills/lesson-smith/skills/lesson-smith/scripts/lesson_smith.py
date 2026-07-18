#!/usr/bin/env python3

"""Maintain and validate a lesson-smith teaching repository.

This is the single CLI entry point for every automation the lesson-smith skill
family needs. It follows scripts/python-cli-script-standard.md: the standard's
two-layer structure is adapted for sub-commands, so each sub-command has its own
typed ``_cmd_*`` worker (the ``_main`` equivalent) that holds the logic and
returns an exit code, while ``main`` only parses argv and dispatches.

Sub-commands:
    sync    Snapshot the current branch's task files into docs/tasks/<branch>/
            and regenerate docs/tasks/SYLLABUS.md (write operation).
    check   Read-only lint: verify language completeness and one-line
            description frontmatter across the repo's special files.

NOTE: The current logic targets the evolve layout (root-level README/TICKET
per task, snapshotted into docs/tasks/). Handling of the showcase / upskill
layout (examples/NN-title/) is still TODO.
The SYLLABUS format follows ref/syllabus-spec.md.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Name-body of the per-task special files that get snapshotted into
# docs/tasks/<branch>/. README-ORIGINAL and SYLLABUS are repo-level, not here.
TASK_FILES = ("README", "TICKET")

# Name-body of the repo-level special files that live at the project root.
REPO_FILES = ("README", "TICKET", "README-ORIGINAL")

MAX_DESCRIPTION_CHARS = 400
BRANCH_DIR_RE = re.compile(r"^\d\d-")


# --------------------------------------------------------------------------- #
# Shared helpers
# --------------------------------------------------------------------------- #
def _skill_root() -> Path:
    """Return the skill root directory (parent of this scripts/ directory)."""
    return Path(__file__).resolve().parent.parent


def load_supported_languages() -> list[str]:
    """Load the list of non-English language codes from supported-languages.json."""
    data = json.loads(
        (_skill_root() / "supported-languages.json").read_text(encoding="utf-8")
    )
    return list(data)


def get_project_root(explicit: Path | None) -> Path:
    """Resolve the teaching repo root: the explicit value, else the git toplevel."""
    if explicit is not None:
        return explicit.resolve()
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=Path(__file__).resolve().parent,
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(result.stdout.strip())


def get_current_branch(project_root: Path) -> str:
    """Return the current git branch name (empty string if detached)."""
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=project_root,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def language_variants(base: str, langs: list[str]) -> list[str]:
    """File names for a special file base: English (no suffix) plus each language."""
    return [f"{base}.md"] + [f"{base}-{lang}.md" for lang in langs]


def read_description(md_file: Path) -> str | None:
    """Extract the one-line ``description`` from a file's YAML frontmatter.

    Returns None when the file has no frontmatter or no description key.
    """
    lines = md_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("description:"):
            value = line[len("description:") :].strip()
            if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
                value = value[1:-1]
            return value
    return None


# --------------------------------------------------------------------------- #
# sync
# --------------------------------------------------------------------------- #
def _cmd_sync(
    project_root: Path,
    quiet: bool = False,
) -> int:
    """Snapshot the current branch's task files, then regenerate the syllabus."""
    branch = get_current_branch(project_root)
    if not branch:
        print(
            "ERROR: could not determine current branch (detached HEAD?)",
            file=sys.stderr,
        )
        return 1

    langs = load_supported_languages()
    dst_dir = project_root / "docs" / "tasks" / branch
    dst_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    for base in TASK_FILES:
        for name in language_variants(base, langs):
            src = project_root / name
            if src.exists():
                shutil.copy2(src, dst_dir / name)
                copied += 1
                if not quiet:
                    print(f"  snapshot: {name} -> docs/tasks/{branch}/{name}")

    if copied == 0 and not quiet:
        print(f"  warning: no task files found at repo root for branch {branch}")

    _generate_syllabus(project_root, langs, quiet=quiet)

    if not quiet:
        print(f"Done. Snapshotted {copied} file(s) into docs/tasks/{branch}/.")
    return 0


def _generate_syllabus(
    project_root: Path,
    langs: list[str],
    quiet: bool = False,
) -> None:
    """Regenerate docs/tasks/SYLLABUS[-<lang>].md per ref/syllabus-spec.md.

    Emits ``# Syllabus`` then, for each task in ascending order, an H2 with the
    branch dir name verbatim (all lowercase) followed by the task README's
    frontmatter description verbatim.
    """
    tasks_dir = project_root / "docs" / "tasks"
    task_dirs = sorted(
        d for d in tasks_dir.iterdir() if d.is_dir() and BRANCH_DIR_RE.match(d.name)
    )

    for lang in [None, *langs]:
        suffix = "" if lang is None else f"-{lang}"
        readme_name = f"README{suffix}.md"
        sections = ["# Syllabus"]
        for d in task_dirs:
            readme = d / readme_name
            desc = read_description(readme) if readme.exists() else None
            if desc is None:
                desc = ""
            sections.append(f"## {d.name}\n\n{desc}")
        out_path = tasks_dir / f"SYLLABUS{suffix}.md"
        out_path.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
        if not quiet:
            print(
                f"  syllabus: wrote docs/tasks/SYLLABUS{suffix}.md ({len(task_dirs)} tasks)"
            )


# --------------------------------------------------------------------------- #
# check
# --------------------------------------------------------------------------- #
def _cmd_check(
    project_root: Path,
    quiet: bool = False,
) -> int:
    """Read-only lint of language completeness and description frontmatter.

    Returns 0 when everything is consistent, 1 when any problem is found.
    """
    langs = load_supported_languages()
    problems: list[str] = []

    _check_language_completeness(project_root, langs, problems)
    _check_descriptions(project_root, langs, problems)
    # TODO: verify docs/tasks/<branch>/ snapshots exist and match the root files.
    # TODO: enforce README description <= 2 sentences (only char/line count is checked now).

    if problems:
        for p in problems:
            print(f"FAIL: {p}", file=sys.stderr)
        print(f"{len(problems)} problem(s) found.", file=sys.stderr)
        return 1
    if not quiet:
        print("OK: language versions and descriptions are consistent.")
    return 0


def _check_language_completeness(
    project_root: Path,
    langs: list[str],
    problems: list[str],
) -> None:
    """For each repo-level special file present, require every language variant."""
    for base in REPO_FILES:
        english = project_root / f"{base}.md"
        if not english.exists():
            continue
        for lang in langs:
            variant = project_root / f"{base}-{lang}.md"
            if not variant.exists():
                problems.append(f"{english.name} exists but {variant.name} is missing")


def _check_descriptions(
    project_root: Path,
    langs: list[str],
    problems: list[str],
) -> None:
    """Each repo-level special file must carry a one-line description <= 200 chars."""
    for base in REPO_FILES:
        for name in language_variants(base, langs):
            path = project_root / name
            if not path.exists():
                continue
            desc = read_description(path)
            if desc is None:
                problems.append(f"{name} is missing a frontmatter description")
            elif len(desc) > MAX_DESCRIPTION_CHARS:
                problems.append(
                    f"{name} description is {len(desc)} chars (max {MAX_DESCRIPTION_CHARS})"
                )


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main(
    argv: list[str] | None = None,
) -> int:
    parser = argparse.ArgumentParser(
        prog="lesson_smith",
        description="Maintain and validate a lesson-smith teaching repository.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_sync = subparsers.add_parser(
        "sync",
        help="snapshot current branch task files and regenerate the syllabus",
    )
    p_sync.add_argument(
        "--project_root",
        type=Path,
        default=None,
        help="repo root (default: git toplevel)",
    )
    p_sync.add_argument(
        "--quiet",
        action="store_true",
        help="suppress normal output",
    )

    p_check = subparsers.add_parser(
        "check",
        help="read-only lint of language completeness and descriptions",
    )
    p_check.add_argument(
        "--project_root",
        type=Path,
        default=None,
        help="repo root (default: git toplevel)",
    )
    p_check.add_argument(
        "--quiet",
        action="store_true",
        help="suppress normal output",
    )

    args = parser.parse_args(argv)
    project_root = get_project_root(args.project_root)

    if args.command == "sync":
        return _cmd_sync(
            project_root=project_root,
            quiet=args.quiet,
        )
    if args.command == "check":
        return _cmd_check(
            project_root=project_root,
            quiet=args.quiet,
        )
    return 2


if __name__ == "__main__":
    sys.exit(main())
