# -*- coding: utf-8 -*-

"""Lint rules for lesson-smith teaching repositories.

The base :class:`Linter` carries the rules every repo type shares (manifest,
language completeness, frontmatter descriptions, task snapshot dirs). Each
repo type gets its own subclass with extra structural rules. Use
:func:`make_linter` to pick the right one for a repo.
"""

import dataclasses
import json
from pathlib import Path

from .constants import (
    DESCRIPTION_FORBIDDEN_CHARS,
    MAX_DESCRIPTION_CHARS,
    REPO_FILE_BASES,
    TASK_DIR_PATTERN,
    TASK_FILE_BASES,
    LangEnum,
    RepoTypeEnum,
)
from .repo import (
    StandardRepo,
    get_variant_filename,
    read_frontmatter_description,
)
from .repo_types import ShowcaseRepo


@dataclasses.dataclass
class LintProblem:
    """One lint finding: where it is and what is wrong."""

    location: str
    message: str

    def __str__(self) -> str:
        return f"{self.location}: {self.message}"


@dataclasses.dataclass
class Linter:
    """Shared lint rules; also the fallback when the repo type is unknown."""

    repo: StandardRepo

    # Special file bases that MUST exist at the project root for this repo
    # type. Bases not listed here are optional, but once any language variant
    # exists, all variants must exist.
    required_root_bases: "tuple[str, ...]" = dataclasses.field(
        default=(), init=False, repr=False
    )

    def lint(self) -> "list[LintProblem]":
        """Run every rule and return the list of problems (empty = clean)."""
        problems: "list[LintProblem]" = []
        self._lint_manifest(problems)
        for base in REPO_FILE_BASES:
            self._lint_file_group(
                self.repo.dir_project_root,
                base,
                required=base in self.required_root_bases,
                problems=problems,
            )
        self._lint_task_snapshots(problems)
        self._lint_type_specific(problems)
        return problems

    # ------------------------------------------------------------------ #
    # Shared rules
    # ------------------------------------------------------------------ #
    def _lint_manifest(self, problems: "list[LintProblem]") -> None:
        """lm.json must exist, parse as JSON, and declare a valid type."""
        path = self.repo.path_lm_json
        if not path.exists():
            problems.append(
                LintProblem("lm.json", "manifest file is missing at the repo root")
            )
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            problems.append(LintProblem("lm.json", "manifest is not valid JSON"))
            return
        if not isinstance(data, dict):
            problems.append(LintProblem("lm.json", "manifest must be a JSON object"))
            return
        valid_types = [t.value for t in RepoTypeEnum]
        if data.get("type") not in valid_types:
            problems.append(
                LintProblem(
                    "lm.json",
                    f"'type' must be one of {valid_types}, got {data.get('type')!r}",
                )
            )

    def _lint_file_group(
        self,
        directory: Path,
        base: str,
        required: bool,
        problems: "list[LintProblem]",
    ) -> None:
        """Lint one special file and all its language variants in a directory.

        Rules: if the file is required, or any variant of it exists, then the
        English version plus every supported language variant must exist; each
        existing variant must carry a valid frontmatter description.
        """
        variants = [
            directory / get_variant_filename(base, lang) for lang in (None, *LangEnum)
        ]
        existing = [p for p in variants if p.exists()]
        if not existing:
            if required:
                problems.append(
                    LintProblem(
                        self._rel(variants[0]),
                        "required file is missing (along with its language variants)",
                    )
                )
            return
        for path in variants:
            if not path.exists():
                problems.append(
                    LintProblem(self._rel(path), "missing language variant")
                )
        for path in existing:
            self._lint_description(path, problems)

    def _lint_description(
        self,
        path: Path,
        problems: "list[LintProblem]",
    ) -> None:
        """Frontmatter description: present, one non-empty line, length, charset."""
        desc = read_frontmatter_description(path)
        if desc is None:
            problems.append(
                LintProblem(
                    self._rel(path),
                    "missing a one-line 'description' in YAML frontmatter",
                )
            )
            return
        if not desc.strip():
            problems.append(
                LintProblem(
                    self._rel(path),
                    "'description' must be a non-empty one-line value",
                )
            )
            return
        if len(desc) > MAX_DESCRIPTION_CHARS:
            problems.append(
                LintProblem(
                    self._rel(path),
                    f"description is {len(desc)} chars "
                    f"(max {MAX_DESCRIPTION_CHARS})",
                )
            )
        forbidden = sorted({c for c in desc if c in DESCRIPTION_FORBIDDEN_CHARS})
        if forbidden:
            problems.append(
                LintProblem(
                    self._rel(path),
                    f"description contains forbidden character(s): "
                    f"{' '.join(forbidden)}",
                )
            )

    def _lint_task_snapshots(self, problems: "list[LintProblem]") -> None:
        """docs/tasks/<branch>/ dirs: strict names, complete README + TICKET."""
        if not self.repo.dir_docs_tasks.exists():
            return
        for directory in sorted(
            d for d in self.repo.dir_docs_tasks.iterdir() if d.is_dir()
        ):
            self._lint_task_dir(directory, problems)

    def _lint_task_dir(
        self,
        directory: Path,
        problems: "list[LintProblem]",
    ) -> None:
        """One task-shaped dir: NN-lowercase-hyphen name, full file groups."""
        if not TASK_DIR_PATTERN.match(directory.name):
            problems.append(
                LintProblem(
                    self._rel(directory),
                    "dir name must match NN-lowercase-hyphen-words "
                    "(e.g. 01-branch-name)",
                )
            )
            return
        for base in TASK_FILE_BASES:
            self._lint_file_group(directory, base, required=True, problems=problems)

    def _lint_type_specific(self, problems: "list[LintProblem]") -> None:
        """Extra structural rules; overridden by per-type linters."""

    def _rel(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.repo.dir_project_root))
        except ValueError:
            return str(path)


