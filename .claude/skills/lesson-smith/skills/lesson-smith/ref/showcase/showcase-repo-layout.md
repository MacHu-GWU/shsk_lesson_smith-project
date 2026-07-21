# Showcase 类型仓库目录结构

showcase 是 examples 系列型仓库: 整个 repo 就是一门课, 内容拆成 examples 下的一个个 mini task. 它和 upskill 的结构几乎一致, 唯一的本质区别是 showcase 有对外 publish 环节: 学完可以抹去所有教学痕迹, 把这个 repo 当作自己的作品拿去面试展示. 本文档在 [ref/repo-layout.md](../repo-layout.md) 的通用标准之上, 只说清 showcase 的特化之处; 通用命名与 frontmatter 约束仍以它为准.

## 1. 定位

showcase 教偏技能性质的内容 (例如某个工具, 某套工作流, 某类工程能力), 学完不止是学会, 还要能把整个 repo 抹去教学痕迹后当作自己的作品对外展示. 整个 repo 就是一门课, 只有一个 Task. 课程内容拆成若干个 mini task, 每个 mini task 放在 examples 下的一个目录里.

为什么这一层叫 examples 而不是 tutorials: showcase 的 repo 最终要拿去给外面看, tutorials 给人的感觉是 "别人在教这个学生", 而 examples 给人的感觉是 "这个学生在教别人, 在展示自己怎么学会的". 后者视角更主动, 更适合对外展示, showcase 尤其吃这一点, 所以统一用 examples.

---

## 2. 唯一的 Task branch: 01-showcase

showcase 只有一个带序号的 Task branch, 名字固定为 01-showcase. 因为整门课就是这一个 Task, 序号必然是 01, 名字直接由类型决定, 创作者不用另取. examples 下的那些 mini task 是这一个 branch 内部的内容, 不是各自独立的 branch.

这一条由 lesson-smith lint 强制: docs/tasks 下必须恰好只有一个目录, 且名为 01-showcase.

---

## 3. 目录结构

```
lm.json                              type = showcase
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
examples/NN-prove-i-get-it/     quiz 环节 (靠后), 标题固定 prove-i-get-it
examples/NN-prove-i-get-it/README.md        题库真身, 走 showcase-examples-quiz-readme-spec
examples/NN-prove-i-get-it/README-<lang>.md
examples/NN-prove-i-get-it/TICKET.md
examples/NN-prove-i-get-it/TICKET-<lang>.md
examples/ZZ-how-i-build-this/   demo 环节 (examples 最后一个), 标题固定 how-i-build-this
examples/ZZ-how-i-build-this/README.md      讲故事底稿, 走 showcase-examples-demo-readme-spec
examples/ZZ-how-i-build-this/README-<lang>.md
examples/ZZ-how-i-build-this/TICKET.md
examples/ZZ-how-i-build-this/TICKET-<lang>.md
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-<lang>.md
docs/tasks/01-showcase/              唯一 branch 的快照
docs/tasks/01-showcase/README.md
docs/tasks/01-showcase/README-<lang>.md
docs/tasks/01-showcase/TICKET.md
docs/tasks/01-showcase/TICKET-<lang>.md
docs/showcase/                       forge 产出: 学习与展示工具文档
docs/showcase/01-showcase-learn.md   学习索引
docs/showcase/02-showcase-runbook.md 跑起来的操作
docs/showcase/03-showcase-quiz.md    quiz 薄壳 (指向题库真身)
docs/showcase/04-showcase-demo.md    demo 薄壳 (指向讲故事底稿 + 默认主线)
docs/showcase/05-showcase-publish.md publish 清单 (自包含, 无 examples 撑)
.claude/skills/showcase-learn/SKILL.md    forge 产出: 带学 skill
.claude/skills/showcase-quiz/SKILL.md     forge 产出: 自测 skill
.claude/skills/showcase-demo/SKILL.md     forge 产出: 讲故事排练 skill
.claude/skills/showcase-publish/SKILL.md  forge 产出: 抹痕迹发布 skill
```

---

## 4. 各文件遵循哪个 spec

