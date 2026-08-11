# Spec for docs/showcase/04-showcase-demo.md (English)

**Scope**: the file `docs/showcase/04-showcase-demo.md` in a showcase repo. Written by `lesson-smith-showcase-forge`, read by the `showcase-demo` skill.

**Skeleton**: [docs-showcase-demo-template.md](docs-showcase-demo-template.md).

**Not generated at the moment**: forge emits the `-cn` set only, per [docs-showcase-demo-cn-spec.md](docs-showcase-demo-cn-spec.md). This spec and its skeleton stay put, ready for the multi-language module to pick up.

---

## 1. What this file is

**A pointer, not a story.** The script itself, all seven beats of it, the follow-up questions, and the audience notes, lives in the README of the demo task, specified in [showcase-demo-readme-spec](../../showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md). That link points at the Chinese spec on purpose: the script is course content a learner reads, so it only exists in `-cn` today, and its English counterpart lands with the multi-language module.

This file does three things: it says **where the script is**, it keeps **a one-line-per-beat copy of the default arc** so the skill does not have to reconstruct it every session, and it records **how the author wants rehearsals run**.

---

## 2. The three sections

**Where the script lives.** A markdown link to the README of the demo task. forge finds it **by name, not by position**: `NN-how-i-build-this` sits after the quiz, but a wrap-up task follows it, so it is not the last thing under `examples/`.

**The default arc.** The seven beats, one line each. The default story is the method itself, how the author used AI to learn a skill quickly and put it to work, which doubles as the narrative and as evidence they can work with AI.

If this repo's script departs from the default, say where in one line. If it does not, say so explicitly rather than leaving the reader to assume.

**Rehearsal preferences (optional).** Whatever the author wants done differently: who the default audience is, how long a slot to rehearse for, which beats need the most work, how hard the pushback should be.

---

## 3. House rules

- **Never copy the whole script here.** Two copies drift apart, and the script is the one that gets rehearsed. Pointer, skeleton, and preferences only.
- Link to files with markdown links, locating by header or keyword rather than line number.
