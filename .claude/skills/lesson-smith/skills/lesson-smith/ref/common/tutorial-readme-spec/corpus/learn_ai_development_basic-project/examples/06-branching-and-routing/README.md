---
description: "Turn a straight-line chain into one that makes decisions. Route input to a specialized chain with RunnableBranch instead of a hand-rolled if/elif, understand what you give up by keeping control flow outside LCEL, and use with_fallbacks to keep a failed call from killing the request."
---

# Branching and Routing: Growing if/else Into Your Chain

> Your pipeline stops being a straight line in this lesson. A classifier looks at the input first, the request goes to whichever chain specializes in that case, and if the primary chain blows up, a backup takes over without the caller ever knowing.

## 1. Overview

Lessons 04 and 05 gave you pipelines that run start to finish in one direction. One input, a fixed sequence of steps, one output. That shape holds up right until real traffic shows up.

Think about how a support bot actually works. A question comes in and the first decision is what kind of question it is. Billing goes one way, a bug report goes another, and whoever handles it was written for that case and nothing else. Most of those single-purpose GPTs in the ChatGPT store work the same way. What looks like one assistant that can do anything is usually a router with a handful of narrow experts sitting behind it.

This lesson builds that up in three stages. First you write the routing by hand in Python, where every moving part is visible. Then `RunnableBranch` pulls the same logic back inside the chain. Then `.with_fallbacks([...])` gives the pipeline somewhere to go when a call fails.

---

## 2. Learning Goals

Start with why this is worth your time.

Real users do not ask tidy questions. In the same hour you will get a dispute over a credit card charge, a stack trace, and someone asking whether you are hiring. No single prompt serves all three well. Sharpen it for billing and it turns wordy about bugs. Load it up with troubleshooting instructions and it starts answering casual questions like a Jira ticket. Every edit that helps one case quietly damages another, and you find yourself negotiating with your own prompt.

Routing ends that negotiation. Write a short, narrow prompt per case and let a classifier pick which one runs.

Fallbacks cover the other way things go wrong. Calls fail in production. Quotas, timeouts, malformed output, a provider having a bad afternoon. Wrapping every step in try/except is not a plan, especially when the failure can surface at any depth in the pipeline. Put routing and fallbacks together and you get a chain that survives contact with users instead of one that only holds up in a demo.

By the end of this task, you'll be able to:

1. Separate classification from routing, and wire both by hand with a plain if/elif.
2. Express the same routing as `RunnableBranch` so the pipeline stays a single runnable end to end.
3. Explain why `RunnablePassthrough.assign` has to run before the branch, and what the predicates see without it.
4. State the cost of keeping control flow outside LCEL: no batching, no streaming, no single trace.
5. Attach a backup chain with `.with_fallbacks([...])` and predict the order a list of them runs in.

---

## 3. Prerequisites

- Lessons 04 and 05 done. You can build a chain with `|` and you have used `RunnablePassthrough.assign` at least once.
- `OPENAI_API_KEY` set in `.env` at the project root, and the earlier scripts running under `uv run python`.
- Comfort with how Python raises and catches exceptions.

---

## 4. What You Will Build or Learn

Three scripts, all short enough to read in one sitting and structured so you can edit them in place. Between them you get a routing skeleton that is close to production shape: a classifier, three specialist chains, a `RunnableBranch` that binds them into one runnable, and a fallback layer for when the primary dies.

The code is the smaller half of the lesson. The larger half is a design question you will keep running into: does Python own the control flow, or does LCEL? Both answers work today. They cost very different amounts a year from now, and you pick one the moment you write the first line.

---

## 5. The Hand-Rolled if/else Version: See the Mechanism First

Start with the version that hides nothing. A classifier chain labels the question, and ordinary Python decides where it goes.

