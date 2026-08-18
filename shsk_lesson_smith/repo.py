# -*- coding: utf-8 -*-

"""Filesystem model of a lesson-smith teaching repository.

This module is only about *where things live*: it turns a project root into
typed path accessors. It reads no file content and runs no git command beyond
locating the root; linting, syncing, and parsing live elsewhere.
"""

import typing as T
import dataclasses
import json
from pathlib import Path
from functools import cached_property

from .constants import (
    ESTIMATED_HOURS_LOWER_FIELD,
    ESTIMATED_HOURS_UPPER_FIELD,
    minutes_to_hours,
    README_BASE,
    TICKET_BASE,
    README_ORIGINAL_BASE,
    SYLLABUS_BASE,
    TASK_DIR_PREFIX_PATTERN,
    LangEnum,
    RepoTypeEnum,
)
from .linter_utils import MarkdownFile


def to_lang(lang: "LangEnum | str | None") -> "LangEnum | None":
    """Normalize a language argument. ``None`` means English (no suffix).

    A plain string is validated against :class:`LangEnum` and raises
    ``ValueError`` when the code is not supported.
    """
    if lang is None or isinstance(lang, LangEnum):
        return lang
    return LangEnum(lang)


def get_variant_name(
    base: str,
    lang: "LangEnum | str | None" = None,
) -> str:
    """Name of a language variant, without any extension.

    ``README`` / ``README-cn``, ``upskill-learn`` / ``upskill-learn-cn``. Used
    for things whose language suffix sits on a bare name rather than a file
    name, such as the forge-generated child skill directories.
    """
    lang = to_lang(lang)
    if lang is None:
        return base
    return f"{base}-{lang.value}"


def get_variant_filename(
    base: str,
    lang: "LangEnum | str | None" = None,
) -> str:
    """File name of a special file variant: ``README.md`` / ``README-cn.md``."""
    return f"{get_variant_name(base, lang)}.md"


def resolve_repo(dir_cwd: "Path | str | None" = None) -> Path:
    """Locate the teaching repo root by walking up from ``dir_cwd``.

    The root is the nearest ancestor (including ``dir_cwd`` itself, which
    defaults to the current working directory) that holds both ``.git`` and
    ``mise.toml``. ``.git`` only needs to exist (it is a file, not a directory,
    inside a git worktree checkout). This mirrors ``git rev-parse
    --show-toplevel`` but keys off our own markers.

    Raises ``FileNotFoundError`` when no ancestor qualifies.
    """
    dir_cwd = Path(dir_cwd).resolve() if dir_cwd is not None else Path.cwd()
    for directory in [dir_cwd, *dir_cwd.parents]:
        if (directory / ".git").exists() and (directory / "mise.toml").is_file():
            return directory
    raise FileNotFoundError(
        f"cannot locate project root from {dir_cwd}: "
        "no ancestor directory contains both .git and mise.toml"
    )


@dataclasses.dataclass
class Metadata:
    """Parsed ``lm.json`` manifest. Base for per-type metadata subclasses.

    The manifest carries ``type`` plus the repo-level estimated time bounds. It
    is kept as a dataclass (not a bare enum) so the manifest can grow more
    structured fields later without touching call sites, and so each repo type
    can subclass it (e.g. ``UpskillMetadata`` in ``repo_for_upskill.py``) to add
    fields specific to that type. Each per-type Repo subclass overrides its
    ``metadata`` property to parse into the matching subclass, via
    :meth:`load_or_none`.

    ``estimated_hours_lower`` / ``estimated_hours_upper`` are the whole repo's
    time budget in decimal hours, summed across every branch's TICKET. They are
    written by ``lesson-smith sync``, not by hand, and are None on a manifest
    that predates them or has not been synced yet.

    ``__post_init__`` coerces and validates ``type`` into a
    :class:`RepoTypeEnum`, raising ``ValueError`` for anything else.
    """

    type: RepoTypeEnum
    estimated_hours_lower: "float | None" = None
    estimated_hours_upper: "float | None" = None

    def __post_init__(self):
        # Coerce a raw string (or reject anything invalid) into the enum.
        self.type = RepoTypeEnum(self.type)

    @classmethod
    def from_dict(cls, data: dict) -> "T.Self":
        """Build from an already-parsed JSON object."""
        if not isinstance(data, dict):
            raise ValueError("lm.json must contain a JSON object")
        return cls(
            type=data.get("type"),
            estimated_hours_lower=data.get(ESTIMATED_HOURS_LOWER_FIELD),
            estimated_hours_upper=data.get(ESTIMATED_HOURS_UPPER_FIELD),
        )

    def to_dict(self) -> dict:
        """Serialize back to the lm.json shape, omitting unset time bounds.

        Field order is the manifest's reading order: what the repo is, then how
        long it takes. Bounds that are None are left out entirely rather than
        written as ``null``, so a manifest that has never been synced keeps the
        same one-field shape it started with.
        """
        data: dict = {"type": self.type.value}
        if self.estimated_hours_lower is not None:
            data[ESTIMATED_HOURS_LOWER_FIELD] = self.estimated_hours_lower
        if self.estimated_hours_upper is not None:
            data[ESTIMATED_HOURS_UPPER_FIELD] = self.estimated_hours_upper
        return data

    @classmethod
    def from_json_file(cls, path: "Path | str") -> "T.Self":
        """Read and parse an ``lm.json`` file into a :class:`Metadata`."""
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_dict(data)

    @classmethod
    def load_or_none(cls, path: "Path | str") -> "T.Self | None":
        """Parse ``lm.json`` gracefully: return None instead of raising.

        Consumers like the linter want to keep running and report a bad manifest
        themselves, so a missing / unreadable / invalid file maps to None.
        """
        try:
            return cls.from_json_file(path)
        except (OSError, json.JSONDecodeError, ValueError):
            return None


