# Spec for docs/{{TYPE}}/03-{{TYPE}}-quiz.md (English)

**Scope**: the file `docs/{{TYPE}}/03-{{TYPE}}-quiz.md` in an {{TYPE}} repo. Written by `lesson-smith-{{TYPE}}-forge`, read by the `{{TYPE}}-quiz` skill.

**Skeleton**: [docs-quiz-template.md](docs-quiz-template.md).

**Not generated at the moment**: forge emits the `-cn` set only, per [docs-quiz-cn-spec.md](docs-quiz-cn-spec.md). This spec and its skeleton stay put, ready for the multi-language module to pick up.

---

## 1. What this file is

**A pointer, not a quiz.** No questions are written here.

The questions, what each one probes, the reference answers, and the deep dives all live in the README of the quiz task, specified in [11-quiz-readme-spec](../../11-quiz-readme-spec/quiz-readme-cn-spec.md). That link points at the Chinese spec on purpose: the bank is course content a learner reads, so it only exists in `-cn` today, and its English counterpart lands with the multi-language module.

This file does two things: it says **where the bank is**, and it records **how the author wants the quiz run**.

The two are written for different readers. The bank is course content a learner reads; this pointer is a meta file only the skill reads. They follow different language rules for that reason.

---

## 2. The two sections

**Where the bank lives.** A markdown link to the README of the quiz task, so `{{TYPE}}-quiz` knows where to read from. forge finds it by the fixed directory name `NN-prove-i-get-it`. One sentence naming the task, plus the number of questions it holds.

**How to run the quiz (optional).** Whatever the author wants done differently: how many questions to draw by default, whether to group by topic, which areas to weight, what tone to take, whether there is a time limit, where the pass mark sits.

When the author has no preferences, say so in one line rather than leaving the section blank.

---

## 3. House rules

- **Never copy questions into this file.** Two copies of a question drift apart, and the bank is the one that is graded against. Pointers and preferences only.
- Link to files with markdown links, locating by header or keyword rather than line number.
