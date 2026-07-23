# Readup 类型仓库目录结构

readup 是 examples 系列型仓库: 整个 repo 就是一门课, 内容拆成 examples 下的一个个 mini task, 学会即止. 学生只需像读一份普通教程那样, 打开 examples 一篇篇顺着读下来. 本文档在 [ref/repo-layout.md](../repo-layout.md) 的通用标准之上, 只说清 readup 的特化之处; 通用命名与 frontmatter 约束仍以它为准.

## 1. 定位

readup 教 "如何做某一类事情" 或 "把某个主题了解清楚", 学会即止, 不需要外部背书. 整个 repo 就是一门课, 只有一个 Task. 课程内容拆成若干个 mini task, 每个 mini task 放在 examples 下的一个目录里.

readup 面向一类特殊读者: 他们还不知道 AI Agent Skill 是什么, 也不会用任何辅助 skill, 只会像读一份普通的教程文档那样, 从头顺着读下来. 所以 readup 刻意保持极简, 只有可供阅读的 examples 内容, 不带任何 AI 学习工具链: 没有带学, 自测这类子 skill, 没有给 AI 看的元文档, 也没有专门出题的 mini task. 学生要做什么, 怎么自查, 全部写在每个 mini task 自己的 README 与 TICKET 里.

为什么这一层叫 examples 而不是 tutorials: 如果这个 repo 最终要拿去给外面看, tutorials 给人的感觉是 "别人在教这个学生", 而 examples 给人的感觉是 "这个学生在教别人, 在展示自己怎么学会的". 后者视角更主动, 更适合展示, 所以统一用 examples.

---

## 2. 唯一的 Task branch: 01-readup

readup 只有一个带序号的 Task branch, 名字固定为 01-readup. 因为整门课就是这一个 Task, 序号必然是 01, 名字直接由类型决定, 创作者不用另取. examples 下的那些 mini task 是这一个 branch 内部的内容, 不是各自独立的 branch.

这一条由 lesson-smith lint 强制: docs/tasks 下必须恰好只有一个目录, 且名为 01-readup.

---

## 3. 目录结构

```
lm.json                              type = readup
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
examples/ZZ-title/                   最后一个 mini task: 梳理已学 + 拔高方向
examples/ZZ-title/README.md
examples/ZZ-title/README-<lang>.md
examples/ZZ-title/TICKET.md
examples/ZZ-title/TICKET-<lang>.md
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-<lang>.md
docs/tasks/01-readup/                唯一 branch 的快照
docs/tasks/01-readup/README.md
docs/tasks/01-readup/README-<lang>.md
docs/tasks/01-readup/TICKET.md
docs/tasks/01-readup/TICKET-<lang>.md
```

readup 到此为止: 没有任何给 AI 看的学习工具文档, 也没有 .claude/skills 下的任何子 skill. 一个 readup repo 就是 "根目录几份门面文件 + examples 一串 mini task + docs/tasks 汇总视图", 打开就能读.

---

## 4. 各文件遵循哪个 spec

根目录 README 与 TICKET 是这一个 branch 的 Task 文件, 也是整门课的阅读入口与验收清单. 它们不遵循教学用的 [ref/readme-spec.md](../readme-spec.md) 与 [ref/ticket-spec.md](../ticket-spec.md) (那是给单个 mini task 的教程正文用的), 而各有专属 spec: root README 遵循 [ref/readup/readup-readme-spec.md](readup-readme-spec.md) (仓库总览加 "怎么读" 的入口, 带一行会流进 SYLLABUS 的 description 承诺; 正文不提及任何斜杠命令), root TICKET 遵循 [ref/readup/readup-ticket-spec.md](readup-ticket-spec.md) (整门课的验收清单, 三段式加一个 "关键能力" H2). 这两份结构固定, 由 lesson-smith-readup-finalize 一次性产出全部语种; description 的长度与字符约束仍照 [ref/repo-layout.md](../repo-layout.md) 第 4 节.

README-ORIGINAL 是对外 README, 遵循 [ref/readme-original-spec.md](../readme-original-spec.md).

examples/NN-title 下的 README 与 TICKET 才是真正的教学文档, 它们直接遵循标准的 [ref/readme-spec.md](../readme-spec.md) 与 [ref/ticket-spec.md](../ticket-spec.md), 不另立 spec: 内容规范和根目录情形完全一样, 唯一区别是所在位置 (examples/NN-title 而非 repo 根).

examples/README 是系列索引, 它不是教程, 也不同于 SYLLABUS 的无脑罗列, 而是把 mini task 按主题分组梳理. 它遵循单独的 [ref/readup/readup-examples-readme-spec.md](readup-examples-readme-spec.md).

docs/tasks/01-readup 下的四个文件是根目录 README 与 TICKET 的快照, 由 lesson-smith sync 生成, 不手写. SYLLABUS 同样由 sync 生成, 对 readup 来说只有 01-readup 一段.

---

## 5. 与通用标准的关系

readup 在 [ref/repo-layout.md](../repo-layout.md) 的基础上做了两处特化: 一是把带序号的 Task branch 收敛成唯一的 01-readup, 二是新增了 examples 这一层放 mini task 及其索引. 它刻意不产出任何 docs 学习文档, 也不带任何子 skill 与出题 mini task: 一个 readup repo 就是一份可以纯阅读的课程. 其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, docs/tasks 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
