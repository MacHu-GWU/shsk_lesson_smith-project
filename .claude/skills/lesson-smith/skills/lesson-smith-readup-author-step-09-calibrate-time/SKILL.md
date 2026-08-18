---
name: lesson-smith-readup-author-step-09-calibrate-time
description: "第 9 步: 梳理全部 Task 的预计用时, 出一张汇总表让创作者按档位拍板, 再改回各 TICKET"
argument-hint: "[自由说明...]"
---

# readup 创作流 第 9 步

你在 **readup 创作工作流的第 9 步**: 统稿之后, 横着比一遍 `examples/` 下全部 Task, 把六档预计用时分配到位.

主剧本是 `lesson-smith` skill 的 `ref/01-readup/readup-authoring-workflow.md`, 本步对应它的第 10 节. 先读那一节接上上下文, 再按下面动手.

**这一步接着统稿那个 session 做**, 不用另开. 统稿刚把全系列通读了一遍, 这一步要的正是同一次通读的记忆.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/15-time-calibration-spec.md`: 这一步的完整做法, 先读它. 汇总表哪六列, 怎么让创作者拍板, 改完复核什么, 都在里面.
- `ref/00-common/04-task-ticket-spec/task-ticket-cn-spec.md` 第 8 节: 六档表本身. **你要把它原样贴给创作者看**, 他记不住 "第 4 档" 是多少分钟.

---

## 3. 这一步的红线

- **档位由创作者拍板, 你只出建议.** 表出完就停下来等他回话, 不许自己定完直接改文件. 这是硬 gate.
- **只能从六档里选, 不许造区间.** 他说 "3 档", 你写 `15 到 30 分钟`, 不是 `15 到 25 分钟`.
- **上限 120 分钟是硬的.** 有 Task 顶到档 6 还嫌紧, 提出来让他考虑拆 Task, 不要写成 `120 到 180 分钟`.
- **一个 Task 都不许漏.** 索引 Task 与收尾 Task 也在 `examples/` 下, 也算数, 档位一样要过一遍.
- **只改 TICKET 第 2 节末尾那一行.** 内容的事统稿那一步已经过了, 这一步不碰教学正文.
- **总和不落盘.** 报给创作者即可, 各 TICKET 才是权威, 写根目录文档那一步会重新加总一遍.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
