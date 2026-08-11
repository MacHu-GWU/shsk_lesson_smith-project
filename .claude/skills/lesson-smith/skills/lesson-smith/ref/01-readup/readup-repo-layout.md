# Readup 类型仓库目录结构

本文档在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 的通用标准之上, **只说 readup 的特化之处**. 通用的命名与 frontmatter 约束仍以它为准.

---

## 1. 定位

readup 教 "如何做某一类事情" 或 "把某个主题了解清楚", **学会即止**, 不需要外部背书. 整个 repo 就是一门课, 只有一个 branch. 课程内容拆成 `examples/` 下一个个 Task.

readup 面向一类特殊读者: **他们还不知道 AI Agent Skill 是什么**, 也不会用任何辅助 skill, 只会像读一份普通教程那样从头顺着读下来.

所以 readup 刻意保持极简, 只有可供阅读的 examples 内容, **不带任何 AI 学习工具链**:

- 没有带学, 自测这类子 skill.
- 没有给 AI 看的元文档.
- 没有专门出题的 Task.

学生要做什么, 怎么自查, 全部写在每个 Task 自己的 README 与 TICKET 里.

**为什么这一层叫 examples 而不是 tutorials**: 如果这个 repo 最终要拿去给外面看, tutorials 给人的感觉是 "别人在教这个学生", 而 examples 给人的感觉是 "这个学生在教别人, 在展示自己怎么学会的". 后者视角更主动, 更适合展示, 所以统一用 examples.

---

## 2. 唯一的 branch: 01-readup

readup 只有一个带序号的 branch, **名字固定为 `01-readup`**. 因为整门课就是这一个 branch, 序号必然是 01, 名字直接由类型决定, 创作者不用另取.

`examples/` 下那些 Task 是这一个 branch 内部的内容, 不是各自独立的 branch.

这一条由 `lesson-smith lint` 强制: `docs/tasks/` 下必须恰好只有一个目录, 且名为 `01-readup`.

---

## 3. 目录结构

```text
lm.json                              type = readup
README.md                            仓库总览, 留空
README-cn.md
README-ORIGINAL.md                   对外 README, 留空
README-ORIGINAL-cn.md
TICKET.md                            留空
TICKET-cn.md
examples/
examples/01-title/                   索引 Task
examples/01-title/README.md          留空
examples/01-title/README-cn.md
examples/01-title/TICKET.md          留空
examples/01-title/TICKET-cn.md
examples/02-title/                   综述 Task
examples/02-title/README-cn.md
examples/02-title/TICKET-cn.md
examples/03-title/                   主线教学 Task 从 03 开始
examples/...
examples/ZZ-title/                   收尾 Task
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-cn.md            生成
docs/tasks/01-readup/                唯一 branch 的快照
docs/tasks/01-readup/README-cn.md
docs/tasks/01-readup/TICKET-cn.md
```

无后缀的英文文件仍然存在, 当前留空, 见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 2 节.

`examples/` 下各个位置分别是什么, 哪些硬哪些软, 见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 4.2 节. **readup 是三类里唯一没有特殊 Task 的**: 综述之后一路主线到收尾, 中间不插任何固定名字的 Task.

readup 到此为止: 没有任何给 AI 看的学习工具文档, 也没有 `.claude/skills/` 下的任何子 skill. 一个 readup repo 就是 "根目录几份门面文件 + examples 一串 Task + docs/tasks 汇总视图", 打开就能读.

---

## 4. 各文件遵循哪个 spec

**根目录 README 与 TICKET** 是这一个 branch 的 Task 文件, 也是整门课的阅读入口与验收清单. 它们**不遵循**教学用的通用 spec (那是给 `examples/` 下单个 Task 用的), 而各有专属 spec:

- `README-cn.md` 遵循 [readup-readme-spec](readup-readme-spec/readup-readme-cn-spec.md). 仓库总览加 "怎么读" 的入口, 带一行会流进 SYLLABUS 的 description; 正文不提及任何斜杠命令.
- `TICKET-cn.md` 遵循 [readup-ticket-spec](readup-ticket-spec/readup-ticket-cn-spec.md). 整门课的验收清单, 三段式加一个 "关键能力" H2.

这两份在 `examples/` 全部定稿并统稿之后才写, 拿成品当素材.

**`README-ORIGINAL-cn.md`** 是对外 README, 遵循 [00-common/02-readme-original-spec](../00-common/02-readme-original-spec/readme-original-cn-spec.md).

**`examples/` 下的 Task** 走哪份 spec, 已经在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 4.2 节末尾说全了, 这里不重复. readup 没有特殊 Task, 所以那套映射对它来说是完整的: 索引走 overview 那两份, 其余 (综述, 主线, 收尾) 全部直接走通用的 task readme 与 task ticket, 不另立 spec.

**`docs/tasks/`** 下的东西全部由 `lesson-smith sync` 生成, 不手写. SYLLABUS 对 readup 来说只有 `01-readup` 一段.

---

## 5. 与通用标准的关系

readup 在通用标准之上做了两处特化:

- 把带序号的 branch 收敛成唯一的 `01-readup`.
- 新增 `examples/` 这一层放 Task 及其索引.

它刻意不产出任何 docs 学习文档, 也不带任何子 skill 与出题 Task: 一个 readup repo 就是一份可以纯阅读的课程.

其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, `docs/tasks/` 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
