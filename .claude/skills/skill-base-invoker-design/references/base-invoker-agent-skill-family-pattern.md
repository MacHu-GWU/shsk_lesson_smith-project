# Base Invoker Agent Skill Family Pattern

A family of skills that share one `<prefix>-base<suffix>` skill. The base holds everything the family has in common. Each invoker skill does one thing: it loads the base, reads the base files it needs, and does its job.

The point is that each shared doc, spec, or script lives in exactly one place, so skills that work together and overlap in context cannot drift apart.

---

## 1. Required rules

Only these are required. Everything else in this document is a recommendation.

- **Naming.** Every skill in the family starts with the same `<prefix>` and ends with the same `<suffix>`. The suffix may be empty. The base is always named `<prefix>-base<suffix>`.
- **The base owns the shared material.** Anything more than one invoker needs lives in the base, not copied into each invoker.
- **An invoker does something.** Each invoker is an action: it states what it does, loads the base, and reads specific base files by path.
- **The base is not bound to an action.** It holds knowledge, specs, scripts, and assets for the whole family. It can be loaded on its own, for example to answer a question about the domain or to decide which invoker fits, but it does not own any single invoker's task.

---

## 2. Naming examples

| Skill | Role |
| :--- | :--- |
| `myproj-base` | base |
| `myproj-plan` | invoker |
| `myproj-build` | invoker |
| `myproj-review` | invoker |

With a suffix, applied to every member of the family:

| Skill | Role |
| :--- | :--- |
| `myproj-base-cn` | base |
| `myproj-plan-cn` | invoker |
| `myproj-review-cn` | invoker |

---

## 3. Recommended layout

```text
<prefix>-base<suffix>/
├── SKILL.md          # mostly an index of what is in this skill
├── references/       # docs, specs, conventions, workflow
├── scripts/          # executable helpers
└── assets/           # templates, schemas, samples
<prefix>-<action><suffix>/
└── SKILL.md          # short: what it does, what to read in the base, local notes
```

`references/`, `scripts/`, and `assets/` are conventions, not requirements. Use whichever the family needs.

---

## 4. What goes in the base, and what stays in the invoker

The test is not "which skill is this most related to". It is **"does any other invoker need to know this?"**

**Base:**

- Shared definitions, specs, conventions, quality bars, output formats.
- Scripts and assets that more than one invoker uses, or that belong to the domain rather than one action.
- **The family workflow.** For example: run `myproj-plan` first, hand its output to `myproj-build`, then `myproj-review`. This looks like it belongs to individual invokers, but every invoker needs it to know who is upstream, who is downstream, and what the handoff looks like. Put it in the base once.

**Invoker:**

- **Its own user experience.** How it talks to the user: what it asks, when it confirms, how it presents results, what it does when input is missing. No other invoker does this the same way.
- Steps and details that only this action needs.
- Anything short and local enough that moving it to the base would only add a hop.

If an invoker needs a shared fact to be different, fix the base rather than overriding it in the invoker.

---

## 5. Recommended SKILL.md shapes

These are starting points. Keep the parts marked essential; the rest is up to the author.

### Base

```markdown
---
name: <prefix>-base<suffix>
description: "Shared knowledge, specs, and scripts for the <prefix> skills: <what it holds>."
---
<What this family is about, in a sentence or two.>

<Essential: an index of the files in this skill and what each one is for.>

<Suggested: which invoker to use for which job, and which base files each invoker reads.>
```

### Invoker

```markdown
---
name: <prefix>-<action><suffix>
description: "<What it does>. Use when <trigger>."
---
<Essential: one sentence on what this skill does.>

<Essential: load the base and read the files this action needs, for example:>
Read ../<prefix>-base<suffix>/SKILL.md, then:
- ../<prefix>-base<suffix>/references/<doc>.md
- ../<prefix>-base<suffix>/references/<doc>.md

Follow those docs to do the work.

<Optional: this invoker's own interaction style, input and output notes, boundaries.>
```

---

## 6. Tips

- **Paths in an invoker are relative to the invoker's own directory**, so they start with `../<prefix>-base<suffix>/`. Move the family together; an invoker copied without its base still loads but no longer shares anything.
- **To run a base script from an invoker**, use `${CLAUDE_SKILL_DIR}/../<prefix>-base<suffix>/scripts/<tool>`. A bare relative path resolves against the shell's working directory, not the skill.
- **Listing the files an invoker reads in both places** (the invoker, and the base index) makes drift easy to spot when the two disagree.
- **When an invoker grows long**, check whether part of it is really shared material that belongs in the base.
- **Not every set of related skills needs this.** One skill, or skills that share only a topic and no actual content, do not need a base.
