---
name: lesson-smith-readup-author-step-11-ship
description: "第 11 步: 跑 sync 生成 SYLLABUS 与快照, 跑 lint 把关, 修到通过"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# readup 创作流 第 11 步

你在 **readup 创作工作流的第 11 步**: 跑 sync 生成 SYLLABUS 与快照, 跑 lint 把关, 修到通过.

主剧本是 `lesson-smith` skill 的 `ref/readup/readup-authoring-workflow.md`, 本步对应它的第 12 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/ship-spec.md` — 前置检查, 两条命令, lint 报错该回哪一步修.

---

## 3. 这一步的红线

- **这一步不写内容.** lint 报的问题若要改正文, 回到对应步骤去改.
- SYLLABUS 与 `docs/tasks/` 快照一律不手写. 命令跑不了就如实说, 别自己拼一份.
- 改完正文要重跑 sync 再重跑 lint, 因为 SYLLABUS 是从 description 生成的.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
