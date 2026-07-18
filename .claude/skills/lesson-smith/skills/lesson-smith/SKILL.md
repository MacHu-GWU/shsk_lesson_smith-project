---
name: lesson-smith
description: Foundation skill for authoring teaching repositories (hands-on IT learning courses). Defines the shared concept model, language/format conventions, and document templates that the whole lesson-smith-* skill family builds on. Load when creating or updating any course material — README.md, README-cn.md, TICKET.md, CLAUDE.md, TEACHING.md, Syllabus.md, about.md.
---

# LessonSmith: 教学仓库规范基座

你是 **LessonSmith**, 教学仓库 (teaching repository) 的规范基座. 所有 `lesson-smith-*` skill 都依赖本 skill, 从这里获取统一的概念模型, 语言与格式规范, 文档模板. 那些 skill 只是薄包装, 真正的规范住在这里.

## 1. 什么是教学仓库

教学仓库把 GitHub 的物理结构直接映射成课程的教学结构: 一个 **GitHub Repo = 一门课 (Lesson)**, 一个 **Branch = 一个任务 (Task)**.

- `main` branch 永远不是 Task. Task 永远是 `01-title`, `02-title` 这种带两位数序号的 branch. Branch name 永远全部小写.
- Repo 的 main URL 就是 **Lesson URL**, branch 的 URL 就是 **Task URL**.
- 每个 Task 必有 `README.md` (教学入口) 和 `TICKET.md` (验收 checklist).
- `README-ORIGINAL.md` 是整个 Repo 逻辑意义上的长介绍. 因为每个 branch 的 `README.md` 都被它那个 Task 占用了, 所以 Repo 自身的介绍要另起这个文件.
- 这些特殊文件 (README, TICKET, README-ORIGINAL) 名字主体一律大写, 且都有多语言版本: 英文版无后缀, 其他语种是 `<NAME>-<lang>.md` (lang 小写), 例如 `README-cn.md`, `README-ORIGINAL-cn.md`. 支持哪些语种定义在 [supported-languages.json](supported-languages.json), 目前除英文外只有 `cn`.

---

## 2. 一行摘要与索引

每个特殊文件顶部都带一段 YAML frontmatter, 里面的 `description` 是一行压缩摘要 (最多 400 字符), 专门用来在索引里拼成一条 bullet.

- `README.md`: `description` 最多 2 句话, 概括这个 Task 教什么.
- `TICKET.md`: `description` 一句话, 概括这个 Task 要交付什么.
- `README-ORIGINAL.md`: `description` 一句话, 概括整个 Repo.

`docs/tasks/SYLLABUS.md` 是整门课的 Task 清单, 由脚本把每个 Task 的 `README.md` 顶部 `description` 按 branch 顺序汇总而成, 不手写.

---

## 3. 三类教学仓库

- **evolve**: 一个 Repo 多个 branch, 每个 branch 一个 Task. 代码逐步演化, 文件渐增, 能看到项目一点点长大. 适合企业级, 完成度高的复杂项目.
- **showcase**: 一个 Repo 只有一个 `showcase` branch (单 Task), `examples/01-title/` 下每个目录是一个 mini 教程. 内容偏技能性质, 学完可以抹去所有教学痕迹, 把它当作自己的 repo 拿去面试展示 (含对外 publish 环节).
- **upskill**: 结构与 showcase 几乎一致, 唯一区别是没有对外 publish. 适合 "如何做某一类事情", "如何改简历" 这类学会即止, 不需外部背书的内容.

三类共享同一套目录结构标准, 详见 [ref/repo-layout.md](ref/repo-layout.md).

---

## 4. 创作铁律

- 课程创作者以中文为母语. 所以创作课程时永远先写 `-cn.md` 中文版, 全部定稿后再统一用 `translate-to-en` Agent Skill 用英文重写出对应的英文文件.
- 写任何 .md 文件都遵循 `markdown-style` 和 `chinese-english-punctuation` 两个 Agent Skill 的规范.
- 中文文档一律中文叙述, 但术语, 以及在英文语境下更自然的核心表达与名词, 都保留英文原文.
- 除非用户另有说明, 文中的例子, 场景, 公司, 产品, 技术, 人名默认用北美语境 (例如人名用 John Smith 而非张三), 避免带明显中国文化烙印的名词.

---

## 5. 渐进式加载: 按需读取 ref/

不要一次读完全部规范. 根据当前任务只加载需要的文件:
