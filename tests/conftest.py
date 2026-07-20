# -*- coding: utf-8 -*-

"""Fixtures that build throwaway teaching repos on the filesystem."""

import json
from pathlib import Path

import pytest


def write_special_file(
    path: Path,
    description: str = "Learn how to do X with Y. 中文叙述 + English terms.",
    body: str = "# Title\n\nbody\n",
):
    """Write a special file with a one-line frontmatter description."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f'---\ndescription: "{description}"\n---\n\n{body}',
        encoding="utf-8",
    )


def make_root(tmp_path: Path, repo_type: str = "evolve") -> Path:
    """Create the minimal root markers: .git/, mise.toml, lm.json."""
    root = tmp_path / "repo"
    (root / ".git").mkdir(parents=True)
    (root / "mise.toml").write_text("", encoding="utf-8")
    (root / "lm.json").write_text(
        json.dumps({"type": repo_type}), encoding="utf-8"
    )
    return root


@pytest.fixture
def evolve_root(tmp_path: Path) -> Path:
    """A fully valid evolve repo: root task files + one task snapshot."""
    root = make_root(tmp_path, "evolve")
    for name in ("README.md", "README-cn.md", "TICKET.md", "TICKET-cn.md",
                 "README-ORIGINAL.md", "README-ORIGINAL-cn.md"):
        write_special_file(root / name)
    task_dir = root / "docs" / "tasks" / "01-intro"
    for name in ("README.md", "README-cn.md", "TICKET.md", "TICKET-cn.md"):
        write_special_file(task_dir / name)
    return root


@pytest.fixture
def showcase_root(tmp_path: Path) -> Path:
    """A fully valid showcase repo: root files + one example mini task."""
    root = make_root(tmp_path, "showcase")
    for name in ("README.md", "README-cn.md",
                 "README-ORIGINAL.md", "README-ORIGINAL-cn.md"):
        write_special_file(root / name)
    example_dir = root / "examples" / "01-hello-world"
    for name in ("README.md", "README-cn.md", "TICKET.md", "TICKET-cn.md"):
        write_special_file(example_dir / name)
    return root