```python
classify_chain = classify_prompt | model | parser  # outputs "billing" / "tech" / "other"

billing_chain = billing_prompt | model | parser
tech_chain    = tech_prompt    | model | parser
default_chain = default_prompt | model | parser

def route(input_dict):
    label = classify_chain.invoke(input_dict).strip().lower()
    if "billing" in label:
        return billing_chain.invoke(input_dict)
    if "tech" in label:
        return tech_chain.invoke(input_dict)
    return default_chain.invoke(input_dict)
```

Notice how little separates the three specialists. Same model, same parser, different system prompt. One is an agent on the billing team, one is a support engineer who leads with a concrete thing to try, one is a friendly generalist. That is what you are really buying with routing. Persona, tone, and length budget stop being compromises and become per-branch decisions.

Now look at the label handling. The classifier hands back free text, not an enum. You asked for one lowercase word and most of the time that is what you get, but sooner or later `Billing.` or `tech support` comes through instead. Hence `.strip().lower()` and the substring test rather than `==`. Every LLM-as-classifier setup deals with some version of this. Structured output from lesson 03 is the durable fix; this is the cheap one, and it is fine for three categories.

The upside of writing it this way is that nothing is hidden. Drop a print statement wherever you are curious. The downside is that the routing lives outside LCEL, so the pipeline as a whole is no longer a runnable. It is a Python function with runnables buried in it, which means no batching over the full pipeline, no streaming through the branch, and a trace that arrives as scattered fragments instead of one story.

Read this version carefully anyway. `RunnableBranch` only looks like an improvement if you already know what it is improving on.

See [example_01_classify_then_route.py](./example_01_classify_then_route.py) for the full demo.

---

## 6. RunnableBranch: Turning if/else Into a Runnable Too

`RunnableBranch` is the same if/else, expressed as something the chain can hold. Give it `(predicate, chain)` pairs and one bare chain at the end:

```python
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

branch = RunnableBranch(
    (lambda d: "billing" in d["label"].lower(), billing_chain),
    (lambda d: "tech" in d["label"].lower(),    tech_chain),
    default_chain,  # the default branch goes last, and it is not a tuple
)
```

Evaluation is top to bottom and stops early. Each predicate gets the current input, **the first truthy result wins**, its chain runs, and nothing below it is ever evaluated. The trailing item has no predicate because it is the catch-all. LangChain requires it, and it has to be last.

There is a gap to close, though. Those predicates want `d["label"]`, and nothing has produced a label yet. Computing a value and folding it into the input dict is precisely what `RunnablePassthrough.assign` did in lesson 05, so it slots in ahead of the branch:

```python
pipeline = (
    RunnablePassthrough.assign(label=classify_chain)  # drop label into the input dict
    | branch                                          # then route on it
)
```

Trace one request through and the shape becomes obvious:

| Stage | What the data looks like |
| :--- | :--- |
| Input | `{"question": "Why was I charged twice this month?"}` |
| After assign | `{"question": "...", "label": "billing"}` |
| Predicates | `"billing" in label` hits on the first try, so the others never run |
| Chosen chain | Gets the entire dict; its prompt only reads `{question}` and ignores `label` |
| Output | Whatever the billing chain answered |

That fourth row matters more than it looks. Nothing gets trimmed on the way down. Keys you assign early are still available late, and prompts silently skip whatever they do not reference. Once you internalize that, passing state through a long chain stops feeling like plumbing.

With both versions in front of you, the tradeoff is easy to state:

| Dimension | Hand-rolled if/elif | RunnableBranch |
| :--- | :--- | :--- |
| Where routing lives | A Python function outside LCEL | Inside the chain |
| What the pipeline is | A function with runnables inside it | A runnable |
| Batching and streaming | Only per downstream chain | `.batch()` and `.stream()` on the whole thing |
| Tracing | Several disconnected calls | One trace, branch included |
| Reuse in a bigger chain | Wrap it in `RunnableLambda` first | Compose with `\|` |
| Learning curve | Lowest, print anything | Predicates receive the whole dict, which takes getting used to |

The finished `pipeline` behaves like any other runnable. Invoke it, batch it, stream it, or drop it whole into something larger. That consistency is the entire design bet LangChain is making: **everything is a runnable, and runnables compose with `|`**.

