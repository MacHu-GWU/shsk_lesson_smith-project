# GitHub Collaboration Basics Runbook

> How to run this course: how to set up before you start, and which environment / command / operational steps come up as you go. When something will not run, look here first.

## 1. Environment Setup

A one-time setup before the examples begin. This course installs nothing and touches no command line — everything happens on github.com in the browser.

- Prerequisites: a GitHub account (free to create at github.com) and a modern web browser. No software to install, no git, no command line. Note that [mise.toml](../../mise.toml) is only a project-root marker for tests, so there are no `mise` tasks to run here.
- First-time setup:
1. Create or sign in to a GitHub account at github.com.
2. That is all — everything else is done in the browser as each mini task walks you through it.

## 2. Operations Along the Way

Overall rhythm: every mini task is read-the-README-and-do-it directly on github.com in the browser. There is no `cd`, no environment variable, no local command, and no service to start; the only spots below step slightly off the beaten path.

Steps worth singling out:

- Before examples/01: you must have a GitHub account you can sign in to — that account is the single prerequisite the whole course assumes. Create it at github.com first, then do everything on your own account.
- At [examples/04-merge-branch](../../examples/04-merge-branch/README.md): the `Compare & pull request` banner does not always appear on the repo home. If it is missing, open the PR manually via the `Pull requests` tab then `New pull request`, and confirm the direction reads `base: main <- compare: your-branch`.

## 3. Common Snags

- Typing in the web editor saves nothing until you click `Commit changes`; a change only lands in the repo after the commit. See the [Commit changes note in 02-edit-files](../../examples/02-edit-files/README.md).
- A merge conflict is not an error: it just means two branches changed the same spot in the same file and GitHub wants a human to choose. See the [merge conflict aside in 04-merge-branch](../../examples/04-merge-branch/README.md).