@dataclasses.dataclass(frozen=True)
class Repo:
    """A teaching repository, addressed by paths.

    One class models every repo type (evolve / showcase / upskill); the layout
    is a union. ``examples/`` is the only type-specific branch, so the accessors
    for it return ``None`` outside showcase / upskill; everything else is a plain
    path that exists in the model regardless of whether the file is on disk yet.

    The object is a pure in-memory address book: constructing it and reading its
    ``path_*`` / ``dir_*`` accessors touches no files. Actually reaching the disk
    happens only when you call a method that needs to (``iter_dir_*`` scans,
    :attr:`metadata` reads lm.json) or when you pull content through a returned
    :class:`MarkdownFile` (which itself reads lazily on first ``.text`` access).

    Accessor naming:

    - ``path_*`` cached properties are files (a :class:`~pathlib.Path`).
    - ``dir_*`` cached properties are directories (a :class:`~pathlib.Path`).
    - ``md_*`` cached properties wrap a special markdown file in a
      :class:`MarkdownFile`, for convenient content access.
    - ``get_path_*`` / ``get_md_*`` ``(lang=...)`` methods build the language
      variant (``lang=None`` is English, which carries no suffix). The
      ``path_*`` / ``md_*`` twin of each is just the English variant, cached.

    Directory layout (union of all repo types)::

        <project_root>/
        |-- lm.json                      manifest: {"type": evolve|showcase|upskill}
        |-- README.md                    + README-<lang>.md
        |-- TICKET.md                    + TICKET-<lang>.md
        |-- README-ORIGINAL.md           + README-ORIGINAL-<lang>.md
        |-- docs/
        |   `-- tasks/
        |       |-- SYLLABUS.md          + SYLLABUS-<lang>.md   (generated)
        |       `-- NN-branch-name/      per-task snapshot
        |           |-- README.md        + README-<lang>.md
        |           `-- TICKET.md        + TICKET-<lang>.md
        `-- examples/                    showcase / upskill only
            `-- NN-title/                one task
                |-- README.md            + README-<lang>.md
                `-- TICKET.md            + TICKET-<lang>.md
    """

    dir_project_root: Path

    def __post_init__(self):
        # Frozen dataclass: assign the normalized value through object.__setattr__.
        object.__setattr__(self, "dir_project_root", Path(self.dir_project_root))

    @classmethod
    def from_cwd(cls, dir_cwd: "Path | str | None" = None) -> "T.Self":
        """Build a :class:`Repo` by resolving the root from ``dir_cwd``."""
        return cls(dir_project_root=resolve_repo(dir_cwd))

    # ------------------------------------------------------------------ #
    # Manifest
    # ------------------------------------------------------------------ #
    @cached_property
    def path_lm_json(self) -> Path:
        """Machine-readable manifest that declares the repo ``type``."""
        return self.dir_project_root / "lm.json"

    @cached_property
    def metadata(self) -> "Metadata | None":
        """Parsed ``lm.json``, or None when it is missing / unreadable / invalid.

        Per-type Repo subclasses override this to parse into their own
        :class:`Metadata` subclass (see repo_for_upskill.py), which is why it is
        an explicit override rather than a class-attribute hook.
        """
        return Metadata.load_or_none(self.path_lm_json)

    @property
    def repo_type(self) -> "RepoTypeEnum | None":
        """Repo type from the manifest, or None when the manifest is unusable.

        The ``examples/`` accessors gate on this.
        """
        return self.metadata.type if self.metadata else None

    @property
    def has_examples_layout(self) -> bool:
        """Whether this repo type keeps tasks under ``examples/``."""
        return self.repo_type in (
            RepoTypeEnum.showcase,
            RepoTypeEnum.upskill,
            RepoTypeEnum.readup,
        )

    @property
    def single_task_branch(self) -> "str | None":
        """The fixed task-branch name for a single-branch repo type (``01-<type>``).

        Showcase, upskill, and readup repos have exactly one task branch, named
        after the type (``01-showcase`` / ``01-upskill`` / ``01-readup``). Returns
        None for evolve, whose branch names are arbitrary and come from git.
        Shared by the linter (to enforce the name) and by sync (to know where to
        snapshot).
        """
        if self.repo_type in (
            RepoTypeEnum.showcase,
            RepoTypeEnum.upskill,
            RepoTypeEnum.readup,
        ):
            return f"01-{self.repo_type.value}"
        return None

    # ------------------------------------------------------------------ #
    # Repo-level special files (project root)
    # ------------------------------------------------------------------ #
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
        return self.dir_project_root / get_variant_filename(README_BASE, lang)

    def get_path_ticket(self, lang: "LangEnum | str | None" = None) -> Path:
        return self.dir_project_root / get_variant_filename(TICKET_BASE, lang)

    def get_path_readme_original(self, lang: "LangEnum | str | None" = None) -> Path:
        return self.dir_project_root / get_variant_filename(README_ORIGINAL_BASE, lang)

    @cached_property
    def md_readme(self) -> MarkdownFile:
        return self.get_md_readme()

    @cached_property
    def md_ticket(self) -> MarkdownFile:
        return self.get_md_ticket()

    @cached_property
    def md_readme_original(self) -> MarkdownFile:
        return self.get_md_readme_original()

    def get_md_readme(self, lang: "LangEnum | str | None" = None) -> MarkdownFile:
        return MarkdownFile(self.get_path_readme(lang))

    def get_md_ticket(self, lang: "LangEnum | str | None" = None) -> MarkdownFile:
        return MarkdownFile(self.get_path_ticket(lang))

    def get_md_readme_original(
        self, lang: "LangEnum | str | None" = None
    ) -> MarkdownFile:
        return MarkdownFile(self.get_path_readme_original(lang))

    # ------------------------------------------------------------------ #
    # docs/tasks aggregation view (all repo types)
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

    @cached_property
    def md_syllabus(self) -> MarkdownFile:
        return self.get_md_syllabus()

    def get_md_syllabus(self, lang: "LangEnum | str | None" = None) -> MarkdownFile:
        return MarkdownFile(self.get_path_syllabus(lang))

    def get_dir_task(self, task_name: str) -> Path:
        """Per-task snapshot directory: ``docs/tasks/<task_name>/``."""
        return self.dir_docs_tasks / task_name

    def get_path_task_readme(
        self, task_name: str, lang: "LangEnum | str | None" = None
    ) -> Path:
        """``docs/tasks/<task_name>/README[-<lang>].md``."""
        return self.get_dir_task(task_name) / get_variant_filename(README_BASE, lang)

    def get_path_task_ticket(
        self, task_name: str, lang: "LangEnum | str | None" = None
    ) -> Path:
        """``docs/tasks/<task_name>/TICKET[-<lang>].md``."""
        return self.get_dir_task(task_name) / get_variant_filename(TICKET_BASE, lang)

    def get_md_task_readme(
        self, task_name: str, lang: "LangEnum | str | None" = None
    ) -> MarkdownFile:
        return MarkdownFile(self.get_path_task_readme(task_name, lang))

    def get_md_task_ticket(
        self, task_name: str, lang: "LangEnum | str | None" = None
    ) -> MarkdownFile:
        return MarkdownFile(self.get_path_task_ticket(task_name, lang))

    def iter_dir_tasks(self) -> "list[Path]":
        """Task snapshot dirs under ``docs/tasks/``, sorted by branch number."""
        return _iter_numbered_dirs(self.dir_docs_tasks)

    # ------------------------------------------------------------------ #
    # examples view (showcase / upskill only)
    # ------------------------------------------------------------------ #
    @cached_property
    def dir_examples(self) -> "Path | None":
        """``examples/`` dir, or None for a repo type that has no examples layout."""
        if not self.has_examples_layout:
            return None
        return self.dir_project_root / "examples"

    def get_dir_example(self, example_name: str) -> "Path | None":
        """One task dir ``examples/<example_name>/``, or None if not applicable."""
        if self.dir_examples is None:
            return None
        return self.dir_examples / example_name

    def get_path_example_readme(
        self, example_name: str, lang: "LangEnum | str | None" = None
    ) -> "Path | None":
        """``examples/<example_name>/README[-<lang>].md``, or None if not applicable."""
        dir_example = self.get_dir_example(example_name)
        if dir_example is None:
            return None
        return dir_example / get_variant_filename(README_BASE, lang)

    def get_path_example_ticket(
        self, example_name: str, lang: "LangEnum | str | None" = None
    ) -> "Path | None":
        """``examples/<example_name>/TICKET[-<lang>].md``, or None if not applicable."""
        dir_example = self.get_dir_example(example_name)
        if dir_example is None:
            return None
        return dir_example / get_variant_filename(TICKET_BASE, lang)

    def get_md_example_readme(
        self, example_name: str, lang: "LangEnum | str | None" = None
    ) -> "MarkdownFile | None":
        path = self.get_path_example_readme(example_name, lang)
        return MarkdownFile(path) if path is not None else None

    def get_md_example_ticket(
        self, example_name: str, lang: "LangEnum | str | None" = None
    ) -> "MarkdownFile | None":
        path = self.get_path_example_ticket(example_name, lang)
        return MarkdownFile(path) if path is not None else None

    def iter_dir_examples(self) -> "list[Path]":
        """Mini task dirs under ``examples/``, sorted; empty if not applicable."""
        if self.dir_examples is None:
            return []
        return _iter_numbered_dirs(self.dir_examples)


