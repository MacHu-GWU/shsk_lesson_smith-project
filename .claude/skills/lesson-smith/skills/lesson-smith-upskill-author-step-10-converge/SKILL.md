---
name: lesson-smith-upskill-author-step-10-converge
description: "第 10 步: 通读全系列统稿, 纠不一致与矛盾, 并给出拆并与形状上的改稿建议"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# upskill 创作流 第 10 步

你在 **upskill 创作工作流的第 10 步**: 通读全系列统稿, 把一篇篇分头写出来的 Task 收敛成一条线.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 11 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/08-series-converge-spec.md`: 找哪两类问题, 怎么改, 什么时候算过.

---

## 3. 这一步的红线

- **一次读完再动手改.** 第 3 篇的问题往往要读到第 8 篇才认得出来.
- **纠错和建议要分开报.** 纠错那类是客观对错, 找到就改; 拆篇并篇这类是建议, 必须明确标成建议, 创作者可能有你不知道的理由.
- 找到的问题先列给创作者过目再改. 术语统一尤其要他点头, 那是口味.
- **quiz 也要一起统.** 题面用的术语要和教学 Task 对得上, 溯源链接要还活着. 它是分开写的, 最容易和主干分叉.
- **过不过由创作者说了算**, 不是你单方面宣布.
- 这一步是后面三步的地基: 锻造, 根目录文档, 出厂全都拿 `examples/` 当素材, 素材不稳就白做.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
