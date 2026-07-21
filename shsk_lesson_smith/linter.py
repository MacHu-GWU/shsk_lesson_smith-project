# -*- coding: utf-8 -*-

"""Linting for teaching repos: the standard rules, results, and dispatcher.

Design (see also linter_for_<type>.py):

- Linting is a *function*, not a Repo method: :func:`lint` takes a :class:`Repo`
  and returns a :class:`LintReport`. Structure (Repo / Metadata) uses subclasses;
  behavior (linting) uses composed functions, so there is no parallel Linter
  class hierarchy.
- Each *check point* is a small function that raises :class:`LintError`
  (the ``check_*`` primitives in linter_utils). :func:`run_check` wraps one into
  a :class:`CheckResult`, so a failing check is collected, never fatal.
- A *rule* is ``(repo) -> list[CheckResult]``. This file holds the rules every
  repo type shares. Each ``linter_for_<type>`` module exposes a ``RULES`` list
  composing these shared rules with its own type-specific ones. :func:`lint`
  dispatches on ``repo.repo_type`` to the right module. Splitting a type into
  its own file is a "grow into it" knob, not an upfront commitment.

Spec source of truth: the shared rules here enforce the type-agnostic specs in the
top-level ``.claude/skills/lesson-smith/skills/lesson-smith/ref/*.md`` files (that
directory's own ``.md`` files, not its subfolders): repo-layout, readme-spec,
ticket-spec, readme-original-spec, syllabus-spec. Type-specific rules live in the
``linter_for_<type>`` modules and reference that type's spec subfolder. Those specs
are authoritative; keep these checks in sync with them.
"""

import dataclasses
import json
import re
from pathlib import Path

from .constants import (
    TASK_DIR_PATTERN,
    LangEnum,
    RepoTypeEnum,
)
from .exc import LintError
from .linter_utils import (
    MarkdownFile,
    check_file_exists,
    check_frontmatter_description,
    check_frontmatter_github_about,
    check_h1_charset,
    check_h1_matches,
    check_no_relative_links,
)
from .repo import Metadata, Repo

# English (None) plus every supported language variant.
LANGS = (None, *LangEnum)


# --------------------------------------------------------------------------- #
# Result types
# --------------------------------------------------------------------------- #
@dataclasses.dataclass
class CheckResult:
    """The outcome of one check point at one location."""

    location: str
    passed: bool
    message: "str | None" = None


