# -*- coding: utf-8 -*-

import pytest

from shsk_lesson_smith.exc import LintError
from pathlib import Path

from shsk_lesson_smith.linter_utils import (
    Frontmatter,
    MarkdownFile,
    check_file_exists,
    check_frontmatter_description,
    check_frontmatter_github_about,
    check_h1_charset,
    check_h1_matches,
    check_no_relative_links,
    find_emoji,
    strip_fenced_code_blocks,
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


class TestEstimatedMinutes:
    """The ``**预计用时:**`` line, parsed into a minute pair."""

    def _md(self, tmp_path, line):
        return MarkdownFile.from_path(
            write(tmp_path / "TICKET-cn.md", f"# Title\n\n1. Do it.\n\n{line}\n")
        )

    def test_parses_a_plain_minute_range(self, tmp_path):
        assert self._md(tmp_path, "**预计用时:** 15 到 30 分钟").estimated_minutes == (
            15,
            30,
        )

    def test_ignores_the_trailing_hours_parenthetical(self, tmp_path):
        # The root TICKET writes minutes plus an hours gloss; minutes are the
        # authoritative pair.
        line = "**预计用时:** 385 到 700 分钟 (约 6.5 到 11.5 小时)"
        assert self._md(tmp_path, line).estimated_minutes == (385, 700)

    @pytest.mark.parametrize(
        "line",
        [
            "**预计用时:** 2 到 3 小时",  # hours, not minutes
            "**预计用时:** 大约两小时",  # prose
            "**预计用时:** 30 分钟",  # single value, not a range
        ],
    )
    def test_returns_none_for_anything_not_in_minute_form(self, tmp_path, line):
        assert self._md(tmp_path, line).estimated_minutes is None

    def test_returns_none_when_the_line_is_absent(self, tmp_path):
        md = MarkdownFile.from_path(write(tmp_path / "TICKET-cn.md", "# Title\n"))
        assert md.estimated_minutes is None


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

    def test_too_long_english(self, tmp_path):
        text = '---\ndescription: "' + "x" * 801 + '"\n---\n'
        with pytest.raises(LintError, match="801 characters"):
            check_frontmatter_description(self._md(tmp_path, text))

    def test_at_the_english_limit_is_fine(self, tmp_path):
        text = '---\ndescription: "' + "x" * 800 + '"\n---\n'
        check_frontmatter_description(self._md(tmp_path, text))

    def test_too_long_chinese(self, tmp_path):
        """The Chinese budget is half the English one, since a character in a
        dense script carries roughly twice the information."""
        text = '---\ndescription: "' + "x" * 401 + '"\n---\n'
        md = MarkdownFile.from_path(write(tmp_path / "README-cn.md", text))
        with pytest.raises(LintError, match="401 characters"):
            check_frontmatter_description(md)

    def test_english_budget_does_not_apply_to_chinese(self, tmp_path):
        """A length legal in English must still fail in Chinese, otherwise the
        wider English budget would silently relax the Chinese one."""
        text = '---\ndescription: "' + "x" * 500 + '"\n---\n'
        check_frontmatter_description(self._md(tmp_path, text))
        md = MarkdownFile.from_path(write(tmp_path / "README-cn.md", text))
        with pytest.raises(LintError, match="400-character limit"):
            check_frontmatter_description(md)

    def test_forbidden_char(self, tmp_path):
        text = '---\ndescription: "He said hi to `you`"\n---\n'
        with pytest.raises(LintError, match="forbidden character"):
            check_frontmatter_description(self._md(tmp_path, text))

    def test_apostrophe_is_allowed(self, tmp_path):
        """The value is already wrapped in double quotes, so an apostrophe
        cannot close it, and English prose needs it constantly."""
        text = '---\ndescription: "It\'s GitHub\'s own About box."\n---\n'
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


class TestCheckFrontmatterGithubAbout:
    def _md(self, tmp_path, text):
        return MarkdownFile.from_path(write(tmp_path / "README-ORIGINAL.md", text))

    def test_valid(self, tmp_path):
        check_frontmatter_github_about(
            self._md(tmp_path, '---\ngithub_about: "Learn X in the browser."\n---\n')
        )

    def test_no_frontmatter(self, tmp_path):
        with pytest.raises(LintError, match="github_about"):
            check_frontmatter_github_about(self._md(tmp_path, "# Title\n"))

    def test_missing_key(self, tmp_path):
        with pytest.raises(LintError, match="no 'github_about' key"):
            check_frontmatter_github_about(
                self._md(tmp_path, '---\ndescription: "x."\n---\n')
            )

    def test_not_double_quoted(self, tmp_path):
        with pytest.raises(LintError, match="double quotes"):
            check_frontmatter_github_about(
                self._md(tmp_path, "---\ngithub_about: Learn X.\n---\n")
            )

    def test_too_long_english(self, tmp_path):
        """English gets only modest headroom here. The cap is GitHub's About
        box, not a style budget, so it does not double the way description does."""
        text = '---\ngithub_about: "' + "x" * 301 + '"\n---\n'
        with pytest.raises(LintError, match="301 characters"):
            check_frontmatter_github_about(self._md(tmp_path, text))

    def test_too_long_chinese(self, tmp_path):
        text = '---\ngithub_about: "' + "x" * 151 + '"\n---\n'
        md = MarkdownFile.from_path(
            write(tmp_path / "README-ORIGINAL-cn.md", text)
        )
        with pytest.raises(LintError, match="150-character limit"):
            check_frontmatter_github_about(md)

    def test_at_the_chinese_limit_is_fine(self, tmp_path):
        text = '---\ngithub_about: "' + "x" * 150 + '"\n---\n'
        md = MarkdownFile.from_path(
            write(tmp_path / "README-ORIGINAL-cn.md", text)
        )
        check_frontmatter_github_about(md)

    def test_forbidden_char(self, tmp_path):
        text = '---\ngithub_about: "Has a `code` char."\n---\n'
        with pytest.raises(LintError, match="forbidden character"):
            check_frontmatter_github_about(self._md(tmp_path, text))


class TestCheckNoRelativeLinks:
    def _md(self, tmp_path, body):
        return MarkdownFile.from_path(write(tmp_path / "TICKET.md", body))

    def test_passes_with_no_links(self, tmp_path):
        check_no_relative_links(self._md(tmp_path, "# T\n\nPlain text, no links.\n"))

    def test_passes_with_absolute_url(self, tmp_path):
        check_no_relative_links(
            self._md(tmp_path, "# T\n\nSee [docs](https://example.com/x) here.\n")
        )

    def test_passes_with_anchor(self, tmp_path):
        check_no_relative_links(self._md(tmp_path, "# T\n\nJump to [top](#intro).\n"))

    def test_passes_with_angle_bracket_absolute(self, tmp_path):
        check_no_relative_links(
            self._md(tmp_path, "# T\n\nSee [x](<https://example.com/y>).\n")
        )

    def test_raises_on_relative_link(self, tmp_path):
        with pytest.raises(LintError, match="relative-path link"):
            check_no_relative_links(
                self._md(tmp_path, "# T\n\nSee [readme](../01-x/README.md).\n")
            )

    def test_raises_on_bare_relative_path_link(self, tmp_path):
        with pytest.raises(LintError, match="relative-path link"):
            check_no_relative_links(
                self._md(tmp_path, "# T\n\nOpen [it](notes.md) first.\n")
            )


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


class TestStripFencedCodeBlocks:
    """Fenced code blocks are literal content, not markdown structure."""

    def test_no_fence_is_unchanged(self):
        assert strip_fenced_code_blocks("# Title\n\ntext") == "# Title\n\ntext"

    def test_drops_block_and_its_fences(self):
        text = "before\n```python\nx = 1\n```\nafter"
        assert strip_fenced_code_blocks(text) == "before\nafter"

    def test_drops_hash_comments_inside_a_block(self):
        text = "before\n```python\n# not a heading\nx = 1\n```\nafter"
        assert strip_fenced_code_blocks(text) == "before\nafter"

    def test_tilde_fences(self):
        text = "a\n~~~\n# comment\n~~~\nb"
        assert strip_fenced_code_blocks(text) == "a\nb"

    def test_longer_fence_can_quote_an_inner_fence(self):
        # A ````-fenced block quoting a ```-fenced one: the inner fence must not
        # close the outer block. The specs themselves are written this way.
        text = "a\n````text\n```python\n# inner\n```\n````\nb"
        assert strip_fenced_code_blocks(text) == "a\nb"

    def test_closing_fence_may_be_longer(self):
        text = "a\n```\nx\n`````\nb"
        assert strip_fenced_code_blocks(text) == "a\nb"

    def test_fence_with_info_string_does_not_close(self):
        # Only a bare fence closes a block, so this stays open to the end.
        text = "a\n```python\nx = 1\n```python\ny = 2\n```\nb"
        assert strip_fenced_code_blocks(text) == "a\nb"

    def test_unclosed_fence_runs_to_end_of_document(self):
        assert strip_fenced_code_blocks("a\n```\nx\ny") == "a"

    def test_indented_opening_fence_up_to_three_spaces(self):
        text = "a\n   ```\n# comment\n   ```\nb"
        assert strip_fenced_code_blocks(text) == "a\nb"


class TestStructuralChecksIgnoreCodeBlocks:
    """H1s, the estimated-time line and relative links all skip fenced blocks."""

    def test_python_comment_is_not_an_h1(self, tmp_path):
        path = write(
            tmp_path / "README.md",
            "# Real Title\n\n```python\n# Q1: the whole hierarchy\n"
            'for e in Entity.query("CUSTOMER#C001"): ...\n```\n',
        )
        md = MarkdownFile.from_path(path)
        assert md.h1_titles == ["Real Title"]
        check_h1_charset(md)

    def test_shell_comment_is_not_an_h1(self, tmp_path):
        path = write(
            tmp_path / "README.md",
            "# Real Title\n\n```bash\n# run it\npython main.py\n```\n",
        )
        md = MarkdownFile.from_path(path)
        assert md.h1_titles == ["Real Title"]

    def test_real_second_h1_is_still_flagged(self, tmp_path):
        path = write(
            tmp_path / "README.md",
            "# One\n\n```python\n# comment\n```\n\n# Two\n",
        )
        md = MarkdownFile.from_path(path)
        assert md.h1_titles == ["One", "Two"]

    def test_sample_relative_link_is_not_flagged(self, tmp_path):
        path = write(
            tmp_path / "TICKET.md",
            "# T\n\nSample:\n\n```text\n[label](../other/README-cn.md)\n```\n",
        )
        check_no_relative_links(MarkdownFile.from_path(path))

    def test_real_relative_link_is_still_flagged(self, tmp_path):
        path = write(
            tmp_path / "TICKET.md",
            "# T\n\n[label](../other/README-cn.md)\n",
        )
        with pytest.raises(LintError, match="relative-path link"):
            check_no_relative_links(MarkdownFile.from_path(path))

    def test_estimated_time_inside_a_block_is_ignored(self, tmp_path):
        path = write(
            tmp_path / "TICKET.md",
            "# T\n\n```text\n**预计用时:** 5 到 15 分钟\n```\n\n"
            "**预计用时:** 30 到 60 分钟\n",
        )
        assert MarkdownFile.from_path(path).estimated_minutes == (30, 60)
