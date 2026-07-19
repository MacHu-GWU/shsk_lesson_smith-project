# Upskill 类型仓库目录结构

upskill 是 examples 系列型仓库的一种 (另一种是 showcase, 两者布局几乎一致, 唯一区别是 upskill 学会即止, 不对外 publish). 本文档在 repo-layout.md 的通用标准之上, 只说清 upskill 的特化之处; 通用命名与 frontmatter 约束仍以 repo-layout.md 为准.

## 1. 定位

upskill 教 "如何做某一类事情", 学会即止, 不需要外部背书. 整个 repo 就是一门课, 只有一个 Task. 课程内容拆成若干个 mini task, 每个 mini task 放在 examples 下的一个目录里.

---

## 2. 唯一的 Task branch: 01-upskill

upskill 只有一个带序号的 Task branch, 名字固定为 01-upskill (showcase 对应固定为 01-showcase). 因为整门课就是这一个 Task, 序号必然是 01, 名字直接由类型决定, 创作者不用另取. examples 下的那些 mini task 是这一个 branch 内部的内容, 不是各自独立的 branch.

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
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-<lang>.md
docs/tasks/01-upskill/               唯一 branch 的快照
docs/tasks/01-upskill/README.md
docs/tasks/01-upskill/README-<lang>.md
docs/tasks/01-upskill/TICKET.md
docs/tasks/01-upskill/TICKET-<lang>.md
```

---

## 4. 各文件遵循哪个 spec

根目录 README 与 TICKET 是这一个 branch 的 Task 文件. README 同时充当仓库总览, 它带一行 frontmatter description (这门课的 "承诺"), 这行描述会流进 SYLLABUS. 它不遵循 readme-spec 的教学正文结构 (总览不是教程), 但 description 的约束照 repo-layout.md 第 4 节.

README-ORIGINAL 是对外 README, 遵循 readme-original-spec.

examples/NN-title 下的 README 与 TICKET 才是真正的教学文档, 它们直接遵循标准的 readme-spec 与 ticket-spec, 不另立 spec: 内容规范和根目录情形完全一样, 唯一区别是所在位置 (examples/NN-title 而非 repo 根). 这也是为什么 readme-spec 与 ticket-spec 的适用范围里已经点名了 examples/XY-title-here.

examples/README 是系列索引, 它不是教程, 也不同于 SYLLABUS 的无脑罗列, 而是把 mini task 按主题分组梳理. 它遵循单独的 examples-readme-spec.md (与 showcase 共用).

docs/tasks/01-upskill 下的四个文件是根目录 README 与 TICKET 的快照, 由 lesson-smith sync 生成, 不手写. SYLLABUS 同样由 sync 生成, 对 upskill 来说只有 01-upskill 一段.

---

## 5. 与通用标准的关系

upskill 在 repo-layout.md 的基础上做了两处特化: 一是把带序号的 Task branch 收敛成唯一的 01-upskill, 二是新增了 examples 这一层放 mini task 及其索引. 其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, docs/tasks 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