def _iter_numbered_dirs(parent: Path) -> "list[Path]":
    """Subdirectories of ``parent`` whose name starts ``NN-``, sorted by name."""
    if not parent.exists():
        return []
    return sorted(
        d
        for d in parent.iterdir()
        if d.is_dir() and TASK_DIR_PREFIX_PATTERN.match(d.name)
    )


# --------------------------------------------------------------------------- #
# Repo-level estimated time.
#
# Each branch's TICKET carries one minute range; the repo's total is the straight
# sum of those ranges. It is computed from the ``docs/tasks/`` snapshots rather
# than from the working tree, because those snapshots are the one place where
# every branch is visible at once — the working tree only ever has one branch
# checked out.
#
# Lives here, next to Repo, because both consumers need it: ``sync`` writes the
# total into lm.json and the linter re-derives it to check the manifest did not
# drift. Same shape as the SYLLABUS, which sync generates and the linter
# re-derives.
# --------------------------------------------------------------------------- #
@dataclasses.dataclass
class EstimatedTime:
    """A repo's summed time budget, plus the branches that could not be read."""

    lower_minutes: int
    upper_minutes: int
    branches_without_estimate: "list[str]" = dataclasses.field(default_factory=list)

    @property
    def lower_hours(self) -> float:
        """Lower bound in decimal hours, rounded for storage in lm.json."""
        return minutes_to_hours(self.lower_minutes)

    @property
    def upper_hours(self) -> float:
        """Upper bound in decimal hours, rounded for storage in lm.json."""
        return minutes_to_hours(self.upper_minutes)

    @property
    def is_complete(self) -> bool:
        """Whether every branch contributed a parseable estimate."""
        return not self.branches_without_estimate


def estimate_repo_time(repo: "Repo") -> EstimatedTime:
    """Sum every ``docs/tasks/<branch>/TICKET`` estimate into a repo total.

    For each branch the first language variant that yields a parseable estimate
    wins, so a repo written in Chinese with empty English placeholders works
    without the caller naming a language. A branch whose TICKET has no usable
    estimate contributes nothing and is named in
    :attr:`EstimatedTime.branches_without_estimate`, so callers can refuse to
    write or trust a total that is silently short.
    """
    langs = (None, *LangEnum)
    lower = upper = 0
    missing: "list[str]" = []
    for dir_task in repo.iter_dir_tasks():
        found = None
        for lang in langs:
            path = repo.get_path_task_ticket(dir_task.name, lang)
            if not path.exists():
                continue
            found = MarkdownFile(path).estimated_minutes
            if found is not None:
                break
        if found is None:
            missing.append(dir_task.name)
            continue
        lower += found[0]
        upper += found[1]
    return EstimatedTime(
        lower_minutes=lower, upper_minutes=upper, branches_without_estimate=missing
    )
