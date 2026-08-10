---
description: "Use an AI agent to map your blind spots across 264 quant interview questions, then take the worst one or two and work them until you can say them out loud. Run interview mode for an honest baseline, learning mode to close a gap, and a retest a day later to prove the gain was real, so you end up able to say where a model stops being trustworthy instead of just plugging numbers into it."
---

# Drilling Quant Interview Questions with an AI Agent, from Finding Blind Spots to Explaining Them

> Nobody memorizes 264 model answers. The point is to use an AI agent to find where your knowledge is thin, then close those gaps one at a time.

## 1. Overview

Quant interviews have a habit that catches people off guard. They rarely ask you to define anything, and nobody wants to hear Black-Scholes recited back at them. You get handed a situation instead, and the interviewer watches how you take it apart.

That is difficult to prepare for, because the skill being tested is not the skill that reading builds. You can close a textbook feeling solid on every chapter and still fall apart on a single follow-up, and there is no way to discover that except by getting questioned.

So treat the 264 questions in this bank as diagnostic equipment rather than a syllabus. They span three tiers and 23 topics, from derivatives pricing through low latency computing, but working all the way through them is not the goal and probably never will be. Two or three hours with an agent as a sparring partner, aimed squarely at the things you cannot yet articulate, beats a complete pass. A gap you have measured is more useful than a chapter you have read.

---

## 2. Learning Goals

The default preparation plan is a book, and the appeal is obvious. A book has a last page, so you always know how much is left.

What a book cannot tell you is where you are weak. Working front to back spreads your hours evenly across material you already own and material that will end the interview, and from the inside those two feel identical. That is the failure mode, and it has nothing to do with effort. It is a method with no feedback in it.

An agent supplies the missing feedback. Random draws keep you out of the corner you would otherwise never leave. Follow-up questions reproduce the pressure of a live room at no cost. And when you stall, the tool that just caught the gap is the same one that can close it, before you have had time to talk yourself out of admitting it was there.

By the end of this lesson, you'll be able to:

1. Switch between interview mode and learning mode in `/practice`, and know which one a given moment calls for.
2. Read the feedback from a baseline session and name 1 to 3 specific weak topics, rather than carrying around a vague sense that the math is the problem.
3. Take one weak topic and work it in learning mode until you can state it in your own words, then confirm the gain with a retest a day later.
4. Say why a model holds, where its assumptions break, and what you reach for once they do.
5. Write yourself a next-steps plan that is specific down to topic and tier.

---

## 3. Prerequisites

- Claude Code installed, so slash commands work inside this repo. Section 11 covers the self study route if you do not have it.
- Working comfort with basic probability, statistics, and calculus, or the patience to start at the E tier and build it.
- 20 to 30 uninterrupted minutes per session. The full path takes 3 to 5 days, since one step has to sit overnight.

---

## 4. What You Will Build or Learn

There is no code in this lesson. What you get instead is a map, plus one worked example of how to use it.

The map is your own coverage across the 23 topics: what you know, what you merely recognize, what you have never seen. Measured rather than estimated.

The worked example is taking the darkest square on that map and lighting it up. That process does not change with scale, so once you have done it once, the remaining 260 questions are more of the same, available whenever you want them.

---

## 5. First, Which Kind of Quant Are You Interviewing For

Quant covers a family of jobs that happen to share a word. They screen for noticeably different things, so whichever one you are targeting determines where your hours are best spent.

| Role | What they own | Day to day work |
| :--- | :--- | :--- |
| Quant / financial engineer | Pricing models, risk systems, trading strategies | Derivatives pricing, risk modeling, alpha research, backtesting |
| Quant developer | Getting quant models running in production | C++ and Python pricing libraries, trading systems, data pipelines |
| Quant researcher | Finding new trading signals and strategies | Statistical analysis, backtesting, alpha generation |
| Risk quant | Building and validating risk models | VaR, stress testing, model validation, regulatory compliance |
| Quant trader | Trading with quantitative methods | Market making, statistical arbitrage, execution algorithms |

Everything in this bank sits underneath all five, which is why none of it is wasted no matter which one you are after. What it leaves out is the second layer that targeted preparation needs, the one shaped by a particular firm and asset class. You will have to build that yourself.

---

## 6. What a Quant Interview Actually Tests

A few real questions from the bank:

- Black-Scholes doesn't apply here. How do you price this exotic option?
- Your VaR model is breaching far more often than it should. Where is the problem?
- How do you backtest a strategy without letting look ahead bias in?
- What separates historical simulation VaR from parametric VaR, and when would you pick one over the other?
- Rates have gone negative. What has to change in your model?

Not one of these yields to a formula you memorized. Each one describes a situation and asks for a judgment, which is what the entire interview is doing.

