---
name: lesson-smith
description: 教学仓库 (hands-on IT 学习课程) 的规范基座. 定义整个 lesson-smith-* skill 家族共享的概念模型, 语言与格式规范, 文档模板. 创建或修改任何课程材料 (README, README-cn, TICKET, README-ORIGINAL, SYLLABUS 等) 时加载.
---

# LessonSmith: 教学仓库规范基座

: v1

上面那行是加载标记. 每个 step skill 开工前都要确认自己能在上下文里看到它, 看不到就先加载本 skill. 这样约定 (每个 session 开头敲一次 author) 变成了一条会自检的规则: 忘了敲, 下一个 step skill 当场发现, 而不是一路写到出厂那步跑 lint 才炸.

你是 **LessonSmith**, 教学仓库 (teaching repository) 的规范基座. 所有 `lesson-smith-*` skill 都依赖本 skill, 从这里获取统一的概念模型, 语言与格式规范, 文档模板. 那些 skill 只是薄包装, 真正的规范住在这里.

## 1. 什么是教学仓库

教学仓库把 GitHub 的物理结构直接映射成课程的教学结构: 一个 **GitHub Repo = 一门课 (Lesson)**, 一个 **Branch = 一个任务 (Task)**.

- `main` branch 永远不是 Task. Task 永远是 `01-title`, `02-title` 这种带两位数序号的 branch. Branch name 永远全部小写.
- Repo 的 main URL 就是 **Lesson URL**, branch 的 URL 就是 **Task URL**.
- **每个 Task 必有 `README.md` (教学入口) 和 `TICKET.md` (验收 checklist), 这一对是硬的.** 在 readup, upskill, showcase 三类里, Task 落在 `examples/NN-title/` 下.
- `README-ORIGINAL.md` 是整个 Repo 逻辑意义上的长介绍. 因为每个 branch 的 `README.md` 都被它那个 Task 占用了, 所以 Repo 自身的介绍要另起这个文件.
- 这些特殊文件 (README, TICKET, README-ORIGINAL) 名字主体一律大写, 且都有多语言版本: 英文版无后缀, 其他语种是 `<NAME>-<lang>.md` (lang 小写). 支持哪些语种定义在 [supported-languages.json](supported-languages.json).

**术语只用 Lesson, Task, 特殊文件三个词.** 人嘴里的 tutorial, example, mini task 都指 Task, 写进文档一律用 Task.

---

## 2. 一行摘要与索引

每个特殊文件顶部都带一段 YAML frontmatter, 里面的 `description` 是一行压缩摘要, 专门用来在索引里拼成一条 bullet.

- `README.md`: 承诺. 一到两句, 学完你能做到什么.
- `TICKET.md`: 判据. 一句话, 做出什么才算完.
- `README-ORIGINAL.md`: 写给学生的一段话, 可多句. 说清这门课学什么, 为什么值得学, 学完有什么收获, 标准是能原样复制粘贴发给一个学生. 它还额外带一个 `github_about`, 那句是写给老师的, 一句话说清这个 repo 教什么即可.

长度预算与字符约束见 [ref/00-common/01-repo-layout.md](ref/00-common/01-repo-layout.md) 第 6 节, 那里是权威, 别在别处复述数字.

`docs/tasks/SYLLABUS.md` 是整门课的 Task 清单, 由脚本把每个 Task 的 `README.md` 顶部 `description` 按 branch 顺序汇总而成, 不手写.

---

## 3. 四类教学仓库

> 注: 类别命名遵循着, 一个词, 精准反应独特特性, 的设计哲学.

- **evolve**: 一个 Repo 多个 branch, 每个 branch 一个 Task. 代码逐步演化, 文件渐增, 能看到项目一点点长大. 适合企业级, 完成度高的复杂项目.
- **showcase**: 一个 Repo 只有一个 `showcase` branch (单 Task), `examples/` 下每个目录是一个 Task. 内容偏技能性质, 学完可以抹去所有教学痕迹, 把它当作自己的 repo 拿去面试展示 (含对外 publish 环节).
- **upskill**: 结构与 showcase 几乎一致, 唯一区别是没有对外 publish. 适合 "如何做某一类事情", "如何改简历" 这类学会即止, 不需外部背书的内容.
- **readup**: upskill 的精简子集, 结构相同但砍掉了整条 AI 工具链: 没有 `upskill-learn` / `upskill-quiz` 那套子 skill, 没有 docs 学习文档, 也没有 quiz 那个 Task. 适合读者还不知道 AI Agent Skill 是什么, 只想像读一份普通教程那样, 打开 `examples/` 一篇篇顺着读下来就能学会的内容; 因此它的根 README 与 TICKET 里绝不出现任何斜杠命令, 只引导 "进 `examples/` 从 01 开始按编号读".

后三类的 `examples/` 里, **第一个 Task 固定是索引** (给整门课一张地图), 位置固定在 01, 目录名随课程而定.

四类共享同一套目录结构标准, 详见 [ref/00-common/01-repo-layout.md](ref/00-common/01-repo-layout.md).

---

## 4. 创作铁律

