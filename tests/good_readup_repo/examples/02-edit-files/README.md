---
description: "Learn to create and edit files right in the GitHub web interface, capturing every change as one clear commit."
---

# Creating and Editing Files on GitHub

> Use GitHub's built-in web editor to create and change files, understand the commit behind every save, and learn to read commit history.

## 1. Overview

In the last task you created a repository. Right now it is nearly empty: just a README. An empty repo is pointless. The value of a project lives in its files, and files get written one piece at a time and improved one change at a time.

The good news: you can do all of this in your browser. No git install, no command line. GitHub ships with a web editor that lets you create files, edit files, and save, all with a few clicks. And every save becomes a traceable point in your project's history. That point is called a commit.

This task connects two ideas, changing a file and recording the change, and builds the single most important habit in the whole GitHub workflow.

---

## 2. Learning Goals

Start with why. When you write a document in Word and press Ctrl+S, the file is overwritten and the previous version is gone. If you change your mind tomorrow and want this morning's draft back, you are mostly out of luck. That is the problem with ordinary saving: it keeps only "now" and erases "before."

Saving on GitHub is different. Every save is a commit, and it does not overwrite history, it appends a new point to it, along with a sentence explaining what you changed. Your project now has a full timeline: any past version can be reopened, and every change carries who made it, when, and why. That is exactly why engineers happily click a few extra times to use GitHub instead of a shared drive for their code.

After this task, you will be able to:

1. Create a new file in the browser with the web editor and save it.
2. Edit an existing file, understanding that each save is one commit.
3. Write a clear commit message that states the intent of the change.
4. Open the commit history and read every step your project has taken.

---

## 3. Prerequisites

- You finished Task 01 and own a repository (the examples below use recipe-box).
- A GitHub account you can sign in to, and a browser.
- A rough sense that a commit is "one recorded change" (established in Task 01).

---

## 4. What You Will Learn

By the end, your recipe-box will hold a few new files, and its Commits page will show a string of commits you left by hand. For the first time you will see it plainly: a project is not a static folder, it is a timeline strung together by commits.

---

## 5. The Web Editor: Your Browser Is the Editor

Many beginners assume that changing a file on GitHub means downloading the repo to their computer first. It does not. GitHub has a built-in web editor, and you write directly in the browser.

A mental model: think of the web editor as a "notepad that lives inside the repo." You open it, type, save, and your work goes straight into the repo without ever touching your hard drive.

What it is good for:

- Small changes to docs, config, or a README, anything that is plain text.
- Quickly fixing a typo or adding a line of explanation.

What it is not good for:

- A large refactor touching dozens of files at once (for that you will eventually use local git, which is out of scope here).

For where you are now, the web editor is more than enough to walk the entire collaboration loop, and that is the point: it gets you into a real workflow with zero setup.

---

## 6. Creating a New File

Let's add a recipe file to recipe-box. Say you are Maria Garcia and you want to store your family's tomato pasta.

How to do it:

1. Open your recipe-box homepage, click the Add file button above the file list, and choose Create new file.
2. There is a filename box at the top of the page. Type pancakes.md. Note: if you type a slash / in the name, GitHub automatically creates a folder for you, so recipes/pancakes.md drops the file into a recipes folder.
3. Write your content in the large editing area below, for example a few lines of Markdown with ingredients and steps.
4. Once the content looks right, look at the Commit changes button in the top-right corner. Don't click yet, the next section is all about that dialog.

**What you will observe:** there is always a Commit changes button in the top-right. GitHub is reminding you that typing alone doesn't count, you have to commit before the change truly lands in the repo.

---

## 7. Editing an Existing File

Changing a file that already exists has a slightly different entry point.

How to do it:

1. Click open the file you want to change, say README.md, to reach its view page.
2. Find the pencil icon at the top-right of the file content (hovering shows Edit this file) and click it to enter edit mode.
3. Edit the text directly, for example add a sentence introducing your project to the README.
4. When done, click Commit changes in the top-right, same as before.

Creating and editing look a little different on screen, but they are the same act underneath: you changed the repo's contents, then recorded that change with one commit. Hold on to this unified mental model and the interface details won't trip you up.

---

## 8. Commit Messages: A Note to the Future

After you click Commit changes, a small dialog appears with a title box, pre-filled with placeholder text like Update README.md. That one line is the commit message, and it is the part of this task that most deserves your attention.