@dataclasses.dataclass
class LintReport:
    """Aggregated results of linting one repo."""

    dir_project_root: Path
    results: "list[CheckResult]"

    @property
    def passed(self) -> bool:
        return all(r.passed for r in self.results)

    def failures(self) -> "list[CheckResult]":
        return [r for r in self.results if not r.passed]

    def to_dict(self) -> dict:
        """Plain-data form: the whole report as nested dicts / lists."""
        return {
            "dir_project_root": str(self.dir_project_root),
            "passed": self.passed,
            "results": [dataclasses.asdict(r) for r in self.results],
        }

    def to_json(self, indent: int = 2) -> str:
        """JSON form, one entry per check point (``ensure_ascii=False``)."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def render(self) -> str:
        """Human-readable report: one line per file, grouped, with emoji status.

        Check points are collected per file, so a file shows a single ✅ / ❌
        line; a failing file lists each problem message beneath it.
        """
        order: "list[str]" = []
        grouped: "dict[str, list[CheckResult]]" = {}
        for result in self.results:
            if result.location not in grouped:
                grouped[result.location] = []
                order.append(result.location)
            grouped[result.location].append(result)

        lines: "list[str]" = []
        for location in order:
            fails = [r for r in grouped[location] if not r.passed]
            if fails:
                lines.append(f"❌ {location}")
                for fail in fails:
                    lines.append(f"     {fail.message}")
            else:
                lines.append(f"✅ {location}")

        lines.append("")
        if self.passed:
            lines.append("PASSED")
        else:
            lines.append(f"FAILED ({len(self.failures())} problem(s))")
        return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Building blocks (also used by linter_for_<type> modules)
# --------------------------------------------------------------------------- #
def run_check(location, check, *args) -> CheckResult:
    """Run one ``check_*`` primitive, catching :class:`LintError` into a result."""
    try:
        check(*args)
        return CheckResult(location=str(location), passed=True, message=None)
    except LintError as error:
        return CheckResult(location=str(location), passed=False, message=str(error))


def lint_file_content(
    path: Path,
    *,
    description: bool = False,
    h1: "str | None" = None,
    h1_expected: "str | None" = None,
    no_relative_links: bool = False,
    github_about: bool = False,
) -> "list[CheckResult]":
    """Content checks for one existing markdown file.

    ``h1`` is ``"charset"`` (allowed character set), ``"match"`` (must equal
    ``h1_expected``), or None (skip the H1 check). ``no_relative_links`` adds the
    TICKET-only check that the body carries no relative-path links.
    ``github_about`` adds the README-ORIGINAL-only tagline check.
    """
    md = MarkdownFile(path)
    out: "list[CheckResult]" = []
    if description:
        out.append(run_check(path, check_frontmatter_description, md))
    if github_about:
        out.append(run_check(path, check_frontmatter_github_about, md))
    if h1 == "charset":
        out.append(run_check(path, check_h1_charset, md))
    elif h1 == "match":
        out.append(run_check(path, check_h1_matches, md, h1_expected))
    if no_relative_links:
        out.append(run_check(path, check_no_relative_links, md))
    return out


def lint_file_group(get_path, *, required: bool, **content) -> "list[CheckResult]":
    """Existence + language completeness + content checks for one special file.

    ``get_path`` maps a language (None = English) to a path. If any variant
    exists, every variant must exist (language completeness). Content checks
    (``description=``, ``h1=``, ``h1_expected=``) run on each existing variant.
    A missing group is a failure only when ``required``.
    """
    variants = [p for lang in LANGS if (p := get_path(lang)) is not None]
    if not variants:
        return []
    existing = [p for p in variants if p.exists()]
    out: "list[CheckResult]" = []
    if not existing:
        if required:
            out.append(run_check(variants[0], check_file_exists, variants[0]))
        return out
    for path in variants:
        out.append(run_check(path, check_file_exists, path))
        if path.exists():
            out.extend(lint_file_content(path, **content))
    return out


def _check_task_dir_name(path: Path) -> None:
    if not TASK_DIR_PATTERN.match(path.name):
        raise LintError(
            f"Directory name {path.name!r} must be NN-lowercase-hyphen-words, "
            "e.g. 01-branch-name."
        )


def lint_task_dir(dir_path: Path, get_readme, get_ticket) -> "list[CheckResult]":
    """A task-shaped dir: strict NN-name, plus complete README + TICKET groups."""
    out = [run_check(dir_path, _check_task_dir_name, dir_path)]
    out.extend(
        lint_file_group(get_readme, required=True, description=True, h1="charset")
    )
    out.extend(
        lint_file_group(
            get_ticket,
            required=True,
            description=True,
            h1="charset",
            no_relative_links=True,
        )
    )
    return out


# --------------------------------------------------------------------------- #
# Shared rules (every repo type runs these)
# --------------------------------------------------------------------------- #
def rule_manifest(repo: Repo) -> "list[CheckResult]":
    """lm.json must exist, be valid JSON, and declare a known ``type``."""

    def _check() -> None:
        path = repo.path_lm_json
        if not path.exists():
            raise LintError("lm.json is missing at the repo root.")
        try:
            Metadata.from_json_file(path)
        except json.JSONDecodeError:
            raise LintError("lm.json is not valid JSON.")
        except ValueError as error:
            raise LintError(f"lm.json is invalid: {error}")

    return [run_check(repo.path_lm_json, _check)]


def rule_readme_original(repo: Repo) -> "list[CheckResult]":
    """Root README-ORIGINAL: complete, valid description and github_about, H1 == repo name.

    README-ORIGINAL is the Lesson-level (whole-repo) intro. Its ``description`` is
    the fuller catalog blurb; its ``github_about`` is the compressed tagline that
    also fits GitHub's About box.
    """
    return lint_file_group(
        repo.get_path_readme_original,
        required=True,
        description=True,
        github_about=True,
        h1="match",
        h1_expected=repo.dir_project_root.name,
    )


def _parse_syllabus_sections(body: str) -> "list[tuple[str, str]]":
    """Parse ``## <branch>`` sections into ``[(branch, description), ...]``.

    The description is everything between an H2 and the next H2, stripped.
    """
    sections: "list[tuple[str, str]]" = []
    branch: "str | None" = None
    desc_lines: "list[str]" = []
    for line in body.splitlines():
        if line.startswith("## "):
            if branch is not None:
                sections.append((branch, "\n".join(desc_lines).strip()))
            branch = line[3:].strip()
            desc_lines = []
        elif branch is not None:
            desc_lines.append(line)
    if branch is not None:
        sections.append((branch, "\n".join(desc_lines).strip()))
    return sections


def _check_syllabus_matches_tasks(repo: Repo, sections) -> None:
    branches = [branch for branch, _ in sections]
    dirs = [d.name for d in repo.iter_dir_tasks()]
    if branches != dirs:
        raise LintError(
            f"SYLLABUS sections {branches} do not match the docs/tasks/ "
            f"directories {dirs} (same set, same order)."
        )


def _check_syllabus_numbering(sections) -> None:
    numbers = []
    for branch, _ in sections:
        match = re.match(r"^(\d\d)-", branch)
        if match is None:
            raise LintError(
                f"SYLLABUS section {branch!r} must start with a two-digit number."
            )
        numbers.append(int(match.group(1)))
    if numbers != list(range(1, len(numbers) + 1)):
        raise LintError(
            f"SYLLABUS task numbers must be consecutive 01, 02, ... with no gaps; "
            f"got {numbers}."
        )


def _check_syllabus_entry(repo: Repo, lang, branch: str, desc: str) -> None:
    if not desc:
        raise LintError(f"SYLLABUS entry {branch!r} has no description line.")
    if "\n" in desc:
        raise LintError(
            f"SYLLABUS entry {branch!r} description must be a single line."
        )
    readme = repo.get_path_task_readme(branch, lang)
    expected = MarkdownFile(readme).description if readme.exists() else None
    if expected is None:
        raise LintError(
            f"SYLLABUS entry {branch!r}: docs/tasks/{branch}/{readme.name} has no "
            "frontmatter description to match against."
        )
    if desc != expected:
        raise LintError(
            f"SYLLABUS entry {branch!r} description does not match the description "
            f"in docs/tasks/{branch}/{readme.name}."
        )


def rule_syllabus(repo: Repo) -> "list[CheckResult]":
    """docs/tasks/SYLLABUS: existence, language completeness, and content.

    Content is generated from the task READMEs, so linting verifies it did not
    drift: H1 is ``Syllabus``; the ``## branch`` sections match the docs/tasks/
    dirs in order; the numbers are consecutive; each one-line description equals
    the matching-language README's frontmatter description.
    """
    out = lint_file_group(repo.get_path_syllabus, required=True)
    for lang in LANGS:
        path = repo.get_path_syllabus(lang)
        if not path.exists():
            continue
        md = MarkdownFile(path)
        out.append(run_check(path, check_h1_matches, md, "Syllabus"))
        sections = _parse_syllabus_sections(md.body)
        out.append(run_check(path, _check_syllabus_matches_tasks, repo, sections))
        out.append(run_check(path, _check_syllabus_numbering, sections))
        for branch, desc in sections:
            out.append(run_check(path, _check_syllabus_entry, repo, lang, branch, desc))
    return out


def rule_task_snapshots(repo: Repo) -> "list[CheckResult]":
    """Every docs/tasks/NN-*/ snapshot: strict name, complete README + TICKET."""
    out: "list[CheckResult]" = []
    for dir_task in repo.iter_dir_tasks():
        name = dir_task.name
        out.extend(
            lint_task_dir(
                dir_task,
                lambda lang, n=name: repo.get_path_task_readme(n, lang),
                lambda lang, n=name: repo.get_path_task_ticket(n, lang),
            )
        )
    return out


# --------------------------------------------------------------------------- #
# Shared helpers for examples-based repo types (upskill / showcase)
#
# These are type-agnostic but only apply to the two types that keep mini tasks
# under examples/, so they live here and each of those linter_for_<type> modules
# composes them (upskill re-exports them for backward-compatible imports).
# --------------------------------------------------------------------------- #
def rule_root_overview(repo: Repo) -> "list[CheckResult]":
    """Repo-root README (course overview) and TICKET (whole-course acceptance).

    Both carry a mandated frontmatter description and H1, so beyond existence and
    language completeness they get the full description + H1-charset checks. The
    root TICKET is optional, but when present it is also checked for relative-path
    links (it ends up in a GitHub Issue). The root README may link relatively, so
    it is not.
    """
    out = lint_file_group(
        repo.get_path_readme, required=True, description=True, h1="charset"
    )
    out += lint_file_group(
        repo.get_path_ticket,
        required=False,
        description=True,
        h1="charset",
        no_relative_links=True,
    )
    return out


def _check_examples_numbering(example_dirs: "list") -> None:
    """The examples mini tasks must be numbered consecutively from 01, no gaps."""
    numbers = []
    for dir_example in example_dirs:
        match = re.match(r"^(\d\d)-", dir_example.name)
        if match is None:
            raise LintError(
                f"examples mini task {dir_example.name!r} must start with a "
                "two-digit number, e.g. 01-title."
            )
        numbers.append(int(match.group(1)))
    if not numbers:
        raise LintError(
            "examples/ has no mini task directories; expected 01-title, "
            "02-title, and so on."
        )
    numbers.sort()
    if numbers != list(range(1, len(numbers) + 1)):
        raise LintError(
            "examples mini tasks must be numbered consecutively from 01 with no "
            f"gaps; got {numbers}."
        )


# --------------------------------------------------------------------------- #
# Dispatch
# --------------------------------------------------------------------------- #
def _rules_module_for(repo_type: "RepoTypeEnum | None"):
    """Lazily import the linter_for_<type> module (avoids an import cycle)."""
    if repo_type is RepoTypeEnum.upskill:
        from . import linter_for_upskill as module
    elif repo_type is RepoTypeEnum.showcase:
        from . import linter_for_showcase as module
    elif repo_type is RepoTypeEnum.evolve:
        from . import linter_for_evolve as module
    else:
        return None
    return module


def lint(repo: Repo) -> LintReport:
    """Lint ``repo`` and return a :class:`LintReport`.

    Dispatches on ``repo.repo_type`` to the matching ``linter_for_<type>``
    rule set. When the type is unknown (missing / broken lm.json), only the
    manifest rule runs, so the report explains the manifest problem instead of
    guessing a layout.
    """
    module = _rules_module_for(repo.repo_type)
    if module is None:
        return LintReport(repo.dir_project_root, rule_manifest(repo))
    results = [result for rule in module.RULES for result in rule(repo)]
    return LintReport(repo.dir_project_root, results)


def lint_project(project_root: "Path | str | None" = None) -> LintReport:
    """Resolve the teaching repo and lint it. The CLI's entire core.

    With ``project_root`` given, that path is the repo root (resolved to an
    absolute path so report locations are absolute). Without it, the root is
    found by walking up from the current working directory (:meth:`Repo.from_cwd`).
    """
    if project_root is not None:
        repo = Repo(dir_project_root=Path(project_root).resolve())
    else:
        repo = Repo.from_cwd()
    return lint(repo)
