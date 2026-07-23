.. _release_history:

Release and Version History
==============================================================================


x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.2.1 (2026-07-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add a third teaching repository type: **readup** — a pared-down variant of
  upskill for pure-reading courses. It keeps the ``examples/`` mini-task layout
  but drops the entire AI toolchain: no learn/quiz child skills, no generated
  learning docs, and no quiz mini task. A reader who has never heard of AI agent
  skills just opens ``examples/`` and reads the mini tasks in order, which is why
  its root README and TICKET carry no slash commands. Ships the
  ``lesson-smith-readup-author`` and ``lesson-smith-readup-finalize`` skills
  (there is no forge step) plus a self-contained ``ref/readup/`` spec set.
- Teach the ``shsk_lesson_smith`` package and the ``lesson-smith`` CLI about the
  readup type: ``lint`` and ``sync`` now recognize ``{"type": "readup"}``, enforce
  the single ``01-readup`` task branch, and validate the readup layout with a rule
  set that omits the quiz-task and forge-output checks. Adds ``ReadupRepo`` and
  ``ReadupMetadata`` to the public API.

**Minor Improvements**

- Broaden the shared README, TICKET, and README-ORIGINAL specs to name readup
  alongside upskill and showcase, so their scope statements stay accurate.

**Miscellaneous**

- Add committed ``good_readup_repo`` / ``bad_readup_repo`` test fixtures and
  linter and sync regression tests for the readup type.


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
