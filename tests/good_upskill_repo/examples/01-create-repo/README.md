---
description: "Build your very first GitHub repository from scratch, and actually understand what a repository and a commit really are."
---

# Create Your First Repository

> Using nothing but a browser, create your first repository on GitHub, and get a solid grip on the two most important ideas behind it: repository and commit.

## 1. Overview

You are going to go to github.com, click a few buttons, and end up with your own project repository containing a README file. No git to install, no command line to touch. All you need is a browser and a GitHub account.

It sounds small, but it is the starting point of everything you will ever do on GitHub. Behind the simple act of creating a repository sit two concepts: what a repository is, and what a commit is. Once those two words make sense, the branches, Pull Requests, and merges that come later have something to hold on to. So the real goal here is not "click the right button" but "know what you just did after you click it."

---

## 2. Learning Goals

Let me tell you why this matters first. Picture Maria Garcia working on a little recipe project. At first she scatters files across her desktop named recipe-final.txt, recipe-final-v2.txt, recipe-really-final.txt. A month later even she cannot tell which one is current, let alone hand it to her friend John Smith so they can edit it together. Files fly around over email and chat, and nobody can say who changed what or which version wins.

A repository exists to end exactly that kind of chaos. It gives a project one single, traceable home: all files live together, every change is recorded, and anyone can see at any time what it looks like now, what it looked like before, and who changed it. This is the foundation of team collaboration, and a foundation feels real only after you have laid one with your own hands.

By the end of this Task you will be able to:

1. Explain in your own words what a repository is, and how it differs from an ordinary folder on your computer.
2. Say what a commit is, and why it is the smallest unit GitHub uses to record a change.
3. Create a public repository with a README entirely in the browser, and explain the difference between public and private.

---

## 3. Prerequisites

- A GitHub account you can log in to (free to create at github.com).
- Basic browser skills: clicking buttons, filling in fields, reading what is on the page.
- No software to install, no command line, no prior git knowledge required.

---

## 4. What You Will Build or Learn

When you finish, your GitHub account will have a real, public repository in it, say recipe-box, whose home page shows a README file with a line of your own writing in it. You can send that page's URL to anyone, and they can open it and see your project.

More importantly, you will genuinely understand what every element on that page means, instead of just clicking through some screenshots and walking away.

---

## 5. What a Repository Actually Is

Let us build the mental model first. A **repository (repo for short) is a project's home.** It looks like a folder, but it can do three things a plain folder cannot:

- **It keeps books.** A plain folder only stores the files as they are right now. A repository also stores the history: what each file used to look like, and who changed it into what it is now, all on the record.
- **It can be shared by many people.** A single repo lets a whole group collaborate, each editing their own part, without stepping on each other's work.
- **It has a URL.** Your repo gets an address like github.com/mariagarcia/recipe-box, and that address is the project's one and only home on the internet.

Here is an analogy. A plain folder is like a desk: you only see what is sitting on it right now. A repository is like a desk with a security camera on it: you can see not just the present, but rewind to any past moment, and even see whose hand moved things around.

One project, one repository. Your recipe project gets a repo, your reading notes project (say my-notes) gets a different repo. They are independent and do not interfere with each other.

---

## 6. What a Commit Is, and Why It Is Central

If a repository is that desk with a camera on it, then a **commit is one key frame in the footage, a save point.**

Whenever you make a meaningful set of changes to the project, you "commit" them, and that act is called a commit. A single commit records three things:

- Which files changed, and exactly what changed in them.
- Who made the change.
- When it happened, plus a one-line note (the commit message) explaining why.

The best analogy is saving a game. You play for a while, beat a boss, and save. If you take a wrong turn later, you can load any save point and start over from there. A commit is a project's save point: once you have committed, that version lives in the history forever, ready for you to revisit or even roll back to.

Here is a detail many beginners miss: **when you check the box Add a README while creating the repository, GitHub automatically makes the first commit for you.** In other words, you are not just creating an empty shell in this lesson, you are also, without quite noticing, making the first commit of your life. The project's history starts keeping books from this very moment. In the next lesson you will make a commit by hand, and that is when you will really see what GitHub did for you here.

---

## 7. What a README Is, and Why You Want One on Day One

README is a file with a name everyone agrees on: it is literally called README (usually README.md). It is the face of the project. When anyone opens your repo, GitHub renders the README right on the home page, like the sign hanging over a shop's door.

A good README answers at least three questions: what the project is for, how to use it, and who maintains it. Even a single line like "Maria's recipe collection" beats a blank page. Making a repo introduce itself from day one is a professional habit.

