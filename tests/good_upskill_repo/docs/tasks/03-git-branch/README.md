---
description: By the end you can explain what problem branches solve and independently create a branch and commit to it without touching main.
---

# Isolate Changes with Git Branches

> Teaches you to create a branch and make changes safely on it, leaving the stable version on main untouched.

## 1. Overview

A branch is a parallel line of work inside a repo. The main branch holds the stable version; new ideas and half-done work live on their own branches and get merged back when ready. This is how teammates avoid stepping on each other.

---

## 2. Learning Goals

If everyone edited main directly, half-done work would mix with the stable version and any one person's mistake would hit the whole team. Branches let each person finish work in their own parallel world first.

After this task, you will be able to:

1. Explain what problem branches solve and what role the main branch plays.
2. Create a new branch from main.
3. Commit changes on the branch and confirm main is unaffected.

---

## 3. Hands On

1. Open your repo and click the branch dropdown showing main in the top-left.
2. Type a new branch name, for example update-notes, and click Create branch.
3. Confirm the current branch shown in the top-left has switched to update-notes.
4. On this branch, edit notes.md, append one line, and commit.
5. Switch back to main with the branch dropdown and confirm notes.md does not have the new line.

---

## 4. Recap

- Main holds the stable version; changes happen on your own branch first.
- A commit belongs only to the branch it was made on.
- Branch names follow the same convention as repo names: lowercase with hyphens, describing what the branch is for.
