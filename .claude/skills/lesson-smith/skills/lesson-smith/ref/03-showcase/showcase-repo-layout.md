# Showcase 类型仓库目录结构

本文档在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 的通用标准之上, **只说 showcase 的特化之处**. 通用的命名与 frontmatter 约束仍以它为准.

---

## 1. 定位

showcase 教 "如何做某一类事情", 但**学会不是终点**: 学完之后要抹去教学痕迹, 把这个 repo 当作自己的作品拿去展示. 整个 repo 就是一门课, 只有一个 branch. 课程内容拆成 `examples/` 下一个个 Task.

和 upskill 的差别集中在收尾: showcase 多两个环节 (讲故事排练与抹痕迹发布), 因此多两个固定 Task, 多两份 doc, 多两个子 skill.

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
examples/01-title/                   索引 Task
examples/01-title/README-cn.md
examples/01-title/TICKET-cn.md
examples/02-title/                   综述 Task
examples/02-title/README-cn.md
examples/02-title/TICKET-cn.md
examples/03-title/                   主线教学 Task 从 03 开始
examples/...
examples/NN-prove-i-get-it/          quiz 环节, 目录名固定
examples/NN-prove-i-get-it/README-cn.md      题库真身
examples/NN-prove-i-get-it/TICKET-cn.md
examples/NN-how-i-build-this/        demo 环节, 紧跟 quiz, 目录名固定
examples/NN-how-i-build-this/README-cn.md    讲故事底稿
examples/NN-how-i-build-this/TICKET-cn.md
examples/ZZ-title/                   收尾 Task, 排在 demo 之后
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-cn.md            生成
docs/tasks/01-showcase/              唯一 branch 的快照
docs/showcase/                          forge 产出: 学习与展示工具文档
docs/showcase/01-showcase-learn-cn.md   学习索引
docs/showcase/02-showcase-runbook-cn.md 跑起来的操作
docs/showcase/03-showcase-quiz-cn.md    quiz 薄壳, 指向题库真身
docs/showcase/04-showcase-demo-cn.md    demo 薄壳, 指向讲故事底稿加默认主线
docs/showcase/05-showcase-publish-cn.md publish 清单, 自包含, 无 examples 撑
docs/showcase/notes/                    可选, 学生用 showcase-learn-cn 时它写的进度笔记
.claude/skills/showcase-learn-cn/SKILL.md    forge 产出: 带学 skill
.claude/skills/showcase-quiz-cn/SKILL.md     forge 产出: 自测 skill
.claude/skills/showcase-demo-cn/SKILL.md     forge 产出: 讲故事排练 skill
.claude/skills/showcase-publish-cn/SKILL.md  forge 产出: 抹痕迹发布 skill
.claude/skills/<上面四个>/ref/agent-skill-interaction-pattern-cn.md   随各 skill 打包的交互基座
```

树里的 `NN-` 与 `ZZ-` 都是占位符, **不是字面值**: `NN-` 表示编号接着往下排, `ZZ-` 表示编号最大的那个, 也就是最后一个. 落地时全都是两位数字, 从 01 连续不跳号, 这一条 lint 查.

无后缀的英文文件仍然存在, 当前留空, 见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 2 节. 上面的树为了少占篇幅, 只在根目录逐一列了两版, 下面各层同理.

---

## 4. 各文件遵循哪个 spec

**根目录 README 与 TICKET** 是这一个 branch 的 Task 文件, 也是整门课的操作入口与验收清单. 它们**不遵循**教学用的通用 spec (那是给 `examples/` 下单个 Task 用的), 而各有专属 spec:

- `README-cn.md` 遵循 [showcase-readme-spec](showcase-readme-spec/showcase-readme-cn-spec.md). 仓库总览加操作入口, 覆盖怎么学与学完怎么展示发布.
- `TICKET-cn.md` 遵循 [showcase-ticket-spec](showcase-ticket-spec/showcase-ticket-cn-spec.md). 整门课的验收清单, 三段式加一个 "关键能力" H2.

这两份在 `examples/` 全部定稿并统稿之后才写, 拿成品当素材.

**`README-ORIGINAL-cn.md`** 是对外 README, 遵循 [00-common/02-readme-original-spec](../00-common/02-readme-original-spec/readme-original-cn-spec.md).

**`examples/` 下的 Task** 走哪份 spec, 已经在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 4.2 节末尾说全了, 这里只补 showcase 独有的那两个.

**showcase 有两个特殊 Task, 挨着排在主线之后, 收尾之前**, 它们的 README 都不走教学 README 的正文结构:

| 目录 | README 走 | TICKET 走 |
| :--- | :--- | :--- |
| `NN-prove-i-get-it` | [00-common/11-quiz-readme-spec](../00-common/11-quiz-readme-spec/quiz-readme-cn-spec.md) 的问答结构 | [00-common/12-quiz-ticket-spec](../00-common/12-quiz-ticket-spec/quiz-ticket-cn-spec.md) |
| `NN-how-i-build-this` | [showcase-demo-readme-spec](showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md) 的讲故事结构 | [showcase-demo-ticket-spec](showcase-demo-ticket-spec/showcase-demo-ticket-cn-spec.md) |

两份 TICKET 的结构仍沿用通用的 task ticket spec, 只是内容固定极简. **quiz 那两份规范和 upskill 共用**, 所以住在通用层, 落地时把里面的 `{{TYPE}}` 换成 `showcase`; demo 那两份是 showcase 独有的, 留在本层.

**`docs/tasks/`** 下的东西全部由 `lesson-smith sync` 生成, 不手写. SYLLABUS 对 showcase 来说只有 `01-showcase` 一段.

`docs/showcase/notes/` **不是 forge 的产物, 也不是布局的一部分**: 学生用 `/showcase-learn-cn` 时, 它经学生同意后往那里写一份进度笔记 (`learn-progress-cn.md`). 一个刚出厂的 repo 里没有这个目录, lint 也不查它. 列在这里只是为了让人知道它是从哪冒出来的.

每个子 skill 的 `ref/` 下那份交互基座**不是可选附件**: 四份 SKILL 模板开工第一句就是去读它, 丢了那个 skill 会静默地失去交互规范. 它由 forge 从 lesson-smith 的 `ref/agent-skill-interaction-pattern-cn.md` 原样拷入; **lint 只查 `SKILL.md` 在不在, 不查它**, 所以出厂前要人工核一眼.

**`docs/showcase/`** 下五份 doc 与四个子 skill 都由 `lesson-smith-showcase-forge` 产出, 它要读的规范与模板**分两处**:

- **和 upskill 共用的三份**在 [00-common/13-forge-shared/](../00-common/13-forge-shared/): [docs-learn](../00-common/13-forge-shared/docs-learn/docs-learn-cn-spec.md), [docs-runbook](../00-common/13-forge-shared/docs-runbook/docs-runbook-cn-spec.md), [docs-quiz](../00-common/13-forge-shared/docs-quiz/docs-quiz-cn-spec.md), 加 learn 与 quiz 两份 SKILL 模板. 里面的 `{{TYPE}}` 落地时换成 `showcase`.
- **showcase 独有的两份**在本层 [forge/](forge/): [docs-showcase-demo](forge/docs-showcase-demo/docs-showcase-demo-cn-spec.md), [docs-showcase-publish](forge/docs-showcase-publish/docs-showcase-publish-cn-spec.md), 加 demo 与 publish 两份 SKILL 模板. 这两份写死 `showcase`, 不带占位符.

两处都**分语种**: 每份 doc 中英各一套 spec 加 template, 子 skill 也是无后缀的英文版与 `-cn` 版各一份. **但 forge 当前只产 `-cn` 那一套**, 因为无后缀的英文课程正文留空, 英文索引只会指向一堆空文件. 英文那一套规范留着, 等多语种模块回来接手.

**publish 那份要特别注意语种**: 作品 repo 只带一个语种, 所以发布时要**留下有内容的那一版 (`-cn`), 删掉留空的占位符, 再把后缀去掉**. 判断哪一版是占位符必须去读文件, 不许看后缀. 做反了就是把整门课删光.

---

## 5. 与通用标准的关系

showcase 在通用标准之上做了三处特化:

- 把带序号的 branch 收敛成唯一的 `01-showcase`.
- 新增 `examples/` 这一层放 Task 及其索引, 其中 quiz 与 demo 两个 Task 的目录名固定.
- 新增 `docs/showcase/` 与四个子 skill 这一整套学习与展示工具链.

其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, `docs/tasks/` 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
