# -*- coding: utf-8 -*-

from pathlib import Path

import pytest

from shsk_lesson_smith.exc import LintError
from shsk_lesson_smith.linter import (
    CheckResult,
    LintReport,
    _check_syllabus_numbering,
    lint,
    rule_syllabus,
)
from shsk_lesson_smith.linter_for_upskill import (
    _check_examples_numbering,
    rule_root_overview,
)
from shsk_lesson_smith.repo import Repo
from shsk_lesson_smith.repo_for_upskill import UpskillRepo
from shsk_lesson_smith.repo_for_showcase import ShowcaseRepo

dir_tests = Path(__file__).absolute().parent
dir_good_upskill_repo = dir_tests / "good_upskill_repo"
dir_bad_upskill_repo = dir_tests / "bad_upskill_repo"
dir_good_showcase_repo = dir_tests / "good_showcase_repo"
dir_bad_showcase_repo = dir_tests / "bad_showcase_repo"


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

    def test_ticket_relative_link(self):
        assert self.has("relative-path link")

    def test_examples_numbering_gap(self):
        assert self.has("numbered consecutively from 01")

    def test_missing_quiz_task(self):
        assert self.has("prove-i-get-it")

    def test_missing_forge_outputs(self):
        assert self.has("01-upskill-learn.md")

    def test_missing_github_about(self):
        assert self.has("github_about")

    def test_snapshot_language_incomplete(self):
        # rule_task_snapshots must flag a broken docs/tasks/<branch>/ snapshot.
        assert self.has("docs/tasks/01-upskill/TICKET-cn.md")


class TestGoodShowcaseRepoIsClean:
    def test_base_repo_passes(self):
        report = lint(Repo(dir_project_root=dir_good_showcase_repo))
        assert report.passed, report.render()
        assert report.failures() == []

    def test_showcase_subclass_passes(self):
        report = lint(ShowcaseRepo(dir_project_root=dir_good_showcase_repo))
        assert report.passed, report.render()


class TestBadShowcaseRepoReproducesErrors:
    """The committed bad_showcase_repo bakes in one error per check type.

    Mirrors bad_upskill_repo (same shared errors) plus the showcase-only demo
    mini task rule.
    """

    def messages(self):
        return [
            f.message
            for f in lint(Repo(dir_project_root=dir_bad_showcase_repo)).failures()
        ]

    def has(self, needle):
        return any(needle in (m or "") for m in self.messages())

    def test_overall_fails(self):
        assert lint(Repo(dir_project_root=dir_bad_showcase_repo)).passed is False

    def test_readme_original_h1_mismatch(self):
        assert self.has("must be exactly 'bad_showcase_repo'")

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

    def test_ticket_relative_link(self):
        assert self.has("relative-path link")

    def test_examples_numbering_gap(self):
        assert self.has("numbered consecutively from 01")

    def test_missing_quiz_task(self):
        assert self.has("prove-i-get-it")

    def test_missing_demo_task(self):
        # Showcase-only: the demo mini task NN-how-i-build-this must exist.
        assert self.has("how-i-build-this")

    def test_missing_forge_outputs(self):
        assert self.has("01-showcase-learn.md")

    def test_missing_github_about(self):
        assert self.has("github_about")

    def test_snapshot_language_incomplete(self):
        assert self.has("docs/tasks/01-showcase/TICKET-cn.md")


class TestShowcaseSingleBranch:
    """rule_single_branch for showcase: exactly one 01-showcase task branch."""

    def _showcase_root(self, tmp_path):
        (tmp_path / "lm.json").write_text('{"type": "showcase"}', encoding="utf-8")
        return tmp_path

    def test_single_branch_wrong_name(self, tmp_path):
        root = self._showcase_root(tmp_path)
        (root / "docs" / "tasks" / "01-course").mkdir(parents=True)
        messages = [f.message for f in lint(Repo(dir_project_root=root)).failures()]
        assert any(
            "exactly one task branch named '01-showcase'" in (m or "")
            for m in messages
        )

    def test_single_branch_too_many(self, tmp_path):
        root = self._showcase_root(tmp_path)
        (root / "docs" / "tasks" / "01-showcase").mkdir(parents=True)
        (root / "docs" / "tasks" / "02-extra").mkdir(parents=True)
        messages = [f.message for f in lint(Repo(dir_project_root=root)).failures()]
        assert any(
            "exactly one task branch named '01-showcase'" in (m or "")
            for m in messages
        )

    def test_demo_not_last_flagged(self, tmp_path):
        # A how-i-build-this that is not the highest-numbered example is flagged.
        from shsk_lesson_smith.linter_for_showcase import _check_demo_task_present

        dirs = [Path("06-how-i-build-this"), Path("07-extra")]
        with pytest.raises(LintError, match="must be the last example"):
            _check_demo_task_present(dirs)


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

    def test_invalid_manifest_type(self, tmp_path):
        (tmp_path / "lm.json").write_text('{"type": "bogus"}', encoding="utf-8")
        report = lint(Repo(dir_project_root=tmp_path))
        assert not report.passed
        assert any("lm.json is invalid" in (m or "") for m in
                   [f.message for f in report.failures()])

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


