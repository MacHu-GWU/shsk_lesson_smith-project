---
name: skill-base-invoker-design
description: "Design, scaffold, extend, refactor, or review a family of Agent Skills built as one <prefix>-base skill that holds the shared docs, scripts, and assets, plus invoker skills that each load the base and do one job."
argument-hint: "[prefix and what the family should do | path to an existing family]"
---
Target: $ARGUMENTS

Read references/base-invoker-agent-skill-family-pattern.md first. It defines the pattern, the few required rules, what belongs in the base versus an invoker, and recommended SKILL.md shapes. Everything below assumes you have read it.

## Pick the job

Work out which of these the target asks for. If no target is given, ask for the prefix and what the family should do.

- **New family.** Before writing any file, propose the prefix, the suffix (often empty), the list of invokers with one line each, and a rough split of what goes in the base. Get the user's confirmation. Names end up in every relative path across the family, so changing them later means touching every file.
- **Add an invoker.** Read the existing base SKILL.md and the base files the new job touches. Reuse what is there. Add to the base only what is new and needed by more than this one invoker, and update the base index to match.
- **Refactor** existing skills into a family. Read all of them, list the material that appears in more than one, and show the user the proposed split before moving anything. Then move the shared material into the base and cut each skill down to an invoker.
- **Review** a family. Check it against the required rules, then look for shared material that lives in more than one place, base files no invoker reads, and invoker paths that do not resolve. Report findings; change files only if the user asks.

If the request does not fit the pattern (one skill on its own, or skills that share a topic but no actual content), say so and suggest writing ordinary skills with `/dot-claude:author-agent-skill` instead.

## Build order

Write the base before the invokers: its files first, then its SKILL.md index, so the index describes files that exist and every invoker path points at something real. Then write each invoker.

For frontmatter fields and other SKILL.md details, consult ../author-agent-skill/references/extend-claude-with-skills.md when you need them. If the base bundles a Python CLI script, it must follow ../author-agent-skill/references/python-cli-script-standard.md.

## Finish

Check that every `../<prefix>-base<suffix>/...` path in every invoker resolves. Then show the user the resulting tree and, for each invoker, which base files it reads.

Default location is `<project>/.claude/skills/`. Never write to `~/.claude/` unless the user asks for it explicitly.
