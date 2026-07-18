---
description: By the end you can merge a branch back into main through a Pull Request and explain the review role a PR plays in teamwork.
---

# Merge a Branch through a Pull Request

> Teaches you to review and merge branch changes back into main with a Pull Request, closing the collaboration loop.

## 1. Overview

Once the work on a branch is done, the last step is merging it back into main. The standard GitHub way is not a direct merge but a Pull Request (PR): present the changes, invite review, then merge once approved.

---

## 2. Learning Goals

Pushing changes straight into main means teammates only discover problems after the fact. A PR turns merging into an open review: the changes are laid out, the discussion is recorded, and problems get caught before they reach main. It is the core ritual of modern team collaboration.

After this task, you will be able to:

1. Open a Pull Request for a branch.
2. Read the change comparison (diff) on the PR page.
3. Complete the merge and delete the branch once its job is done.

---

## 3. Hands On

1. Open your repo and switch to the update-notes branch from the previous lesson.
2. Click Contribute and choose Open pull request.
3. Confirm the direction is from update-notes into main, fill in a title and a one-line summary, and click Create pull request.
4. Review the diff under the Files changed tab and confirm the changes look right.
5. Click Merge pull request, then click Delete branch.
6. Switch back to main and confirm notes.md now shows the line added on the branch.

---

## 4. Recap

- A PR is the formal request to merge your branch into main, with review and discussion built in.
- After the merge the branch's job is done; delete it promptly to keep the repo tidy.
- You have now closed the collaboration loop: create a repo, edit files, open a branch, merge back to main.
