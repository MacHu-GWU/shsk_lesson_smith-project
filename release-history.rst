.. _release_history:

Release and Version History
==============================================================================

x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.3.0 (2026-08-12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **Drop the Chinese-to-English rewrite step from every authoring flow.** The previous cycle built a whole pipeline for it; the output did not hold up (chinglish, silently compressed content, terminology that forked across documents), so rather than ship a batch of English that would need redoing, the step is removed whole. ``rewrite-en-spec.md`` and ``run-rewrite-en.md`` now live in the skill's ``archive/``, and each of the three workflows keeps a closing ``附: 中译英 (当前跳过)`` section recording the decision. Courses are authored in Chinese only. The unsuffixed English files still exist so the layout never changes, but they are deliberately empty placeholders until multi-language returns as its own module. **This is the expected end state of a finished repo, not an outstanding debt.**
- **Lint gained a per-language switch, which is what makes the above safe.** ``LINT_ENABLED_BY_LANG`` in ``constants`` decides whether a language takes part in linting at all, and every rule that walks language variants goes through ``linted_langs()``. A disabled language is skipped whole: not required to exist, contents never checked. English ships disabled, so a tree full of empty English placeholders lints clean instead of failing every content check for a reason that says nothing about the course. Turning English back on is a one-word change here rather than a rewrite of the linter.
- **Reorganize ``ref/`` into one common layer and three type layers.** It used to be flat top-level specs plus a folder per type, with the same rules written once per type and free to drift. Now ``00-common/`` carries the shared standard in reading order (01 layout, 02 to 07 document specs, 08 to 10 the process steps, 11 to 14 what several types share), and ``01-readup/`` ``02-upskill/`` ``03-showcase/`` hold only what is genuinely specific to each. Roughly 850 duplicated lines (both quiz specs plus the entire forge material set) moved into the common layer, where the type name is a ``{{TYPE}}`` placeholder substituted at generation time. That placeholder is the one cost of sharing, and it is mechanically checkable: both forge skills fail their verify phase if ``{{`` survives into the output.
- **Every document spec is now a directory holding a spec and a template.** The old shape was one file whose top comment held the entire specification and whose body doubled as the template. Measured at 171 comment lines to 13 template lines, it also could not use horizontal rules (two hyphens truncate an HTML comment), rendered as a blank block in any preview, offered no headings for other specs to link into, and left a delete-the-comment step that could be forgotten. Split apart, the spec is ordinary renderable markdown and the template is pure skeleton with bracketed placeholders and not one comment, copied over whole with nothing to strip. The ``corpus/`` folders are retired along with it.
- **Split each authoring flow into step skills.** The three ``lesson-smith-*-author`` skills are now routers: they load the base skill, read the main script, work out which step the creator is on, and hand off. The work itself lives in 23 new step skills, one per phase — readup has 10 steps in 6 phases, upskill 13 in 8, showcase 14 in 9. Each step skill names exactly the specs that step needs and the red lines it must hold, so a phase no longer has to carry the whole standard in context. Each also checks for the ``LESSON-SMITH-LOADED`` marker on entry, which turns "type the author command once per session" from an easily forgotten convention into a rule that catches itself immediately rather than at ship time.
- **Add the three process specs the step skills run on**: ``08-series-converge-spec`` (read the whole series and make it one line, with the two classes of problem to look for and who decides), ``09-root-docs-spec`` (write the three root documents from the finished examples, including a mandatory stop for the creator to sign off on the ``README-ORIGINAL`` frontmatter), and ``10-ship-spec`` (preflight, the two commands, and which step each lint error sends you back to). ``14-wrap-up-readme-spec`` is new as well, covering the closing task that every type has.
- **Frontmatter length limits are per language.** ``description`` allows 400 characters in Chinese and 800 in English; ``github_about`` allows 150 and 300. A character carries very different amounts of information depending on the script, so a single global cap would either fail every English variant or keep the Chinese ones far under-used. The two fields get different headroom on purpose: the ``description`` cap is a style budget we choose, while the ``github_about`` cap is external, since GitHub truncates its About box around 350 characters whatever the script. The language is derived from the file name, so a check on a single file is correct without the caller having to say which variant it handed over.

**Minor Improvements**

- Allow the ASCII apostrophe inside ``description`` and ``github_about``. The value is already wrapped in double quotes, so an apostrophe cannot close the wrapper, and English prose needs it constantly. It stays banned in H1 titles, where the reasoning is different: an H1 travels around as a bare unwrapped string with no quotes protecting it.
- Settle the vocabulary on three words — Lesson, Task, and special file — and apply it everywhere including lint messages, which previously said "mini task". ``tutorial``, ``example``, and ``mini task`` are all names for a Task; only Task appears in the specs now, so two documents can no longer look like they are describing different things.
- Record ``lm.json`` in the authoring flow. Nothing ever told a creator to create it, yet ``rule_manifest`` runs first and short-circuits the whole report, so a missing manifest surfaced at ship time as one unexplained line with every other check silently skipped. Step 1 of all three workflows now creates it, and the ship spec lists it first in the preflight and covers both failure modes in its error table.
- Extract ``get_variant_name`` from ``get_variant_filename``, for the language suffixes that sit on a bare name rather than a file name, such as the forge-generated child skill directories.
- State the checks the layout and ship specs had been omitting: the single numbered branch must be named ``01-<type>``, the special task directory names and their positions are enforced, and the forge outputs are checked for existence. All three were already implemented; only the documentation was incomplete, which left the same file contradicting itself.

**Bugfixes**

- ``lesson-smith lint`` required the showcase demo task to be the highest-numbered example, contradicting the layout spec's hard rule that the wrap-up task comes after every special task. Any showcase repo built to the current standard therefore failed at the ship step with an error that argued with the specification, and pinning the linter version meant it would not heal on its own. The rule now checks what the spec actually says: the demo comes directly after the quiz, and something follows it. Because the demo's directory name is fixed, that second clause also catches a missing wrap-up task for free.
- ``rule_forge_outputs`` looked for the unsuffixed English file and directory names, and sat outside the per-language switch. Forge emits the ``-cn`` set only, so every conformant upskill repo failed five checks and every showcase repo nine. The rule now derives names per language from language-free bases and walks ``linted_langs()`` like every other rule.
- Drop the ``examples/README`` requirement. The series index became an ordinary first task under ``examples/``, which lint cannot tell apart from a teaching task, so the rule was demanding a file the current layout does not have.

**Breaking Changes**

- The three ``lesson-smith-*-finalize`` skills are removed. Their work is now the last two step skills of each flow (root documents, then ship).
- ``MAX_DESCRIPTION_CHARS`` and ``MAX_GITHUB_ABOUT_CHARS`` are replaced by ``max_description_chars(lang)`` and ``max_github_about_chars(lang)``.
- ``DOCS_UPSKILL_FILES``, ``DOCS_SHOWCASE_FILES``, and ``FORGE_SKILLS`` are replaced by ``DOCS_UPSKILL_FILE_BASES``, ``DOCS_SHOWCASE_FILE_BASES``, and ``FORGE_SKILL_BASES``, which hold language-free bases rather than finished file names.
- Every path under ``ref/`` moved. Anything pointing into the old flat layout or the old per-type folders needs to be repointed at ``ref/00-common/`` or the numbered type layer.

**Miscellaneous**

- The six test fixture repos were rebuilt against the current standard: English variants emptied to match the placeholder rule, an index task added at ``01`` with everything renumbered behind it, the ``docs/<type>/`` documents and child skills regenerated exactly as forge would produce them, and the retired vocabulary and dead links cleaned out.
- ``doc-writing-styles`` remains a required companion plugin, now for ``markdown-style`` and ``chinese-english-punctuation`` only. The ``rewrite-in-en-*`` pipeline it also ships is no longer part of any lesson-smith flow.


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