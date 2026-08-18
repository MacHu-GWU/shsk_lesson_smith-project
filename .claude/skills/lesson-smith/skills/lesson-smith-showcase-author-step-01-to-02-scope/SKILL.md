---
name: lesson-smith-showcase-author-step-01-to-02-scope
description: "第 1 到 2 步: 想清楚这门课教什么, 写 README-ORIGINAL 粗稿, 并把 examples 之外要学的东西先做完"
argument-hint: "[自由说明...]"
---

# showcase 创作流 第 1 到 2 步

你在 **showcase 创作工作流的第 1 到 2 步**: 定题. 把这门课教什么想清楚, 并把 `examples/` 之外的地基铺好.

主剧本是 `lesson-smith` skill 的 `ref/03-showcase/showcase-authoring-workflow.md`, 本步对应它的第 2 到 3 节. 先读那两节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-showcase-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/03-showcase/showcase-repo-layout.md`: showcase 的目录结构与命名, 先读它对齐整体布局.
- `ref/00-common/02-readme-original-spec/`: 写 `README-ORIGINAL-cn.md` 的规范与骨架.

---

## 3. 这一步的红线

- **README-ORIGINAL 这一版是粗稿种子, 不要抠 description.** 第 14 步会拿定稿的 examples 当素材整份重写它. 现在内容还没写, 抠也抠不准.
- **第 2 步很多课压根没有.** 纯讲解型的课, 要学的东西全在 `examples/` 里. 没有就直说没有, **不要为了凑一个步骤去造点什么出来**.
- 有的话就**先做完再往下走**. 从第 3 步开始就默认它们存在了, 边写教程边补代码, 教程会跟着半成品漂.
- 这一步**不碰 `examples/` 下任何 Task**. 一个 Task 都还不该有, 连规划底稿也还没建.
- **别忘了建 `lm.json`**, 内容 `{"type": "showcase"}`. 它是整仓唯一声明 repo 类型的地方, 缺了 lint 会短路成一条报错, 其余一项都不查.
- 只写 `-cn.md`.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
