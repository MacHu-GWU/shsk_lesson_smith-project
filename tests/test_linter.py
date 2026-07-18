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
            "must exactly match the repo name" in (m or "")
            for m in self._fail_messages(upskill_copy)
        )

    def test_missing_examples_dir(self, upskill_copy):
        shutil.rmtree(upskill_copy / "examples")
        assert any(
            "examples/ directory is missing" in (m or "")
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
