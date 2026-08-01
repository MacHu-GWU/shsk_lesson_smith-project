.. _release_history:

Release and Version History
==============================================================================

x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.2.3 (2026-07-31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Minor Improvements**

- All lesson-smith skills can now be self-invoked by Claude models; removed ``disable-model-invocation: true`` from all nine skill frontmatter.

**Miscellaneous**

- Skills-only release.


0.2.2 (2026-07-31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the ``lesson-smith-retrofit`` skill for converting an existing teaching repo whose content is already good but does not follow the lesson-smith spec. It reads the target type from the new repo's ``lm.json``, loads the matching author, forge, and finalize skills, then walks a six-step workflow: check out the legacy repo's highest-numbered teaching branch, locate its material (either the old ``01-Learn-This-Project`` layout or ``docs/tutorials/`` with screenshots under ``img/``), migrate the course content into ``examples/``, and refine in the pieces the legacy repo never had. It covers the author stage only and hands off to forge and finalize, which stay human-driven. The skill is deliberately temporary and self-contained: its playbook and prompt template live in its own directory, so deleting it once the migration is done leaves the base skill untouched.
- Redefine the ``README-ORIGINAL`` frontmatter so it stops reading like a table of contents. Its ``description`` is now specified as the paragraph you would paste to a student: first what the course is about, then why it is worth learning and what you gain, with enumerating knowledge points called out as a red line. Its ``github_about`` is repositioned for the other audience, the course author and fellow teachers, answering only what the repo teaches. The three ``finalize`` skills now stop for the author to sign off on both fields instead of finalizing them unattended.

**Minor Improvements**

- Clarify that the root ``README`` frontmatter ``description`` is a Task-level (branch-level) blurb answering what you will learn, so naming representative ``examples`` themes there is correct, the opposite of the README-ORIGINAL rule. Scoped explicitly to that one line: the body still links to ``examples/README`` rather than restating the mini tasks.
- Require technical terms, product names, and jargon to stay in English in the Chinese versions of these frontmatter fields, since the line travels alone into the syllabus and course index where a translated term is unrecognizable.

**Miscellaneous**

- Skills-only release. The ``shsk_lesson_smith`` Python package, the ``lesson-smith`` CLI, and their lint and sync rules are unchanged.


0.2.1 (2026-07-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add a third teaching repository type: **readup** — a pared-down variant of upskill for pure-reading courses. It keeps the ``examples/`` mini-task layout but drops the entire AI toolchain: no learn/quiz child skills, no generated learning docs, and no quiz mini task. A reader who has never heard of AI agent skills just opens ``examples/`` and reads the mini tasks in order, which is why its root README and TICKET carry no slash commands. Ships the ``lesson-smith-readup-author`` and ``lesson-smith-readup-finalize`` skills (there is no forge step) plus a self-contained ``ref/readup/`` spec set.
- Teach the ``shsk_lesson_smith`` package and the ``lesson-smith`` CLI about the readup type: ``lint`` and ``sync`` now recognize ``{"type": "readup"}``, enforce the single ``01-readup`` task branch, and validate the readup layout with a rule set that omits the quiz-task and forge-output checks. Adds ``ReadupRepo`` and ``ReadupMetadata`` to the public API.

**Minor Improvements**

- Broaden the shared README, TICKET, and README-ORIGINAL specs to name readup alongside upskill and showcase, so their scope statements stay accurate.

**Miscellaneous**

- Add committed ``good_readup_repo`` / ``bad_readup_repo`` test fixtures and linter and sync regression tests for the readup type.


0.1.1 (2026-07-22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First release.
- Ship the ``lesson-smith`` skill family, a set of Claude skills for authoring teaching repositories where a GitHub Repo maps to a Lesson and a Branch maps to a Task. Includes a shared specification base skill plus ``author``, ``forge``, and ``finalize`` skills for guiding the full authoring workflow.
- Support two repository types: **upskill** (learn-and-done skill tutorials) and **showcase** (skill tutorials that can be published as a personal portfolio repo). Each type ships its own repo layout, document specs, and authoring workflow.
- Ship the ``shsk_lesson_smith`` Python package with a public API to resolve, model, and validate teaching repositories (``Repo``, ``UpskillRepo``, ``ShowcaseRepo``, ``lint``, ``sync``).
- Add the ``lesson-smith`` command line tool (powered by Python Fire) with two commands: ``lesson-smith lint`` validates a teaching repo against its type's spec and exits non-zero on failure, and ``lesson-smith sync`` snapshots the current branch's task files and regenerates the ``SYLLABUS`` index. Both support ``--project-root``, ``--json``, and ``--quiet`` flags.

**Minor Improvements**

- Provide type-specific linters for upskill and showcase repos, covering special files (README, TICKET, README-ORIGINAL), frontmatter descriptions, and H1 heading rules.
- Support multi-language teaching material: English files carry no suffix and other languages use a ``<NAME>-<lang>.md`` suffix (currently ``cn`` in addition to English).