See [example_02_runnable_branch.py](./example_02_runnable_branch.py) for the full demo.

---

## 7. Fallback Chains: An Automatic Backup When the Primary Breaks

Rather than defending against failure call by call, declare what should happen instead:

```python
chain_with_fallback = primary.with_fallbacks([fallback])
```

If `primary` raises, LangChain swallows the exception, runs `fallback`, and returns its result. As far as the caller is concerned, nothing went wrong. Pass more than one and they are tried in sequence, so `.with_fallbacks([fallback_a, fallback_b])` only lets an exception escape after both have failed.

A useful fallback is almost always a downgrade you chose on purpose. Three patterns cover most cases. Drop to a smaller, cheaper model that is less likely to be throttled. Drop to a looser prompt that asks for less structure and therefore fails less often. Or stop trying and return prepared text, so the user reads a sentence instead of staring at a 500.

Script 03 needs the fallback to fire on every run, so **the primary is a `RunnableLambda` that raises unconditionally**, marked with a loud `TEACHING HACK` comment. Production code puts a real LLM chain in that slot, failure is rare, and the backup stays asleep until it is needed. The wiring around it is identical either way, which is the reason the script is worth reading despite the fake primary.

Keep one limit in mind. Fallbacks react to exceptions and nothing else. A call that succeeds and returns garbage looks exactly like a call that succeeded. Catching bad answers is the job of validation, scoring, or a retry loop, so do not expect `.with_fallbacks([...])` to cover it.

See [example_03_fallback_chain.py](./example_03_fallback_chain.py) for the full demo.

---

## 8. How to Run

Nothing new here. Confirm `OPENAI_API_KEY` is set in `.env`, then run from the project root:

```bash
uv run python examples/06-branching-and-routing/example_01_classify_then_route.py
uv run python examples/06-branching-and-routing/example_02_runnable_branch.py
uv run python examples/06-branching-and-routing/example_03_fallback_chain.py
```

Scripts 01 and 02 print the question, then the answer. Script 01 also prints a `[classified as: ...]` line so you can see the label the routing acted on.

---

## 9. Exercises

### Exercise 1: Hit All Three Branches

**Goal:** Watch classification and routing behave as two separate steps.

**How to do it:**

1. Run `example_01_classify_then_route.py`. For each of the three built-in questions, compare the `[classified as: ...]` line against the tone of the answer below it.
2. Swap in three questions of your own: one clearly about billing, one clearly technical, one unrelated to your product.
3. Add a fourth that straddles two categories on purpose, something mentioning both a payment and an error message, and see what the classifier does with it.

**What you'll see:**

The three clear cases land on the same branch every time. The ambiguous one wobbles. Run it repeatedly and the label may change between runs, with the answer style following right behind.

> **Key insight:** The classifier sets the ceiling for the whole route. Excellent specialist chains are wasted on a bad label, which is why the classification prompt deserves the most care.

### Exercise 2: Add a Branch of Your Own

**Goal:** Go from reading `RunnableBranch` to changing it.

**How to do it:**

1. Open `example_02_runnable_branch.py` and locate the `RunnablePassthrough.assign` line. Confirm for yourself that this is where the label enters the dict.
2. Teach the classifier a new category in its system prompt. `shipping` works well.
3. Build a `shipping_chain` with a logistics support persona.
4. Add its `(predicate, chain)` tuple to `RunnableBranch`, above `default_chain`.
5. Send a shipping question to confirm your branch fires, then send something unrelated to confirm the default still catches it.

**What you'll see:**

The new branch works immediately and nothing else in the pipeline needed touching. Put the tuple after `default_chain` and LangChain complains on construction, since the default has to sit last.

> **Key insight:** One new branch, two edits: the classifier prompt and the tuple list. That low cost of change is exactly what you bought by moving control flow into the chain.

### Exercise 3: Remove the Teaching Hack, Then Stack Two Fallbacks

