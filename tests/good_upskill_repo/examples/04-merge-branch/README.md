---
description: "Learn to merge a branch back into the main line through a reviewed Pull Request, closing the full collaboration loop."
---

# Merge a Branch through a Pull Request

> Teaches you to take the changes on the branch from the last lesson, have them looked at through a Pull Request, and merge them cleanly back into main.

## 1. Overview

Last lesson you made changes safely on a branch while main stayed untouched. But changes sitting on a branch have no value: they have to return to main to become the project's official version. A Pull Request (PR for short) is the formal "please merge my changes in" request. It is not a one-click overwrite; it gives the team a chance to look first, discuss, and only then merge. In this lesson we walk the last stretch from branch to main, and in doing so close the collaboration loop of the whole course.

---

## 2. Learning goals

Picture ordering at a coffee shop. You do not barge into the back and work the espresso machine yourself. You hand your order to the barista, who confirms it and passes it to the kitchen. A Pull Request is that order slip: instead of changing main directly, you file a request so the change passes one confirmation before it enters the main line. Why add this step? Because main is the stable version everyone shares. The moment someone pushes unfinished or buggy code straight to main, the whole team is affected. A PR splits "making a change" from "officially adopting the change" into two steps, leaving room for a check and a discussion in between. That is the core rhythm of modern team collaboration.

By the end of this Task, you will be able to:

1. Explain what a Pull Request is and how it fundamentally differs from editing main directly.
2. Say what problem code review solves for a team.
3. Open a PR on your own, walk it through review and merge, and delete the used-up branch afterward.
4. Recognize what a merge conflict is and roughly when it shows up.

---

## 3. Prerequisites

- You have finished Lesson 03 and have a repo with a branch (for example update-notes) that carries some changes.
- You understand that a branch is a parallel line of work and main is the stable trunk (covered in Lesson 03).
- You can edit files and commit on the GitHub web UI (covered in Lesson 02).

---

## 4. What you will learn

By the end you will have merged a branch's changes back into main through a PR with your own hands, and seen those changes actually appear on main. You will know what each area of the PR page is for, and understand for the first time why engineering teams everywhere revolve around the PR.

---

## 5. What a Pull Request is

A Pull Request is a request: "please pull the changes on my branch into the target branch (usually main)." The word request is the key: it is a request, not a command. Filing the request and actually merging are two separate things, with a review in between.

A PR page brings three things together in one place:

- **The diff**: exactly which lines your branch changed relative to main, red for removed and green for added, at a glance.
- **The conversation**: a discussion area where you and your teammates can leave notes, ask questions, and comment line by line.
- **The merge button**: once the discussion is settled and everyone is satisfied, one click folds the changes into main.

Think of a PR as an online review meeting for a set of changes: what changed is laid out on the table, the relevant people gather around to look, and once they agree, the change is adopted. It turns the once-verbal, private, easy-to-skip "can you check whether my change is okay" into a recorded, traceable, formal process.

---

## 6. Code review: why look before merging

Code review means: before a change is merged into main, someone other than the author reads it first. This is the biggest reason PRs exist.

Say Maria Garcia has edited notes.md on a branch and opened a PR. Her teammate John Smith opens the PR, sees the diff, and can:

- **Leave a comment**: ask a question or make a suggestion next to a specific line, for example "did this miss a heading?".
- **Approve**: if it looks good, click Approve to say "I have looked, I support merging".
- **Request changes**: if it still needs work, send it back for the author to revise.

Why is this step worth the time? Three concrete benefits:

1. **Catch bugs early**: another pair of eyes often spots a mistake you stared past for an hour.
2. **Knowledge stops living in one head**: whoever reviewed the change now understands that area too, so the project does not stall when one person is on vacation.
3. **A record is left behind**: six months later when someone asks "why is this line written this way", the PR conversation is the answer.

In solo practice you are both the author and the reviewer, so it may feel redundant. But on a team, code review is the default gate on nearly every serious project. Taking it seriously now lays the groundwork for joining a team later.

---

## 7. Hands-on: open a Pull Request

1. Open the repo you changed in Lesson 03 and confirm the update-notes branch has at least one commit.
2. GitHub usually pops a yellow banner at the top of the repo home reading update-notes had recent pushes, with a Compare & pull request button on the right. Click it. (If it does not appear, click the Pull requests tab, then New pull request, and manually pick base main and compare update-notes.)
3. Confirm the direction at the top reads base: main <- compare: update-notes, that is, "merge update-notes into main".
4. Give the PR a clear title, for example Add study notes for week one, and use the description box below to say in a sentence or two what you changed and why.
5. Scroll down and glance at the diff under Files changed to confirm the changes are the lines you expected.
6. Click Create pull request. Congratulations, your first PR is open.

---

## 8. Merge: fold the changes back into main

Once the PR is open and review has passed, it is time to merge.

1. On the PR page, scroll down to the green Merge pull request button and click it.
2. GitHub asks you to confirm a merge commit message; keep the default and click Confirm merge.
3. The page turns to a purple line reading Pull request successfully merged and closed. This means the changes from update-notes are now in main.
4. Go back to the repo home, switch the branch dropdown to main, open notes.md, and you will see those changes really did land on main.

