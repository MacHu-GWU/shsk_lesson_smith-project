---
name: lesson-smith-upskill-author-step-12-root-docs
description: "第 12 步: 写 repo 根目录那三份 (README, TICKET, 重写 README-ORIGINAL)"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# upskill 创作流 第 12 步

你在 **upskill 创作工作流的第 12 步**: 拿定稿的 `examples/` 当素材, 写 repo 根目录那三份文档.

主剧本是 `lesson-smith` skill 的 `ref/02-upskill/upskill-authoring-workflow.md`, 本步对应它的第 13 节. 先读那一节接上上下文, 再按下面动手.

**这一步接着第 11 步那个 session 做**, 不用另开. 锻造已经把整套 examples 读进来了, 要的正是同一批素材.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-upskill-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/09-root-docs-spec.md`: 这一步的完整做法, 先读它.
- 它会指向三份分文档 spec: `ref/02-upskill/upskill-readme-spec/`, `ref/02-upskill/upskill-ticket-spec/`, `ref/00-common/02-readme-original-spec/`. 每个目录里一份 spec 一份 template, template 整份复制过去填空即可.

---

## 3. 这一步的红线

- **不碰 `examples/`.** 索引, 主线, quiz, 收尾都属于 examples, 在统稿那一步就该写完了.
- **README-ORIGINAL 的 `description` 与 `github_about` 必须停下来让创作者拍板.** 不许单方面定稿.
- **根 README 要提到 `upskill-learn-cn` 与 `upskill-quiz-cn`**, 这两个子 skill 第 11 步刚产出来, 就在手边, **写之前先确认它们真的在**. 不提 runbook, 那是给 skill 读的.
- 根 TICKET 里不写相对路径链接, 它要进 GitHub Issue. 提到 Task 或子 skill 一律用文字.
- 根 TICKET 第 4 节关键能力: 纯 bullet, 不带 checkbox, **10 条以内且必须取舍**.
- 根 README 的 description 是 "你将学到什么", 不是 README-ORIGINAL 那段的复制.
- 没有单独的 "课程内容" 一节. 目录本身就是索引, 再单开一节说一遍是纯复述.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
