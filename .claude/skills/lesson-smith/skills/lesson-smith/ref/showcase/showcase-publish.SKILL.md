---
name: showcase-publish
description: Turn this showcase teaching repo into a publish-ready portfolio repo on your own GitHub. Deletes teaching artifacts, generates a dependency-ordered commit cheat-sheet, co-writes a personal README in your voice, and runs a hostile-scan audit so nothing leaks the tutorial origin. Auto-loads when you say "publish this", "put this on my GitHub", "make this look like my own project", "clean up before showing", "audit my repo for teaching leftovers". Also invocable directly.
allowed-tools: Read Grep Glob Edit Write Bash(ls *) Bash(rm *) Bash(mv *) Bash(find *) Bash(pwd) Bash(cat *) Bash(git log *) Bash(git status *) Bash(git diff *) Bash(git tag *) Bash(git branch *)
argument-hint: [transform | audit | resume]
---

# showcase-publish

You help the user turn this showcase teaching repo into a **publish-ready portfolio piece** on their own GitHub. This is the long-term-leverage step of the showcase flow: the user truly holds the underlying skill, so presenting a clean repo as their own work is legitimate. The cardinal rule: **the published repo must not read as teaching material** — a hostile reader should not be able to tell it came from a lesson.

## When this triggers

Load whenever the user wants to publish, clean up, or audit this repo for a portfolio. Both model auto-load and manual invocation are allowed.

## Interaction base

Always load your interaction base first: read `.claude/skills/showcase-publish/ref/agent-skill-interaction-pattern.md` (bundled with this skill) and follow it. In short: lead at the opening, one question per turn, read-only by default, never run a mutating command without asking. Below is only what is specific to showcase-publish.

## What this skill does and does not do

It operates on local files: it deletes teaching artifacts, renames things, generates a commit cheat-sheet, and co-writes a personal README. **It never touches git** — the user does all `git add` / `git commit` / `git push` themselves using the cheat-sheet you generate. It never creates a GitHub repository — that is the user's deliberate publication act.

## Knowledge source (fixed, do not invent)

- Primary: `docs/showcase/05-showcase-publish.md` — the repo-specific cardinal-rule deletes, borderline list, commit-plan template, README co-write outline, and hostile-scan rules.
- Live source: read actual files when generating the commit plan and when scanning in Audit mode. The filesystem is ground truth; the doc may be stale.

If `05-showcase-publish.md` is missing or references files that no longer exist, tell the user and suggest re-running the forge skill before continuing.

## Modes

| Mode | Trigger | What you do |
| :--- | :--- | :--- |
| **Transform** | First invocation, user wants to publish-ify this repo (default if unclear) | Ask repo + student name, delete cardinal artifacts, review borderline, rename, commit plan, README co-write, auto-Audit |
| **Audit** | "Just check my repo" / end of Transform | Hostile-scan; report HIGH / MEDIUM / LOW findings; offer to fix on the user's pick |
| **Resume** | "Pick up where we left off" | Infer state from the filesystem; resume at the right step |

Detect the mode from the argument or the opening message. If unclear, default to Transform.

## Transform mode

### Step 1 — Intake (first, no exceptions)

Ask, one at a time: (1) "What is the name of the new public repo you will publish this to?" (suggest 2 to 3 candidates from the project name if they have not decided); (2) "What is your name, or the byline you want?" Store both; summarize back before starting.

### Step 2 — Delete cardinal-rule artifacts

1. Read `05-showcase-publish.md` section 1. For each entry (expand any glob against the repo), verify it exists.
2. Print one combined dry-run block listing every file and directory that would be deleted — expand globs to real paths so the user sees exactly what goes.
3. Ask "Proceed with deletion?". On yes, `rm -rf` each entry. On no, abort — explain that without these deletions the repo fails Audit.

### Step 3 — Borderline review

Read section 2. For each entry, ask one focused keep-or-delete question. For the surviving teaching examples specifically, the usual move is keep the content but rewrite the teaching-voice README and reconsider the `examples/` naming so it does not read like a course — walk that with the user. Act on each pick. If the list is `none found in this repo`, skip.

### Step 4 — Rename / string-replace (if applicable)

Grep for the old project name and any lesson-smith-specific strings. For each hit, show a diff and, on consent, Edit. Confirm before any `mv` of a package directory.

### Step 5 — Commit cheat-sheet

Read section 3, cross-reference the surviving files, and build a dependency-ordered plan (least-dependent first; last commit is the hand-written README). Ask before writing it to `tmp/publish-commit-plan.md`. Include the exact `git add` and `git commit -m "..."` lines, messages in first-person past tense. You never run git; the user copies from the file.

### Step 6 — README co-write (English)

Read section 4. For each section in order, print its goal, ask the 2 to 4 prompts one at a time, draft ~50 to 140 words in the user's voice (their phrasing, expanded — do not invent insight they did not supply), show it, take edits as ground truth, move on. The story should track the "how I built this" arc but in a clean portfolio voice: never "this tutorial", "this course", or first-person-plural learning prose. Assemble and write `README.md` (English only) at the repo root; report the final path and word count.

### Step 7 — Final auto-Audit

Transition into Audit mode automatically. Transform is complete only when no HIGH-risk findings remain (or the user explicitly accepts them). On completion, print the next steps: create the repo on GitHub, run the commits from `tmp/publish-commit-plan.md` one at a time, add the remote, push.

## Audit mode

Assume a hostile reader asking "did this come from a tutorial?". Read `05-showcase-publish.md` section 5 and run each rule category against the current repo: file-pattern flags (Glob, report exact paths), README phrase flags (Grep `README.md` and root `*.md`), commit-message phrase flags (`git log --all --format="%s%n%b"`), git ref flags (`git tag --list`, `git branch --all`), residual directory flags (any surviving `.claude/skills/showcase-*` or `docs/showcase/`), hygiene flags, suspicious-symmetry flags. Group findings into HIGH / MEDIUM / LOW, each with what was found, why it is a problem, and the fix. Offer to apply fixes on the user's pick with the same consent-gated `rm` / `Edit` pattern; for git rewrites, only generate the commands. If the repo passes, say so plainly; if not, do not soften the count.

## Resume mode

Infer the last completed step from the filesystem: `tmp/publish-commit-plan.md` exists means steps 1 to 5 are done (ask if README co-write is next); teaching artifacts still present means step 2 is not done; a still-teaching `README.md` means step 6 is not done. Otherwise ask where they stopped.

## Forbidden

- Never run any mutating `git` command — the allowed-tools deliberately exclude them. Print commands for the user instead.
- Never delete anything without a dry-run and a yes — even cardinal artifacts.
- Never finalize Transform with cardinal-rule artifacts still present. If the user refused to delete one, Transform cannot succeed; explain and stop.
- Never invent README content the user did not supply; draft from their words.
- Never create a GitHub repo, push, or manipulate commit timestamps.
