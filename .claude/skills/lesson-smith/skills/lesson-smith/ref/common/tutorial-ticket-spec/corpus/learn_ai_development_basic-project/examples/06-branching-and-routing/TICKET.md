---
description: "Get all three scripts running, watch the same pipeline take different paths depending on what the classifier says, and watch with_fallbacks quietly hand off to a backup chain when the primary one blows up."
---

# Teach Your Chain to Branch and Fall Back

## 1. Goal

Your chain has been a straight line so far. This lesson turns it into a graph that can make decisions. You'll get three versions working: a plain if/elif router you write yourself, so the mechanism is out in the open where you can see it; `RunnableBranch`, which moves that routing inside the chain; and `.with_fallbacks([...])`, so one broken chain doesn't take the whole call down with it. When you're done, you should be able to explain what you give up by routing outside the LCEL chain, which is batch, streaming, and end to end tracing, and which of the three you'd reach for in a given situation.

---

## 2. What to Do

1. Read the lesson README all the way through. Before you move on, make sure you can separate the two jobs in your head: deciding what kind of question this is, and deciding what to do about it.
2. Open the `.env` file at the project root and confirm `OPENAI_API_KEY` is set. Then run `example_01_classify_then_route.py` and watch two things: the label the classifier hands back, and which chain actually gets called.
3. Keep feeding 01 new questions until you've hit all three branches, billing, tech, and other. Check every result against the branch you expected before you ran it.
4. Run `example_02_runnable_branch.py` and put it side by side with 01. Find the exact line where `RunnablePassthrough.assign` drops the label into the input dict.
5. Now extend 02. Add a category of your own, shipping works fine, wire up its predicate and its chain, and confirm two things: your new branch gets picked when it should, and the default chain still catches anything that doesn't match.
6. Run `example_03_fallback_chain.py`. The primary chain is a `RunnableLambda` labeled `TEACHING HACK` that throws every single time. Replace it with one that works and confirm the fallback never fires.
7. Give 03 a second fallback, then make the first fallback throw too. See whether LangChain keeps walking down the list until something succeeds.

**Estimated time:** 30 to 45 minutes

---

## 3. Checklist

- [ ] **All three scripts run**: 01, 02, and 03 each run locally and print something.
- [ ] **Every branch reached**: you've hit billing, tech, and other with different inputs, and traced each result back to the label the classifier returned.
- [ ] **The label injection makes sense**: you can point to where `RunnablePassthrough.assign` sits in the pipeline and explain why the predicates are blind without it.
- [ ] **You added a branch yourself**: your own predicate and chain are wired into 02, your branch fires when it should, and the default chain still picks up the leftovers.
- [ ] **You can name the trade off**: you can explain that the hand rolled if/elif version breaks the pipeline into pieces, and once it isn't a single runnable, batch, streaming, and end to end tracing are gone.
- [ ] **Fallbacks actually fire**: you can demo `.with_fallbacks([...])` stepping in when the primary chain throws, with the caller getting a normal result and not a try/except in sight.
- [ ] **You know how the list behaves**: you can explain that fallbacks run one at a time in order, and the exception only reaches the caller after every one of them has failed.
- [ ] **You spotted the teaching hack**: you can explain that the always failing primary chain in 03 is there to make the demo reproducible, and that a real primary chain fails once in a while, not on every call.