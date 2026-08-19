.. _release_history:

Release and Version History
==============================================================================

x.y.z (Backlog)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.3.3 (2026-08-19)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- **Structural lint checks no longer look inside fenced code blocks.** ``MarkdownFile`` grew a ``body_outside_code`` property, and the three checks that read the body line by line now go through it: the H1 scan, the estimated-time line, and the TICKET relative-link scan. Before this, a Python comment written at column zero inside a ``` ```python ``` block counted as an H1, so a perfectly ordinary teaching README that labels its snippets — ``# 读一行``, ``# Q1: the whole hierarchy`` — failed with "The document has 4 H1 titles, but exactly one is allowed." The same bug reached two other checks that nobody had hit yet: a ``**预计用时:**`` line quoted inside a sample would have been summed into a repo's time budget, and a TICKET illustrating what a relative link looks like would have been failed for containing one. All three came from the same root cause, so all three are fixed together rather than special-casing the one that surfaced.
- **The workaround this removes was worse than the bug.** With no way to exempt a code block, the only fix available to an author was to mangle otherwise-correct sample code: indent the comment by a space, move a section label into a trailing inline comment, or split one coherent snippet into three so each label could become a markdown heading. Lint should not push authors to write worse examples.

**Miscellaneous**

- ``strip_fenced_code_blocks`` follows CommonMark closely enough for real documents: an opening fence is three or more backticks or tildes indented by at most three spaces, and only a fence of the same character, at least as long, and carrying no info string closes it. That last rule is what lets a ````` ```` ````` block quote an inner ``` ``` ``` block, which the specs themselves rely on. An unclosed fence runs to the end of the document.
- Fifteen new tests cover the fence grammar (both fence characters, info strings, longer closing fences, nesting, unclosed blocks, indented fences) and, for each of the three checks, one case that must stay quiet next to one that must still fail. A fix that silences a check everywhere is not a fix.
- ``01-repo-layout`` section 8 now states the exclusion as part of the documented lint contract, so an author reading the spec knows sample code is exempt rather than discovering it by trial.


