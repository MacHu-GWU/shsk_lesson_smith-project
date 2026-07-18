# -*- coding: utf-8 -*-

import subprocess

from shsk_lesson_smith.repo_types import resolve_repo
from shsk_lesson_smith.sync import generate_syllabus, sync_repo

from conftest import write_special_file


def git(root, *args):
    subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )


class TestSyncRepo:
    def test_evolve_sync_snapshots_and_generates_syllabus(self, evolve_root, tmp_path):
        # Turn the fixture into a real git repo on a task branch.
        import shutil

        shutil.rmtree(evolve_root / ".git")
        git(evolve_root, "init")
        git(evolve_root, "checkout", "-b", "02-second")
        write_special_file(
            evolve_root / "README.md", description="Second task promise."
        )
        write_special_file(
            evolve_root / "README-cn.md", description="第二个 Task 的承诺."
        )

        repo = resolve_repo(evolve_root)
        assert sync_repo(repo, quiet=True) == 0

        snapshot = evolve_root / "docs" / "tasks" / "02-second"
        for name in ("README.md", "README-cn.md", "TICKET.md", "TICKET-cn.md"):
            assert (snapshot / name).exists()

        syllabus = (evolve_root / "docs" / "tasks" / "SYLLABUS.md").read_text(
            encoding="utf-8"
        )
        assert syllabus.startswith("# Syllabus\n")
        assert "## 01-intro" in syllabus
        assert "## 02-second" in syllabus
        assert "Second task promise." in syllabus
        syllabus_cn = (
            evolve_root / "docs" / "tasks" / "SYLLABUS-cn.md"
        ).read_text(encoding="utf-8")
        assert "第二个 Task 的承诺." in syllabus_cn

    def test_sync_refuses_non_evolve_repo(self, showcase_root):
        repo = resolve_repo(showcase_root)
        assert sync_repo(repo, quiet=True) == 1

    def test_sync_refuses_non_task_branch(self, evolve_root):
        import shutil

        shutil.rmtree(evolve_root / ".git")
        git(evolve_root, "init")
        git(evolve_root, "checkout", "-b", "main")
        repo = resolve_repo(evolve_root)
        assert sync_repo(repo, quiet=True) == 1


class TestGenerateSyllabus:
    def test_missing_description_becomes_empty_section(self, evolve_root):
        task_dir = evolve_root / "docs" / "tasks" / "02-empty"
        task_dir.mkdir()
        repo = resolve_repo(evolve_root)
        generate_syllabus(repo, quiet=True)
        syllabus = (evolve_root / "docs" / "tasks" / "SYLLABUS.md").read_text(
            encoding="utf-8"
        )
        assert "## 02-empty" in syllabus


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.sync",
        preview=False,
    )
