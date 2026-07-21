---
description: "An interview-style self test that checks whether you understand the whole course, not just the how but the why."
---

# GitHub Collaboration Basics Self Test

> This document is a way to verify everything you learned across the whole course, checking that you know not just how things work but why they work that way. Treat each question as if an interviewer were asking you face to face: answer on your own first, then compare against the reference answer and the deeper explanation.

## 1. What is a repository

**Question**

> In one sentence, what is a repository, and how is it different from an ordinary folder on your computer?

**What it probes**

> Whether you see a repo as a "project container with full history", not just a pile of files.

**Reference answer**

> A repository is the home of a project. It holds all of the project's files plus a record of every change every file has ever gone through. An ordinary folder only has the current state of its files; a repo additionally keeps the complete change history.

**Deep dive**

> The key difference is "history". In a plain folder, once you change a file the old version is gone; a repo records every change as a commit, so you can always look back or even roll back. See the part of [01-create-repo](../01-create-repo/README.md) that explains the repository concept.

---

## 2. What is a commit

**Question**

> What is a commit? Why do people say it is like a save point in a game?

**What it probes**

> Whether you understand a commit as "a snapshot with a note attached", not just saving a file.

**Reference answer**

> A commit is a snapshot of the project at one moment, together with a short note describing what changed. Like a save point in a game, it records the current state so you can return to that point later.

**Deep dive**

> The save-point analogy captures two things: a commit is a discrete point in time (not continuous autosave), and you can return to any of those points. Each commit has an author, a timestamp, and a message. See the part of [01-create-repo](../01-create-repo/README.md) that compares a commit to a save point.

---

## 3. Why check Add a README when creating a repo

**Question**

> When you create a new repository on GitHub, what does checking Add a README file do? What happens if you leave it unchecked?

**What it probes**

> Whether you understand what a README is for, and the initial state of an empty repo.

**Reference answer**

> When checked, GitHub automatically creates a README.md and makes the first commit for you, so the repo is non-empty the moment it exists and you can edit it right there in the browser. If you leave it unchecked, the repo is empty and GitHub shows you a screen of command-line instructions, which is unfriendly for beginners.

**Deep dive**

> The README is the intro page people see first when they open your repo, and GitHub renders it front and center on the home page. For this fully browser-based course, checking README has another practical benefit: it gives you a file to start practicing edits on right away. See the part of [01-create-repo](../01-create-repo/README.md) that covers initializing a README.

---

## 4. The difference between public and private

**Question**

> When you create a repo, does choosing public or private affect anything real?

**What it probes**

> Pure knowledge check, whether you know what visibility means.

**Reference answer**

> A public repo can be seen by anyone; a private one is visible only to you and the people you invite. The code's functionality is unaffected; the only difference is who can access it.

**Deep dive**

> This course recommends public, because the later Pull Request review process is more visible and intuitive in a public repo, and it also makes for an easy portfolio piece. See the part of [01-create-repo](../01-create-repo/README.md) that compares public and private.

---

## 5. Why commit every change instead of batching them up

**Question**

> Why is it recommended to commit once per small change, rather than making a big pile of changes and submitting them all at once?

**What it probes**

> Whether you understand the value of small commits for "revertability and traceability".

**Reference answer**

> Small commits keep the history clear: each commit does exactly one thing, so when something breaks it is easy to pinpoint which change introduced it, and easy to roll back just that one step. Committing a big pile at once turns the history into a blob that is hard to search and hard to undo.

**Deep dive**

> The granularity of a commit directly determines how readable the history is. An ideal commit is "one semantically complete small thing". See the part of [02-edit-files](../02-edit-files/README.md) that covers how commits record changes.

---

## 6. Why commit messages matter

**Question**

> Who is actually affected by whether a commit message is well written? Give an example of a good message and a bad one.

**What it probes**

> Whether you understand that a message is written for future readers (including yourself).

**Reference answer**

> A commit message is written for future readers, letting people get the gist of what changed without opening the diff. A good message might be Add install steps to README; a bad one is update or asdf, which tells you nothing after the fact.

**Deep dive**

> Six months later, when you or a teammate dig through the history to find "which change introduced this", the message is what you rely on. One clear message is the cheapest form of communication. See the part of [02-edit-files](../02-edit-files/README.md) that covers commit messages.

