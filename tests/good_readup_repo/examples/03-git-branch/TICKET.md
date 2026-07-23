---
description: "Create a branch and commit changes on it while the main line (default branch) stays untouched."
---

# Open a Branch and Commit Changes on It

## 1. Goal

Open a new branch in your own repo, edit and commit a file on that branch, and confirm the default branch (main) was not touched by the change. This step lets you feel the isolation a branch gives you firsthand: work in progress stays on its own branch while the main line stays clean.

---

## 2. What to Do

1. Open your repo and use the branch switcher at top left (the dropdown that shows main) to create a branch. Use a lowercase, hyphenated name such as add-tagline.
2. Confirm you are standing on the new branch (the dropdown shows the new name), then edit README.md, add a line, and commit. When committing, confirm it selected Commit directly to the new branch.
3. Use the branch switcher to go back to main, open the same README.md, and confirm the line you just added is not on main.

**Estimated time:** 10 to 15 minutes

---

## 3. Checklist

- [ ] **New branch created**: the branch switcher shows a branch other than main, with a descriptive lowercase hyphenated name.
- [ ] **Change committed on the branch**: README.md on the new branch has your added line, with a matching commit.
- [ ] **main untouched**: switching back to main and viewing the same file, the added line is absent and main is unchanged.
- [ ] **Can explain the principle**: you can state in one sentence why committing on a branch does not change main.
