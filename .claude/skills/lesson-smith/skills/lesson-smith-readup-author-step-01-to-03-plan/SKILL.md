---
name: lesson-smith-readup-author-step-01-to-03-plan
description: "第 1 到 3 步: 规划这门课教什么, 写 README-ORIGINAL 粗稿, 定内容边界"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# readup 创作流 第 1 到 3 步

你在 **readup 创作工作流的第 1 到 3 步**: 想清楚教什么, 写 README-ORIGINAL 粗稿, 定下内容边界.

主剧本是 `lesson-smith` skill 的 `ref/01-readup/readup-authoring-workflow.md`, 本步对应它的第 2 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/02-readme-original-spec/`: 写第 1 步那版 `README-ORIGINAL-cn.md` 粗稿. 目录里一份 spec 一份 template.
- `ref/01-readup/readup-repo-layout.md`: 目录结构与命名.

---

## 3. 这一步的红线

- **粗稿就是粗稿.** 不要在 description 上纠缠, 它会在第 9 步整份重写.
- 只写 `-cn.md`. 英文是第 10 步一次性产出的.
- 规划结果写进 `examples/_lm-example-plan.md`, 别只留在对话里.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
