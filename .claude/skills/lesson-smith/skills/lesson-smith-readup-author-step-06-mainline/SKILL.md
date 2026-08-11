---
name: lesson-smith-readup-author-step-06-mainline
description: "第 6 步: 风格锁死之后一路把主线教学 Task 写完"
argument-hint: "[自由说明...]"
---

# readup 创作流 第 6 步

你在 **readup 创作工作流的第 6 步**: 把主线写完.

主剧本是 `lesson-smith` skill 的 `ref/01-readup/readup-authoring-workflow.md`, 本步对应它的第 7 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/03-task-readme-spec/` 与 `ref/00-common/04-task-ticket-spec/`: 每个 Task 的 README 与 TICKET.

这一步只写主线. 两头归第 7 步, 那两份 overview spec 现在不用读.

---

## 3. 这一步和上一阶段的区别

前面三步是**边写边定风格**, 这一步风格已经锁死, 剩下的是产量. 所以:

- **拿前几篇当标尺.** 深浅, 长度, 小节骨架, 语气都对齐 02 到 04 那几篇, 不要写着写着自己漂了.
- **发现风格要改, 停下来说.** 别一边改风格一边往后写, 那样前面写的全部变成待返工. 回到 plan 改完再继续.

---

## 4. 这一步的红线

- **README 与 TICKET 成对写, 成对改.**
- **计划变了就更新 `examples/_lm-example-plan.md`.** 写到中途发现要拆篇并篇是正常的, 但改了要落回文件, 不然第 8 步统稿时对不上账.
- **别提前写两头.** 索引和收尾都要等主线定形, 现在写出来的一定是计划而不是成品的地图.
- readup 没有出题 Task, 自查靠每篇自己的 TICKET.
- 只写 `-cn.md`.

---

## 5. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