- **只写中文.** 课程创作者以中文为母语, 所有文档都写 `-cn.md`. 无后缀的英文文件仍然存在, 当前**留空占位**. 中译英那一步暂时跳过, 等重写质量的问题解决之后才回来做, 见 [ref/rewrite-en-spec.md](ref/rewrite-en-spec.md).
- **链接的语种跟着文件本身走**: 一份文件里指向 repo 内其他**文件**的相对路径链接用 `-cn` 版. 指向**目录**的链接则没有语种之分 (各语种的文件都落在同一个目录下), 两边都是 `examples/01-title/`, 换后缀反而会变成死链; **目录名里出现 `-cn` 一律是命名错误**.
- 写任何 .md 文件都遵循 `markdown-style` 和 `chinese-english-punctuation` 两个 Agent Skill 的规范.
- 中文文档一律中文叙述, 但术语, 以及在英文语境下更自然的核心表达与名词, 都保留英文原文.
- 除非用户另有说明, 文中的例子, 场景, 公司, 产品, 技术, 人名默认用北美语境 (人名用 John Smith 而非张三, 公司, 产品与民生设施都取北美日常常见的; 加拿大, 澳大利亚或全球化的也行, 唯独不要带明显中国烙印的名词).

---

## 5. 渐进式加载: 按需读取 ref/

不要一次读完全部规范. 按当前任务, 只加载需要的那几份.

`ref/` 分四层: `00-common/` 是四类共享的通用层, `01-readup/` `02-upskill/` `03-showcase/` 是各类型的特化层, 特化层只写差异.

**通用层, 文档规范 (在 ref/00-common/ 下):**

- 布局, 命名, frontmatter 约束有疑问, 或要跑 `lesson-smith lint` / `sync` 时 → [01-repo-layout.md](ref/00-common/01-repo-layout.md): 术语, 语种, 命名, 目录结构, frontmatter, 校验工具.
- 写 repo 对外长介绍 README-ORIGINAL 时 → [02-readme-original-spec](ref/00-common/02-readme-original-spec/readme-original-cn-spec.md).
- 写某个教学 Task 的 README 时 → [03-task-readme-spec](ref/00-common/03-task-readme-spec/task-readme-cn-spec.md).
- 写某个教学 Task 的 TICKET 时 → [04-task-ticket-spec](ref/00-common/04-task-ticket-spec/task-ticket-cn-spec.md).
- 写 `examples/` 第一个那个索引 Task 时 → [05-overview-readme-spec](ref/00-common/05-overview-readme-spec/overview-readme-cn-spec.md) 与 [06-overview-ticket-spec](ref/00-common/06-overview-ticket-spec/overview-ticket-cn-spec.md).
- 关心 SYLLABUS 的格式或内容 (它由 sync 生成, 也被 lint 校验) 时 → [07-syllabus-spec.md](ref/00-common/07-syllabus-spec.md).

每个 spec 目录里都是**一份 spec 加一份 template**: spec 是规范, template 是可以整份复制过去填空的骨架, 里面没有任何注释.

**通用层, 流程步骤 (在 ref/00-common/ 下):**

- `examples/` 全部写完, 要通读统稿时 → [08-series-converge-spec.md](ref/00-common/08-series-converge-spec.md): 找哪两类问题, 怎么改, 什么时候算过.
- 统稿之后写 repo 根目录那三份时 → [09-root-docs-spec.md](ref/00-common/09-root-docs-spec.md): 采集什么素材, 三份各写什么, 含一道必须让创作者拍板的 gate.
- 创作流最后一步, 跑 sync 与 lint 出厂时 → [10-ship-spec.md](ref/00-common/10-ship-spec.md): 前置检查, 两条命令, lint 报错回哪一步修.

**通用交互件 (不限教学仓库, 任何互动 skill 都可加载):**

- 写或改一个需要和用户互动的 skill 时 → [ref/agent-skill-interaction-pattern.md](ref/agent-skill-interaction-pattern.md): 通用交互模式底座 (英文版, forge 会把它拷进生成的每个子 skill 的 `ref/` 下). 你自己和创作者互动时读中文版 [ref/agent-skill-interaction-pattern-cn.md](ref/agent-skill-interaction-pattern-cn.md), 两版内容一致, 改一版同步另一版.

**readup 类型专属 (在 ref/01-readup/ 下):**

- readup 的目录结构特化 → [readup-repo-layout.md](ref/01-readup/readup-repo-layout.md).
- 从零创作一个 readup repo → [readup-authoring-workflow.md](ref/01-readup/readup-authoring-workflow.md): 完整创作工作流.
- 写 repo 根目录 README (仓库总览加 "怎么读" 的入口, 不提任何斜杠命令) → [readup-readme-spec](ref/01-readup/readup-readme-spec/readup-readme-cn-spec.md).
- 写 repo 根目录 TICKET (整门课的验收清单) → [readup-ticket-spec](ref/01-readup/readup-ticket-spec/readup-ticket-cn-spec.md).

**upskill 类型专属 (在 ref/02-upskill/ 下):**

