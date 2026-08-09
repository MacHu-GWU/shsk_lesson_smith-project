---
name: lesson-smith-readup-author-step-09-wrap-cn
description: "第 9 步: 写四份全局文档的中文版 (examples 索引, 根 README, 根 TICKET, README-ORIGINAL)"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# readup 创作流 第 9 步

你在 **readup 创作工作流的第 9 步**: 写四份全局文档的中文版: examples 索引, 根 README, 根 TICKET, README-ORIGINAL.

主剧本是 `lesson-smith` skill 的 `ref/readup/readup-authoring-workflow.md`, 本步对应它的第 10 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/readup/readup-wrap-cn-spec.md` — 这一步的完整做法, 先读它.
- 它会指向四份分文档 spec: `readup-examples-readme-spec.md`, `readup-readme-spec.md`, `readup-ticket-spec.md`, `ref/readme-original-spec.md`.

---

## 3. 这一步的红线

- **一份英文都不写.** 英文是下一步整门课统一重写出来的.
- **README-ORIGINAL 的 description 与 github_about 必须停下来让创作者拍板.** 不许单方面定稿.
- readup 红线: 根 README 与根 TICKET 里不出现任何斜杠命令.
- 根 TICKET 里不写相对路径链接, 它要进 GitHub Issue.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
