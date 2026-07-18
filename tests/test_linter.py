# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

import pytest

from shsk_lesson_smith.linter import CheckResult, LintReport, lint
from shsk_lesson_smith.repo import Repo
from shsk_lesson_smith.repo_for_upskill import UpskillRepo

dir_good_upskill_repo = Path(__file__).absolute().parent / "good_upskill_repo"


@pytest.fixture
def upskill_copy(tmp_path):
    """A writable copy of the good upskill fixture, for mutation tests."""
    dst = tmp_path / "repo"
    shutil.copytree(dir_good_upskill_repo, dst)
    return dst


class TestGoodUpskillRepoIsClean:
    def test_base_repo_passes(self):
        report = lint(Repo(dir_project_root=dir_good_upskill_repo))
        assert report.passed, report.render()
        assert report.failures() == []

    def test_upskill_subclass_passes(self):
        report = lint(UpskillRepo(dir_project_root=dir_good_upskill_repo))
        assert report.passed, report.render()

    def test_report_shape(self):
        report = lint(Repo(dir_project_root=dir_good_upskill_repo))
        assert isinstance(report, LintReport)
        assert all(isinstance(r, CheckResult) for r in report.results)
        # More than one check point ran (per-check-point granularity).
        assert len(report.results) > 10


class TestViolations:
    def _fail_messages(self, root):
        return [f.message for f in lint(Repo(dir_project_root=root)).failures()]

    def _fail_locations(self, root):
        return [f.location for f in lint(Repo(dir_project_root=root)).failures()]

    def test_missing_language_variant(self, upskill_copy):
        (upskill_copy / "examples" / "01-create-repo" / "README-cn.md").unlink()
        locations = self._fail_locations(upskill_copy)
        assert any("README-cn.md" in loc for loc in locations)

    def test_forbidden_char_in_description(self, upskill_copy):
        target = upskill_copy / "examples" / "01-create-repo" / "README.md"
        target.write_text(
            '---\ndescription: He said "hi".\n---\n\n# Title\n', encoding="utf-8"
        )
        assert any(
            "forbidden character" in (m or "") for m in self._fail_messages(upskill_copy)
        )

    def test_emoji_in_h1(self, upskill_copy):
        target = upskill_copy / "examples" / "02-edit-files" / "README.md"
        target.write_text(
            "---\ndescription: ok.\n---\n\n# 📋 Files\n", encoding="utf-8"
        )
        assert any("emoji" in (m or "") for m in self._fail_messages(upskill_copy))

    def test_bad_example_dir_name(self, upskill_copy):
        (upskill_copy / "examples" / "01-create-repo").rename(
            upskill_copy / "examples" / "01-Bad_Name"
        )
        assert any(
            "NN-lowercase-hyphen" in (m or "") for m in self._fail_messages(upskill_copy)
        )

    def test_readme_original_h1_must_match_repo_name(self, upskill_copy):
        target = upskill_copy / "README-ORIGINAL.md"
        target.write_text(
            "---\ndescription: ok.\n---\n\n# Wrong Title\n", encoding="utf-8"
        )
        assert any(
            "must be exactly" in (m or "")
            for m in self._fail_messages(upskill_copy)
        )

    def test_missing_examples_dir(self, upskill_copy):
        shutil.rmtree(upskill_copy / "examples")
        assert any(
            "examples/ directory is missing" in (m or "")
            for m in self._fail_messages(upskill_copy)
        )


class TestSyllabusContent:
    def _fail_messages(self, root):
        return [f.message for f in lint(Repo(dir_project_root=root)).failures()]

    def test_syllabus_h1_must_be_syllabus(self, upskill_copy):
        target = upskill_copy / "docs" / "tasks" / "SYLLABUS-cn.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("# Syllabus", "# 大纲"),
            encoding="utf-8",
        )
        assert any("must be exactly 'Syllabus'" in (m or "")
                   for m in self._fail_messages(upskill_copy))

    def test_description_must_match_task_readme(self, upskill_copy):
        target = upskill_copy / "docs" / "tasks" / "SYLLABUS.md"
        target.write_text(
            target.read_text(encoding="utf-8").replace("Overview", "Wrong overview"),
            encoding="utf-8",
        )
        assert any("does not match" in (m or "")
                   for m in self._fail_messages(upskill_copy))

    def test_sections_must_match_task_dirs(self, upskill_copy):
        (upskill_copy / "docs" / "tasks" / "01-upskill").rename(
            upskill_copy / "docs" / "tasks" / "01-course"
        )
        assert any("do not match the docs/tasks/" in (m or "")
                   for m in self._fail_messages(upskill_copy))


class TestUpskillSingleBranch:
    def _fail_messages(self, root):
        return [f.message for f in lint(Repo(dir_project_root=root)).failures()]

    def test_branch_must_be_01_upskill(self, upskill_copy):
        (upskill_copy / "docs" / "tasks" / "01-upskill").rename(
            upskill_copy / "docs" / "tasks" / "01-course"
        )
        assert any(
            "exactly one task branch named '01-upskill'" in (m or "")
            for m in self._fail_messages(upskill_copy)
        )

    def test_two_branches_rejected(self, upskill_copy):
        shutil.copytree(
            upskill_copy / "docs" / "tasks" / "01-upskill",
            upskill_copy / "docs" / "tasks" / "02-extra",
        )
        assert any(
            "exactly one task branch named '01-upskill'" in (m or "")
            for m in self._fail_messages(upskill_copy)
        )


class TestBrokenManifest:
    def test_broken_manifest_only_runs_manifest_rule(self, upskill_copy):
        (upskill_copy / "lm.json").write_text("{ not json", encoding="utf-8")
        report = lint(Repo(dir_project_root=upskill_copy))
        assert not report.passed
        assert len(report.results) == 1
        assert "lm.json is not valid JSON" in report.results[0].message

    def test_missing_manifest(self, upskill_copy):
        (upskill_copy / "lm.json").unlink()
        report = lint(Repo(dir_project_root=upskill_copy))
        assert "lm.json is missing" in report.failures()[0].message


class TestRender:
    def test_render_clean_has_check_marks(self):
        out = lint(Repo(dir_project_root=dir_good_upskill_repo)).render()
        assert "✅" in out
        assert "PASSED" in out

    def test_render_failure_groups_by_file(self, upskill_copy):
        (upskill_copy / "examples" / "01-create-repo" / "README-cn.md").unlink()
        out = lint(Repo(dir_project_root=upskill_copy)).render()
        assert "❌" in out
        assert "FAILED" in out


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.linter",
        preview=False,
    )
