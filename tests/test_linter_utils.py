# -*- coding: utf-8 -*-

import pytest

from shsk_lesson_smith.exc import LintError
from pathlib import Path

from shsk_lesson_smith.linter_utils import (
    Frontmatter,
    MarkdownFile,
    check_file_exists,
    check_frontmatter_description,
    check_h1_charset,
    check_h1_matches,
    find_emoji,
)


def write(path, text):
    path.write_text(text, encoding="utf-8")
    return path


class TestFindEmoji:
    def test_finds_emoji(self):
        assert find_emoji("hello 🚀 world") == "🚀"
        assert find_emoji("✅ done") == "✅"
        assert find_emoji("📋 list") == "📋"

    def test_plain_text_has_none(self):
        assert find_emoji("Create a Repo, edit files: done.") is None
        assert find_emoji("中文标题也没有 emoji") is None


class TestFrontmatter:
    def test_from_lines_extracts_description(self):
        fm = Frontmatter.from_lines(["title: x", "description: Learn X.", "tags: a"])
        assert fm == Frontmatter(description="Learn X.", description_raw="Learn X.")

    def test_from_lines_no_description(self):
        assert Frontmatter.from_lines(["title: x"]) == Frontmatter(description=None)

    def test_from_lines_unquotes(self):
        fm = Frontmatter.from_lines(['description: "Learn X."'])
        assert fm.description == "Learn X."
        assert fm.description_raw == '"Learn X."'


class TestMarkdownFile:
    def test_parses_frontmatter_and_body(self, tmp_path):
        path = write(
            tmp_path / "README.md",
            "---\ndescription: Learn X.\n---\n\n# Title\n\nbody line\n",
        )
        md = MarkdownFile.from_path(path)
        assert md.has_frontmatter is True
        assert md.frontmatter == Frontmatter(
            description="Learn X.", description_raw="Learn X."
        )
        assert md.description == "Learn X."
        assert md.h1 == "Title"
        assert md.h1_titles == ["Title"]
        assert "body line" in md.body

    def test_frontmatter_is_none_when_absent(self, tmp_path):
        md = MarkdownFile.from_path(write(tmp_path / "README.md", "# Title\n"))
        assert md.frontmatter is None

    def test_frontmatter_present_but_no_description(self, tmp_path):
        md = MarkdownFile.from_path(
            write(tmp_path / "README.md", "---\ntitle: x\n---\n\n# Title\n")
        )
        assert md.has_frontmatter is True
        assert md.frontmatter == Frontmatter(description=None)
        assert md.description is None

    def test_no_frontmatter(self, tmp_path):
        path = write(tmp_path / "README.md", "# Title\n\nbody\n")
        md = MarkdownFile.from_path(path)
        assert md.has_frontmatter is False
        assert md.description is None
        assert md.h1 == "Title"

    def test_unclosed_frontmatter_is_not_frontmatter(self, tmp_path):
        path = write(tmp_path / "README.md", "---\ndescription: X\n\n# Title\n")
        md = MarkdownFile.from_path(path)
        assert md.has_frontmatter is False
        assert md.description is None

    def test_quoted_description_is_unwrapped(self, tmp_path):
        path = write(tmp_path / "README.md", '---\ndescription: "Learn X."\n---\n')
        md = MarkdownFile.from_path(path)
        assert md.description == "Learn X."

    def test_multiple_h1(self, tmp_path):
        path = write(tmp_path / "README.md", "# One\n\ntext\n\n# Two\n")
        md = MarkdownFile.from_path(path)
        assert md.h1_titles == ["One", "Two"]
        assert md.h1 == "One"

    def test_no_h1(self, tmp_path):
        path = write(tmp_path / "README.md", "## Only H2\n\ntext\n")
        md = MarkdownFile.from_path(path)
        assert md.h1_titles == []
        assert md.h1 is None

    def test_text_is_read_lazily(self, tmp_path):
        # Constructing does not touch the disk; only accessing .text does.
        md = MarkdownFile(tmp_path / "nope.md")
        with pytest.raises(FileNotFoundError):
            _ = md.text

    def test_accepts_str_path(self, tmp_path):
        path = write(tmp_path / "README.md", "# Title\n")
        md = MarkdownFile(str(path))
        assert isinstance(md.path, Path)
        assert md.h1 == "Title"


