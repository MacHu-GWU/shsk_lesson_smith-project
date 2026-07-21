# GitHub Collaboration Basics Learning Index

> What there is to learn in this course, where it lives, and in what order to go through it. The showcase-learn skill walks you along this index.

## 1. Study Material

This is a read-and-do course: the tutorials themselves are the thing to learn, and everything lives in the `examples/` progression. There is no separate source code, config, or side documentation to study.

- No extra study material outside the guided path — it is all in the six mini tasks under [examples/](../../examples/README.md). The only thing you bring from outside is your own GitHub account, which you practice on directly in the browser.
- Gotcha: [mise.toml](../../mise.toml) at the repo root is only a project-root marker for tests, not a real toolchain. There are no `mise` tasks to run for this course; do not go looking for build or setup commands there.

## 2. Guided Path

The examples/01, 02 ... progression is the path the student walks. The trailing quiz and demo tasks are handled by their own skills. The whole line breaks into three stretches:

- **Set up your repository**: examples/01 to examples/02 — create a repository from scratch and record every change with a clean commit. Covers repository, commit, README, public vs private, the web editor, commit messages, and commit history.
- **Branches and Pull Requests**: examples/03 to examples/04 — the heart of collaboration: isolate unfinished work on a branch, then merge it back into main through a reviewed Pull Request. Covers branch, the default branch main, Pull Request, code review, merge, deleting a merged branch, and merge conflicts.
- **Prove it and tell it**: examples/05 to examples/06 — an interview-style self-test that checks you know both the how and the why, then the story script for telling how you built this (handled by showcase-quiz and showcase-demo).

See the [examples theme index](../../examples/README.md) and the [SYLLABUS](../tasks/SYLLABUS.md).
