---
name: lesson-smith-readup-author-step-04-to-07-write
description: "第 4 到 7 步: 一篇篇写 examples 下的 Task, 直到最后一篇梳理与拔高"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# readup 创作流 第 4 到 7 步

你在 **readup 创作工作流的第 4 到 7 步**: 一篇篇写 examples 下的 Task, 直到最后一篇梳理与拔高.

主剧本是 `lesson-smith` skill 的 `ref/01-readup/readup-authoring-workflow.md`, 本步对应它的第 5 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/03-task-readme-spec/` 与 `ref/00-common/04-task-ticket-spec/`: 每个教学 Task 的 README 与 TICKET.
- `ref/00-common/05-overview-readme-spec/` 与 `ref/00-common/06-overview-ticket-spec/`: 第 7 步补开头那个索引 Task.

---

## 3. 这一步的红线

- **README 与 TICKET 成对写, 成对改.** TICKET 的 "要做的事情" 呼应 README 的练习, "检查清单" 呼应学习目标. 只改一边是统稿时返工最多的来源.
- **第 5 步不许跳.** 写完前三篇要停下来精修并更新 plan. 这是整条流程里最容易被跳过的一步, 跳了就是用没锁死的风格一路写到底.
- readup 没有出题 Task, 自查靠每篇自己的 TICKET.
- 只写 `-cn.md`.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