---

## 7. How to create a new file in the browser

**Question**

> Without the command line, entirely on the GitHub website, how do you add a new file to a repo?

**What it probes**

> Pure hands-on question, whether you have actually done it.

**Reference answer**

> On the repo home page, click the Add file dropdown, choose Create new file, enter a file name and content, then scroll down and click Commit changes to create it.

**Deep dive**

> The web editor lets you add, delete, and modify files without ever touching git, and each Commit changes is equivalent to making one commit. See the part of [02-edit-files](../02-edit-files/README.md) that covers creating a file with the web editor.

---

## 8. What is commit history and how do you view it

**Question**

> Where can you see all of a repo's commits? What can that list tell you?

**What it probes**

> Whether you know where the history lives and what it is for.

**Reference answer**

> In the repo, click commits (usually above the file list, where the commit count is shown) to see every commit from oldest to newest, including author, timestamp, and message. It tells you how the project evolved all the way along.

**Deep dive**

> The commit history is the project's timeline, and opening any single commit shows you exactly which lines that change touched. This is the core value of version control: every change is on the record. See the part of [02-edit-files](../02-edit-files/README.md) that covers commit history.

---

## 9. What is a branch

**Question**

> Use an analogy to explain what a branch is.

**What it probes**

> Whether you understand a branch as an "isolated parallel line of work".

**Reference answer**

> A branch is like saving a separate copy of the whole project. You can change anything on the copy without affecting the original main line at all. When it is ready you merge it back; if it goes badly you just throw the copy away.

**Deep dive**

> The key word is "isolation": a branch keeps unfinished or risky changes on their own line so they do not pollute the stable version everyone shares. See the part of [03-git-branch](../03-git-branch/README.md) that uses the saved-copy analogy for a branch.

---

## 10. What is the default branch main

**Question**

> What is special about the main branch? Why is it discouraged to make changes directly on main?

**What it probes**

> Whether you understand main as the team's shared stable trunk.

**Reference answer**

> main is the repo's default branch, representing the project's current official, stable version, and it is the shared baseline for everyone. Changing main directly is like shoving unverified work into the version everyone is using, which is risky.

**Deep dive**

> Precisely because main is the shared baseline, the rule of modern collaboration is "don't touch main directly; make changes on a branch first". See the part of [03-git-branch](../03-git-branch/README.md) that covers the default branch.

---

## 11. Why collaboration cannot do without branches

**Question**

> If a team of five all commit directly to main, what goes wrong? How do branches solve it?

**What it probes**

> Whether you can connect the value of a branch to a real collaboration scenario.

**Reference answer**

> If everyone commits to main, unfinished or buggy code from different people interferes with each other, and main can be broken at any moment. Branches let each person work on their own line, and only after finishing and verifying do they merge, so main always stays usable.

**Deep dive**

> A branch physically separates "work in progress" from "the stable finished product", which is the precondition for multiple people to make progress in parallel. See the part of [03-git-branch](../03-git-branch/README.md) that covers why collaboration needs branches.

---

## 12. How to create a branch in the browser

**Question**

> Entirely on the GitHub website, how do you create a new branch and switch to it?

**What it probes**

> Pure hands-on question.

**Reference answer**

> In the branch dropdown at the top left of the repo home page, type a new name and click Create branch. This creates a new branch based on the current one and switches you to it.

**Deep dive**

> A new branch starts as a complete copy of the current branch, and after that any commits you make on it stay only on this line. See the part of [03-git-branch](../03-git-branch/README.md) that covers creating a branch on the web.

---

## 13. Do changes on a branch affect main

**Question**

> You switch to a new branch, change a file, and commit. If you now look at main, have main's files changed? Why?

**What it probes**

> Whether you truly understand the isolation of a branch.

**Reference answer**

> They have not changed. Your commit lands only on the current branch's line; main stays at the state it was in before you branched off, until you explicitly merge the changes back into main.

**Deep dive**

> This is exactly the point of a branch: isolation. Only the merge action brings a branch's changes back into main. See the part of [03-git-branch](../03-git-branch/README.md) that covers changes not affecting the trunk.

---

## 14. What is a Pull Request

**Question**

> What is a Pull Request? What is the significance of the word request in the name?

