---
name: lesson-smith-upskill-author-step-07-to-08-quiz
description: "第 7 到 8 步: 扫全部教学内容规划题库, 再写 quiz 那个固定 Task 的题库 README 与 TICKET"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# upskill 创作流 第 7 到 8 步

你在 **upskill 创作工作流的第 7 到 8 步**: 规划并写出 quiz 那个固定 Task, 目录名 `examples/NN-prove-i-get-it`.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 8 到 9 节. 先读那两节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/11-quiz-readme-spec/`: 题库真身的问答结构 (每题一个 H2, 四段).
- `ref/00-common/12-quiz-ticket-spec/`: 它的 TICKET, 内容固定极简.
- 这两份和另一类共用, 里面的 `<type>` 是占位符, **写进 repo 时一律换成 `upskill`**.

---

## 3. 这一步的红线

- **先规划再动笔.** 第 7 步要扫一遍全部教学 Task 与其它教学材料, 把问题清单和题量写进 `examples/_lm-quiz-plan.md`, 和创作者讨论几轮锁定, 再进第 8 步写题. 上来就出题, 出的是想到哪写到哪的题.
- **每道题都要能在 repo 里找到出处.** 找不到出处的就是超纲题, 直接砍掉, 不要靠常识硬凑一道.
- **深入解读必须带溯源链接**, 定位用 header 或关键字, 不用行号.
- **题量看 repo 复杂度, 20 到 50 题是常态.** 不要为了凑数注水, 也不要因为省事只写十几道.
- **题由创作者拍板.** 你提建议, 他定哪些留哪些砍. 这是他的课, 考什么是他的判断.
- 目录名固定 `NN-prove-i-get-it`, forge 靠这个名字定位它, 不许改.
- TICKET 里那两条判据 (读一遍题库, 测到 70% 通过) 不许删, 措辞可以按课程微调.
- 只写 `-cn.md`.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