That is exactly why we strongly suggest checking Add a README when you create the repo: it gives you a face and quietly completes your first commit at the same time, two birds with one stone.

---

## 8. Public or Private

When you create a repo, GitHub asks you to pick a visibility, with two choices:

- **Public:** anyone on the internet can see the repo's contents and history. Note that seeing is not the same as changing, by default others can only look, not edit.
- **Private:** only you and the people you explicitly invite can see it.

How do you choose? A simple rule: if the project itself holds no secrets (passwords, private information, unreleased business content) and you are happy for others to see or even learn from it, go public. Open source projects, learning exercises, and portfolio pieces all use Public.

**In this lesson we choose Public.** The reason is practical: a public repo has a URL you can send to anyone to show off, and it makes the collaboration demos in later lessons easier. Do not worry about safety, there is nothing inside but a README. Just remember one hard line: never put passwords, API keys, or other secrets into a public repo.

---

## 9. Exercises

### Exercise 1: Create your first public repository

**Goal:** create a public repository with a README under your own account.

**How to do it:**

1. Log in to github.com and look at the top right corner. Click the plus sign (+), and in the menu that drops down choose New repository.
2. In the Repository name field, type a name. Use all lowercase with hyphens between words, for example recipe-box. GitHub tells you underneath, in real time, whether the name is available.
3. The Description field is optional, but a one-line summary (like A place to keep my favorite recipes) makes the repo look more polished.
4. Set Visibility to Public.
5. Find the group of options under Initialize this repository with, and check Add a README file.
6. Click the green Create repository button at the bottom.

**What you will observe:**

The page jumps to your new repo's home, with a URL like github.com/your-username/recipe-box. The README's content is shown in the middle. Look above the file list and you will see a line of commit info (usually Initial commit) with the time just now, that is the first commit GitHub made for you.

> **Key insight:** without writing a single line of code, you already own a project that has a history, a face, and a URL. A repository plus its first commit is the complete birth ceremony of a project on GitHub.

### Exercise 2: Find and read the first commit

**Goal:** see for yourself that the auto-generated commit really exists.

**How to do it:**

1. On the repo home page, find the commit line (Initial commit) above the file list. Next to it there is usually a small clock or fork icon with a commit count, like 1 Commit.
2. Click it to open the commit history list.
3. Open that Initial commit and see what it recorded.

**What you will observe:**

You will see that this commit added one README file, tagged with the author (you) and the time. Green lines mark the content that was added.

> **Key insight:** the history starts recording from the very first commit. From now on, every change in the repo gets logged, one after another, and never lost.

---

## 10. Recap: What We Learned

- A **repository** is a project's home: a folder that keeps books, can be shared, and has a URL. One project, one repo.
- A **commit** is the smallest unit of a project's history, like a game save: it records what changed, who changed it, when, and why.
- Checking **Add a README** when creating a repo gives you a face file and completes your first commit at the same time.
- **Public vs private** is a visibility setting: public means anyone can look (but cannot edit by default), private means only you and invitees can see it. If it holds no secrets and you are happy to share, go public.

---

## 11. A Note from Your Mentor

**Why this exercise matters:**

I have watched too many people treat GitHub as "a place to upload files," a cloud drive, and assume that is the end of it. What they miss is precisely GitHub's most valuable part: history. The repo you built today has been keeping books since its first commit, and that book-keeping is the essential difference between it and a cloud drive. A cloud drive only knows what a file looks like right now. GitHub knows its whole life.

**Key insights:**

- The difference between a repository and a folder is not in what it stores, but in what it remembers. It remembers every step.
- A commit is not just "save." It stamps the project's history with a tamper-proof timestamp. That is the bedrock that lets a team trust each other, trace accountability, and roll back.

**Next step:**

Right now your repo holds only a README. In a real project you keep adding files and editing them, leaving a clear commit behind each time. In the next lesson (02, creating and editing files on GitHub) you will do exactly that by hand, and feel what it is like to press commit yourself.

---

## 12. Quick Reference

**Path to create a repo:** top-right + sign -> New repository -> type a name -> set Visibility to Public -> check Add a README -> Create repository.

**Key concepts:**

- `repository`: a project's home, a "folder" that records its entire history.
- `commit`: a save point for one change, recording what changed, who, when, and why.
- `README`: the project's face file, shown on the repo home page.
- `visibility`: Public (anyone can look) or Private (only you and invitees can see).