- upskill 的目录结构特化 → [upskill-repo-layout.md](ref/02-upskill/upskill-repo-layout.md).
- 从零创作一个 upskill repo → [upskill-authoring-workflow.md](ref/02-upskill/upskill-authoring-workflow.md).
- 写 repo 根目录 README (仓库总览加怎么学的操作入口) → [upskill-readme-spec](ref/02-upskill/upskill-readme-spec/upskill-readme-cn-spec.md).
- 写 repo 根目录 TICKET (整门课的验收清单) → [upskill-ticket-spec](ref/02-upskill/upskill-ticket-spec/upskill-ticket-cn-spec.md).
- 写 quiz 那个 Task 的 README (题库真身) → [upskill-quiz-readme-spec](ref/02-upskill/upskill-quiz-readme-spec/upskill-quiz-readme-cn-spec.md); 它的 TICKET → [upskill-quiz-ticket-spec](ref/02-upskill/upskill-quiz-ticket-spec/upskill-quiz-ticket-cn-spec.md).
- forge 要读的东西全在 `ref/02-upskill/forge/` 下. 写 `docs/upskill/` 那三份 doc → [docs-upskill-learn](ref/02-upskill/forge/docs-upskill-learn/docs-upskill-learn-cn-spec.md) (学习索引), [docs-upskill-runbook](ref/02-upskill/forge/docs-upskill-runbook/docs-upskill-runbook-cn-spec.md) (跑起来的操作), [docs-upskill-quiz](ref/02-upskill/forge/docs-upskill-quiz/docs-upskill-quiz-cn-spec.md) (quiz 薄壳). 每个目录里中英各一套 spec 加 template, **当前只产 `-cn`**.
- 产出 `upskill-learn-cn` / `upskill-quiz-cn` 两个子 skill 时 → [upskill-learn-cn.SKILL.md](ref/02-upskill/forge/upskill-learn-cn.SKILL.md), [upskill-quiz-cn.SKILL.md](ref/02-upskill/forge/upskill-quiz-cn.SKILL.md): 近乎静态的 SKILL 模板, 直接拷. 英文版同目录下, 当前不产出.

**showcase 类型专属 (在 ref/03-showcase/ 下):**

- showcase 的目录结构特化 → [showcase-repo-layout.md](ref/03-showcase/showcase-repo-layout.md).
- 从零创作一个 showcase repo → [showcase-authoring-workflow.md](ref/03-showcase/showcase-authoring-workflow.md).
- 写 repo 根目录 README (覆盖怎么学与学完怎么展示发布) → [showcase-readme-spec](ref/03-showcase/showcase-readme-spec/showcase-readme-cn-spec.md).
- 写 repo 根目录 TICKET (整门课的验收清单) → [showcase-ticket-spec](ref/03-showcase/showcase-ticket-spec/showcase-ticket-cn-spec.md).
- 写 quiz 那个 Task → [showcase-quiz-readme-spec](ref/03-showcase/showcase-quiz-readme-spec/showcase-quiz-readme-cn-spec.md), [showcase-quiz-ticket-spec](ref/03-showcase/showcase-quiz-ticket-spec/showcase-quiz-ticket-cn-spec.md).
- 写 demo 那个 Task → [showcase-demo-readme-spec](ref/03-showcase/showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md), [showcase-demo-ticket-spec](ref/03-showcase/showcase-demo-ticket-spec/showcase-demo-ticket-cn-spec.md).
- forge 要读的东西全在 `ref/03-showcase/forge/` 下. 写 `docs/showcase/` 那五份 doc → [docs-showcase-learn](ref/03-showcase/forge/docs-showcase-learn/docs-showcase-learn-cn-spec.md), [docs-showcase-runbook](ref/03-showcase/forge/docs-showcase-runbook/docs-showcase-runbook-cn-spec.md), [docs-showcase-quiz](ref/03-showcase/forge/docs-showcase-quiz/docs-showcase-quiz-cn-spec.md), [docs-showcase-demo](ref/03-showcase/forge/docs-showcase-demo/docs-showcase-demo-cn-spec.md), [docs-showcase-publish](ref/03-showcase/forge/docs-showcase-publish/docs-showcase-publish-cn-spec.md). 每个目录里中英各一套 spec 加 template, **当前只产 `-cn`**.
- 产出四个子 skill 时 → [showcase-learn-cn.SKILL.md](ref/03-showcase/forge/showcase-learn-cn.SKILL.md), [showcase-quiz-cn.SKILL.md](ref/03-showcase/forge/showcase-quiz-cn.SKILL.md), [showcase-demo-cn.SKILL.md](ref/03-showcase/forge/showcase-demo-cn.SKILL.md), [showcase-publish-cn.SKILL.md](ref/03-showcase/forge/showcase-publish-cn.SKILL.md): 近乎静态的 SKILL 模板, 直接拷. 英文版同目录下, 当前不产出.

**维护规范文件本身时:**

- 新增或修改 `ref/` 下的 spec 文件时 → [spec-file-format.md](spec-file-format.md): spec 目录的形态 (一份 spec 加一份 template), 哪些文件分语种.
