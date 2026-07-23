---
name: lesson-smith
description: 教学仓库 (hands-on IT 学习课程) 的规范基座. 定义整个 lesson-smith-* skill 家族共享的概念模型, 语言与格式规范, 文档模板. 创建或修改任何课程材料 (README, README-cn, TICKET, README-ORIGINAL, SYLLABUS 等) 时加载.
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

## 3. 四类教学仓库

> 注: 类别命名遵循着, 一个词, 精准反应独特特性, 的设计哲学.

- **evolve**: 一个 Repo 多个 branch, 每个 branch 一个 Task. 代码逐步演化, 文件渐增, 能看到项目一点点长大. 适合企业级, 完成度高的复杂项目.
- **showcase**: 一个 Repo 只有一个 `showcase` branch (单 Task), `examples/01-title/` 下每个目录是一个 mini 教程. 内容偏技能性质, 学完可以抹去所有教学痕迹, 把它当作自己的 repo 拿去面试展示 (含对外 publish 环节).
- **upskill**: 结构与 showcase 几乎一致, 唯一区别是没有对外 publish. 适合 "如何做某一类事情", "如何改简历" 这类学会即止, 不需外部背书的内容.
- **readup**: upskill 的精简子集, 结构相同但砍掉了整条 AI 工具链: 没有 upskill-learn / upskill-quiz 那套子 skill, 没有 docs 学习文档, 也没有 quiz 那个 mini task. 适合读者还不知道 AI Agent Skill 是什么, 只想像读一份普通教程那样, 打开 examples 一篇篇顺着读下来就能学会的内容; 因此它的根 README 与 TICKET 里绝不出现任何斜杠命令, 只引导 "读 examples/README, 再依次读各 mini task 的 README 与 TICKET".

四类共享同一套目录结构标准, 详见 [ref/repo-layout.md](ref/repo-layout.md).

---

## 4. 创作铁律

- 课程创作者以中文为母语. 所以创作课程时永远先写 `-cn.md` 中文版, 全部定稿后再统一用 `translate-to-en` Agent Skill 用英文重写出对应的英文文件.
- 写任何 .md 文件都遵循 `markdown-style` 和 `chinese-english-punctuation` 两个 Agent Skill 的规范.
- 中文文档一律中文叙述, 但术语, 以及在英文语境下更自然的核心表达与名词, 都保留英文原文.
- 除非用户另有说明, 文中的例子, 场景, 公司, 产品, 技术, 人名默认用北美语境 (人名用 John Smith 而非张三, 公司, 产品与民生设施都取北美日常常见的; 加拿大, 澳大利亚或全球化的也行, 唯独不要带明显中国烙印的名词). 翻译成英文时同样保持这个语境, 不要退回国内视角.

---

## 5. 渐进式加载: 按需读取 ref/

不要一次读完全部规范. 按当前任务, 只加载需要的那几份.

**通用标准 (所有类型的教学仓库共用, 在 ref/ 根):**

- 布局, 命名, 校验有疑问, 或要跑 lesson-smith lint / sync 时 → [ref/repo-layout.md](ref/repo-layout.md): 目录结构与命名标准.
- 写某个 Task 或 mini task 的教学 README 时 → [ref/readme-spec.md](ref/readme-spec.md): README 规范加模板.
- 写 TICKET 时 → [ref/ticket-spec.md](ref/ticket-spec.md): 任务卡片规范加模板.
- 写 repo 对外长介绍 README-ORIGINAL 时 → [ref/readme-original-spec.md](ref/readme-original-spec.md): 电梯陈述规范加模板.
- 关心 SYLLABUS 的格式或内容 (它由 lesson-smith sync 生成, 也被 lint 校验) 时 → [ref/syllabus-spec.md](ref/syllabus-spec.md).

**通用交互件 (不限教学仓库, 任何互动 skill 都可加载):**

