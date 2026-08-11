# Spec for docs/<type>/02-<type>-runbook.md (English)

**Scope**: the file `docs/<type>/02-<type>-runbook.md` in an <type> repo. Written by `lesson-smith-<type>-forge`, read by the `<type>-learn` skill.

**Skeleton**: [docs-runbook-template.md](docs-runbook-template.md).

**Not generated at the moment**: forge emits the `-cn` set only, per [docs-runbook-cn-spec.md](docs-runbook-cn-spec.md). This spec and its skeleton stay put, ready for the multi-language module to pick up.

---

## 1. What this file is

**The operations manual for the course.** It covers one thing only: how to get the material running.

- It does not teach. The teaching is in `examples/` and in the material itself.
- It does not index. That is what `01-<type>-learn.md` is for.

---

## 2. The point of the file

**Spell out the steps an experienced hand performs without thinking.**

Someone who built the course knows from the directory layout which directory to work in and which command comes first, so they rarely say it out loud. A student following along stalls on exactly those steps. Anything in the category of "never written down but required" belongs here.

If this file does not save someone a stall, it is not earning its place.

---

## 3. The two halves

**First, the one-time setup that comes before the first task**: required tools and versions, and the commands to run once. Most of these already live in `mise.toml` under tasks and tool versions. **Copy them verbatim rather than paraphrasing.**

**Second, the operations that come up along the way**: anything involved in getting an example running. Changing directory, exporting environment variables, starting a service, and the steps that leave the terminal entirely, such as signing up for an account or flipping a setting in a browser.

**Keep it short.** When the tasks simply advance one after another with nothing extra to do, a sentence or two on the general pattern is enough. Only the places that break the pattern deserve to be called out by name.

---

## 4. House rules

- **Commands must run exactly as written.** Copy them; do not paraphrase or tidy them up.
- Link to files with markdown links, locating by header or keyword rather than line number.
- **Keep empty sections and say they are empty** (for example "none yet, fill this in as they come up"). Deleting the heading hides the fact that nobody has checked.