At this moment a change has completed its full journey: born on a branch, seen through a PR, and finally merged into the trunk to become an official part of the project.

---

## 9. Delete the branch after merging

After a successful merge, GitHub offers a Delete branch button right there. Go ahead and click it.

Why delete? Because update-notes has done its job: its changes are all in main now, and keeping the branch around only clutters the branch list. What you delete is the label for that line of work, not the changes themselves; the changes already live safely in main's history. If you ever need it, the branch can be restored later.

Remember it in one line: one branch for one thing, and when the thing is done (merged) put the branch away.

---

## 10. Aside: what a merge conflict is

Most merges are clean and go through with one click. But once in a while you hit a merge conflict, and it is worth recognizing its face.

A merge conflict happens when **two branches change the same part of the same file, differently**. Say someone on main changed a line to A, and you changed the same line to B on your branch. When GitHub merges, it finds two versions fighting over that spot, and it will not guess which is right for you, so it stops and asks a human to decide.

Do not be afraid of it. At this stage you only need to know two things:

- It is not an error; it is GitHub saying "I am not sure here, you decide which to keep".
- Resolving it is a manual pick: keep A, keep B, or blend the two, then confirm.

As long as everyone edits their own files, or you sync main's new changes into your branch in time, conflicts are rare. Resolving conflicts in depth is a topic for later; this course only points at it.

---

## 11. The big picture: one full collaboration loop

Stringing the whole course together, you have now walked a complete cycle:

1. **Create a repo** (Lesson 01): give the project a single home.
2. **Edit files** (Lesson 02): record every change with a commit.
3. **Open a branch** (Lesson 03): isolate unfinished changes from main.
4. **Open a PR** (this lesson): lay the branch's changes out for review.
5. **Merge** (this lesson): after discussion passes, merge back into main and delete the branch.

These five steps are not a one-off; they are a wheel that keeps turning. On a real project, for every feature added and every bug fixed, the team repeats this branch -> PR -> review -> merge loop. The single loop you completed today is the thing that happens every day in countless teams.

---

## 12. Exercises

### Exercise 1: run the full PR loop

**Goal:** merge the update-notes changes back into main through a PR with your own hands.

**How to do it:**

1. Open the repo from Lesson 03 and confirm update-notes has changes.
2. Open a PR per Section 7, with a clear title and description.
3. Leave one comment of your own on the PR diff, pretending you are the reviewer.
4. Merge the PR per Section 8, then delete the branch per Section 9.
5. Switch to main, open notes.md, and confirm the changes are there.

**What you will observe:**

After the merge, the lines that were only on update-notes now appear on main; and update-notes is gone from the branch list.

> **Key insight:** the value of a change is not that it was written, but that it was reviewed and then merged into the trunk.

### Exercise 2: cause a small conflict on purpose

**Goal:** see a merge conflict with your own eyes and lose your fear of it.

**How to do it:**

1. Create a new branch, for example edit-title, change the first line of notes.md to a sentence, and commit.
2. Go back to main and change that same first line of notes.md to a different sentence, and commit.
3. Open a PR for edit-title and watch GitHub's warning.

**What you will observe:**

GitHub flags that this PR has a conflict and cannot be merged automatically until the conflict is resolved.

> **Key insight:** a conflict is not a disaster; it is the system honestly saying "there are two versions of the same spot, you make the call".

---

## 13. Recap: what we learned

- A **Pull Request** is a "please merge my changes in" request that splits making a change from adopting it into two steps.
- **Code review** has a change looked at before it enters main: catch bugs early, spread knowledge, leave a record.
- **Merge** officially folds a branch's changes into main; after merging, **delete the branch** to stay tidy.
- A **merge conflict** shows up when two changes clash; it is not an error, just something a human must decide.
- Create repo -> edit files -> open branch -> open PR -> merge is a collaboration loop that repeats over and over.

---

## 14. Mentor's note

**Why this exercise matters:**

I have mentored many beginners, and the step they most underestimate is the PR. Plenty of people can use git, but the ones who make a team run smoothly are those who take review seriously. A good PR is not just correct code; it also explains "what I changed and why", so someone else can understand it in five minutes and merge with confidence. The first PR you open in this course, however simple, is you practicing that habit.

**Key insights:**

- A PR is a vehicle for team communication, not just a button that merges code. The title and description you write are for your future teammates.
- Reviewing others' code and being reviewed are among the fastest places to grow; do not treat it as nitpicking.

**Next step:**

Back on a real project, try opening a PR for every change, even when you are the only person. Force yourself to state the why in the description, and you will find you think more clearly. By the time you join a team, this routine is already muscle memory.

---

## 15. Quick reference

**Open a PR:** on the repo home click Compare & pull request, or go Pull requests -> New pull request, and confirm the direction is base main <- compare your branch.

**Merge:** on the PR page Merge pull request -> Confirm merge -> a successfully merged line means it worked.

**Clean up:** click Delete branch to remove the used-up branch.

**Key concepts:**

- `Pull Request`: a request to merge a branch's changes into a target branch.
- `code review`: the process of someone else reviewing changes before they merge.
- `merge conflict`: two changes clash and a human must decide which to keep.