Why does it matter? Imagine six months from now John Smith takes over your project, scrolls to some change, and sees only Update README.md. He has no idea what you changed or why. Now imagine that line reads Add setup steps for new contributors, he gets it at a glance. A commit message is a note you leave for your future self and your teammates, the cheapest and most valuable documentation a project has.

A good commit message:

- Says in one sentence what the change did, not that "a file was changed."
- Starts with a verb, like a command: Add, Fix, Update, Remove.
- Bad examples: update, fix, asdf, "changed stuff." Nobody can decode these later.
- Good examples: Add tomato pasta recipe, Fix typo in README title.

The dialog usually also has a larger description box (optional). Leave it blank for small changes; for complex ones, write a few sentences here to expand. Fill in the title, click the green Commit changes, and your change is officially in the repo.

---

## 9. Commit History: Reading the Project's Timeline

Commits pile up one by one into a commit history, the project's full timeline. Learning to read it is how you truly grasp what GitHub is recording for you.

How to read it:

1. Back on the repo homepage, above the file list, find a link with a clock icon labeled Commits (it usually shows the count, for example 5 commits) and click it.
2. You'll see a list ordered newest to oldest, one row per commit: your commit message on the left, plus the author avatar and a "how long ago" timestamp.
3. Click any commit to see exactly which lines it changed: green for additions, red for deletions. This line-by-line comparison is called a diff.

An analogy: commit history is like a game's list of save files. Each commit is a save point, the message is the name you gave that save, and the diff is what you see when you open it, "how this save differs from the last." Name your saves well and you can find them when you need to load one.

**What you will observe:** the more care you put into commit messages, the clearer this timeline reads. That is instant positive feedback, a good habit that pays off on the spot.

---

## 10. Exercises

### Exercise 1: Create a Recipe File

**Goal:** use the web editor to add a new file to recipe-box and leave a decent commit.

**How to do it:**

1. In recipe-box, Add file, Create new file, name it recipes/pancakes.md.
2. Write a few lines of Markdown: a title, an ingredient list, a few steps.
3. Set the commit message to Add pancake recipe and click Commit changes.

**What you will observe:** the repo homepage now has a recipes folder with pancakes.md inside. You just added content to the project using nothing but a browser.

> **Key insight:** a slash in the filename auto-creates a folder, a hidden but frequently used trick of the web editor.

### Exercise 2: Edit a File and Read the History

**Goal:** edit an existing file, then find that change again in the commit history.

**How to do it:**

1. Open README.md, click the pencil icon, and add a sentence introducing your recipe-box.
2. Set the commit message to Update README with project intro and commit.
3. Go to the Commits page, find that commit, and click it open to see its diff.

**What you will observe:** in the diff, the sentence you added is highlighted in green. The project history is accurate down to the line.

> **Key insight:** every save is permanently recorded and you can return to any point in history at any time, a safety net a plain shared drive can't give you.

---

## 11. Recap: What We Learned

- The web editor lets you create and edit repo files in the browser with zero setup.
- Creating (Add file) and editing (the pencil icon) have different entry points, but both are "a change plus one commit."
- A commit message is a note to the future: start with a verb, state what you did in one sentence.
- The commit history is the project's timeline, and each commit opens to a line-by-line diff.

---

## 12. A Note from Your Mentor

**Why this exercise matters:**

Among the newcomers I have mentored, what separates someone who "knows git" from someone who "can merely push code" is often this one line, the commit message. Anyone can learn the clicks, but whether you'll spend ten extra seconds writing a clear sentence for a teammate half a year out, that is what shows an engineer's professionalism. The habit you build now will follow you your whole career.

**Key insights:**

- Code is written for people to read, and so is a commit message. Both save the future you time.
- Frequent, small, semantically clear commits beat hoarding a huge batch and committing it all at once.

**Next steps:**

On a real project, try to make each commit do exactly one thing. Adding a feature is adding a feature, fixing a typo is fixing a typo, don't mix them. Then your commit history reads like a diary you can follow instead of a tangle.

---

## 13. Quick Reference

**Create a file:** repo homepage -> Add file -> Create new file -> type a name (slash auto-creates folders) -> write content -> Commit changes.

**Edit a file:** open the file -> pencil icon (Edit this file) -> change content -> Commit changes.

**View history:** repo homepage -> Commits (clock icon) -> click a commit to see its diff.

**A good commit message:** start with a verb, one sentence stating the intent. For example Add tomato pasta recipe.
