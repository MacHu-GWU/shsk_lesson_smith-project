---
description: "You have run at least two practice sessions, you hold a baseline score and a retest score to compare, you can name 1 to 3 weak topics of your own, and you can explain at least 3 core concepts from them without looking at notes."
---

# Use AI Drills to Map Your Blind Spots, Then Close the Weakest Ones

## 1. Goal

This bank holds 264 questions across three tiers and 23 topics, from derivatives pricing all the way out to low latency computing. You're not going to grind through all of it, and you don't need to. What you're after is two things: a map of your own blind spots, and the experience of taking the worst one or two and working them up to where you can talk about them out loud.

That's why the sequence is fixed. Random session first to set a baseline, then dig into one topic, then retest a day later to find out whether anything stuck. Don't skip the random draw. Pick your own questions and you'll pick the easy ones, and the map you walk away with is fiction.

One line worth drawing up front: this bank isn't here to help you memorize formulas for an interview. The bar for having learned something is always whether you can explain it to another person in your own words, and whether you know the conditions under which the model breaks. Plug numbers into a formula and two follow up questions from an interviewer will find you out.

---

## 2. What to Do

1. Spend ten minutes skimming questions-index.md so you have a map of the three tiers and the 23 topics, and know what terrain you're about to work in.
2. Pick your starting tier from your background. New to quant finance, start at E. One or two years in, skim E and spend your time on M. Three years or more, go straight to M and H. If you're not sure, paste your resume or a summary of your projects to the agent and let it recommend a tier and a topic.
3. Run /practice in Claude Code, take the random question, choose interview mode, and answer all six, three multiple choice and three short answer. Write down the score and the feedback. That's your baseline.
4. Sort the questions you missed, and the ones you only half answered, back into their topics. The 1 to 3 topics where you scored under half are your priorities.
5. Run /practice again, this time by topic, pick one of those priorities, and switch to learning mode. Keep asking follow up questions until you can state the concept in your own words.
6. Wait at least a day, then retest that same topic in interview mode and compare against your baseline. The wait is doing real work. Retesting the same afternoon only measures short term memory.
7. Widen the coverage. Run two or three more sessions on topics you haven't touched yet, and make sure you hit all three tiers, not just the one that feels comfortable.
8. Take one concept you just worked out and implement it in Python, Monte Carlo pricing or a VaR calculation, and watch where it falls apart on real data.

**Estimated time:** 20 to 30 minutes per session, spread across 3 to 5 days, 3 to 4 hours in total

---

## 3. Checklist

- [ ] **Both modes exercised**: you've run at least one session in interview mode and one in learning mode, and you know when to stop being tested and start being taught.
- [ ] **Baseline saved**: the score and feedback from that first random interview session are written down somewhere, so later progress has something to measure against.
- [ ] **Weak topics named**: you can name 1 to 3 specific topics where you scored lowest, not just a vague sense that the math is the problem.
- [ ] **The retest moved**: retesting the same topic a day later, you got at least 1 to 2 more questions right than you did on the baseline.
- [ ] **Core concepts explained**: without looking at notes, you can explain at least 3 core concepts, say the assumptions behind Black-Scholes, where VaR stops being trustworthy, or what makes delta hedging work at all.
- [ ] **Failure conditions stated**: for the topic you dug into, you can say under what conditions its model breaks, not just how to run the formula.
- [ ] **Coverage widened**: you've attempted at least one question at each of the three tiers, and you've practiced more than the topic you started on.
- [ ] **One concept implemented**: at least one concept exists as Python you actually ran, not just as a question you read.
- [ ] **A next step exists**: you have a plan for what to practice next, specific down to topic and tier, rather than more of the same.