根目录 README 与 TICKET 是这一个 branch 的 Task 文件, 也是整门课的操作入口与验收清单. 它们不遵循教学用的 [ref/readme-spec.md](../readme-spec.md) 与 [ref/ticket-spec.md](../ticket-spec.md) (那是给单个 mini task 的教程正文用的), 而各有专属 spec: root README 遵循 [showcase-readme-spec.md](showcase-readme-spec.md) (仓库总览加操作入口, 覆盖怎么学与学完怎么展示发布), root TICKET 遵循 [showcase-ticket-spec.md](showcase-ticket-spec.md) (整门课的验收清单, 三段式加一个 "关键能力" H2). 这两份结构固定, 由 lesson-smith-showcase-finalize 一次性产出全部语种; description 的长度与字符约束仍照 [ref/repo-layout.md](../repo-layout.md) 第 4 节.

README-ORIGINAL 是对外 README, 遵循 [ref/readme-original-spec.md](../readme-original-spec.md).

examples/NN-title 下的 README 与 TICKET 才是真正的教学文档, 它们直接遵循标准的 [ref/readme-spec.md](../readme-spec.md) 与 [ref/ticket-spec.md](../ticket-spec.md), 不另立 spec: 内容规范和根目录情形完全一样, 唯一区别是所在位置 (examples/NN-title 而非 repo 根).

examples/README 是系列索引, 它不是教程, 也不同于 SYLLABUS 的无脑罗列, 而是把 mini task 按主题分组梳理. 它遵循单独的 [showcase-examples-readme-spec.md](showcase-examples-readme-spec.md).

examples 下有两个特殊 mini task, 都走各自专属结构而非教学 readme-spec:

- quiz 环节: 目录固定命名 NN-prove-i-get-it, 靠后. 它的 README 走 [showcase-examples-quiz-readme-spec.md](showcase-examples-quiz-readme-spec.md) 的问答结构, TICKET 走 [showcase-examples-quiz-ticket-spec.md](showcase-examples-quiz-ticket-spec.md) (固定极简: 读一遍题库加 /showcase-quiz 测到 70% 通过).
- demo 环节: 目录固定命名 how-i-build-this, 是 examples 的最后一个 mini task. 它的 README 走 [showcase-examples-demo-readme-spec.md](showcase-examples-demo-readme-spec.md) 的讲故事底稿结构, TICKET 走 [showcase-examples-demo-ticket-spec.md](showcase-examples-demo-ticket-spec.md) (固定极简: 读一遍底稿加 /showcase-demo 排练到能流畅讲完).

docs/tasks/01-showcase 下的四个文件是根目录 README 与 TICKET 的快照, 由 lesson-smith sync 生成, 不手写. SYLLABUS 同样由 sync 生成, 对 showcase 来说只有 01-showcase 一段.

docs/showcase 下的五份 doc 由 lesson-smith-showcase-forge 产出, 各自的规范见 [docs-showcase-learn-spec.md](docs-showcase-learn-spec.md), [docs-showcase-runbook-spec.md](docs-showcase-runbook-spec.md), [docs-showcase-quiz-spec.md](docs-showcase-quiz-spec.md), [docs-showcase-demo-spec.md](docs-showcase-demo-spec.md), [docs-showcase-publish-spec.md](docs-showcase-publish-spec.md).

---

## 5. 与通用标准的关系

showcase 在 [ref/repo-layout.md](../repo-layout.md) 的基础上做了两处特化: 一是把带序号的 Task branch 收敛成唯一的 01-showcase, 二是新增了 examples 这一层放 mini task 及其索引. 其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, docs/tasks 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.

---

## 6. publish: showcase 特有的对外环节

publish 是 showcase 区别于其它类型的核心. 它不是一份静态文件, 而是一个由 /showcase-publish skill 执行的运行时步骤: 学完全部课程后, 学生跑一次 publish, 把这个教学 repo 就地转成一个可以放上自己 GitHub 的 portfolio repo. 它的清单 (删哪些教学痕迹, 怎么排 commit, 怎么重写 README, 怎么做敌意扫描) 由 forge 产出的 docs/showcase/05-showcase-publish.md 承载, 规范见 [docs-showcase-publish-spec.md](docs-showcase-publish-spec.md).

publish 会删掉的教学痕迹通常包括: demo 那个 mini task (how-i-build-this), docs/showcase 整个目录, 四个生成的子 skill (showcase-learn/quiz/demo/publish), 各语种的本地化 README (形如 README-cn.md), 以及 README-ORIGINAL. 换言之 demo 底稿本身也是教学痕迹, publish 时会一并抹去; 学生是在 publish 之前读 demo, 排练好怎么讲这段经历, 之后再 publish 出一个干净的作品 repo 拿去展示. 这个 "抹痕迹发布" 环节 upskill 没有, 是 showcase 独有的.
