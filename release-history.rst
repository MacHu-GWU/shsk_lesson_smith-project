.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.1 (2026-07-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Ship the ``lesson-smith`` skill family, a set of Claude skills for authoring
  teaching repositories where a GitHub Repo maps to a Lesson and a Branch maps
  to a Task. Includes a shared specification base skill plus ``author``,
  ``forge``, and ``finalize`` skills for guiding the full authoring workflow.
- Support two repository types: **upskill** (learn-and-done skill tutorials) and
  **showcase** (skill tutorials that can be published as a personal portfolio
  repo). Each type ships its own repo layout, document specs, and authoring
  workflow.
- Ship the ``shsk_lesson_smith`` Python package with a public API to resolve,
  model, and validate teaching repositories (``Repo``, ``UpskillRepo``,
  ``ShowcaseRepo``, ``lint``, ``sync``).
- Add the ``lesson-smith`` command line tool (powered by Python Fire) with two
  commands: ``lesson-smith lint`` validates a teaching repo against its type's
  spec and exits non-zero on failure, and ``lesson-smith sync`` snapshots the
  current branch's task files and regenerates the ``SYLLABUS`` index. Both
  support ``--project-root``, ``--json``, and ``--quiet`` flags.

**Minor Improvements**

- Provide type-specific linters for upskill and showcase repos, covering special
  files (README, TICKET, README-ORIGINAL), frontmatter descriptions, and H1
  heading rules.
- Support multi-language teaching material: English files carry no suffix and
  other languages use a ``<NAME>-<lang>.md`` suffix (currently ``cn`` in addition
  to English).
