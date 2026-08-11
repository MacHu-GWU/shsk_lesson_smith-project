---
name: lesson-smith-upskill-author-step-01-to-03-plan
description: "第 1 到 3 步: 想清楚教什么, 写 README-ORIGINAL 粗稿, 完成 examples 之外的做的部分, 和 AI 讨论出课程规划"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# upskill 创作流 第 1 到 3 步

你在 **upskill 创作工作流的第 1 到 3 步**: 把这门课要教什么想清楚, 并把地基铺好.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 2 到 4 节. 先读那几节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/02-upskill/upskill-repo-layout.md`: upskill 的目录结构与命名, 先读它对齐整体布局.
- `ref/00-common/02-readme-original-spec/`: 写 `README-ORIGINAL-cn.md` 的规范与骨架.

---

## 3. 这一步的红线

- **README-ORIGINAL 这一版是粗稿种子, 不要抠 description.** 第 12 步会拿定稿的 examples 当素材整份重写它. 现在内容还没写, 抠也抠不准.
- **examples 之外的 "做的部分" 要先做完.** 从第 4 步开始就默认它们存在了. 边写教程边补代码, 教程会跟着半成品漂.
- **规划要落到 `examples/_lm-example-plan.md`**, 别只留在对话里. 那份文件后面几步还要反复改, 允许进 git.
- 这一步**不碰 `examples/` 下任何 Task**. 一个 Task 都还不该有.
- 只写 `-cn.md`.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