That gives us the standard for the rest of this lesson. Restating a definition proves nothing. Two other things do:

- Can you explain it, in your own words, to someone who has never heard of it?
- Do you know the conditions under which it stops working?

The second carries more weight, and it roughly marks the boundary between junior and senior. Every model is a set of assumptions with math sitting on top. Inside those assumptions it serves you well. Outside them it keeps producing answers at exactly the same confidence, and they are wrong. When an interviewer follows up twice on something, that boundary is usually what they are circling.

---

## 7. The Terrain: Three Tiers, 23 Topics, 264 Questions

Some orientation before you start. The three tiers ask genuinely different kinds of question:

| Tier | Questions | What it asks | Typical shape |
| :--- | :--- | :--- | :--- |
| E (easy) | About 92 | What it is, why it matters | Core concepts, vocabulary, basic mechanics |
| M (medium) | About 88 | How you build it | Implementation detail, patterns that survive production |
| H (hard) | About 84 | Why this choice, what you traded away | Architecture, advanced theory, tradeoff analysis |

The same 23 topics run through all three tiers and the numbering matches across them, so `E-07` and `H-07` are one topic at two depths. Coverage spans derivatives, fixed income, market microstructure, structured products, regulatory frameworks, probability and statistics, stochastic calculus, numerical methods, optimization theory, time series, Python, C++, system design, low latency computing, data engineering, cloud computing, machine learning, alternative data, portfolio construction, risk modeling, backtesting methodology, model validation, and cross domain troubleshooting.

Every question carries a unique ID shaped `{tier}-{topic}-{number}`:

- `E-01-01` is easy tier, topic 01, question 1.
- `M-04-02` is medium tier, topic 04, question 2.
- `H-07-03` is hard tier, topic 07, question 3.

Those IDs are the shared vocabulary between you and the agent. When you want a specific question, say the ID.

The two index files serve different moments. Reach for `questions.md` when you are browsing, since it carries a real description of all 264 and something in it will eventually catch your eye. Reach for `questions-index.md` when you already know what you are hunting for, since it is nothing but IDs and titles sorted by tier and topic.

Question one is a poor default. Start from a tier that matches where you actually are:

| Your background | Where to start |
| :--- | :--- |
| New to quant finance | Start at E and get the foundation solid |
| One or two years in | Skim E, spend your time on M |
| Three years or more | Go straight to M and H |
| A specific target role | Match the tier to that role's seniority |

Not sure? Hand the agent your background and let it choose:

```
Here is my background: [paste your resume or project summary]
Recommend a difficulty tier and topics that fit me.
```

---

## 8. What One Question Looks Like

Each question is a standalone write up living at a path like this:

```
pool/{tier}/{topic}/{question-id}/README.md
```

For example:

```
pool/01-easy/01-derivatives-fundamentals/E-01-01-forward-vs-futures/README.md
pool/02-medium/07-stochastic-calculus/M-07-01-black-scholes-pde/README.md
pool/03-hard/13-system-design/H-13-01-distributed-risk-platform/README.md
```

The skeleton never varies, which tells you where to slow down:

| Section | What it gives you |
| :--- | :--- |
| Interview Question | The question phrased the way an interviewer would phrase it. Answer it before reading on |
| Question Breakdown | What is really being tested, and which points the interviewer is listening for |
| Key Concepts | The groundwork the answer stands on, taken piece by piece |
| Reference Answer | What a strong answer looks like, in structure and in depth |
| Follow-Up Questions | The follow-ups, which is where candidates pull apart from each other |
| Real-World Use Cases | Where this concept has burned people in live markets |
| Recommended Reading | Where to go if you want to push further |

Reading one of these end to end and following all of it feels like learning without being learning. Stop at Interview Question, build your own answer first, and only then read down to the reference.

---

## 9. Two Modes: Interview Tests You, Learning Fills You In

Inside Claude Code, run:

```
/practice
```

The agent starts by asking how you want a question chosen, and there are three ways:

1. Name it yourself with a question ID.
2. Random, drawn from the whole bank.
3. Random within a topic, where you name a topic or tier and it draws inside that range.

Then it asks which mode you want, and the division between those two modes is what this lesson is really about:

| | Interview mode | Learning mode |
| :--- | :--- | :--- |
| What it does | Tests you with 3 multiple choice and 3 short answer questions | Walks you through the write up while you ask questions |
| Pacing | One question at a time, feedback after each | Yours, for as many follow-ups as you want |
| What you get | A score and a list of weak spots | One concept you can actually explain |
| When to use it | You want to find out whether you really know this | You already know you don't |
| What it forces | Saying the answer out loud | Pushing until nothing is fuzzy |