**Goal:** Establish what actually triggers a fallback and what order a list runs in.

**How to do it:**

1. Run `example_03_fallback_chain.py`, verify the answer came from the fallback, then find the `TEACHING HACK` block.
2. Replace the always-raising `RunnableLambda` with a chain that works. Run again and confirm the fallback stays out of it.
3. Restore the raising primary, add a second fallback, switch to `.with_fallbacks([fallback_a, fallback_b])`, and make `fallback_a` raise too.
4. Add a print to all three chains and watch the order they fire in.

**What you'll see:**

Step 2 produces silence from the fallback, because nothing raised. Step 3 prints primary, then `fallback_a`, then `fallback_b`, and the value you get back came from `fallback_b`.

> **Key insight:** A fallback list is a degradation path, not a race. Each entry should be simpler and more reliable than the one above it, and the last one ideally does not depend on any external service.

---

## 10. Recap: What We Learned

- Classification and routing are separate jobs. One produces a label, the other picks a chain from it.
- Hand-rolled if/elif is the most readable option and it costs you the single-runnable property, because the routing sits outside LCEL.
- `RunnableBranch` takes `(predicate, chain)` tuples plus a bare default. First truthy predicate wins; the default goes last.
- `RunnablePassthrough.assign` computes the label and folds it into the input dict. Skip it and the predicates have nothing to read.
- The whole input dict flows down to the chosen chain, and unused keys are ignored.
- `.with_fallbacks([...])` runs backups in order when the primary raises, and only surfaces the exception once every one of them has failed.
- Fallbacks respond to exceptions only. A successful call with a bad answer sails right through.

---

## 11. A Note From Your Mentor

**Why this exercise matters:**

This is where your project starts to resemble a system. A chain used to be a line from input to output. Systems are graphs. They choose, they split, and they have a plan for the moment something breaks.

If you keep one thing from this lesson, make it the comparison in sections 5 and 6. Both versions work and you could defend either one in an interview. Only one of them lets you add batching next quarter without rewriting the middle, or wire up tracing in an afternoon, or nest the whole thing inside a larger agent. Frameworks rarely pay off on the day you adopt them. They pay off on the day the requirements move.

**Key insights:**

- Giving control flow to the framework buys composability, and composability is the thing all of LCEL is organized around.
- Every mistake the classifier makes is inherited by everything downstream, so that prompt earns the most attention.
- Fallbacks belong in the design, not in a patch. Deciding what happens when a step dies is far cheaper before it dies.
- The always-failing primary stands in for a real outage. You are practicing the wiring, not the lambda.

**What to do next:**

Find the prompt in your own project that has been stretched to cover every case, and split it into a classifier plus two or three specialists. The usual result surprises people: each branch prompt ends up shorter than the original, and the answers get better.

---

## 12. Quick Reference

**Running this lesson:** `uv run python examples/06-branching-and-routing/example_01_classify_then_route.py`, swapping `01` for `02` or `03`.

**The three APIs:**

- `RunnableBranch((pred, chain), ..., default_chain)`: if/else inside a chain. First truthy predicate wins, default goes last.
- `RunnablePassthrough.assign(label=classify_chain)`: adds a computed key to the input dict and leaves everything else alone.
- `primary.with_fallbacks([fallback_a, fallback_b])`: tries backups in order when the primary raises, reraising only after all of them fail.

**Key files:**

- `example_01_classify_then_route.py`: routing by hand, with classification and dispatch visibly separate.
- `example_02_runnable_branch.py`: `RunnableBranch` and `RunnablePassthrough.assign` keeping the pipeline a single runnable.
- `example_03_fallback_chain.py`: `.with_fallbacks([...])`, with a primary that fails on purpose and admits it in a `TEACHING HACK` comment.

Your chain can now choose its own path. Lesson 07 goes the other direction and makes a chain do several things at once: `RunnableParallel` for concurrent branches, splitting long input into chunks that get processed in parallel and merged back together (map-reduce), and the shift from sequential steps to parallel work plus aggregation.