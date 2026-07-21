# Upskill 类型仓库目录结构

upskill 是 examples 系列型仓库: 整个 repo 就是一门课, 内容拆成 examples 下的一个个 mini task, 学会即止, 不对外 publish. 本文档在 [ref/repo-layout.md](../repo-layout.md) 的通用标准之上, 只说清 upskill 的特化之处; 通用命名与 frontmatter 约束仍以它为准.

## 1. 定位

upskill 教 "如何做某一类事情", 学会即止, 不需要外部背书. 整个 repo 就是一门课, 只有一个 Task. 课程内容拆成若干个 mini task, 每个 mini task 放在 examples 下的一个目录里.

为什么这一层叫 examples 而不是 tutorials: 如果这个 repo 最终要拿去给外面看, tutorials 给人的感觉是 "别人在教这个学生", 而 examples 给人的感觉是 "这个学生在教别人, 在展示自己怎么学会的". 后者视角更主动, 更适合展示, 所以统一用 examples.

---

## 2. 唯一的 Task branch: 01-upskill

upskill 只有一个带序号的 Task branch, 名字固定为 01-upskill. 因为整门课就是这一个 Task, 序号必然是 01, 名字直接由类型决定, 创作者不用另取. examples 下的那些 mini task 是这一个 branch 内部的内容, 不是各自独立的 branch.

这一条由 lesson-smith lint 强制: docs/tasks 下必须恰好只有一个目录, 且名为 01-upskill.

---

## 3. 目录结构

```
lm.json                              type = upskill
README.md                            仓库总览 (是这一个 branch 的 Task README)
README-<lang>.md
README-ORIGINAL.md                   对外 README (电梯陈述)
README-ORIGINAL-<lang>.md
TICKET.md                            这一个 branch 的 Task TICKET
TICKET-<lang>.md
examples/
examples/README.md                   系列索引 (把 mini task 按主题梳理)
examples/README-<lang>.md
examples/01-title/
examples/01-title/README.md          mini task 教程
examples/01-title/README-<lang>.md
examples/01-title/TICKET.md          mini task 任务卡片
examples/01-title/TICKET-<lang>.md
examples/02-title/
examples/...
examples/NN-prove-i-get-it/     quiz 环节 (靠后, 通常倒数第 2), 标题固定 prove-i-get-it
examples/NN-prove-i-get-it/README.md        题库真身, 走 upskill-examples-quiz-readme-spec (不走教学 README 结构)
examples/NN-prove-i-get-it/README-<lang>.md
examples/NN-prove-i-get-it/TICKET.md
examples/NN-prove-i-get-it/TICKET-<lang>.md
examples/ZZ-title/                   最后一个 mini task: 梳理已学 + 拔高方向
examples/ZZ-title/README.md
examples/ZZ-title/README-<lang>.md
examples/ZZ-title/TICKET.md
examples/ZZ-title/TICKET-<lang>.md
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-<lang>.md
docs/tasks/01-upskill/               唯一 branch 的快照
docs/tasks/01-upskill/README.md
docs/tasks/01-upskill/README-<lang>.md
docs/tasks/01-upskill/TICKET.md
docs/tasks/01-upskill/TICKET-<lang>.md
docs/upskill/                        forge 产出: 学习工具文档
docs/upskill/01-upskill-learn.md     学习索引
docs/upskill/02-upskill-runbook.md   跑起来的操作
docs/upskill/03-upskill-quiz.md      quiz 薄壳 (指向题库真身)
.claude/skills/upskill-learn/SKILL.md    forge 产出: 带学 skill
.claude/skills/upskill-quiz/SKILL.md     forge 产出: 自测 skill
```

---

## 4. 各文件遵循哪个 spec

根目录 README 与 TICKET 是这一个 branch 的 Task 文件, 也是整门课的操作入口与验收清单. 它们不遵循教学用的 [ref/readme-spec.md](../readme-spec.md) 与 [ref/ticket-spec.md](../ticket-spec.md) (那是给单个 mini task 的教程正文用的), 而各有专属 spec: root README 遵循 [ref/upskill/upskill-readme-spec.md](upskill-readme-spec.md) (仓库总览加 "怎么学" 的操作入口, 带一行会流进 SYLLABUS 的 description 承诺), root TICKET 遵循 [ref/upskill/upskill-ticket-spec.md](upskill-ticket-spec.md) (整门课的验收清单, 三段式加一个 "关键能力" H2). 这两份结构固定, 由 lesson-smith-upskill-finalize 一次性产出全部语种; description 的长度与字符约束仍照 [ref/repo-layout.md](../repo-layout.md) 第 4 节.

README-ORIGINAL 是对外 README, 遵循 [ref/readme-original-spec.md](../readme-original-spec.md).

examples/NN-title 下的 README 与 TICKET 才是真正的教学文档, 它们直接遵循标准的 [ref/readme-spec.md](../readme-spec.md) 与 [ref/ticket-spec.md](../ticket-spec.md), 不另立 spec: 内容规范和根目录情形完全一样, 唯一区别是所在位置 (examples/NN-title 而非 repo 根). 这也是为什么这两个 spec 的适用范围里已经点名了 examples/XY-title-here.

examples/README 是系列索引, 它不是教程, 也不同于 SYLLABUS 的无脑罗列, 而是把 mini task 按主题分组梳理. 它遵循单独的 [ref/upskill/upskill-examples-readme-spec.md](upskill-examples-readme-spec.md).

quiz 那个 mini task 是个例外: 目录固定命名 NN-prove-i-get-it, 它的 README 不走教学 readme-spec 的正文结构, 而走 [ref/upskill/upskill-examples-quiz-readme-spec.md](upskill-examples-quiz-readme-spec.md) 的问答结构. 它的 TICKET 另有规范 [ref/upskill/upskill-examples-quiz-ticket-spec.md](upskill-examples-quiz-ticket-spec.md) (内容固定极简: 读一遍题库 + /upskill-quiz 测到 70% 通过, 结构沿用 [ref/ticket-spec.md](../ticket-spec.md)).

docs/tasks/01-upskill 下的四个文件是根目录 README 与 TICKET 的快照, 由 lesson-smith sync 生成, 不手写. SYLLABUS 同样由 sync 生成, 对 upskill 来说只有 01-upskill 一段.

docs/upskill 下的三份 doc 由 lesson-smith-upskill-forge 产出, 各自的规范见 [docs-upskill-learn-spec.md](docs-upskill-learn-spec.md), [docs-upskill-runbook-spec.md](docs-upskill-runbook-spec.md), [docs-upskill-quiz-spec.md](docs-upskill-quiz-spec.md).

---

## 5. 与通用标准的关系

upskill 在 [ref/repo-layout.md](../repo-layout.md) 的基础上做了两处特化: 一是把带序号的 Task branch 收敛成唯一的 01-upskill, 二是新增了 examples 这一层放 mini task 及其索引. 其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, docs/tasks 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