0.3.2 (2026-08-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **``lm.json`` gained a repo-level time budget, generated rather than written.** ``estimated_hours_lower`` and ``estimated_hours_upper`` hold the whole repository's span in decimal hours, and ``lesson-smith sync`` computes them as a third operation after the snapshot and the SYLLABUS: read every ``docs/tasks/<branch>/TICKET``, add the lower bounds, add the upper bounds, divide by 60 once at the end, round to two places. The snapshots are the source because they are the only place where every branch is visible at once — a working tree only ever has one branch checked out. This completes the chain 0.3.1 started: six-tier estimates per task, summed into the root TICKET, summed again across branches into the manifest.
- **The linter re-derives that total and compares it for equality.** Rounding to a fixed two places makes the stored value exactly reproducible, so drift is a mismatch rather than a tolerance question — the same treatment the SYLLABUS gets against the task READMEs. The usual failure is re-estimating one task and forgetting to re-run sync, and the error says so. Note this is deliberately not the rounding used by the hours gloss in the root TICKET, which stays at the nearest half hour because it is prose for a human to read.
- **Sync refuses to write a total it had to interpret.** If any branch's TICKET states its estimate as anything other than a minute range — an hour range, a prose phrase, a single number — the manifest is left completely untouched and the report names the branch. A total that silently skipped a branch is worse than no total at all.

**Breaking Changes**

- **``lesson-smith lint`` now fails a repo whose ``lm.json`` has no time budget, or whose budget disagrees with the TICKETs.** Every repo built against an earlier version reports one new failure until it is re-synced. The fix is to run ``lesson-smith sync`` — but a repo whose TICKETs still carry free-hand estimates has to be put on the six-tier ladder first, since sync will not guess.
- **Pin 0.3.2 or later.** The two manifest fields do not exist before it: sync from an earlier version will not write them while lint from this one requires them. ``01-repo-layout`` section 8 now names 0.3.2 as the version to pin, and says why mixing the two is the one combination that bites.
- ``Metadata`` grew ``estimated_hours_lower`` / ``estimated_hours_upper`` (both optional) and a ``to_dict``. Anything constructing a ``Metadata`` positionally still works; anything serialising one by hand should go through ``to_dict`` so unset bounds are omitted rather than written as ``null``.

**Miscellaneous**

- **The ladder itself is still not a machine check.** What lint enforces is the arithmetic — that ``lm.json`` equals the sum of the TICKETs, and that each TICKET states its estimate in minutes at all. Whether a given task genuinely belongs in tier 3 rather than tier 4 is left to the specs and the preflight checklists, and pinning the tiers in code stays deferred.
- The computation lives next to ``Repo`` rather than in either consumer, because both need it: sync writes the total and the linter re-derives it. Same shape as the SYLLABUS.
- The six test fixture repos were re-estimated onto the ladder and re-synced, so each now carries a worked example of the whole chain: per-task tiers, a root TICKET stating their sum in minutes with an hours gloss, and an ``lm.json`` holding the same total in decimal hours.


0.3.1 (2026-08-18)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- **A TICKET's estimated time is now a choice from six tiers, not a free-hand number.** ``3 到 5``, ``5 到 15``, ``15 到 30``, ``30 到 60``, ``60 到 90``, ``90 到 120`` minutes: pick one tier and copy both numbers verbatim. Left open, every writing session invented a fresh ruler (``20 到 45 分钟``, "about an hour", "half a day"), and a course whose cards each measure themselves differently gives a student nothing to compare across a board. The 120-minute ceiling is hard: an estimate above two hours means the Task should be split, not that the range should be widened. The ladder lives in ``00-common/04-task-ticket-spec`` section 8, which every other TICKET spec already inherits, so there is still exactly one copy of the rule. The index task is narrowed further to tier 1 or 2, and the quiz and demo tasks keep their fixed ``30 到 60 分钟``, which was already tier 4.
- **The root TICKET's estimate is a mechanical sum instead of a judgement call.** Lower bound is the sum of every Task's lower bound, upper bound the sum of the uppers, added straight with no discount and no buffer, written as raw minutes with an hours conversion in parentheses: ``385 到 700 分钟 (约 6.5 到 11.5 小时)``. The minute pair is authoritative and the hours are there for humans. ``09-root-docs-spec`` used to say the creator's number wins and otherwise estimate conservatively; that instruction is gone, and the three root TICKET specs now check the sum in their preflight.
- **New authoring step: calibrate time.** It sits directly after the converge step and before the root documents — step 9 for readup, 11 for upskill, 12 for showcase — and is the first step whose whole job is the scale of a course rather than its content. The agent reads every task, produces one table (directory, what it covers taken verbatim from the README ``description``, what the estimate says today, which tier it suggests, unchanged/up/down, and why), reprints the six-tier ladder underneath because nobody remembers what "tier 4" means, and then **stops**. The creator answers in plain language — "01 through 03 are all tier 2, 07 is heavier than that, make it tier 5" — and only then does anything get written back. Deciding the tiers is a human gate of the same kind as signing off on the ``README-ORIGINAL`` frontmatter. Specified in the new ``00-common/15-time-calibration-spec.md`` and driven by one new step skill per type.
- **Why it is its own step rather than part of converge.** Converge settles content: terminology, depth, whether one chapter hands off to the next. This settles scale, using the same read-through but a completely different test — folded together, the second one loses every time. It has to come after every task exists (the index, quiz, demo, and wrap-up tasks all count toward the total) and before the root documents (their estimate is the sum of these). For upskill and showcase it is placed before forge, because it edits ``examples/`` and a course should have exactly one moment where ``examples/`` is final. It shares the converge session, since it wants the same read-through still in context.

**Breaking Changes**

- **Inserting a step renumbered every step behind it, so eight slash commands changed name.** readup: ``step-09-root-docs`` → ``step-10-root-docs``, ``step-10-ship`` → ``step-11-ship``. upskill: ``step-11-forge`` → ``step-12-forge``, ``step-12-root-docs`` → ``step-13-root-docs``, ``step-13-ship`` → ``step-14-ship``. showcase: ``step-12-forge`` → ``step-13-forge``, ``step-13-root-docs`` → ``step-14-root-docs``, ``step-14-ship`` → ``step-15-ship``. Step counts are now 11 steps in 7 phases for readup, 14 in 9 for upskill, and 15 in 10 for showcase. Anything holding an old command name — notes, saved prompts, a half-finished course — needs repointing.

**Minor Improvements**

- Each ``prompts/run-*.md`` input template now carries the exact slash command to type on its own line, so filling one in and sending it no longer requires remembering which command it belongs to.
- The converge step skills hand off explicitly: do not close the session, the next step wants this same read-through, here is the command to type.
- The root-document step skills gained a red line stating that the root TICKET estimate is a sum and must not be re-estimated, so the rule is present at the moment it would be broken rather than only in the spec.

**Miscellaneous**

- ``lesson-smith lint`` and ``sync`` are untouched by this release: everything here is specs and skills. The six-tier ladder is carried by the specs and the preflight checklists only. (0.3.2 adds the machine-checked half.)
- Added a project-local ``maintain-lesson-smith`` skill: what the plugin is for, how ``ref/`` and the skill family are organised, the layering rules, and which references have to be updated together for each kind of change. Inserting this step touched about thirty files across five of those surfaces, which is exactly the ripple that skill exists to enumerate.


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