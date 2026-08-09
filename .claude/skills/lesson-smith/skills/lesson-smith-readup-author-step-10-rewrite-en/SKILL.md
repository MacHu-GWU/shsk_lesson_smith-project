---
name: lesson-smith-readup-author-step-10-rewrite-en
description: "第 10 步: 把整门课一次性重写成英文"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# readup 创作流 第 10 步

你在 **readup 创作工作流的第 10 步**: 把整门课一次性重写成英文.

主剧本是 `lesson-smith` skill 的 `ref/readup/readup-authoring-workflow.md`, 本步对应它的第 11 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/rewrite-en-spec.md` — 这一步的唯一权威, 照它做即可.

---

## 3. 这一步的红线

- **不要问创作者要文件清单.** 六组 glob 写在规范第 2 节里.
- **只跑一次, 不许拆开**, 也不要自己起 agent 编排它. 拆开跑, 跨篇的术语与标题统一就没了, 而事后没有任何一步会补回来.
- 不要加 `--no-reconcile`.
- 跑完按规范第 7 节检查. 其中把 `README-ORIGINAL.md` 的 H1 改回 repo 名是**必做**的一步, 不是抽查.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
