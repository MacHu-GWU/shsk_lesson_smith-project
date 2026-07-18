# -*- coding: utf-8 -*-

from pathlib import Path

from shsk_lesson_smith.linter import CheckResult, LintReport, lint
from shsk_lesson_smith.repo import Repo
from shsk_lesson_smith.repo_for_upskill import UpskillRepo

dir_tests = Path(__file__).absolute().parent
dir_good_upskill_repo = dir_tests / "good_upskill_repo"
dir_bad_upskill_repo = dir_tests / "bad_upskill_repo"


def lint_good():
    return lint(Repo(dir_project_root=dir_good_upskill_repo))


def lint_bad():
    return lint(Repo(dir_project_root=dir_bad_upskill_repo))


class TestGoodUpskillRepoIsClean:
    def test_base_repo_passes(self):
        report = lint_good()
        assert report.passed, report.render()
        assert report.failures() == []

    def test_upskill_subclass_passes(self):
        report = lint(UpskillRepo(dir_project_root=dir_good_upskill_repo))
        assert report.passed, report.render()

    def test_report_shape(self):
        report = lint_good()
        assert isinstance(report, LintReport)
        assert all(isinstance(r, CheckResult) for r in report.results)
        # Per-check-point granularity: many checks ran across the repo.
        assert len(report.results) > 10


class TestBadUpskillRepoReproducesErrors:
    """The committed bad_upskill_repo bakes in one error per check type."""

    def messages(self):
        return [f.message for f in lint_bad().failures()]

    def test_overall_fails(self):
        assert lint_bad().passed is False

    def has(self, needle):
        return any(needle in (m or "") for m in self.messages())

    def test_readme_original_h1_mismatch(self):
        assert self.has("must be exactly 'bad_upskill_repo'")

    def test_root_readme_language_incomplete(self):
        assert self.has("README-cn.md")

    def test_description_forbidden_char(self):
        assert self.has("description contains forbidden character")

    def test_description_too_long(self):
        assert self.has("over the 400-character limit")

    def test_task_ticket_language_incomplete(self):
        assert self.has("examples/01-create-repo/TICKET-cn.md")

    def test_bad_example_dir_name(self):
        assert self.has("must be NN-lowercase-hyphen-words")

    def test_emoji_in_h1(self):
        assert self.has("contains an emoji")

    def test_missing_frontmatter_description(self):
        assert self.has("missing the required one-line 'description'")

    def test_forbidden_char_in_h1(self):
        assert self.has("The H1 title")
        assert self.has("An H1 may use only")

    def test_syllabus_h1_must_be_syllabus(self):
        assert self.has("must be exactly 'Syllabus'")

    def test_syllabus_description_mismatch(self):
        assert self.has("does not match the description")


class TestManifestAndSingleBranch:
    """Rules that cannot coexist with the bad repo above, built minimally."""

    def _upskill_root(self, tmp_path):
        (tmp_path / "lm.json").write_text('{"type": "upskill"}', encoding="utf-8")
        return tmp_path

    def test_broken_manifest_only_runs_manifest_rule(self, tmp_path):
        (tmp_path / "lm.json").write_text("{ not json", encoding="utf-8")
        report = lint(Repo(dir_project_root=tmp_path))
        assert not report.passed
        assert len(report.results) == 1
        assert "lm.json is not valid JSON" in report.results[0].message

    def test_missing_manifest(self, tmp_path):
        report = lint(Repo(dir_project_root=tmp_path))
        assert "lm.json is missing" in report.failures()[0].message

    def test_single_branch_wrong_name(self, tmp_path):
        root = self._upskill_root(tmp_path)
        (root / "docs" / "tasks" / "01-course").mkdir(parents=True)
        messages = [f.message for f in lint(Repo(dir_project_root=root)).failures()]
        assert any(
            "exactly one task branch named '01-upskill'" in (m or "")
            for m in messages
        )

    def test_single_branch_too_many(self, tmp_path):
        root = self._upskill_root(tmp_path)
        (root / "docs" / "tasks" / "01-upskill").mkdir(parents=True)
        (root / "docs" / "tasks" / "02-extra").mkdir(parents=True)
        messages = [f.message for f in lint(Repo(dir_project_root=root)).failures()]
        assert any(
            "exactly one task branch named '01-upskill'" in (m or "")
            for m in messages
        )


class TestRender:
    def test_render_clean(self):
        out = lint_good().render()
        assert "✅" in out
        assert "PASSED" in out

    def test_render_failure(self):
        out = lint_bad().render()
        assert "❌" in out
        assert "FAILED" in out


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.linter",
        preview=False,
    )
