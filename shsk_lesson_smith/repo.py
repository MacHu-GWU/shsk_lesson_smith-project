# -*- coding: utf-8 -*-

"""Filesystem model of a lesson-smith teaching repository.

:class:`StandardRepo` is the layout every teaching repo shares, whatever its
type. Naming conventions on the class:

- ``dir_xxx`` cached properties are directories.
- ``path_xxx`` cached properties are files.
- ``get_xxx(lang=...)`` methods return the language variant of a special file
  (``lang=None`` means English, which carries no suffix).

The core field is ``dir_project_root``. Construct a repo directly when the
root is already known (test fixtures do this, since a nested ``.git`` dir
cannot be committed to git), or use the :meth:`StandardRepo.from_cwd` factory
to resolve the root the way ``git rev-parse --show-toplevel`` works: walk up
from a working directory until a directory containing both ``.git`` and
``mise.toml`` is found.
"""

import dataclasses
import json
import subprocess
from functools import cached_property
from pathlib import Path

from .constants import (
    SYLLABUS_BASE,
    TASK_DIR_PREFIX_PATTERN,
    LangEnum,
    RepoTypeEnum,
)


def to_lang(lang: "LangEnum | str | None") -> "LangEnum | None":
    """Normalize a language argument. ``None`` means English.

    A plain string is validated against :class:`LangEnum` and raises
    ``ValueError`` when the code is not supported.
    """
    if lang is None or isinstance(lang, LangEnum):
        return lang
    return LangEnum(lang)


def get_variant_filename(
    base: str,
    lang: "LangEnum | str | None" = None,
) -> str:
    """File name of a special file variant: ``README.md`` / ``README-cn.md``."""
    lang = to_lang(lang)
    if lang is None:
        return f"{base}.md"
    return f"{base}-{lang.value}.md"


def read_frontmatter_description(path: Path) -> "str | None":
    """Extract the one-line ``description`` from a file's YAML frontmatter.

    Returns None when the file does not exist, has no frontmatter, or has no
    one-line ``description`` key.
    """
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
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


@dataclasses.dataclass
class StandardRepo:
    """The directory layout standard shared by every teaching repo type.

    Type-specific repos (evolve / showcase / upskill) subclass this in
    ``repo_types.py`` and add their own paths.
    """

    dir_project_root: Path

    def __post_init__(self):
        self.dir_project_root = Path(self.dir_project_root).resolve()

    @classmethod
    def from_cwd(cls, dir_cwd: "Path | str | None" = None) -> "StandardRepo":
        """Factory: locate the project root by walking up from ``dir_cwd``.

        The root is the nearest ancestor (including ``dir_cwd`` itself, which
        defaults to the current working directory) holding both ``.git`` and
        ``mise.toml``. ``.git`` only needs to exist (it is a file, not a
        directory, in a git worktree checkout).
        """
        dir_cwd = Path(dir_cwd).resolve() if dir_cwd is not None else Path.cwd()
        for directory in [dir_cwd, *dir_cwd.parents]:
            if (directory / ".git").exists() and (directory / "mise.toml").is_file():
                return cls(dir_project_root=directory)
        raise FileNotFoundError(
            f"cannot locate project root from {dir_cwd}: "
            "no ancestor directory contains both .git and mise.toml"
        )

    # ------------------------------------------------------------------ #
    # Repo-level special files
    # ------------------------------------------------------------------ #
    @cached_property
    def path_lm_json(self) -> Path:
        """Machine-readable manifest declaring the repo type."""
        return self.dir_project_root / "lm.json"

    @cached_property
    def path_readme(self) -> Path:
        return self.get_path_readme()

    @cached_property
    def path_ticket(self) -> Path:
        return self.get_path_ticket()

    @cached_property
    def path_readme_original(self) -> Path:
        return self.get_path_readme_original()

    def get_path_readme(self, lang: "LangEnum | str | None" = None) -> Path:
        return self.dir_project_root / get_variant_filename("README", lang)

    def get_path_ticket(self, lang: "LangEnum | str | None" = None) -> Path:
        return self.dir_project_root / get_variant_filename("TICKET", lang)

    def get_path_readme_original(self, lang: "LangEnum | str | None" = None) -> Path:
        return self.dir_project_root / get_variant_filename("README-ORIGINAL", lang)

    # ------------------------------------------------------------------ #
    # docs/tasks aggregation view
    # ------------------------------------------------------------------ #
    @cached_property
    def dir_docs(self) -> Path:
        return self.dir_project_root / "docs"

    @cached_property
    def dir_docs_tasks(self) -> Path:
        return self.dir_docs / "tasks"

    @cached_property
    def path_syllabus(self) -> Path:
        return self.get_path_syllabus()

    def get_path_syllabus(self, lang: "LangEnum | str | None" = None) -> Path:
        return self.dir_docs_tasks / get_variant_filename(SYLLABUS_BASE, lang)

    def get_dir_task(self, branch_name: str) -> Path:
        """Snapshot directory of one task: ``docs/tasks/<branch_name>/``."""
        return self.dir_docs_tasks / branch_name

    def iter_task_dirs(self) -> "list[Path]":
        """Task snapshot dirs under docs/tasks/, sorted by branch number."""
        if not self.dir_docs_tasks.exists():
            return []
        return sorted(
            d
            for d in self.dir_docs_tasks.iterdir()
            if d.is_dir() and TASK_DIR_PREFIX_PATTERN.match(d.name)
        )

    # ------------------------------------------------------------------ #
    # Repo metadata
    # ------------------------------------------------------------------ #
    @cached_property
    def repo_type(self) -> "RepoTypeEnum | None":
        """Repo type declared in lm.json, or None when missing / invalid."""
        path = self.path_lm_json
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        try:
            return RepoTypeEnum(data.get("type"))
        except (ValueError, AttributeError):
            return None

    @cached_property
    def current_branch(self) -> str:
        """Current git branch name (empty string when HEAD is detached)."""
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=self.dir_project_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
