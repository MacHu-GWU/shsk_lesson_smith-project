# -*- coding: utf-8 -*-

import pytest

from shsk_lesson_smith.cli import Command


class TestCommand:
    def test_check_clean_repo(self, evolve_root, capsys):
        Command().check(project_root=str(evolve_root))
        assert "OK" in capsys.readouterr().out

    def test_check_broken_repo(self, evolve_root, capsys):
        (evolve_root / "README-cn.md").unlink()
        with pytest.raises(SystemExit) as excinfo:
            Command().check(project_root=str(evolve_root))
        assert excinfo.value.code == 1
        assert "FAIL" in capsys.readouterr().err

    def test_check_outside_any_repo(self, tmp_path):
        with pytest.raises(SystemExit) as excinfo:
            Command().check(project_root=str(tmp_path))
        assert excinfo.value.code == 1

    def test_sync_failure_raises_system_exit(self, showcase_root):
        with pytest.raises(SystemExit) as excinfo:
            Command().sync(project_root=str(showcase_root))
        assert excinfo.value.code == 1


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.cli",
        preview=False,
    )
