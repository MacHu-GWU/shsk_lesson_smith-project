# -*- coding: utf-8 -*-

"""Syncing for teaching repos: keep the generated / archived files up to date.

Sync is not pass/fail like linting; it *performs actions* and reports what it
wrote. Design mirrors the linter where it helps:

- Each sync operation is a function ``(repo) -> list[SyncAction]`` that does its
  work and returns what it did. :func:`sync` runs the :data:`OPERATIONS` list in
  order and collects the actions into a :class:`SyncReport`. Adding a future
  sync rule is one entry in that list.
- The only type-specific input is the branch to snapshot, and that comes from
  :attr:`Repo.single_task_branch`, so the operations stay uniform across types.

Today there are three operations, run in this order: snapshot the current
branch's task files into ``docs/tasks/<branch>/``, regenerate ``SYLLABUS`` from
those snapshots, then sum their estimated times into ``lm.json``. The last two
both read the snapshots, so both must follow the first.
"""

import dataclasses
import json
import shutil
from pathlib import Path

from .constants import TASK_FILE_BASES, LangEnum
from .linter_utils import MarkdownFile
from .repo import Repo, estimate_repo_time, get_variant_filename

# English (None) plus every supported language variant.
LANGS = (None, *LangEnum)


@dataclasses.dataclass
class SyncAction:
    """One file sync wrote, and why."""

    kind: str  # "snapshot" | "syllabus" | "manifest"
    path: str
    detail: str = ""


@dataclasses.dataclass
class SyncReport:
    """What a sync run did."""

    dir_project_root: Path
    actions: "list[SyncAction]"

    def to_dict(self) -> dict:
        return {
            "dir_project_root": str(self.dir_project_root),
            "actions": [dataclasses.asdict(a) for a in self.actions],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def render(self) -> str:
        """Human-readable summary: one line per file written."""
        markers = {"snapshot": "📄", "syllabus": "📋", "manifest": "🧾"}
        lines = []
        for action in self.actions:
            marker = markers.get(action.kind, "📋")
            suffix = f"  ({action.detail})" if action.detail else ""
            lines.append(f"{marker} {action.kind}: {action.path}{suffix}")
        lines.append("")
        lines.append(f"Synced {len(self.actions)} file(s).")
        return "\n".join(lines)


def op_snapshot_branch(repo: Repo) -> "list[SyncAction]":
    """Copy the current branch's task files into ``docs/tasks/<branch>/``.

    The branch is :attr:`Repo.single_task_branch` (fixed for showcase / upskill).
    Evolve, whose branch comes from git, is not supported yet.
    """
    branch = repo.single_task_branch
    if branch is None:
        raise NotImplementedError(
            "sync for evolve repos (branch from git) is not implemented yet."
        )
    dst_dir = repo.get_dir_task(branch)
    dst_dir.mkdir(parents=True, exist_ok=True)

    actions: "list[SyncAction]" = []
    for base in TASK_FILE_BASES:
        for lang in LANGS:
            name = get_variant_filename(base, lang)
            src = repo.dir_project_root / name
            if src.exists():
                dst = dst_dir / name
                shutil.copy2(src, dst)
                actions.append(SyncAction("snapshot", str(dst), f"from {name}"))
    return actions


def op_generate_syllabus(repo: Repo) -> "list[SyncAction]":
    """Regenerate ``docs/tasks/SYLLABUS[-<lang>].md`` from the task snapshots.

    One file per language: ``# Syllabus`` then, for each task dir in order, an
    H2 with the branch name and the matching-language README's frontmatter
    description verbatim.
    """
    task_dirs = repo.iter_dir_tasks()
    actions: "list[SyncAction]" = []
    for lang in LANGS:
        sections = ["# Syllabus"]
        for dir_task in task_dirs:
            readme = repo.get_path_task_readme(dir_task.name, lang)
            desc = MarkdownFile(readme).description if readme.exists() else None
            sections.append(f"## {dir_task.name}\n\n{desc or ''}")
        out_path = repo.get_path_syllabus(lang)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
        actions.append(
            SyncAction("syllabus", str(out_path), f"{len(task_dirs)} task(s)")
        )
    return actions


def op_estimated_hours(repo: Repo) -> "list[SyncAction]":
    """Sum the task snapshots' estimated times into ``lm.json``.

    Each branch TICKET states one minute range; the repo total is their straight
    sum, stored as decimal hours in ``estimated_hours_lower`` /
    ``estimated_hours_upper``. Writing it here rather than by hand is the whole
    point: the number is mechanical, and a hand-maintained one drifts the first
    time a single task is re-estimated.

    Two cases leave the manifest untouched and say so in the action's detail: an
    unreadable manifest (the linter reports that properly, and rewriting it would
    destroy whatever the creator has in there), and any branch whose TICKET has
    no parseable estimate (a total that silently skipped a branch is worse than
    no total at all).
    """
    path = repo.path_lm_json
    metadata = repo.metadata
    if metadata is None:
        return [SyncAction("manifest", str(path), "skipped: lm.json missing or invalid")]

    estimate = estimate_repo_time(repo)
    if not estimate.is_complete:
        names = ", ".join(estimate.branches_without_estimate)
        return [
            SyncAction("manifest", str(path), f"skipped: no estimate in {names}")
        ]

    metadata.estimated_hours_lower = estimate.lower_hours
    metadata.estimated_hours_upper = estimate.upper_hours
    path.write_text(
        json.dumps(metadata.to_dict(), indent=4, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return [
        SyncAction(
            "manifest",
            str(path),
            f"{estimate.lower_hours} to {estimate.upper_hours} hours",
        )
    ]


# Sync operations, run in order by sync(). Snapshot must precede both of the
# others, since they are generated from the freshly snapshotted task files.
OPERATIONS = [op_snapshot_branch, op_generate_syllabus, op_estimated_hours]


def sync(repo: Repo) -> SyncReport:
    """Run every sync operation on ``repo`` and report what was written."""
    actions = [action for op in OPERATIONS for action in op(repo)]
    return SyncReport(repo.dir_project_root, actions)


def sync_project(project_root: "Path | str | None" = None) -> SyncReport:
    """Resolve the teaching repo and sync it. The CLI's entire core.

    With ``project_root`` given, that path is the repo root; without it, the
    root is found by walking up from the current working directory.
    """
    if project_root is not None:
        repo = Repo(dir_project_root=Path(project_root).resolve())
    else:
        repo = Repo.from_cwd()
    return sync(repo)
