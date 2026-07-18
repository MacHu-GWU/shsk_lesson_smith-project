# -*- coding: utf-8 -*-

from shsk_lesson_smith.linter import (
    EvolveLinter,
    Linter,
    ShowcaseLinter,
    UpskillLinter,
    make_linter,
)
from shsk_lesson_smith.repo_types import resolve_repo

from conftest import make_root, write_special_file


def lint_messages(root):
    return [str(p) for p in make_linter(resolve_repo(root)).lint()]


class TestMakeLinter:
    def test_picks_class_by_repo_type(self, tmp_path):
        root = make_root(tmp_path, "evolve")
        assert type(make_linter(resolve_repo(root))) is EvolveLinter

        (root / "lm.json").write_text('{"type": "showcase"}', encoding="utf-8")
        assert type(make_linter(resolve_repo(root))) is ShowcaseLinter

        (root / "lm.json").write_text('{"type": "upskill"}', encoding="utf-8")
        assert type(make_linter(resolve_repo(root))) is UpskillLinter

        (root / "lm.json").unlink()
        assert type(make_linter(resolve_repo(root))) is Linter


class TestEvolveLint:
    def test_valid_repo_is_clean(self, evolve_root):
        assert lint_messages(evolve_root) == []

    def test_missing_manifest(self, evolve_root):
        (evolve_root / "lm.json").unlink()
        messages = lint_messages(evolve_root)
        assert any("lm.json" in m and "missing" in m for m in messages)

    def test_invalid_manifest_type(self, evolve_root):
        (evolve_root / "lm.json").write_text('{"type": "bad"}', encoding="utf-8")
        messages = lint_messages(evolve_root)
        assert any("'type' must be one of" in m for m in messages)

    def test_missing_language_variant(self, evolve_root):
        (evolve_root / "TICKET-cn.md").unlink()
        messages = lint_messages(evolve_root)
        assert any(
            "TICKET-cn.md" in m and "missing language variant" in m
            for m in messages
        )

    def test_missing_required_root_file(self, evolve_root):
        (evolve_root / "TICKET.md").unlink()
        (evolve_root / "TICKET-cn.md").unlink()
        messages = lint_messages(evolve_root)
        assert any("TICKET.md" in m and "required file is missing" in m
                   for m in messages)

    def test_description_rules(self, evolve_root):
        write_special_file(evolve_root / "README.md", description="x" * 401)
        write_special_file(
            evolve_root / "README-cn.md", description='He said "hi" to you'
        )
        (evolve_root / "TICKET.md").write_text("# No frontmatter\n", encoding="utf-8")
        messages = lint_messages(evolve_root)
        assert any("README.md" in m and "401 chars" in m for m in messages)
        assert any(
            "README-cn.md" in m and "forbidden character" in m for m in messages
        )
        assert any(
            "TICKET.md" in m and "missing a one-line 'description'" in m
            for m in messages
        )

    def test_missing_docs_tasks(self, evolve_root):
        import shutil

        shutil.rmtree(evolve_root / "docs")
        messages = lint_messages(evolve_root)
        assert any("docs/tasks" in m and "missing" in m for m in messages)

    def test_bad_task_dir_name(self, evolve_root):
        (evolve_root / "docs" / "tasks" / "01-Bad_Name").mkdir()
        messages = lint_messages(evolve_root)
        assert any("01-Bad_Name" in m for m in messages)

    def test_task_snapshot_incomplete(self, evolve_root):
        (evolve_root / "docs" / "tasks" / "01-intro" / "TICKET-cn.md").unlink()
        messages = lint_messages(evolve_root)
        assert any(
            "01-intro" in m and "TICKET-cn.md" in m for m in messages
        )


class TestShowcaseLint:
    def test_valid_repo_is_clean(self, showcase_root):
        assert lint_messages(showcase_root) == []

    def test_root_ticket_not_required(self, showcase_root):
        # No TICKET at root in the fixture, and that is fine for showcase.
        assert lint_messages(showcase_root) == []

    def test_missing_examples_dir(self, showcase_root):
        import shutil

        shutil.rmtree(showcase_root / "examples")
        messages = lint_messages(showcase_root)
        assert any("examples" in m and "missing" in m for m in messages)

    def test_example_missing_ticket(self, showcase_root):
        (showcase_root / "examples" / "01-hello-world" / "TICKET.md").unlink()
        (showcase_root / "examples" / "01-hello-world" / "TICKET-cn.md").unlink()
        messages = lint_messages(showcase_root)
        assert any(
            "01-hello-world" in m and "TICKET.md" in m for m in messages
        )


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.linter",
        preview=False,
    )
