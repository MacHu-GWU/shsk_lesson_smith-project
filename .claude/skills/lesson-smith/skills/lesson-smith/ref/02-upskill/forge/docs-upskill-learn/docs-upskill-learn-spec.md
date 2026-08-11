# Spec for docs/upskill/01-upskill-learn.md (English)

**Scope**: the file `docs/upskill/01-upskill-learn.md` in an upskill repo. Written by `lesson-smith-upskill-forge`, read by the `upskill-learn` skill.

**Skeleton**: [docs-upskill-learn-template.md](docs-upskill-learn-template.md).

**Not generated at the moment**: forge emits the `-cn` set only, per [docs-upskill-learn-cn-spec.md](docs-upskill-learn-cn-spec.md). The unsuffixed English course files under `examples/` are deliberately left empty, so an English index would have nothing to point at. This spec and its skeleton stay put, ready for the multi-language module to pick up.

---

## 1. What this file is

A **map of what there is to study**, not a body of teaching. The knowledge itself lives in `examples/` and in the material the course points at. This file answers three questions and nothing more:

- What is there to learn?
- Where does each piece live?
- In what order should it be taken?

It is an index, not a complete inventory of everything the course touches.

---

## 2. Section 1, Study Material

Everything worth studying that sits **outside** the numbered progression under `examples/`: source at the repo root, other docs, config files.

**A human has to name these.** Unlike `examples/`, they are not self-evident from the directory layout. How much you write depends on which shape the course has:

| Shape | What it means | How thick this section gets |
| :--- | :--- | :--- |
| **A** | The tutorials are the material. The course is mostly reading, and everything lives under `examples/`. | Thin. A single line such as "nothing extra, it is all in the guided path" is a legitimate answer. |
| **B** | The real thing (usually code) lives elsewhere in the repo, and `examples/` walks you through it. | This is the centerpiece. Track down the material scattered across the repo. |

Give three things per entry: a markdown link (to the file, and to a specific header or keyword when that helps), one line on what to take from it, and one line on why it matters or what to watch out for.

---

## 3. Section 2, Guided Path

The numbered tasks under `examples/` are the route, and the `upskill-learn` skill walks the learner along it.

forge can derive this section by listing the directory, so it is the easy half. Keep it at the level of **how the route progresses as a whole**: break it into a few stages and say what each stage leaves the learner with. Link out to the index task at `examples/01` and to `docs/tasks/SYLLABUS`.

- Under shape B, name which study-material entries each stage draws on.
- **Do not summarize the tasks one by one.** That is what the tasks themselves are for.

---

## 4. House rules

- Cite with markdown links throughout. Locate by header or keyword, **never by line number**, since line numbers drift as the code changes.
- **This file is meant to be edited by hand** as well as regenerated. If an entry is wrong, fix it here; a later forge run can always overwrite it.
