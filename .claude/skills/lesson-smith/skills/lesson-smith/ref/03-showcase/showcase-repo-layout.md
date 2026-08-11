# Showcase 类型仓库目录结构

本文档在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 的通用标准之上, **只说 showcase 的特化之处**. 通用的命名与 frontmatter 约束仍以它为准.

---

## 1. 定位

showcase 教 "如何做某一类事情", 但**学会不是终点**: 学完之后要抹去教学痕迹, 把这个 repo 当作自己的作品拿去展示. 整个 repo 就是一门课, 只有一个 branch. 课程内容拆成 `examples/` 下一个个 Task.

和 upskill 的差别集中在收尾: showcase 多两个环节 (讲故事排练与抹痕迹发布), 因此多两个固定 Task, 多两份 doc, 多两个子 skill.

**为什么这一层叫 examples 而不是 tutorials**: 如果这个 repo 最终要拿去给外面看, tutorials 给人的感觉是 "别人在教这个学生", 而 examples 给人的感觉是 "这个学生在教别人, 在展示自己怎么学会的". 后者视角更主动, 更适合展示, 所以统一用 examples.

---

## 2. 唯一的 branch: 01-showcase

showcase 只有一个带序号的 branch, **名字固定为 `01-showcase`**. 因为整门课就是这一个 branch, 序号必然是 01, 名字直接由类型决定, 创作者不用另取.

`examples/` 下那些 Task 是这一个 branch 内部的内容, 不是各自独立的 branch.

这一条由 `lesson-smith lint` 强制: `docs/tasks/` 下必须恰好只有一个目录, 且名为 `01-showcase`.

---

## 3. 目录结构

```text
lm.json                              type = showcase
README.md                            仓库总览, 留空
README-cn.md
README-ORIGINAL.md                   对外 README, 留空
README-ORIGINAL-cn.md
TICKET.md                            留空
TICKET-cn.md
examples/
examples/01-title/                   索引 Task, 位置固定在 01
examples/01-title/README-cn.md
examples/01-title/TICKET-cn.md
examples/02-title/                   教学 Task 从 02 开始
examples/02-title/README-cn.md
examples/02-title/TICKET-cn.md
examples/...
examples/NN-prove-i-get-it/          quiz 环节, 靠后, 目录名固定
examples/NN-prove-i-get-it/README-cn.md      题库真身
examples/NN-prove-i-get-it/TICKET-cn.md
examples/ZZ-how-i-build-this/        demo 环节, examples 最后一个, 目录名固定
examples/ZZ-how-i-build-this/README-cn.md    讲故事底稿
examples/ZZ-how-i-build-this/TICKET-cn.md
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-cn.md            生成
docs/tasks/01-showcase/              唯一 branch 的快照
docs/showcase/                       forge 产出: 学习与展示工具文档
docs/showcase/01-showcase-learn.md   学习索引
docs/showcase/02-showcase-runbook.md 跑起来的操作
docs/showcase/03-showcase-quiz.md    quiz 薄壳, 指向题库真身
docs/showcase/04-showcase-demo.md    demo 薄壳, 指向讲故事底稿加默认主线
docs/showcase/05-showcase-publish.md publish 清单, 自包含, 无 examples 撑
.claude/skills/showcase-learn/SKILL.md    forge 产出: 带学 skill
.claude/skills/showcase-quiz/SKILL.md     forge 产出: 自测 skill
.claude/skills/showcase-demo/SKILL.md     forge 产出: 讲故事排练 skill
.claude/skills/showcase-publish/SKILL.md  forge 产出: 抹痕迹发布 skill
```

无后缀的英文文件仍然存在, 当前留空, 见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 2 节. 上面的树为了少占篇幅, 只在根目录逐一列了两版, 下面各层同理.

---

## 4. 各文件遵循哪个 spec

**根目录 README 与 TICKET** 是这一个 branch 的 Task 文件, 也是整门课的操作入口与验收清单. 它们**不遵循**教学用的通用 spec (那是给 `examples/` 下单个 Task 用的), 而各有专属 spec:

- `README-cn.md` 遵循 [showcase-readme-spec](showcase-readme-spec/showcase-readme-cn-spec.md). 仓库总览加操作入口, 覆盖怎么学与学完怎么展示发布.
- `TICKET-cn.md` 遵循 [showcase-ticket-spec](showcase-ticket-spec/showcase-ticket-cn-spec.md). 整门课的验收清单, 三段式加一个 "关键能力" H2.

这两份在 `examples/` 全部定稿并统稿之后才写, 拿成品当素材.

**`README-ORIGINAL-cn.md`** 是对外 README, 遵循 [00-common/02-readme-original-spec](../00-common/02-readme-original-spec/readme-original-cn-spec.md).

**`examples/01-title/`** 是索引 Task, 位置固定在 01 但名字随课程而定. README 遵循 [00-common/05-overview-readme-spec](../00-common/05-overview-readme-spec/overview-readme-cn-spec.md), TICKET 遵循 [00-common/06-overview-ticket-spec](../00-common/06-overview-ticket-spec/overview-ticket-cn-spec.md).

**`examples/02-title/` 往后**才是教学 Task, 它们直接遵循通用的 [00-common/03-task-readme-spec](../00-common/03-task-readme-spec/task-readme-cn-spec.md) 与 [00-common/04-task-ticket-spec](../00-common/04-task-ticket-spec/task-ticket-cn-spec.md), 不另立 spec.

**两个固定 Task 是例外**, 它们的 README 都不走教学 README 的正文结构:

| 目录 | README 走 | TICKET 走 |
| :--- | :--- | :--- |
| `NN-prove-i-get-it` | [showcase-examples-quiz-readme-spec.md](showcase-examples-quiz-readme-spec.md) 的问答结构 | [showcase-examples-quiz-ticket-spec.md](showcase-examples-quiz-ticket-spec.md) |
| `ZZ-how-i-build-this` | [showcase-examples-demo-readme-spec.md](showcase-examples-demo-readme-spec.md) 的讲故事结构 | [showcase-examples-demo-ticket-spec.md](showcase-examples-demo-ticket-spec.md) |

两份 TICKET 的结构仍沿用通用的 task ticket spec, 只是内容固定极简.

**`docs/tasks/`** 下的东西全部由 `lesson-smith sync` 生成, 不手写. SYLLABUS 对 showcase 来说只有 `01-showcase` 一段.

**`docs/showcase/`** 下五份 doc 由 `lesson-smith-showcase-forge` 产出, 规范见 [docs-showcase-learn-spec.md](docs-showcase-learn-spec.md), [docs-showcase-runbook-spec.md](docs-showcase-runbook-spec.md), [docs-showcase-quiz-spec.md](docs-showcase-quiz-spec.md), [docs-showcase-demo-spec.md](docs-showcase-demo-spec.md), [docs-showcase-publish-spec.md](docs-showcase-publish-spec.md).

---

## 5. 与通用标准的关系

showcase 在通用标准之上做了三处特化:

- 把带序号的 branch 收敛成唯一的 `01-showcase`.
- 新增 `examples/` 这一层放 Task 及其索引, 其中末尾两个 Task 的目录名固定.
- 新增 `docs/showcase/` 与四个子 skill 这一整套学习与展示工具链.

其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, `docs/tasks/` 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