**What it probes**

> Whether you understand a PR as a "request to merge" that splits the change and its adoption into two steps.

**Reference answer**

> A Pull Request is a request to "please merge the changes on my branch into the target branch". The word request signals that it is a request, not a command: proposing the request and actually merging are two separate things, with a review in between.

**Deep dive**

> Separating "the change" from "officially adopting the change" is the core design of a PR: that gap in the middle is left for review and discussion. See the part of [04-merge-branch](../04-merge-branch/README.md) that covers what a Pull Request is.

---

## 15. What three things are on a PR page

**Question**

> When you open a PR page, what are the three main parts you can see, and what is each for?

**What it probes**

> Whether you are familiar with the makeup of a PR.

**Reference answer**

> The diff (which lines your branch changed relative to the target, red for deletions and green for additions), the conversation (a discussion area where you can comment line by line), and the merge button (which merges in one click once the discussion passes).

**Deep dive**

> These three bring the "content, discussion, and decision" of a change together on one traceable page, which is why the PR became the vehicle for team communication. See the part of [04-merge-branch](../04-merge-branch/README.md) that lists the three areas of a PR.

---

## 16. What problem does code review solve

**Question**

> What benefits do you actually get from having someone review your work before merging?

**What it probes**

> Whether you can name the real value of review, rather than treating it as a formality.

**Reference answer**

> Three benefits: catching bugs the author missed on their own; spreading knowledge so it does not live in only one person's head; and leaving a traceable discussion record of the change. It is the default gate for almost every serious project.

**Deep dive**

> The value of review is not obvious in solo practice, but on a team it is the safeguard for quality and knowledge transfer. Six months later, the answer to "why is this line written this way" lives in the PR conversation. See the part of [04-merge-branch](../04-merge-branch/README.md) that covers code review.

---

## 17. How to open a Pull Request

**Question**

> Once your branch has changes, how do you open a PR in the browser?

**What it probes**

> Pure hands-on question.

**Reference answer**

> The repo home page usually pops up a Compare & pull request button; click it. Or go to the Pull requests tab and click New pull request. Confirm the direction is base main <- compare your branch, fill in the title and description, and click Create pull request.

**Deep dive**

> The direction (base <- compare) is the key: base is the target being merged into (usually main), and compare is your branch carrying the changes. See the part of [04-merge-branch](../04-merge-branch/README.md) that covers opening a PR hands-on.

---

## 18. What happens to main after a merge

**Question**

> After you click Merge pull request and confirm, how do you verify that the changes really made it into main?

**What it probes**

> Whether you understand the result of a merge and how to confirm it.

**Reference answer**

> After merging, the page shows successfully merged. Switch back to the repo home page, set the branch dropdown to main, open the relevant file, and you will see the branch's changes really did land on main.

**Deep dive**

> A merge is the action that officially brings a branch's commits into main, after which those changes become part of the project's official version. See the part of [04-merge-branch](../04-merge-branch/README.md) that covers merge.

---

## 19. Why delete the branch after merging

**Question**

> After a PR merges successfully, GitHub prompts Delete branch. Is deleting it safe? Why do it?

**What it probes**

> Whether you understand what deleting a branch actually deletes.

**Reference answer**

> It is safe. The branch's changes are already in main, and all you delete is the label for that "line of work"; the changes themselves live safely in main's history. Deleting keeps the branch list tidy: one branch per task, and once the task is done you retire it.

**Deep dive**

> A deleted branch can be restored later if needed, so there is no worry about losing anything. See the part of [04-merge-branch](../04-merge-branch/README.md) that covers deleting a branch after merging.

---

## 20. What is a merge conflict

**Question**

> In what situation does a merge conflict occur? When you hit one, how should you think about it?

**What it probes**

> Whether you recognize a conflict and are not afraid of it.

**Reference answer**

> A merge conflict occurs when two branches change the same spot in the same file in different ways. It is not an error; it is just GitHub saying "there are two competing versions here, I dare not guess for you, so you decide which one to keep".

**Deep dive**

> Resolving it just means manually picking which one to keep and then confirming; as long as people edit different files or sync with main promptly, conflicts are rare. Deeper resolution is a topic for later. See the part of [04-merge-branch](../04-merge-branch/README.md) that covers merge conflicts.