- 写或改一个需要和用户互动的 skill 时 → [ref/agent-skill-interaction-pattern.md](ref/agent-skill-interaction-pattern.md): 通用交互模式底座 (英文权威版, forge 会把它拷进生成的每个 skill 的 ref/ 下). 人类维护者读中文版 [ref/agent-skill-interaction-pattern-cn.md](ref/agent-skill-interaction-pattern-cn.md), 两版内容一致, 改一版同步另一版.

**upskill 类型专属 (在 ref/upskill/ 下, 只在处理 upskill repo 时才读):**

- upskill 的目录结构特化 → [ref/upskill/upskill-repo-layout.md](ref/upskill/upskill-repo-layout.md).
- 从零创作一个 upskill repo (带创作者走完整流程) → [ref/upskill/upskill-authoring-workflow.md](ref/upskill/upskill-authoring-workflow.md): 完整创作工作流 (由 lesson-smith-upskill-author skill 加载).
- 写 repo 根目录 README (upskill 仓库总览加怎么学的操作入口) → [ref/upskill/upskill-readme-spec.md](ref/upskill/upskill-readme-spec.md).
- 写 repo 根目录 TICKET (upskill 整门课的验收清单) → [ref/upskill/upskill-ticket-spec.md](ref/upskill/upskill-ticket-spec.md).
- 写 examples/README 系列索引 → [ref/upskill/upskill-examples-readme-spec.md](ref/upskill/upskill-examples-readme-spec.md).
- 写 docs/upskill/01-upskill-learn.md (学习索引) → [ref/upskill/docs-upskill-learn-spec.md](ref/upskill/docs-upskill-learn-spec.md).
- 写 docs/upskill/02-upskill-runbook.md (跑起来的操作) → [ref/upskill/docs-upskill-runbook-spec.md](ref/upskill/docs-upskill-runbook-spec.md).
- 写 docs/upskill/03-upskill-quiz.md (quiz 薄壳) → [ref/upskill/docs-upskill-quiz-spec.md](ref/upskill/docs-upskill-quiz-spec.md).
- 写 quiz 环节那个 mini task 的 README (题库真身) → [ref/upskill/upskill-examples-quiz-readme-spec.md](ref/upskill/upskill-examples-quiz-readme-spec.md); 它的 TICKET → [ref/upskill/upskill-examples-quiz-ticket-spec.md](ref/upskill/upskill-examples-quiz-ticket-spec.md).
- 产出 upskill-learn / upskill-quiz 两个子 skill 时 → [ref/upskill/upskill-learn.SKILL.md](ref/upskill/upskill-learn.SKILL.md), [ref/upskill/upskill-quiz.SKILL.md](ref/upskill/upskill-quiz.SKILL.md): 近乎静态的 SKILL 模板.

**readup 类型专属 (在 ref/readup/ 下, 只在处理 readup repo 时才读):**

- readup 的目录结构特化 → [ref/readup/readup-repo-layout.md](ref/readup/readup-repo-layout.md).
- 从零创作一个 readup repo (带创作者走完整流程) → [ref/readup/readup-authoring-workflow.md](ref/readup/readup-authoring-workflow.md): 完整创作工作流 (由 lesson-smith-readup-author skill 加载).
- 写 repo 根目录 README (readup 仓库总览加 "怎么读" 的入口, 不提任何斜杠命令) → [ref/readup/readup-readme-spec.md](ref/readup/readup-readme-spec.md).
- 写 repo 根目录 TICKET (readup 整门课的验收清单) → [ref/readup/readup-ticket-spec.md](ref/readup/readup-ticket-spec.md).
- 写 examples/README 系列索引 → [ref/readup/readup-examples-readme-spec.md](ref/readup/readup-examples-readme-spec.md).

**维护规范文件本身时:**

- 新增或修改 ref/ 下的 spec 文件时 → [spec-file-format.md](spec-file-format.md): spec 文件的写法 (文件即模板, 规范写在顶部注释).