class TestRootOverviewContentChecks:
    """The upskill root README/TICKET get full description + H1 checks, and the
    root TICKET is checked for relative-path links."""

    def _fails(self, root):
        return [
            r.message
            for r in rule_root_overview(Repo(dir_project_root=root))
            if not r.passed
        ]

    def _write(self, path, body):
        path.write_text(body, encoding="utf-8")

    def test_root_readme_bad_h1_flagged(self, tmp_path):
        for name in ("README.md", "README-cn.md"):
            self._write(tmp_path / name, '---\ndescription: "ok."\n---\n\n# Bad — Title\n')
        assert any("H1" in (m or "") for m in self._fails(tmp_path))

    def test_root_readme_unquoted_description_flagged(self, tmp_path):
        for name in ("README.md", "README-cn.md"):
            self._write(tmp_path / name, "---\ndescription: ok.\n---\n\n# Title\n")
        assert any("double quotes" in (m or "") for m in self._fails(tmp_path))

    def test_root_ticket_relative_link_flagged(self, tmp_path):
        for name in ("README.md", "README-cn.md"):
            self._write(tmp_path / name, '---\ndescription: "ok."\n---\n\n# Title\n')
        for name in ("TICKET.md", "TICKET-cn.md"):
            self._write(
                tmp_path / name,
                '---\ndescription: "ok."\n---\n\n# Ticket\n\nSee [x](../y.md).\n',
            )
        assert any("relative-path link" in (m or "") for m in self._fails(tmp_path))

    def test_valid_root_files_pass(self, tmp_path):
        for name in ("README.md", "README-cn.md"):
            self._write(tmp_path / name, '---\ndescription: "ok."\n---\n\n# Title\n')
        for name in ("TICKET.md", "TICKET-cn.md"):
            self._write(
                tmp_path / name, '---\ndescription: "ok."\n---\n\n# Ticket\n\nAll good.\n'
            )
        assert self._fails(tmp_path) == []


class TestLinterInternalBranches:
    """Cover the check branches not reachable from the good / bad fixtures."""

    def test_syllabus_numbering_non_consecutive(self):
        with pytest.raises(LintError, match="consecutive"):
            _check_syllabus_numbering([("01-a", "x"), ("03-b", "y")])

    def test_syllabus_numbering_bad_prefix(self):
        with pytest.raises(LintError, match="two-digit number"):
            _check_syllabus_numbering([("intro", "x")])

    def test_examples_numbering_bad_prefix(self):
        with pytest.raises(LintError, match="two-digit number"):
            _check_examples_numbering([Path("bad-name")])

    def test_examples_numbering_empty(self):
        with pytest.raises(LintError, match="no mini task"):
            _check_examples_numbering([])

    def test_syllabus_rule_entry_and_match_modes(self, tmp_path):
        # One crafted SYLLABUS trips: sections-vs-dirs mismatch, non-consecutive
        # numbering, a multi-line entry, an empty entry, and an entry with no
        # matching task README.
        tasks = tmp_path / "docs" / "tasks"
        (tasks / "01-upskill").mkdir(parents=True)
        (tasks / "SYLLABUS.md").write_text(
            "# Syllabus\n\n## 01-upskill\n\nmulti\nline\n\n"
            "## 02-empty\n\n## 04-ghost\n\nghost desc\n",
            encoding="utf-8",
        )
        blob = " | ".join(
            (r.message or "")
            for r in rule_syllabus(Repo(dir_project_root=tmp_path))
            if not r.passed
        )
        assert "do not match the docs/tasks/" in blob  # matches-tasks
        assert "consecutive" in blob  # numbering gap [1, 2, 4]
        assert "single line" in blob  # 01-upskill multi-line desc
        assert "no description line" in blob  # 02-empty
        assert "no frontmatter description to match" in blob  # 04-ghost


class TestDispatch:
    """lint() dispatches on repo type to the matching linter_for_<type> module."""

    def test_showcase_dispatch(self, showcase_root):
        report = lint(Repo(dir_project_root=showcase_root))
        assert isinstance(report, LintReport)
        # More than one result means it ran the showcase RULES, not manifest-only.
        assert len(report.results) > 1

    def test_evolve_dispatch(self, evolve_root):
        report = lint(Repo(dir_project_root=evolve_root))
        assert isinstance(report, LintReport)
        assert len(report.results) > 1


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
