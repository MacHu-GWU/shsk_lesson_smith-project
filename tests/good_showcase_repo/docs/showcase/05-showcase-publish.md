# GitHub Collaboration Basics Publish Checklist

> The showcase-publish skill uses this doc to turn this teaching repo into a publish-ready portfolio repo. Machine-facing: paths and tables, not prose. Generated for this specific repo; globs below are expanded against the actual tree.

## 1. Cardinal Deletes — Never Publishable

- path: `**/README-cn.md`
  reason: locale README, a teaching-language counterpart to the English one
  detected_by: filename match (real hits: README-cn.md, README-ORIGINAL-cn.md, examples/README-cn.md, examples/01-create-repo/README-cn.md, examples/02-edit-files/README-cn.md, examples/03-git-branch/README-cn.md, examples/04-merge-branch/README-cn.md, examples/05-prove-i-get-it/README-cn.md, examples/06-how-i-build-this/README-cn.md)
- path: `README-ORIGINAL.md` (and locales)
  reason: outward lesson pitch, only exists for teaching repos
  detected_by: filename match
- path: `examples/README.md` (and locales)
  reason: the series index — teaching-stage scaffolding, not portfolio content
  detected_by: filename match
- path: `lm.json`, `docs/tasks/`, `docs/showcase/`
  reason: lesson-smith manifest and generated teaching views
  detected_by: dir / file presence
- path: `.claude/skills/showcase-learn/`, `.claude/skills/showcase-quiz/`, `.claude/skills/showcase-demo/`, `.claude/skills/showcase-publish/`
  reason: the four generated child skills
  detected_by: dir presence
- path: the quiz and demo mini tasks — `examples/05-prove-i-get-it/`, `examples/06-how-i-build-this/` (whole dirs)
  reason: the quiz and the demo story are teaching-stage self-check and rehearsal, not portfolio content
  detected_by: dir presence, the mini tasks from the quiz onward
- path: `**/TICKET.md` (and locales)
  reason: teaching task cards at the root and in each example
  detected_by: filename match

## 2. Borderline Items — Ask the User

- path: the technical teaching mini tasks (examples/01 to 04, the surviving example content)
  reason: this is a browser-only walkthrough course with no code deliverable, so the teaching examples are the only content; keeping them means rewriting the teaching-voice README so the published repo reads as your own notes, not a tutorial. Consider instead publishing the real GitHub repo you practiced on and keeping this one private.
  default: ask

_(None beyond the examples found in this repo.)_

## 3. Dependency-Ordered Commit Plan

| # | Files | Suggested message (first-person past tense) | Rationale |
| :- | :--- | :--- | :--- |
| 1 | the surviving example notes (examples/01 to 04, rewritten) | Add my GitHub collaboration notes | the content, ordered as I learned it |
| 2 | README.md | Write the project README | the front door, written last, in my own voice |

## 4. README Co-write Outline (English)

- section: Project description
  goal: what this is and who cares, in the user's own voice
  prompts: ["In one sentence, what is this?", "Who would care about it?", "What does it let you do?"]
  length: 60 to 100 words
- section: What I learned
  goal: specific, not filler
  prompts: ["What surprised you?", "What was the hardest part and how did you get past it?"]
  length: 60 to 120 words
- section: What is next (optional)
  goal: one honest next step
  prompts: ["If you spent another week, what would you add?"]
  length: 40 to 80 words

## 5. Hostile-Scan Rules

- File-pattern flags (HIGH): any `**/README-cn.md`, `README-ORIGINAL.md`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET.md`. Glob and report exact paths.
- README phrase flags (HIGH): "this tutorial", "this course", "in this lesson", "as a student", "we learned". Grep README.md and any root `*.md`.
- Commit-message phrase flags (MEDIUM): same phrase set over `git log --all --format="%s%n%b"`.
- Git ref flags (MEDIUM): `git tag --list` and `git branch --all` for names like `01-showcase`, `tutorial-base`, `from-course`, `original`.
- Residual directory flags (HIGH): any surviving `.claude/skills/showcase-*` or `docs/showcase/`.
- Hygiene flags (LOW): `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/`.
- Suspicious symmetry flags (MEDIUM): identical comment banners or docstring shapes across many files (heuristic, surface not enforce).
