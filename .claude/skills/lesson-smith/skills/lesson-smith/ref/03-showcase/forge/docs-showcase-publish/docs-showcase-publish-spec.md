# Spec for docs/showcase/05-showcase-publish.md (English)

**Scope**: the file `docs/showcase/05-showcase-publish.md` in a showcase repo. Written by `lesson-smith-showcase-forge`, read by the `showcase-publish` skill.

**Skeleton**: [docs-showcase-publish-template.md](docs-showcase-publish-template.md).

**Not generated at the moment**: forge emits the `-cn` set only, per [docs-showcase-publish-cn-spec.md](docs-showcase-publish-cn-spec.md). This spec and its skeleton stay put, ready for the multi-language module to pick up.

**Self-contained**: unlike quiz and demo, publish has no task under `examples/` backing it. Everything the skill needs is in this one file.

---

## 1. What this file is

**A checklist cut for one specific repo.** Publishing turns a teaching repo into a portfolio repo the learner can put on their own GitHub, one a hostile reader cannot trace back to a lesson.

This file answers, for this repo and no other: what counts as a teaching artifact, how to remove it, how to stage the commits, how to write the README, and how to audit the result.

**Generate it against the real tree.** Expand every glob into the actual matching paths, and cite real files in the commit plan. A checklist full of placeholders is a checklist nobody can follow.

---

## 2. The six sections

The skill reads these by number, so **keep all six and keep them in order**. A section with nothing in it keeps its heading and says so.

### 2.1 Cardinal deletes

Files and directories that give away a teaching origin on sight. They go before publishing, no discussion. Give each one `path`, `reason`, `detected_by`.

For a showcase repo that normally means:

| What | Why |
| :--- | :--- |
| `README-ORIGINAL` and its variants | an outward lesson pitch; only teaching repos have one |
| `lm.json`, `docs/tasks/`, `docs/showcase/` | the lesson-smith manifest and its generated views |
| the four generated child skills under `.claude/skills/` | learn, quiz, demo, publish |
| the index task at `examples/01-*/` | a teaching-stage map, not portfolio content |
| the quiz task and everything after it | `NN-prove-i-get-it`, `NN-how-i-build-this`, and the wrap-up task. These three sit together at the end: self-check, story rehearsal, retrospective. None of them is the work itself |
| every `TICKET` and its variants | teaching task cards, at the root and in each task |
| `examples/_lm-*.md` | authoring drafts |

Only the technical teaching tasks **before** the quiz survive, and they are handled as borderline in the next section.

### 2.2 Language collapse

**A portfolio repo carries one language.** A tree where every file has both a plain and a suffixed variant is a lesson-smith signature by itself, and empty placeholder files are worse: they look abandoned.

So the checklist has to state three things:

1. **Which language survives.** Whichever variant actually holds the content. In a Chinese-only repo that is `-cn`; the unsuffixed English files are empty placeholders.
2. **Delete every other variant**, including the empty placeholders. List them as real paths, not a glob.
3. **Strip the suffix from the survivors.** `README-cn.md` becomes `README.md`, `docs/some-doc-cn.md` becomes `docs/some-doc.md`. Do this after the deletes, so nothing is overwritten on the way.

Getting this backwards deletes the entire course and keeps a tree of empty files, and no later step catches it. **Read a file before deciding it is the placeholder.** Do not decide by suffix alone.

### 2.3 Borderline items

Things that are not obviously teaching but are worth a second look. Flag them for the learner rather than deleting them. Give each one `path`, `reason`, `default` (keep or ask).

The surviving teaching tasks are always on this list. They carry the portfolio content, but their teaching voice, and the `examples/` naming itself, may need rewriting so the repo does not read like a course. Other usual suspects: `tmp/`, scratch notes, half-finished work.

### 2.4 Dependency-ordered commit plan

Least dependent first, so the history reads like something that grew rather than something that landed. A row per commit against this repo's real files: the commit number, the files to stage, a suggested message in first-person past tense, and one line of rationale.

The last commit is always the hand-written README. Ten to fifteen rows is typical.

### 2.5 README outline

The structure the publish skill co-writes with the learner. The README should tell the same story as the demo script, but in a clean portfolio voice: **never "tutorial", "course", "lesson", or first-person-plural learning prose.**

Per section: name, a one-line goal, two to four questions the skill will ask, and a length target. The usual set is Project description, Install and run, What I built and how it works, What I learned, and optionally What is next. Two hundred fifty to five hundred words in total.

**Say which language the README is written in.** It is not automatic: the learner may want an English README over a repo whose content is in another language, and that is a legitimate choice they should be asked about once rather than have decided for them.

### 2.6 Hostile-scan rules

Assume a reader who is looking for the seam. Give each category a detection method and a severity.

| Category | Severity | How to detect |
| :--- | :--- | :--- |
| leftover cardinal artifacts | HIGH | glob for `README-ORIGINAL`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET*.md` |
| any surviving language-suffixed file | HIGH | glob for `**/*-<locale>.md`; a portfolio repo has no locale system |
| teaching voice in the README | HIGH | grep the README and root `*.md` for "this tutorial", "this course", "in this lesson", "as a student", "we learned" |
| teaching voice in commit messages | MEDIUM | the same phrases over `git log --all --format="%s%n%b"` |
| git refs that name the lesson | MEDIUM | `git tag --list` and `git branch --all` for `01-showcase`, `tutorial-base`, `from-course`, `original` |
| leftover child skill directories | HIGH | any surviving `.claude/skills/showcase-*` or `docs/showcase/` |
| hygiene | LOW | `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/` |
| suspicious symmetry | MEDIUM | identical comment banners or docstring shapes across many files; surface it, do not enforce |

**HIGH means fatal on a single hit.** MEDIUM is recoverable but conspicuous. LOW is cosmetic.

---

## 3. House rules

- **Machine-facing.** Tables, lists, real paths. The skill reads this file; nobody recites it aloud. Skip prose the skill template already covers.
- **Keep empty sections.** If this repo has no `tmp/` and no borderline items, keep the heading and write "none found in this repo". The skill expects all six sections to be present.
- Expand every glob at generation time. The point of this file is that it is specific to one repo.
