# -*- coding: utf-8 -*-

import pytest

from shsk_lesson_smith.constants import LangEnum, RepoTypeEnum
from shsk_lesson_smith.repo import (
    StandardRepo,
    get_variant_filename,
    read_frontmatter_description,
    to_lang,
)

from conftest import make_root, write_special_file


class TestLangHelpers:
    def test_to_lang(self):
        assert to_lang(None) is None
        assert to_lang("cn") is LangEnum.cn
        assert to_lang(LangEnum.cn) is LangEnum.cn
        with pytest.raises(ValueError):
            to_lang("fr")

    def test_get_variant_filename(self):
        assert get_variant_filename("README") == "README.md"
        assert get_variant_filename("README", "cn") == "README-cn.md"
        assert get_variant_filename("TICKET", LangEnum.cn) == "TICKET-cn.md"


class TestStandardRepo:
    def test_from_cwd_walks_up(self, tmp_path):
        root = make_root(tmp_path)
        nested = root / "docs" / "tasks" / "01-intro"
        nested.mkdir(parents=True)
        repo = StandardRepo.from_cwd(nested)
        assert repo.dir_project_root == root

    def test_from_cwd_fails_outside_repo(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            StandardRepo.from_cwd(tmp_path)

    def test_direct_construction_needs_no_root_markers(self, tmp_path):
        # No .git / mise.toml needed when the root is given directly.
        repo = StandardRepo(dir_project_root=tmp_path)
        assert repo.dir_project_root == tmp_path.resolve()

    def test_paths(self, tmp_path):
        root = make_root(tmp_path)
        repo = StandardRepo(dir_project_root=root)
        assert repo.path_lm_json == root / "lm.json"
        assert repo.path_readme == root / "README.md"
        assert repo.get_path_readme("cn") == root / "README-cn.md"
        assert repo.get_path_ticket("cn") == root / "TICKET-cn.md"
        assert repo.get_path_readme_original() == root / "README-ORIGINAL.md"
        assert repo.dir_docs_tasks == root / "docs" / "tasks"
        assert repo.path_syllabus == root / "docs" / "tasks" / "SYLLABUS.md"
        assert (
            repo.get_path_syllabus("cn")
            == root / "docs" / "tasks" / "SYLLABUS-cn.md"
        )
        assert repo.get_dir_task("01-intro") == root / "docs" / "tasks" / "01-intro"

    def test_repo_type(self, tmp_path):
        root = make_root(tmp_path, "showcase")
        assert StandardRepo(dir_project_root=root).repo_type is RepoTypeEnum.showcase

        (root / "lm.json").write_text('{"type": "nope"}', encoding="utf-8")
        assert StandardRepo(dir_project_root=root).repo_type is None

        (root / "lm.json").write_text("not json", encoding="utf-8")
        assert StandardRepo(dir_project_root=root).repo_type is None

        (root / "lm.json").unlink()
        assert StandardRepo(dir_project_root=root).repo_type is None

    def test_iter_task_dirs(self, tmp_path):
        root = make_root(tmp_path)
        repo = StandardRepo(dir_project_root=root)
        assert repo.iter_task_dirs() == []
        (root / "docs" / "tasks" / "02-second").mkdir(parents=True)
        (root / "docs" / "tasks" / "01-first").mkdir()
        (root / "docs" / "tasks" / "not-a-task").mkdir()
        names = [d.name for d in repo.iter_task_dirs()]
        assert names == ["01-first", "02-second"]


class TestReadFrontmatterDescription:
    def test_happy_path(self, tmp_path):
        path = tmp_path / "README.md"
        write_special_file(path, description="Do X.")
        assert read_frontmatter_description(path) == "Do X."

    def test_quoted_value_is_unwrapped(self, tmp_path):
        path = tmp_path / "README.md"
        path.write_text('---\ndescription: "Do X."\n---\n', encoding="utf-8")
        assert read_frontmatter_description(path) == "Do X."

    def test_missing_cases(self, tmp_path):
        path = tmp_path / "README.md"
        assert read_frontmatter_description(path) is None
        path.write_text("# No frontmatter\n", encoding="utf-8")
        assert read_frontmatter_description(path) is None
        path.write_text("---\ntitle: x\n---\n", encoding="utf-8")
        assert read_frontmatter_description(path) is None


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.repo",
        preview=False,
    )
