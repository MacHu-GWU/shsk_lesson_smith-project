# Vercel Basics Series Index

This course gets a website of yours onto the internet, teaches you to change it without breaking it, and shows you how to find out what happened when it breaks anyway. It is about the platform and nothing else. Writing the frontend or backend code that runs on Vercel is somebody else's tutorial. Budget three to four hours to read it through and work the exercises.

Seven lessons in four blocks. The first block is background, including what to do on the day this tutorial goes out of date. Then comes the main line, four hands-on lessons that put a site online, change it, and debug it. After that, thirty questions to find out what actually stuck. The last block tells you where you stand and what to reach for next.

Do them in order. Later lessons use what earlier ones produced, so jumping around costs more time than it saves.

## 1. What Problem Is This Actually Solving

You will not touch a keyboard in this block. Skip it anyway and everything after it turns into steps you follow without knowing why you are following them.

- [01-why-vercel](01-why-vercel/README.md): Getting a website online used to take a dozen separate steps, and most of them had nothing to do with the website. Vercel spent ten years absorbing them one layer at a time. You come out of this lesson knowing where the course stops and you are on your own, and holding a prompt to use on the day the screenshots here stop matching your screen.

---

## 2. The Main Line: Ship It, Change It, Fix It

These four run as one sequence. Each lesson leaves behind something the next one needs, so do not shuffle them. At the end there is a real site, live, that anyone with the link can open.

- [02-sign-up-vercel](02-sign-up-vercel/README.md): Signing up takes two minutes. The two decisions buried inside it deserve longer than that: how much the free tier actually gives you before it stops, and whose account this should live under. Neither one costs you anything today, which is exactly why people get them wrong.
- [03-deploy-your-first-app](03-deploy-your-first-app/README.md): Deploy a working site from a template and get a public URL for it. The URL is the fun part. The pipeline underneath is the part that matters: code moves from GitHub to Vercel, and only in that direction. Lessons 04 and 05 both assume you have that picture in your head.
- [04-deployment-environment-and-git-branch](04-deployment-environment-and-git-branch/README.md): The heaviest lesson here, and the one worth slowing down for. Open a branch, change something, watch it show up in Preview while Production sits there untouched, then merge and ship it. This is not a teaching exercise. It is what professional teams do every day of the week.
- [05-view-logs](05-view-logs/README.md): Something broke and you need evidence. One question decides where to look: does the page load at all? The answer tells you which of the two kinds of logs holds your clue. The lesson finishes by turning a wall of log output into a question an AI can actually work with.

---

## 3. Find Out What Stuck

- [06-prove-i-get-it](06-prove-i-get-it/README.md): Thirty scenarios, all of them things that will genuinely happen to you. None of them ask where a button lives. They ask what you would do. Every one comes with a reference answer and a longer explanation, and when a question stumps you, the link under it points straight back at the lesson you need.

---

## 4. Where This Leaves You

- [07-where-to-go-next](07-where-to-go-next/README.md): Names the thing you are actually taking with you, which is a way of working that does not care whether the project is a weekend toy or a company. It is just as honest about the gaps, including which parts of debugging you can hand to an AI and the one part you cannot. Then eight directions to go from here, each with search terms and a prompt you can paste.

---

## 5. In Closing

There is a gap between something that runs on your laptop and something other people can actually use, and ten years ago that gap stopped most people cold. You just crossed it. You can put a site on the internet, change it without holding your breath, and open the logs instead of guessing when it misbehaves.

The clicking you will forget within a month. A few of the ideas will stay with you. Complexity does not disappear when a platform hides it, it just relocates to somewhere you are not looking. Releases can be both safe and reversible because the thing you built never changes and only the pointer to it moves. Risky work belongs somewhere isolated until it has proven itself, and then it comes back to the main line, a pattern that is older than Git and much bigger than Vercel. And now that AI can do most of the analysis for you, the scarce skill is knowing which log to open in the first place.

The screenshots in here will drift out of date and the interface will move around, and none of that touches the logic underneath. When this tutorial and [Vercel's own docs](https://vercel.com/docs) disagree, the docs win. When the docs do not cover it at all, screenshot the problem and ask an AI.