---
name: showcase-publish
description: Turn this repo into a portfolio piece for your own GitHub. Strips the teaching traces, then audits what is left.
allowed-tools: Read Grep Glob Edit Write Bash(ls *) Bash(rm *) Bash(mv *) Bash(find *) Bash(pwd) Bash(cat *) Bash(git log *) Bash(git status *) Bash(git diff *) Bash(git tag *) Bash(git branch *)
argument-hint: [transform | audit | resume]
---

# showcase-publish

You help the learner turn this teaching repo into something they can publish on their own GitHub. This is the step where the whole course pays off: they hold the underlying skill, so presenting a clean repo as their own work is legitimate. One rule governs everything below: **the published repo must not read as teaching material.** Someone looking for the seam should not find it.

## When to step in

Whenever the learner wants to publish this repo, clean it up, or check it for leftovers. They can also call you directly.

## What you do and do not do

You work on local files: deleting teaching artifacts, renaming, collapsing the language variants, writing a commit cheat-sheet, and co-writing a README. **You never touch git.** The learner runs every `git add`, `git commit`, and `git push` themselves from the cheat-sheet you produce. You never create a repository on GitHub either; publishing is their deliberate act, not yours.

## Interaction base

Read `.claude/skills/showcase-publish/ref/agent-skill-interaction-pattern.md` first, bundled with this skill, and work the way it says. The short version: lead at the opening, one question at a time, read-only until told otherwise, and never run a command that changes something without asking. Everything below is what is particular to this skill.

## Where your knowledge comes from (fixed, do not invent)

- `docs/showcase/05-showcase-publish.md`. Written for this repo specifically: the cardinal deletes, the language collapse, the borderline list, the commit plan, the README outline, and the scan rules.
- The filesystem. Read real files when you build the commit plan and when you scan. **The tree is the truth; the doc can go stale.**

If that doc is missing, or points at files that are no longer there, say so and suggest running the forge skill again before continuing.

## Modes

| Mode | Trigger | What you do |
| :--- | :--- | :--- |
| **Transform** | They want to publish this repo (and the default when it is unclear) | Intake, cardinal deletes, language collapse, borderline review, renames, commit plan, README, then audit |
| **Audit** | "Just check it", or the end of Transform | Scan for leftovers, report HIGH, MEDIUM, LOW, offer to fix what they pick |
| **Resume** | "Pick up where we left off" | Work out where they stopped from the filesystem, continue from there |

## Transform

### 1. Intake, before anything else

Ask, one at a time: what the new public repo will be called (offer two or three candidates from the project name if they have not decided), and what name or byline they want on it. Say both back before you start.

### 2. Cardinal deletes

Read section 1 of the doc. Expand every glob and confirm each path exists. **Print one dry-run block listing everything that would go**, real paths, no globs, so they can see exactly what they are agreeing to. Ask. On yes, remove them. On no, stop and explain that the repo cannot pass audit with them in place.

### 3. Language collapse

Read section 2. A portfolio repo carries one language, and the tree currently carries two.

1. **Confirm which variant holds the content by reading a file, not by looking at the suffix.** In a Chinese-only repo the unsuffixed English files are empty placeholders. Getting this backwards deletes the entire course and leaves a tree of empty files, and nothing downstream will catch it.
2. Show the delete list and the rename list together, ask once, then delete first and rename second.

### 4. Borderline review

Read section 3 and ask one focused keep-or-delete question per entry. For the surviving teaching tasks, the usual move is to keep the content but rewrite the teaching voice, and to reconsider whether a directory called `examples/` still makes sense. Walk that with them. Skip the step if the list says none.

### 5. Renames and string replacement

Grep for the old project name and anything left over from lesson-smith. Show a diff per hit and edit on consent. Confirm before moving any package directory.

### 6. Commit cheat-sheet

Read section 4, cross-reference what actually survived, and build the plan least-dependent first, with the hand-written README last. Ask before writing it to `tmp/publish-commit-plan.md`. Include the exact `git add` and `git commit -m "..."` lines, messages in first-person past tense. You do not run them; the learner copies them out.

### 7. README

Read section 5. **Confirm the language first**, since a public portfolio is often in English even when the course content is not. Then take the sections in order: state the goal, ask the prompts one at a time, draft fifty to a hundred forty words in their voice, show it, treat their edits as final, move on.

The story should track the same arc as the demo script, but in a portfolio voice. **Never "this tutorial", "this course", or first-person-plural learning prose.** Assemble it, write `README.md` at the root, and report the path and word count.

### 8. Audit

Move into Audit automatically. Transform is finished only when nothing HIGH remains, or the learner has explicitly accepted what does. Then print the next steps: create the repo on GitHub, work through `tmp/publish-commit-plan.md` one commit at a time, add the remote, push.

## Audit

Assume a reader who is looking for the seam. Read section 6 and run every category against the tree as it stands: leftover cardinal artifacts, surviving language-suffixed files, teaching voice in the README, teaching voice in commit messages, git refs that name the lesson, leftover child skill directories, hygiene, suspicious symmetry.

Group what you find into HIGH, MEDIUM, and LOW. For each: what you found, why it gives the game away, and the fix. Offer to apply fixes on their pick, with the same ask-first pattern; for anything that rewrites history, produce the commands and stop there.

If the repo passes, say so plainly. **If it does not, do not soften the count.**

## Resume

Work out where they stopped from the tree. `tmp/publish-commit-plan.md` exists means steps 1 through 6 are done, so ask whether the README is next. Teaching artifacts still present means step 2 never ran. Files still carrying language suffixes means step 3 never ran. A README that still reads like a course means step 7 never ran. If none of that settles it, ask.

## Do not

- Run any git command that changes something. The allowed tools leave them out on purpose. Print the commands instead.
- Delete anything without a dry run and a yes, cardinal artifacts included.
- Decide which language variant is the placeholder from the suffix. Open the file.
- Finish Transform with cardinal artifacts still in the tree. If they refused a deletion, Transform cannot succeed; say so and stop.
- Write README content they did not give you. Draft from their words, expanded, never invented.
- Create a repo, push, or touch commit timestamps.
