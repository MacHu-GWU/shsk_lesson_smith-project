---
name: lesson-smith-upskill-author-step-12-forge
description: "第 12 步: 锻造学习工具链, 产出 docs/upskill 三份 doc 与 upskill-learn-cn, upskill-quiz-cn 两个子 skill"
argument-hint: "[自由说明...]"
---

# upskill 创作流 第 12 步

你在 **upskill 创作工作流的第 12 步**: 锻造学习工具链.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 13 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 这一步怎么做

**这一步的活儿由 `/lesson-smith-upskill-forge` 完成**, 不在这里手写. 它产出两样东西:

- `docs/upskill/` 下三份 doc: 学习索引, 跑起来的操作, quiz 薄壳.
- `.claude/skills/` 下两个子 skill: `upskill-learn-cn` 与 `upskill-quiz-cn`.

规范与模板都在 `ref/00-common/13-forge-shared/` 下, 由那个 skill 自己去读, 你不用预读.

为方便编辑那次调用的输入, 用模板 `prompts/run-lesson-smith-upskill-forge.md`.

---

## 3. 这一步的红线

- **统稿没过不许跑.** forge 产出的是索引和指针, 指向 `examples/` 里的文件与标题, 而统稿会改标题, 会拆篇并篇, 甚至调编号. 早跑一步, 链接和锚点全指在会变的东西上, 而且没有任何检查会报出来.
- **只产 `-cn` 那一套.** 英文规范和骨架就在 `ref/00-common/13-forge-shared/` 各个 spec 目录里躺着, 但当前不产出, 因为无后缀的英文课程正文留空, 英文索引只会指向一堆空文件.
- **有三件事机器猜不出, 必须停下来问创作者**: 哪些算学习素材 (以及这门课是情况 A 还是 B), runbook 里有哪些隐性步骤, quiz 想怎么考.
- **别在这里出题.** 题库真身是第 8 步写的, forge 只负责定位它并写好那份薄壳的指针.
- 跑完**别急着关 session**: 第 13 步接着在这个 session 里做, 它要的正是刚读进来的这批素材.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
