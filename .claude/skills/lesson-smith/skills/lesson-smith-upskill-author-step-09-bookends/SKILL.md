---
name: lesson-smith-upskill-author-step-09-bookends
description: "第 9 步: 回头补 examples 的两头, 开头的索引 Task 与结尾的梳理拔高 Task"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# upskill 创作流 第 9 步

你在 **upskill 创作工作流的第 9 步**: 补 `examples/` 的两头. 两个都写完, examples 才算齐.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 10 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/05-overview-readme-spec/` 与 `ref/00-common/06-overview-ticket-spec/`: 开头那个索引 Task.
- `ref/00-common/03-task-readme-spec/` 与 `ref/00-common/04-task-ticket-spec/`: 结尾那篇梳理拔高走通用的教学 Task 规范, 没有专属 spec.

---

## 3. 这一步的红线

- **索引 Task 位置固定在 01**, 目录名随课程而定 (`01-overview` 只是推荐, 不强制). lint 认不出它, 整个忘了写也不报错, 所以这一步漏了就是真漏了.
- **索引里的链接要写 `../`.** 它住在 `examples/01-title/` 里, 指向兄弟 Task 得写 `../02-title/README-cn.md`. 少写一层就是整片死链, 这是这份文件唯一一个高频错误.
- **固定位置的特殊 Task 各自单独成组.** quiz 一组, 梳理拔高一组, 不许几个挤一组, 也不许混进教学 Task 的列表.
- **索引 TICKET 是轻的**: 检查清单 3 到 4 条封顶, 明确推翻通用规范的 "常见 5 到 9 条".
- **梳理拔高排在最后一个位置**, 在 quiz 之后. 它除了梳理学了什么, 还要给拔高方向: 能搜哪些关键字, 以及一句话的话题, 方便学生直接复制去喂给 AI.
- **地图只能在路修完之后画.** 如果发现主干还在动, 说明第 6 步没完, 回去写完再来.
- 只写 `-cn.md`.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