Interview mode earns its keep on the short answer half. Elimination will carry you through multiple choice whether you understand the material or not, but explaining something in your own words has no shortcut, and the agent will name the specific holes in what you said. Nothing else in this repo feels as much like a real interview, and nothing else finds out so quickly that you cannot articulate something you were certain about.

Learning mode rewards persistence. The agent has no patience to lose on your fifth follow-up, which is the one clear advantage it holds over a human mentor, so keep pushing on any corner that still feels soft until you could turn around and teach it.

---

## 10. Three Rules People Skip

The method is not complicated. All of the difficulty lives in three rules, and those three are exactly the ones that get dropped.

**One: the baseline session has to be a random draw.**

Left to yourself, you will choose questions you can answer. Not deliberately. You will simply find yourself drawn toward the topic you half remember, it will go smoothly, and you will come away with a number that describes nothing. Randomizing is the only thing standing between you and a flattering baseline, and a flattering baseline is worse than none at all.

**Two: the retest has to wait a day.**

Testing yourself the same afternoon you studied measures short term memory. The score comes back high and gives you nothing to act on. Put a day between the two and the identical test starts measuring what actually stuck. Spaced repetition is not a scheduling convenience. The interval is the instrument.

**Three: the bar is saying it, not reading it.**

Comprehension while the document is open is the most misleading signal available to you. Close it, try to rebuild the concept from scratch, and you find out how much of that fluency was yours and how much belonged to the page. Nothing counts as finished until you have said it out loud with nothing in front of you.

Put the three together and you have the method. Draw at random for a baseline, close one topic on purpose, retest a day later to confirm it, then move to the next region of the map.

---

## 11. The Self Study Route, No Agent Required

The bank works fine without Claude Code. You just have to do the part the agent would have done for you.

1. Pick a question from `questions-index.md` and note its ID.
2. Find its write up with the path format in section 8, or let `locate_question.py` in the repo root resolve it for you.
3. Stop at Interview Question, write out your own answer, then read on and compare.
4. Answer the Follow-Up Questions too. The real gap is usually hiding down there.

Everything is plain Markdown, so pasting a whole write up into any AI and telling it to play interviewer also works. It takes more effort than `/practice`, but the method underneath is identical: test, close the gap, verify a day later.

---

## 12. Exercises

These four exercises form one connected path, and the middle of it has to sit overnight, so budget 3 to 5 days end to end.

### Exercise 1: Set an Honest Baseline with a Random Draw

**Goal:** Get a starting number you have not quietly flattered.

**How to do it:**

1. Spend ten minutes skimming `questions-index.md` for a rough feel of the three tiers and 23 topics.
2. Pick your starting tier from the table in section 7. If you are unsure, paste your resume to the agent and let it recommend one.
3. Run `/practice` and take the random draw.
4. Choose interview mode.
5. Answer all six questions, 3 multiple choice and 3 short answer, without looking anything up along the way.
6. Save the score and the feedback exactly as they came in. That is your baseline.

**What you'll see:**

Your multiple choice score will almost certainly beat your short answer score. The gap between them is information by itself. It means you recognize these concepts without being able to assemble them into sentences.

> **Key insight:** A baseline is not valuable because of the number. It is valuable because the questions were drawn at random. Take that away and every comparison you make afterward is meaningless.

### Exercise 2: Dig Into One Weak Topic

**Goal:** Take the darkest region on your map and get it to the point where you can talk about it.

**How to do it:**

1. Reread the feedback from exercise 1 and sort the misses, including the half answers, by topic.
2. Pull the 1 to 3 topics where you scored under half, and rank them by how much they matter for the role you want.
3. Run `/practice`, choose random within a topic, and name the one you ranked first.
4. Switch to learning mode and go through the write up alongside the agent.
5. Every time something is fuzzy, ask. Do not let it slide. Push at least as far as the Follow-Up Questions.
6. Close the conversation, look at nothing, and say the concept out loud in your own words.

**What you'll see:**

Step 6 is harder than it sounds. Wherever you stall halfway through a sentence marks the part you never actually absorbed, so go back and keep asking.

> **Key insight:** Follow-up questions are free here. Asking a person the same thing a fifth time costs you something socially; asking an agent costs you nothing, and that advantage is worth spending all the way down.

### Exercise 3: Retest a Day Later and Prove the Gain

**Goal:** Run a controlled comparison instead of trusting how confident you feel.

**How to do it:**

1. Wait at least one day. Do not finish exercise 2 and roll straight into this.
2. Run `/practice`, choose random within a topic, and name the same topic you studied.
3. Choose interview mode and answer all six.
4. Set the new score next to your baseline, paying particular attention to how the short answer feedback changed.
5. Then run two or three more sessions on topics you have not touched, hitting all three tiers instead of only the comfortable one.

