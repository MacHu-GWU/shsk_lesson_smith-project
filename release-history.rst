.. _release_history:

Release and Version History
==============================================================================

x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.3.0 (2026-08-07)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Switch the English-production step of every authoring flow from ``translate-to-en`` to ``doc-writing-styles:rewrite-in-en-tutorial``. The replacement is a whole pipeline behind one command: a cheap drafter transcribes each document literally, a pass over the drafts fixes shared titles and terminology, a strong rewriter writes each document from its draft without ever seeing the Chinese, and a reconciler verifies both hops across the set. The guidance therefore inverts. The entire course goes over in a single call rather than fanned out per mini task, because cross-document terminology, recurring section labels, and mutually referenced titles can only be unified while one run holds every document at once, and nothing afterward puts them back. All hand-rolled subagent orchestration guidance is gone from the skills; orchestration belongs to the command now.
- Add ``ref/rewrite-en-spec.md`` as the single authority for that step, and point every caller at it (the base skill, the three authoring workflows, the three author skills, retrofit, and the per-document specs). The base skill's rule used to be one sentence of prose repeated in eight places with slight drift. It now names the command, pins the file set to the three ``examples`` globs, states the two constraints that must travel in the call, gives the link rules, and lists what the upstream engine already covers so nobody restates it. **An author session no longer asks the creator which files to process**: the glob set is part of the spec, not part of the request.
- Add ``prompts/run-rewrite-en.md``, a self-contained input template for kicking the step off from a fresh session where the lesson-smith skill is not loaded. Inside an author session the template is unnecessary, since the skill assembles the same call from the spec.
- **Put every Chinese file through the one rewrite pass.** The root ``README``, ``TICKET``, and ``README-ORIGINAL`` used to be exempt: their structure is fixed and low-ambiguity, so ``finalize`` wrote all languages at once. That exemption is withdrawn. All three are now written in Chinese only, in a step that runs after the examples are final, and their English comes from the same single rewrite pass as everything else. The reason the exemption looked safe is also the reason it was not: the root README links to ``README-ORIGINAL`` and ``examples/README``, whose canonical English titles are fixed by the rewrite pipeline's cross-document brief, so a second path to English guarantees the titles and terminology disagree.
- **Move ``forge`` to after the rewrite.** ``docs/upskill/`` and ``docs/showcase/`` are English-only by spec, and their entries link to English example files by path and cite English headers as anchors. Running forge before the rewrite meant writing links to files that did not exist yet, anchored to headings forge had translated itself and that the rewrite pipeline would independently name something else. Nothing in the repo checks links under ``docs/``, so this failed silently. Forge now reads the finished English and writes English, and its spec says why.
- **Frontmatter length limits are now per language.** ``description`` allows 400 characters in Chinese and 800 in English; ``github_about`` allows 200 and 300. A character carries very different amounts of information depending on the script, so 400 characters of Chinese rewritten into English lands around 700 to 900, and a single global cap would have failed every English ``README-ORIGINAL`` the moment that file joined the rewrite set. The English text is a rewrite of the Chinese rather than a compression of it, and the budget now says so. The two fields get different headroom on purpose: the ``description`` cap is a style budget we choose, while the ``github_about`` cap is external, since GitHub truncates its About box around 350 characters whatever the script. The language is derived from the file name, so ``check_frontmatter_description`` stays correct when called on a single file.

**Minor Improvements**

- State the two constraints ``lesson-smith lint`` enforces that a general-purpose rewriting pipeline has no way to know, since neither is part of its conservation contract. YAML frontmatter has to keep its shape: one line, a double-quoted value, no quote-like characters inside, within the language's character budget, and still as tight as the Chinese was. H1 titles admit no punctuation beyond commas, colons, and periods. The engine restates the ``markdown-style`` body rules itself and machine-checks the dash rule as H7, so only the H1 character set has to be passed in.
- ``README-ORIGINAL``'s H1 must equal the repo name byte for byte, which collides with the engine treating heading text as prose. Rather than arguing with its core contract over one line in one file, where losing the argument would be silent, the rewrite step repairs that H1 itself after the run.
- Correct the cross-language link rule everywhere it appears, and give the directory case its own clause. Retargeting a ``-cn`` suffix applies to **file** references only. **Directory** references carry no language marker, since every language variant lives in the same directory, so rewriting one produces a dead link. A directory name that does contain ``-cn`` is a naming error against the layout spec rather than something to retarget, and gets reported for the creator to fix. Previously the specs said only "links follow the file's language", which reads as applying to both.
- Drop the seven copies of the warning that the translation step leaves markdown links untouched and therefore needs the retargeting rule written into its input. Retargeting is a conserved property of the rewriting engine now, machine-checked and auto-repaired as H3 on two of the three hops. Restating it invited authors to hand-patch something upstream already does better.

**Bugfixes**

- ``lesson-smith-upskill-forge`` told the model to write its three ``docs/upskill/`` documents in Chinese first and rewrite them into English later, contradicting those documents' own specs, which state they are English-only meta files for AI consumption and do not follow the Chinese-first rule.

**Miscellaneous**

- This release makes ``doc-writing-styles`` a hard dependency at plugin version 0.2.1 or later, which is where the ``rewrite-in-en-*`` pipeline ships.


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