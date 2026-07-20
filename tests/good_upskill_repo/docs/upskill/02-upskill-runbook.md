# GitHub Collaboration Basics Runbook

> How to run this course: how to set up before you start, and which operational steps come up as you go. When something will not run, look here first.

## 1. Environment Setup

A one-time setup before the examples begin.

- Prerequisites: a modern web browser and a free GitHub account. There is nothing to install: no git, no command line, no local tooling. (The [mise.toml](../../mise.toml) at the repo root is for maintainers of this course, not for learners.)
- First-time setup:
1. If you do not have an account, create a free one at https://github.com/signup.
2. Sign in and confirm you can reach your profile at https://github.com/ followed by your username.

## 2. Operations Along the Way

Overall rhythm: every mini task is read-the-README-and-do-it-in-the-browser. There is no command line and nothing to install, so the operational surface is small. The one thing to keep in mind is that each task reuses the repository you create in 01, so keep working in that same repo throughout.

Steps worth singling out:

- At examples/01-create-repo: this is where you create the repository that every later task reuses. Make it public so that later a Pull Request and its review are visible.
- At examples/03-git-branch: the branch switcher is the dropdown near the top-left of the Code tab, showing the current branch name; that is where you create and switch branches.
- At examples/04-merge-branch: opening and merging a Pull Request happens entirely in the browser. If the Merge button is greyed out, see Common Snags.

## 3. Common Snags

- A Pull Request will not merge: usually the branch has no real difference from the base branch, or GitHub reports a merge conflict. Make sure your branch actually changed a file. If there is a conflict, resolve it in the web editor, or recreate the branch from an up-to-date main.
- You cannot find where to switch branches: look for the branch dropdown near the top-left of the Code tab.
