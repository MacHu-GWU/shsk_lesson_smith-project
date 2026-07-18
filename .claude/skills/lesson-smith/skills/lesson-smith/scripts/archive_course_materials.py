#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Archive course materials to docs/tutorials/${BRANCH_NAME}/

This script copies README.md, README-cn.md, and TICKET.md from the project root
to docs/tutorials/${BRANCH_NAME}/, creating the directory if needed.

Usage:
    python archive_course_materials.py

No external dependencies required (stdlib only).
"""

import shutil
import subprocess
from pathlib import Path


def get_project_root() -> Path:
    """Get the project root directory (where .git is located)."""
    dir_here = Path(__file__).absolute().parent
    # Navigate up from: .claude/skills/lesson-smith/scripts/ -> project root
    return dir_here.parent.parent.parent.parent


def get_current_branch_name(project_root: Path) -> str:
    """Get the current git branch name."""
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=project_root,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def archive_course_materials() -> None:
    """Copy course materials to docs/tutorials/${BRANCH_NAME}/."""
    project_root = get_project_root()
    branch_name = get_current_branch_name(project_root)

    if not branch_name:
        print("Error: Could not determine current branch name.")
        print("Are you in a detached HEAD state?")
        return

    # Source files
    files_to_copy = ["README.md", "README-cn.md", "TICKET.md"]

    # Destination directory
    dst_dir = project_root / "docs" / "tutorials" / branch_name
    dst_dir.mkdir(parents=True, exist_ok=True)

    print(f"Project root: {project_root}")
    print(f"Branch name: {branch_name}")
    print(f"Destination: {dst_dir}")
    print()

    copied = []
    skipped = []

    for filename in files_to_copy:
        src_path = project_root / filename
        dst_path = dst_dir / filename

        if src_path.exists():
            shutil.copy2(src_path, dst_path)
            copied.append(filename)
            print(f"  Copied: {filename}")
        else:
            skipped.append(filename)
            print(f"  Skipped (not found): {filename}")

    print()
    print(f"Done! Copied {len(copied)} file(s) to {dst_dir.relative_to(project_root)}/")

    if skipped:
        print(f"Warning: {len(skipped)} file(s) not found: {', '.join(skipped)}")


if __name__ == "__main__":
    archive_course_materials()