@dataclasses.dataclass
class EvolveLinter(Linter):
    """Evolve repos: root README / TICKET are the current task's files."""

    def __post_init__(self):
        self.required_root_bases = ("README", "TICKET", "README-ORIGINAL")

    def _lint_type_specific(self, problems: "list[LintProblem]") -> None:
        if not self.repo.dir_docs_tasks.exists():
            problems.append(
                LintProblem("docs/tasks", "aggregation view directory is missing")
            )


@dataclasses.dataclass
class ShowcaseLinter(Linter):
    """Showcase repos: mini tasks live in examples/NN-title/."""

    def __post_init__(self):
        self.required_root_bases = ("README", "README-ORIGINAL")

    def _lint_type_specific(self, problems: "list[LintProblem]") -> None:
        repo = self.repo
        if isinstance(repo, ShowcaseRepo):
            dir_examples = repo.dir_examples
        else:
            dir_examples = repo.dir_project_root / "examples"
        if not dir_examples.exists():
            problems.append(
                LintProblem("examples", "examples/ directory is missing")
            )
            return
        for directory in sorted(d for d in dir_examples.iterdir() if d.is_dir()):
            self._lint_task_dir(directory, problems)


@dataclasses.dataclass
class UpskillLinter(ShowcaseLinter):
    """Upskill repos share the showcase layout, hence the showcase rules."""


REPO_TYPE_TO_LINTER: "dict[RepoTypeEnum, type[Linter]]" = {
    RepoTypeEnum.evolve: EvolveLinter,
    RepoTypeEnum.showcase: ShowcaseLinter,
    RepoTypeEnum.upskill: UpskillLinter,
}


def make_linter(repo: StandardRepo) -> Linter:
    """Pick the linter class matching the repo's declared type."""
    klass = REPO_TYPE_TO_LINTER.get(repo.repo_type, Linter)
    return klass(repo=repo)