**What you'll see:**

If the deep dive worked, your short answer feedback slides from needs improvement toward partially correct or correct, and what the agent flags changes character: the concept is no longer unclear, only the wording is imprecise. That shift tells you more than the score does.

> **Key insight:** Sleeping on it is not a ritual. A same day test and a next day test measure two different things, and only one of them predicts how you will do in the room.

### Exercise 4: Implement One Concept in Python

**Goal:** Move a concept you just worked out off the page and into code that runs.

**How to do it:**

1. From the topic you dug into, pick a concept you can implement. Monte Carlo option pricing and historical simulation VaR both work well.
2. Write it in Python from scratch. No calling a library function that already does it.
3. Feed it a stretch of real market data and run it.
4. Now break one assumption on purpose and run it again. Let volatility vary over time, or swap the return distribution for something fat tailed.
5. Note where the output stops being trustworthy.

**What you'll see:**

Step 4 is the payoff. The clean result a model produces while its assumptions hold looks identical to the clean result it produces after they break. Watch that happen once and model failure boundaries stop being a phrase you repeat.

> **Key insight:** Ask two candidates when a model breaks and you can hear the difference immediately. One of them has broken it.

---

## 13. Recap: What We Learned

- Quant interviews test judgment inside a specific situation, not your ability to recite definitions and formulas.
- Two standards tell you whether you have learned something: you can explain it in your own words, and you know when it stops working.
- The 264 questions are not there to be finished. They are there to measure you. A blind spot you have found beats a chapter you have read.
- Interview mode exposes problems and learning mode solves them. You alternate; you do not pick one.
- The baseline has to be a random draw, or you will pick the softballs and end up with a fictional map.
- The retest has to wait a day, because same day retesting only measures short term memory.
- Implementing something yourself and watching it fall over is the shortest path from knowing about it to understanding it.

Reading a book on quantitative finance leaves you knowing more than you did. Naming your three weakest topics and closing two of them makes you a different candidate. Only the second one shows up in the room.

---

## 14. A Note From Your Mentor

**Why this exercise matters:**

I have watched a lot of people prepare for these interviews. Nearly all of them put in real hours, and the outcomes still vary enormously. The variable is almost never how much they read. It is whether they were willing to get caught out while it was still practice.

Reading alone parks you in a pleasant state of mostly knowing this. That state survives right up until the third follow-up on interview day, and then it does not, and there is no second attempt. What an AI agent really buys you is moving that unpleasant moment into your own living room, where the entire cost is a few minutes of feeling dumb.

**Key insights:**

- Understanding a derivation beats memorizing a formula. Knowing why the Black-Scholes PDE holds is worth far more than being able to plug numbers into it, because follow-ups always push toward the derivation.
- Thinking in tradeoffs beats hunting for a silver bullet. Every model has conditions under which it fails, and knowing when your tools break is frequently the whole difference between senior and junior.
- Building something beats reading about it. This bank is a starting point. The real learning arrives when you implement a model in Python or C++ and then watch it come apart on real data.
- Quantitative finance is far too large to master end to end. Accept that early, then spend your limited hours on the gaps you actually measured instead of spreading them evenly.

**What to do next:**

Make the loop your default rhythm for the next few weeks. One random session, one gap chosen, a deep dive, a retest a day later, then the next gap. Three or four sessions a week at 20 to 30 minutes each is plenty. Give it a month and you will have a map that keeps getting brighter, instead of a stack of chapters you have read.

When you move into targeted preparation, add the layer your target firm calls for. Buy side and sell side ask about different things, and different asset classes go to different depths. What this bank gives you is the foundation underneath all of it, and with that solid, the extra layer goes quickly.

---

## 15. Quick Reference

**Starting a session:**

```
/practice
```

**Three ways to pick a question:** give a question ID, take a random draw, or draw at random inside a topic.

**Two modes:** interview mode (3 multiple choice and 3 short answer, with feedback and a score), learning mode (your pace, ask anything).

**Question ID format:** `E-XX-XX` for easy, `M-XX-XX` for medium, `H-XX-XX` for hard.

**Write up path:**

```
pool/{tier}/{topic}/{question-id}/README.md
```

**Key files:**

- `questions.md`: the full outline, with a real description of all 264 questions.
- `questions-index.md`: the lookup table, organized by tier and topic.
- `locate_question.py`: resolves a question ID to its write up path.
- `pool/`: the root of every write up.

**One standard session:** 20 to 30 minutes, 3 multiple choice and 3 short answer, read the feedback, write down the weak topics, come back in a few days.