class TestCheckFileExists:
    def test_passes_when_present(self, tmp_path):
        path = write(tmp_path / "README.md", "x")
        check_file_exists(path)  # no raise

    def test_raises_when_missing(self, tmp_path):
        with pytest.raises(LintError):
            check_file_exists(tmp_path / "nope.md")


class TestCheckFrontmatterDescription:
    def _md(self, tmp_path, text):
        return MarkdownFile.from_path(write(tmp_path / "README.md", text))

    def test_valid(self, tmp_path):
        check_frontmatter_description(
            self._md(tmp_path, '---\ndescription: "Learn X."\n---\n')
        )

    def test_missing_frontmatter(self, tmp_path):
        with pytest.raises(LintError, match="no YAML frontmatter"):
            check_frontmatter_description(self._md(tmp_path, "# Title\n"))

    def test_missing_key(self, tmp_path):
        with pytest.raises(LintError, match="no 'description' key"):
            check_frontmatter_description(self._md(tmp_path, "---\ntitle: x\n---\n"))

    def test_not_double_quoted(self, tmp_path):
        with pytest.raises(LintError, match="double quotes"):
            check_frontmatter_description(
                self._md(tmp_path, "---\ndescription: Learn X.\n---\n")
            )

    def test_single_quoted_is_rejected(self, tmp_path):
        with pytest.raises(LintError, match="double quotes"):
            check_frontmatter_description(
                self._md(tmp_path, "---\ndescription: 'Learn X.'\n---\n")
            )

    def test_empty(self, tmp_path):
        with pytest.raises(LintError, match="is empty"):
            check_frontmatter_description(
                self._md(tmp_path, '---\ndescription: ""\n---\n')
            )

    def test_too_long(self, tmp_path):
        text = '---\ndescription: "' + "x" * 401 + '"\n---\n'
        with pytest.raises(LintError, match="401 characters"):
            check_frontmatter_description(self._md(tmp_path, text))

    def test_forbidden_char(self, tmp_path):
        text = '---\ndescription: "He said hi to `you`"\n---\n'
        with pytest.raises(LintError, match="forbidden character"):
            check_frontmatter_description(self._md(tmp_path, text))


class TestCheckH1Charset:
    def _md(self, tmp_path, text):
        return MarkdownFile.from_path(write(tmp_path / "README.md", text))

    def test_valid(self, tmp_path):
        check_h1_charset(self._md(tmp_path, "# Create a Repo, edit files: go\n"))

    def test_valid_chinese(self, tmp_path):
        check_h1_charset(self._md(tmp_path, "# 使用 Git Branch 隔离改动\n"))

    def test_missing(self, tmp_path):
        with pytest.raises(LintError, match="no H1 title"):
            check_h1_charset(self._md(tmp_path, "## H2 only\n"))

    def test_multiple(self, tmp_path):
        with pytest.raises(LintError, match="2 H1 titles"):
            check_h1_charset(self._md(tmp_path, "# One\n\n# Two\n"))

    def test_forbidden_char(self, tmp_path):
        with pytest.raises(LintError, match="forbidden character"):
            check_h1_charset(self._md(tmp_path, "# Learn Git — fast\n"))

    def test_emoji(self, tmp_path):
        with pytest.raises(LintError, match="emoji"):
            check_h1_charset(self._md(tmp_path, "# 📋 What You Learn\n"))


class TestCheckH1Matches:
    def _md(self, tmp_path, text):
        return MarkdownFile.from_path(write(tmp_path / "README.md", text))

    def test_valid(self, tmp_path):
        check_h1_matches(
            self._md(tmp_path, "# good_upskill_repo\n"), "good_upskill_repo"
        )

    def test_mismatch(self, tmp_path):
        with pytest.raises(LintError, match="must be exactly"):
            check_h1_matches(self._md(tmp_path, "# Wrong Name\n"), "good_upskill_repo")

    def test_missing(self, tmp_path):
        with pytest.raises(LintError, match="no H1 title"):
            check_h1_matches(self._md(tmp_path, "text only\n"), "good_upskill_repo")


if __name__ == "__main__":
    from shsk_lesson_smith.tests import run_cov_test

    run_cov_test(
        __file__,
        "shsk_lesson_smith.linter_utils",
        preview=False,
    )
