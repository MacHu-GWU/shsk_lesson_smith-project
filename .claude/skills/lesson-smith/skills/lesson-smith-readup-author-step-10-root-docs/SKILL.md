---
name: lesson-smith-readup-author-step-10-root-docs
description: "第 10 步: 写 repo 根目录那三份 (README, TICKET, 重写 README-ORIGINAL)"
argument-hint: "[自由说明...]"
---

# readup 创作流 第 10 步

你在 **readup 创作工作流的第 10 步**: 拿定稿的 `examples/` 当素材, 写 repo 根目录那三份文档.

主剧本是 `lesson-smith` skill 的 `ref/01-readup/readup-authoring-workflow.md`, 本步对应它的第 11 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-readup-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/09-root-docs-spec.md`: 这一步的完整做法, 先读它.
- 它会指向三份分文档 spec: `ref/01-readup/readup-readme-spec/`, `ref/01-readup/readup-ticket-spec/`, `ref/00-common/02-readme-original-spec/`. 每个目录里一份 spec 一份 template, template 整份复制过去填空即可.

---

## 3. 这一步的红线

- **不碰 `examples/`.** 索引, 主线, 收尾都属于 examples, 在统稿与时间梳理那两步就该定稿了.
- **README-ORIGINAL 的 `description` 与 `github_about` 必须停下来让创作者拍板.** 不许单方面定稿.
- readup 红线: 根 README 与根 TICKET 里不出现任何斜杠命令.
- 根 TICKET 里不写相对路径链接, 它要进 GitHub Issue.
- 根 README 的 description 是 "你将学到什么", 不是 README-ORIGINAL 那段的复制.
- **根 TICKET 的预计用时不许估**: 它是 `examples/` 下各 Task 的机械加总 (下限加下限, 上限加上限), 档位在时间梳理那一步已经定死了.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
