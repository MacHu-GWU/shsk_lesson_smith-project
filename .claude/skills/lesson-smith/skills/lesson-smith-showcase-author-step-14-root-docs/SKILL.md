---
name: lesson-smith-showcase-author-step-14-root-docs
description: "第 14 步: 写 repo 根目录那三份 (README, TICKET, 重写 README-ORIGINAL)"
argument-hint: "[自由说明...]"
---

# showcase 创作流 第 14 步

你在 **showcase 创作工作流的第 14 步**: 拿定稿的 `examples/` 当素材, 写 repo 根目录那三份文档.

主剧本是 `lesson-smith` skill 的 `ref/03-showcase/showcase-authoring-workflow.md`, 本步对应它的第 15 节. 先读那一节接上上下文, 再按下面动手.

**这一步接着第 13 步那个 session 做**, 不用另开. 锻造已经把整套 examples 读进来了, 要的正是同一批素材.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-showcase-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 要读的规范

- `ref/00-common/09-root-docs-spec.md`: 这一步的完整做法, 先读它.
- 它会指向三份分文档 spec: `ref/03-showcase/showcase-readme-spec/`, `ref/03-showcase/showcase-ticket-spec/`, `ref/00-common/02-readme-original-spec/`. 每个目录里一份 spec 一份 template, template 整份复制过去填空即可.

---

## 3. 这一步的红线

- **不碰 `examples/`.** 索引, 主线, quiz, demo, 收尾都属于 examples, 在统稿与时间梳理那两步就该定稿了.
- **README-ORIGINAL 的 `description` 与 `github_about` 必须停下来让创作者拍板.** 不许单方面定稿.
- **根 README 要覆盖两件事**: 怎么学 (进 examples 从 01 顺着走, 用 learn 与 quiz 两个子 skill), 以及**学完怎么展示发布** (用 demo 排练, 用 publish 抹痕迹). 后面这一半是 showcase 区别于 upskill 的地方, 漏了根 README 就只是个 upskill.
- **四个子 skill 第 13 步刚产出来, 就在手边, 写之前先确认它们真的在.** 顺序要点明: 先 demo 排练, 再 publish 发布.
- **不提 runbook.** `docs/showcase/02-showcase-runbook-cn.md` 是给 skill 读的元文件, 根 README 一个字都不提它; 环境 setup 交给 `/showcase-learn-cn` 在学生真遇到麻烦时介入.
- 根 TICKET 里不写相对路径链接, 它要进 GitHub Issue. 提到 Task 或子 skill 一律用文字.
- 根 TICKET 第 4 节关键能力: 纯 bullet, 不带 checkbox, **10 条以内且必须取舍**.
- **根 TICKET 的预计用时不许估**: 它是 `examples/` 下各 Task 的机械加总 (下限加下限, 上限加上限), 档位在时间梳理那一步已经定死了.
- 根 README 的 description 是 "你将学到什么", 不是 README-ORIGINAL 那段的复制.
- 没有单独的 "课程内容" 一节. 目录本身就是索引, 再单开一节说一遍是纯复述.

---

## 4. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
