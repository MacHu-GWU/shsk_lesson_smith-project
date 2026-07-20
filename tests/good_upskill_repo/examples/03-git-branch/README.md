---
description: Learn to use a branch to keep unfinished changes off the main line, and understand why collaboration depends on branches.
---

# Isolating Your Changes With a Branch

> How to open a branch on GitHub, edit files freely on it, and leave main completely untouched.

## 1. Overview

So far you built a repo in 01 and learned to edit files directly in 02. But you may have felt a small unease already: every commit lands straight on the main line. What happens when you are halfway through a change, change your mind, or the code simply does not work yet? Your main line gets polluted with half-finished work.

A branch is what solves this. It lets you open a separate line where you can experiment freely while main stays clean and usable. This whole lesson happens in the browser, with no command line.

---

## 2. Learning Goals

Start with the why. In real projects, the main line (usually called main) represents "the version that is always ready to ship". Teammates build on it, and automation deploys from it. If you pile unfinished, untested work straight onto main, it is like dumping construction debris in someone's living room.

A branch gives you an isolated workbench: your changes sit on your own branch until they are ready, then you merge them back. This is where all team collaboration begins -- without branches, several people working on the same repo would immediately step on each other.

By the end of this Task, you will be able to:

1. Explain what a branch is, and why the default branch (main) is special.
2. Create a new branch on GitHub in the browser.
3. Edit and commit files on the new branch while confirming main stays unchanged.

---

## 3. Prerequisites

- Finished 01: you own a repo.
- Finished 02: you can create and edit files in the browser and write a commit message.
- A browser and your GitHub account. Nothing to install.

---

## 4. What You Will Learn

By the end you will hold two lines with your own hands: an untouched main, and a branch you just opened. You will see the same file existing as two versions on the two lines, without interfering with each other. That picture -- one repo, several parallel versions -- is the key to understanding Pull Requests later.

---

## 5. What a Branch Actually Is

Picture yourself writing an important document. You are not sure a new approach will work, so you save a separate copy called "document-experiment" and rework the copy aggressively. The original sits there untouched. If the experiment turns out well, you replace the original with it; if it goes wrong, you just delete the copy and the original is unharmed.

A branch is exactly that "save a separate copy" move, only smarter:

- Instead of clumsily copying the whole repo, it forks a new line of history off some commit.
- Every commit you make on the branch only accumulates on this line and never touches other branches.
- You can compare the two lines at any time, and merge one line's work into another whenever you want.

In one sentence: a branch is an independently evolving sequence of commits that lets you push work forward without disturbing the main line.

---

## 6. Why the Default Branch (main) Is Special

When any repo is created, GitHub gives you a default branch, and the current convention names it main (older projects may call it master). It is special because:

- When someone opens your repo, the home page shows the contents of main by default.
- It is treated as the "official version" -- teams and automation trust that whatever is on main works.
- As you will see later, changes on other branches are all headed toward being merged back into main.

Precisely because main matters this much, we do not want to make risky, uncertain changes directly on it. The rule is simple: keep main stable, do the experimenting on a branch.

---

## 7. Creating a Branch in the Browser

GitHub's web UI has a branch switcher: the dropdown button at the top left of your repo's file list that reads main. Creating a branch happens right here:

1. Open your repo and stay on the default Code tab.
2. Click the dropdown that shows main; a search box pops up.
3. Type the name you want for the new branch, for example add-tagline.
4. A line appears reading Create branch add-tagline from main. Click it.
5. After the page refreshes, that dropdown now shows add-tagline instead of main. That means you are now standing on the new branch.

Name branches in lowercase words joined by hyphens, describing what the branch is for, such as add-tagline, fix-typo, or update-readme. This is the common convention on teams.

---

## 8. Editing Files on the Branch

Now that you are standing on add-tagline, the editing is exactly like 02, with one difference: the changes land on this branch, not on main.

1. Confirm the top-left button shows add-tagline, not main.
2. Open README.md and click the pencil icon at the top right to edit.
3. Add a line, for example a tagline for the project.
4. Click Commit changes at the top right and write a commit message in the dialog, for example Add project tagline.
5. Notice the dialog asks where to commit. Confirm it has selected Commit directly to the add-tagline branch, then confirm.

Once committed, click the branch dropdown again and flip between main and add-tagline. Look at the file on main and it is unchanged; switch to add-tagline and you see the line you just added. Same file, two lines, two versions.

---

## 9. Exercise

### Exercise 1: Open a Branch and Verify main Is Untouched

**Goal:** See with your own eyes that changes on a branch never touch main.

**How to do it:**

1. In your repo, use the branch switcher to create a branch named add-tagline.
2. Standing on add-tagline, edit README.md, add a tagline line, and commit.
3. Use the switcher to go back to main and open the same README.md.

**What you will observe:**

The README.md on main does not contain the tagline line you just added -- it is exactly as before. Switch back to add-tagline and the line reappears.

> **Key insight:** Changes are bound to a branch. As long as you do not actively merge, main will never change just because you are tinkering on another branch.

---

## 10. Recap: What We Learned

- A branch is an independent sequence of commits, like saving a separate copy of a document to experiment on.
- main is the default branch and represents the official, trusted version.
- The branch switcher is the entry point for creating and switching branches in the browser.
- Committing on a branch does not affect main, and that isolation is the whole point.

---

## 11. A Note From Your Mentor

**Why this exercise matters:**

When I onboard newcomers, the one instinct I most want them to build early is: never do anything uncertain on main. This is not tidiness for its own sake, it is the foundation of collaboration. When ten people are changing one repo, main is the shared baseline everyone trusts; keep every half-finished thing on your own branch and no one trips over your intermediate state.

**Key insights:**

- Isolation is not about hiding, it is about keeping "in progress" and "finished" clearly apart.
- A branch is best when it maps to a single thing, so that merging and reviewing it later stay clean.

**Next step:**

You now have a branch with a finished change, but it is sitting off to the side all by itself. The next lesson, 04, teaches you to use a Pull Request to review its changes and officially merge them back into main -- that is the step where the collaboration loop truly closes.

---

## 12. Quick Reference

**Create a branch:** repo Code tab -> click the main dropdown at top left -> type a new name -> click Create branch xxx from main.

**Switch branch:** pick another branch from the same dropdown.

**Commit on a branch:** edit a file -> Commit changes -> confirm it selected Commit directly to the xxx branch.

**Key conventions:**

- `main`: the default branch, the official version, keep it stable.
- Branch name: lowercase with hyphens, describing what the branch does, such as `add-tagline`.
