# -*- coding: utf-8 -*-

"""The ``sync`` operation: snapshot task files and regenerate the syllabus.

Currently only the evolve layout is supported (root-level README / TICKET per
task branch, snapshotted into docs/tasks/<branch>/). The showcase / upskill
layout (examples/NN-title/) is still TODO.
"""

import shutil
import sys

from .constants import (
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


def generate_syllabus(
    repo: StandardRepo,
    quiet: bool = False,
) -> None:
    """Regenerate docs/tasks/SYLLABUS[-<lang>].md per ref/syllabus-spec.md.

    Emits ``# Syllabus`` then, for each task in ascending order, an H2 with the
    branch dir name verbatim (all lowercase) followed by the task README's
    frontmatter description verbatim.
    """
    task_dirs = repo.iter_task_dirs()
    for lang in (None, *LangEnum):
        readme_name = get_variant_filename("README", lang)
        sections = ["# Syllabus"]
        for directory in task_dirs:
            desc = read_frontmatter_description(directory / readme_name) or ""
            sections.append(f"## {directory.name}\n\n{desc}")
        out_path = repo.get_path_syllabus(lang)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n\n".join(sections) + "\n", encoding="utf-8")
        if not quiet:
            rel = out_path.relative_to(repo.dir_project_root)
            print(f"  syllabus: wrote {rel} ({len(task_dirs)} tasks)")


def sync_repo(
    repo: StandardRepo,
    quiet: bool = False,
) -> int:
    """Snapshot the current branch's task files, then regenerate the syllabus.

    Returns an exit code: 0 on success, 1 on failure.
    """
    if repo.repo_type is not RepoTypeEnum.evolve:
        print(
            "ERROR: sync currently only supports the evolve layout "
            f"(lm.json type is {repo.repo_type.value if repo.repo_type else None!r})",
            file=sys.stderr,
        )
        return 1

    branch = repo.current_branch
    if not branch:
        print(
            "ERROR: could not determine current branch (detached HEAD?)",
            file=sys.stderr,
        )
        return 1
    if not TASK_DIR_PATTERN.match(branch):
        print(
            f"ERROR: current branch {branch!r} is not a task branch "
            "(expected NN-lowercase-hyphen-words, e.g. 01-branch-name)",
            file=sys.stderr,
        )
        return 1

    dst_dir = repo.get_dir_task(branch)
    dst_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    for base in TASK_FILE_BASES:
        for lang in (None, *LangEnum):
            name = get_variant_filename(base, lang)
            src = repo.dir_project_root / name
            if src.exists():
                shutil.copy2(src, dst_dir / name)
                copied += 1
                if not quiet:
                    print(f"  snapshot: {name} -> docs/tasks/{branch}/{name}")

    if copied == 0 and not quiet:
        print(f"  warning: no task files found at repo root for branch {branch}")

    generate_syllabus(repo, quiet=quiet)

    if not quiet:
        print(f"Done. Snapshotted {copied} file(s) into docs/tasks/{branch}/.")
    return 0
