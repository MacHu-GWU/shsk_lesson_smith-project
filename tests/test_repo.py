# -*- coding: utf-8 -*-

import pytest

from shsk_lesson_smith.constants import LangEnum, RepoTypeEnum
from shsk_lesson_smith.linter_utils import MarkdownFile
from shsk_lesson_smith.repo import (
    Metadata,
    Repo,
    get_variant_filename,
    resolve_repo,
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


class TestResolveRepo:
    def test_walks_up_to_root(self, tmp_path):
        root = make_root(tmp_path)
        nested = root / "docs" / "tasks" / "01-intro"
        nested.mkdir(parents=True)
        assert resolve_repo(nested) == root

    def test_fails_outside_repo(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            resolve_repo(tmp_path)

    def test_repo_from_cwd(self, tmp_path):
        root = make_root(tmp_path)
        assert Repo.from_cwd(root).dir_project_root == root


class TestMetadata:
    def test_coerces_and_validates_type(self):
        assert Metadata(type="upskill").type is RepoTypeEnum.upskill
        assert Metadata(type=RepoTypeEnum.evolve).type is RepoTypeEnum.evolve
        with pytest.raises(ValueError):
            Metadata(type="nope")

    def test_from_dict(self):
        assert Metadata.from_dict({"type": "evolve"}).type is RepoTypeEnum.evolve
        with pytest.raises(ValueError):
            Metadata.from_dict({})  # missing type -> None -> invalid
        with pytest.raises(ValueError):
            Metadata.from_dict(["not", "an", "object"])

    def test_from_json_file(self, tmp_path):
        root = make_root(tmp_path, "showcase")
        assert Metadata.from_json_file(root / "lm.json").type is RepoTypeEnum.showcase


class TestRepoConstruction:
    def test_direct_construction_needs_no_root_markers(self, tmp_path):
        repo = Repo(dir_project_root=tmp_path)
        assert repo.dir_project_root == tmp_path

    def test_is_frozen(self, tmp_path):
        repo = Repo(dir_project_root=tmp_path)
        with pytest.raises(Exception):
            repo.dir_project_root = tmp_path / "x"

    def test_str_path_is_coerced(self, tmp_path):
        from pathlib import Path

        repo = Repo(dir_project_root=str(tmp_path))
        assert isinstance(repo.dir_project_root, Path)


class TestRepoPaths:
    def test_root_files(self, tmp_path):
        root = make_root(tmp_path)
        repo = Repo(dir_project_root=root)
        assert repo.path_lm_json == root / "lm.json"
        assert repo.path_readme == root / "README.md"
        assert repo.get_path_readme("cn") == root / "README-cn.md"
        assert repo.get_path_ticket("cn") == root / "TICKET-cn.md"
        assert repo.get_path_readme_original() == root / "README-ORIGINAL.md"

    def test_docs_tasks_paths(self, tmp_path):
        root = make_root(tmp_path)
        repo = Repo(dir_project_root=root)
        assert repo.dir_docs_tasks == root / "docs" / "tasks"
        assert repo.path_syllabus == root / "docs" / "tasks" / "SYLLABUS.md"
        assert repo.get_path_syllabus("cn") == root / "docs" / "tasks" / "SYLLABUS-cn.md"
        assert repo.get_dir_task("01-intro") == root / "docs" / "tasks" / "01-intro"


class TestRepoMarkdownAccessors:
    def test_md_accessors_return_markdown_file(self, tmp_path):
        root = make_root(tmp_path)
        write_special_file(root / "README.md", description="Learn X.")
        repo = Repo(dir_project_root=root)
        assert isinstance(repo.md_readme, MarkdownFile)
        assert repo.md_readme.path == repo.path_readme
        # Content is only read on access, and it reads the right file.
        assert repo.md_readme.description == "Learn X."

    def test_get_md_lang_variant(self, tmp_path):
        root = make_root(tmp_path)
        write_special_file(root / "README-cn.md", description="学 X.")
        repo = Repo(dir_project_root=root)
        assert repo.get_md_readme("cn").path == root / "README-cn.md"
        assert repo.get_md_readme("cn").description == "学 X."


class TestRepoTypeGating:
    def test_metadata_and_repo_type(self, tmp_path):
        root = make_root(tmp_path, "showcase")
        repo = Repo(dir_project_root=root)
        assert repo.metadata == Metadata(type=RepoTypeEnum.showcase)
        assert repo.repo_type is RepoTypeEnum.showcase

    def test_broken_manifest_is_graceful(self, tmp_path):
        root = make_root(tmp_path, "showcase")
        (root / "lm.json").write_text("{ not json", encoding="utf-8")
        repo = Repo(dir_project_root=root)
        assert repo.metadata is None
        assert repo.repo_type is None

    def test_examples_gating(self, tmp_path):
        showcase = Repo(dir_project_root=make_root(tmp_path / "s", "showcase"))
        assert showcase.dir_examples == showcase.dir_project_root / "examples"
        assert showcase.has_examples_layout is True

        evolve = Repo(dir_project_root=make_root(tmp_path / "e", "evolve"))
        assert evolve.dir_examples is None
        assert evolve.get_dir_example("01-x") is None
        assert evolve.iter_dir_examples() == []


class TestRepoIteration:
    def test_iter_dir_tasks(self, tmp_path):
        root = make_root(tmp_path)
        repo = Repo(dir_project_root=root)
        assert repo.iter_dir_tasks() == []
        (root / "docs" / "tasks" / "02-second").mkdir(parents=True)
        (root / "docs" / "tasks" / "01-first").mkdir()
        (root / "docs" / "tasks" / "not-a-task").mkdir()
        assert [d.name for d in repo.iter_dir_tasks()] == ["01-first", "02-second"]

    def test_iter_dir_examples(self, tmp_path):
        root = make_root(tmp_path, "upskill")
        repo = Repo(dir_project_root=root)
        (root / "examples" / "02-b").mkdir(parents=True)
        (root / "examples" / "01-a").mkdir()
        assert [d.name for d in repo.iter_dir_examples()] == ["01-a", "02-b"]


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.repo",
        preview=False,
    )
