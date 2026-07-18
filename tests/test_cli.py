# -*- coding: utf-8 -*-

import json as json_module
import shutil
from pathlib import Path

import pytest

from shsk_lesson_smith.cli import Command

dir_tests = Path(__file__).absolute().parent
dir_good_upskill_repo = dir_tests / "good_upskill_repo"
dir_bad_upskill_repo = dir_tests / "bad_upskill_repo"


class TestLint:
    def test_clean_prints_report_and_returns_zero(self, capsys):
        # No SystemExit means a zero exit code.
        Command().lint(project_root=str(dir_good_upskill_repo))
        out = capsys.readouterr().out
        assert "✅" in out
        assert "PASSED" in out

    def test_quiet_prints_nothing(self, capsys):
        Command().lint(project_root=str(dir_good_upskill_repo), quiet=True)
        assert capsys.readouterr().out == ""

    def test_json_output(self, capsys):
        Command().lint(project_root=str(dir_good_upskill_repo), json=True)
        data = json_module.loads(capsys.readouterr().out)
        assert data["passed"] is True
        assert isinstance(data["results"], list)
        assert {"location", "passed", "message"} <= set(data["results"][0])

    def test_failure_exits_nonzero(self):
        with pytest.raises(SystemExit) as excinfo:
            Command().lint(project_root=str(dir_bad_upskill_repo))
        assert excinfo.value.code == 1

    def test_quiet_failure_still_exits_nonzero(self, capsys):
        with pytest.raises(SystemExit) as excinfo:
            Command().lint(project_root=str(dir_bad_upskill_repo), quiet=True)
        assert excinfo.value.code == 1
        assert capsys.readouterr().out == ""

    def test_json_failure_output(self, capsys):
        with pytest.raises(SystemExit):
            Command().lint(project_root=str(dir_bad_upskill_repo), json=True)
        data = json_module.loads(capsys.readouterr().out)
        assert data["passed"] is False
        assert any(r["passed"] is False for r in data["results"])

    def test_not_in_a_repo_errors(self, tmp_path, capsys):
        # No project_root and cwd not in a repo -> friendly error, exit 1.
        import os

        cwd = os.getcwd()
        os.chdir(tmp_path)
        try:
            with pytest.raises(SystemExit) as excinfo:
                Command().lint()
        finally:
            os.chdir(cwd)
        assert excinfo.value.code == 1
        assert "ERROR" in capsys.readouterr().err


class TestSync:
    @pytest.fixture
    def writable_good_repo(self, tmp_path):
        dst = tmp_path / "good_upskill_repo"
        shutil.copytree(dir_good_upskill_repo, dst)
        return dst

    def test_sync_prints_actions_and_returns_zero(self, writable_good_repo, capsys):
        Command().sync(project_root=str(writable_good_repo))
        out = capsys.readouterr().out
        assert "snapshot" in out
        assert "syllabus" in out
        assert "Synced" in out

    def test_sync_quiet(self, writable_good_repo, capsys):
        Command().sync(project_root=str(writable_good_repo), quiet=True)
        assert capsys.readouterr().out == ""

    def test_sync_json(self, writable_good_repo, capsys):
        Command().sync(project_root=str(writable_good_repo), json=True)
        data = json_module.loads(capsys.readouterr().out)
        assert isinstance(data["actions"], list)
        assert {"kind", "path", "detail"} <= set(data["actions"][0])

    def test_sync_evolve_errors(self, tmp_path, capsys):
        root = tmp_path / "evolve"
        root.mkdir()
        (root / "lm.json").write_text('{"type": "evolve"}', encoding="utf-8")
        with pytest.raises(SystemExit) as excinfo:
            Command().sync(project_root=str(root))
        assert excinfo.value.code == 1
        assert "ERROR" in capsys.readouterr().err


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.cli",
        preview=False,
    )
