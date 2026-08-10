# Vercel Basics Series Index

This course teaches you how to ship a website on Vercel, change it safely, and track down what went wrong when something breaks. It's deliberately narrow: it covers the platform itself, not how to write the frontend or backend code that runs on it. Reading it end to end and doing the exercises takes about three to four hours.

The seven lessons below are grouped into four blocks. The first lays the groundwork: what problem this platform actually solves, plus what to do when this tutorial eventually goes stale. The second is the main line — three hands-on lessons that take you through shipping, changing, and troubleshooting, one at a time. The third is a self-check that tests whether any of it actually stuck. The fourth wraps up: it helps you place where you stand and pick your next move.

Read them in order. Later lessons build directly on what earlier ones produced, so skipping ahead will leave gaps.

## 1. First, Understand the Problem You're Solving

There's no hands-on work in this block, but it decides whether everything after it is real understanding or rote memorization.

- [01-why-vercel](01-why-vercel/README.md): shipping a website used to mean clearing a dozen hurdles, and Vercel spent ten years eating through them one layer at a time. By the end you'll know exactly where this course draws its boundaries, and you'll have a ready-made prompt for the day the screenshots stop matching what you see.

---

## 2. The Main Line: Ship, Change, Troubleshoot

Do these three lessons back to back — each one's output is the next one's starting point. By the end you'll have an actual website live on the internet.

- [02-sign-up-vercel](02-sign-up-vercel/README.md): create an account. Along the way, work out two things — where the free tier's limits actually sit, and why account independence matters — both are the kind of mistake you don't notice until much later.
- [03-deploy-your-first-app](03-deploy-your-first-app/README.md): push a website live from a ready-made template and get a public URL. The real point is understanding the one-way pipeline that carries code from GitHub to Vercel — the next two lessons both build on it.
- [04-deployment-environment-and-git-branch](04-deployment-environment-and-git-branch/README.md): the densest lesson in the whole course. You branch, change code, verify it in Preview, confirm Production hasn't budged, then merge and release. This is the exact workflow professional teams run every single day.
- [05-view-logs](05-view-logs/README.md): where to go looking for clues when something breaks. One question — can the site even load? — tells the two kinds of logs apart, and from there you turn raw logs into a question an AI can actually act on.

---

## 3. Check Whether It Actually Landed

- [06-prove-i-get-it](06-prove-i-get-it/README.md): thirty scenario questions, all drawn from situations you'll genuinely run into. None of them test where a button lives — they test judgment and good practice. Each one comes with a reference answer and a deeper explanation, and if you can't answer it, the source link sends you back to fill the gap.

---

## 4. Wrapping Up and Where to Go Next

- [07-where-to-go-next](07-where-to-go-next/README.md): spells out what you're actually leaving with — a way of working that has nothing to do with how big the project is. It draws an honest line around what you still can't do, sorts out which parts of debugging you can hand to AI and which one you can't, then hands you eight directions to grow in, each one with search terms and a prompt ready to copy.

---

## 5. In Closing

Finish the whole line and you move from being able to build something nobody else can see, to being able to ship it, change it safely, and stay calm when it breaks. That wall stopped countless people ten years ago. Now you get to walk right past it.

What outlasts the tutorial is a handful of mental models. Complexity never disappears, it only moves. An immutable instance plus a single pointer gives you version switching that's both safe and reversible. An isolated space that gets merged back into the main line is the general pattern for iterating safely. And in the age of AI, knowing where to find the evidence is worth more than knowing how to analyze it.

One last thing to remember: the screenshots in this tutorial will eventually stop matching what you see on screen, but the underlying logic won't change. The [official Vercel documentation](https://vercel.com/docs) is the final word — and if you can't find the answer there, screenshot it and ask an AI.
