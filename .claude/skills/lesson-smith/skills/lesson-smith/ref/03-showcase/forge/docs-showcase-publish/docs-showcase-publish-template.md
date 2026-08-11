# [Course Name] Publish Checklist

> The showcase-publish skill reads this file to turn this teaching repo into a portfolio repo. Machine-facing: paths and tables, not prose. Generated against this specific tree, with every glob already expanded.

## 1. Cardinal Deletes

[Everything here gives away a teaching origin on sight and goes before publishing. Expand each glob and list the real matches one by one.]

- path: `README-ORIGINAL.md` (and its language variants)
  reason: an outward lesson pitch; only teaching repos have one
  detected_by: filename match
- path: `lm.json`, `docs/tasks/`, `docs/showcase/`
  reason: the lesson-smith manifest and its generated views
  detected_by: file and directory presence
- path: `.claude/skills/showcase-learn*/`, `.claude/skills/showcase-quiz*/`, `.claude/skills/showcase-demo*/`, `.claude/skills/showcase-publish*/`
  reason: the four generated child skills
  detected_by: directory presence
- path: `examples/01-title/` (whole directory)
  reason: the index task, a teaching-stage map rather than portfolio content
  detected_by: fixed position at 01
- path: `examples/NN-prove-i-get-it/`, `examples/ZZ-how-i-build-this/`, and any recap task between them (whole directories)
  reason: self-check and retrospective, not the work itself; only the technical tasks before the quiz survive, and those are handled in section 3
  detected_by: directory presence from the quiz task onward
- path: `**/TICKET*.md`
  reason: teaching task cards, at the root and in every task
  detected_by: filename match
- path: `examples/_lm-*.md`
  reason: authoring drafts
  detected_by: filename match

## 2. Language Collapse

[A portfolio repo carries one language. Name the surviving variant, delete the rest, then strip the suffix. Read a file before calling it a placeholder; do not judge by suffix alone.]

- Surviving language: [e.g. `-cn`, because that is where the content is]
- Delete (empty placeholders and other variants, real paths, not globs):
- [README.md]
- [examples/02-title/README.md]
- [...]
- Rename after deleting:
- [README-cn.md] to [README.md]
- [examples/02-title/README-cn.md] to [examples/02-title/README.md]
- [...]

## 3. Borderline Items

[Not obviously teaching, but worth a second look. Flag for the learner; do not delete on your own.]

- path: the technical teaching tasks before the quiz
  reason: this is the portfolio content, but the teaching voice and the `examples/` naming may need rewriting so the repo does not read like a course
  default: ask
- path: [e.g. `tmp/`, `notes/`, `*.draft.md`]
  reason: [looks like local scratch]
  default: [keep or ask]

_(If there is nothing beyond the tasks, write: none found in this repo.)_

## 4. Dependency-Ordered Commit Plan

[Least dependent first, so the history reads like something that grew. Real paths from this repo. The last commit is always the hand-written README.]

| # | Files | Suggested message (first-person past tense) | Rationale |
| :- | :--- | :--- | :--- |
| 1 | [root config, e.g. mise.toml, pyproject.toml, .gitignore] | Set up the toolchain | root config; everything builds on it |
| 2 | [shared skeleton or utilities] | Add the base structure | the rest depends on it |
| ... | [one content file per commit] | [Add / Wire up / Document ...] | [what depends on what] |
| N | README.md | Write the project README | the front door, written last |

## 5. README Outline

[The structure the publish skill co-writes with the learner. Clean portfolio voice: never "tutorial", "course", "lesson", or "we learned". 250 to 500 words total.]

- language: [ask the learner once; English is common for a public portfolio even when the course content is in another language]
- section: Project description
  goal: what this is and who would care, in the learner's own voice
  prompts: ["In one sentence, what is this?", "Who would care about it?", "What does it let you do?"]
  length: 60 to 100 words
- section: Install and run
  goal: the shortest path from clone to a working run
  prompts: ["What is the shortest sequence of commands that produces output?"]
  length: 40 to 80 words
- section: What I built and how it works
  goal: the shape of the work, plus one design choice worth talking about
  prompts: ["What are the main pieces?", "What is one choice you are glad you made?"]
  length: 80 to 140 words
- section: What I learned
  goal: something specific, not filler
  prompts: ["What surprised you?", "What was the hardest part, and how did you get past it?"]
  length: 60 to 120 words
- section: What is next (optional)
  goal: one honest next step
  prompts: ["Given another week, what would you add?"]
  length: 40 to 80 words

## 6. Hostile-Scan Rules

[Assume a reader looking for the seam. Each category with a detection method and a severity.]

- Leftover cardinal artifacts (HIGH): glob for `README-ORIGINAL*`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET*.md`. Report exact paths.
- Surviving language-suffixed files (HIGH): glob for `**/*-<locale>.md`. A portfolio repo has no locale system.
- Teaching voice in the README (HIGH): grep the README and root `*.md` for "this tutorial", "this course", "in this lesson", "as a student", "we learned".
- Teaching voice in commit messages (MEDIUM): the same phrases over `git log --all --format="%s%n%b"`.
- Git refs naming the lesson (MEDIUM): `git tag --list` and `git branch --all` for `01-showcase`, `tutorial-base`, `from-course`, `original`.
- Leftover child skill directories (HIGH): any surviving `.claude/skills/showcase-*` or `docs/showcase/`.
- Hygiene (LOW): `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/`.
- Suspicious symmetry (MEDIUM): identical comment banners or docstring shapes across many files. Surface it, do not enforce.
