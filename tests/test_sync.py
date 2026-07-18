# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

import pytest

from shsk_lesson_smith.linter import lint
from shsk_lesson_smith.repo import Repo
from shsk_lesson_smith.sync import SyncReport, sync

dir_tests = Path(__file__).absolute().parent
dir_good_upskill_repo = dir_tests / "good_upskill_repo"


@pytest.fixture
def writable_good_repo(tmp_path):
    """A writable copy of the good upskill repo, keeping its name.

    Sync writes files, so it needs a writable location; the name is preserved so
    the README-ORIGINAL H1 (which must equal the repo dir name) stays valid.
    """
    dst = tmp_path / "good_upskill_repo"
    shutil.copytree(dir_good_upskill_repo, dst)
    return dst


class TestSync:
    def test_returns_report_of_actions(self, writable_good_repo):
        report = sync(Repo(dir_project_root=writable_good_repo))
        assert isinstance(report, SyncReport)
        kinds = {a.kind for a in report.actions}
        assert kinds == {"snapshot", "syllabus"}

    def test_snapshots_root_task_files(self, writable_good_repo):
        # Remove the snapshot dir, then let sync rebuild it from root files.
        shutil.rmtree(writable_good_repo / "docs" / "tasks" / "01-upskill")
        sync(Repo(dir_project_root=writable_good_repo))
        snapshot = writable_good_repo / "docs" / "tasks" / "01-upskill"
        for name in ("README.md", "README-cn.md", "TICKET.md", "TICKET-cn.md"):
            assert (snapshot / name).exists()

    def test_generates_syllabus_from_task_readme(self, writable_good_repo):
        (writable_good_repo / "docs" / "tasks" / "SYLLABUS.md").unlink()
        sync(Repo(dir_project_root=writable_good_repo))
        syllabus = (
            writable_good_repo / "docs" / "tasks" / "SYLLABUS.md"
        ).read_text(encoding="utf-8")
        assert syllabus.startswith("# Syllabus\n")
        assert "## 01-upskill" in syllabus
        # Description is taken verbatim from the task README.
        assert "Overview of this GitHub basics upskill course" in syllabus

    def test_sync_output_is_lint_clean(self, writable_good_repo):
        # Sync from a mangled state, then the repo must lint clean.
        shutil.rmtree(writable_good_repo / "docs" / "tasks" / "01-upskill")
        (writable_good_repo / "docs" / "tasks" / "SYLLABUS.md").unlink()
        sync(Repo(dir_project_root=writable_good_repo))
        report = lint(Repo(dir_project_root=writable_good_repo))
        assert report.passed, report.render()

    def test_sync_is_idempotent(self, writable_good_repo):
        repo = Repo(dir_project_root=writable_good_repo)
        sync(repo)
        first = _read_docs(writable_good_repo)
        sync(repo)
        assert _read_docs(writable_good_repo) == first

    def test_evolve_not_supported_yet(self, tmp_path):
        root = tmp_path / "evolve"
        root.mkdir()
        (root / "lm.json").write_text('{"type": "evolve"}', encoding="utf-8")
        with pytest.raises(NotImplementedError):
            sync(Repo(dir_project_root=root))


def _read_docs(root: Path):
    docs = root / "docs" / "tasks"
    return {
        str(p.relative_to(root)): p.read_text(encoding="utf-8")
        for p in sorted(docs.rglob("*.md"))
    }


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.sync",
        preview=False,
    )
