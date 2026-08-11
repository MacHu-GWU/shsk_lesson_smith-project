---
name: lesson-smith-upskill-author-step-13-ship
description: "第 13 步: 出厂, 跑 sync 生成 SYLLABUS 与快照, 再跑 lint 把整仓过一遍修到通过"
argument-hint: "[自由说明...]"
---

# upskill 创作流 第 13 步

你在 **upskill 创作工作流的第 13 步**: 出厂. 跑 sync 与 lint, 把整仓修到通过.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 14 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/10-ship-spec.md`: 前置清单, 两条命令怎么跑, lint 常见问题对照表.

---

## 3. 这一步的红线

- **先确认前置齐了.** `docs/upskill/` 下三份 doc 与两个子 skill 都要在, 那是第 11 步的产物, lint 会查它们.
- **SYLLABUS 与 `docs/tasks/` 快照一律由 sync 生成, 不许手写.** 命令不可用或报错就如实说, 不要自己拿键盘补一份出来.
- **改完正文要重跑 sync 再重跑 lint.** SYLLABUS 是从各份 README 的 description 生成的, 只改正文不重跑就会对不上.
- **报出来的路径应该全是 `-cn` 的.** 出现无后缀的英文路径说明按语种开关没生效, 那是 lint 配置的问题, 不是你要去填的空文件.
- 修 lint 报错时**别顺手改教学内容**. 结构问题改结构, 内容问题回去找创作者.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
