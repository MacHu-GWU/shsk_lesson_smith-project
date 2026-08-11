# Upskill 类型仓库目录结构

本文档在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 的通用标准之上, **只说 upskill 的特化之处**. 通用的命名与 frontmatter 约束仍以它为准.

---

## 1. 定位

upskill 教 "如何做某一类事情", **学会即止**, 不需要外部背书, 也不对外 publish. 整个 repo 就是一门课, 只有一个 branch. 课程内容拆成 `examples/` 下一个个 Task.

和 readup 的区别是它**带一套 AI 学习工具链**: `docs/upskill/` 下三份给 AI 看的元文档, 加 `/upskill-learn-cn` 与 `/upskill-quiz-cn` 两个子 skill, 都由 forge 产出.

---

## 2. 唯一的 branch: 01-upskill

upskill 只有一个带序号的 branch, **名字固定为 `01-upskill`**. 因为整门课就是这一个 branch, 序号必然是 01, 名字直接由类型决定, 创作者不用另取.

`examples/` 下那些 Task 是这一个 branch 内部的内容, 不是各自独立的 branch.

这一条由 `lesson-smith lint` 强制: `docs/tasks/` 下必须恰好只有一个目录, 且名为 `01-upskill`.

---

## 3. 目录结构

```text
lm.json                              type = upskill
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
examples/NN-prove-i-get-it/README-cn.md      题库真身, 不走教学 README 结构
examples/NN-prove-i-get-it/TICKET-cn.md
examples/ZZ-title/                   收尾 Task, 排在 quiz 之后
docs/tasks/
docs/tasks/SYLLABUS.md               生成
docs/tasks/SYLLABUS-cn.md            生成
docs/tasks/01-upskill/               唯一 branch 的快照
docs/upskill/                          forge 产出: 学习工具文档
docs/upskill/01-upskill-learn-cn.md    学习索引
docs/upskill/02-upskill-runbook-cn.md  跑起来的操作
docs/upskill/03-upskill-quiz-cn.md     quiz 薄壳, 指向题库真身
.claude/skills/upskill-learn-cn/SKILL.md   forge 产出: 带学 skill
.claude/skills/upskill-quiz-cn/SKILL.md    forge 产出: 自测 skill
```

树里的 `NN-` 与 `ZZ-` 都是占位符, **不是字面值**: `NN-` 表示编号接着往下排, `ZZ-` 表示编号最大的那个, 也就是最后一个. 落地时全都是两位数字, 从 01 连续不跳号, 这一条 lint 查.

无后缀的英文文件仍然存在, 当前留空, 见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 2 节. 上面的树为了少占篇幅, 只在根目录逐一列了两版, 下面各层同理.

---

## 4. 各文件遵循哪个 spec

**根目录 README 与 TICKET** 是这一个 branch 的 Task 文件, 也是整门课的操作入口与验收清单. 它们**不遵循**教学用的通用 spec (那是给 `examples/` 下单个 Task 用的), 而各有专属 spec:

- `README-cn.md` 遵循 [upskill-readme-spec](upskill-readme-spec/upskill-readme-cn-spec.md). 仓库总览加 "怎么学" 的操作入口, 带一行会流进 SYLLABUS 的 description.
- `TICKET-cn.md` 遵循 [upskill-ticket-spec](upskill-ticket-spec/upskill-ticket-cn-spec.md). 整门课的验收清单, 三段式加一个 "关键能力" H2.

这两份在 `examples/` 全部定稿并统稿之后才写, 拿成品当素材.

**`README-ORIGINAL-cn.md`** 是对外 README, 遵循 [00-common/02-readme-original-spec](../00-common/02-readme-original-spec/readme-original-cn-spec.md).

**`examples/` 下的 Task** 走哪份 spec, 已经在 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 4.2 节末尾说全了, 这里只补 upskill 独有的那一个.

**upskill 只有一个特殊 Task: quiz**, 目录固定命名 `NN-prove-i-get-it`, 排在主线之后, 收尾之前.

- README 不走教学 README 的正文结构, 而走 [00-common/11-quiz-readme-spec](../00-common/11-quiz-readme-spec/quiz-readme-cn-spec.md) 的问答结构.
- TICKET 另有规范 [00-common/12-quiz-ticket-spec](../00-common/12-quiz-ticket-spec/quiz-ticket-cn-spec.md), 内容固定极简 (读一遍题库加 `/upskill-quiz-cn` 测到 70%), 结构仍沿用通用的 task ticket spec.

这两份**和 showcase 共用**, 所以住在通用层, 落地时把里面的 `{{TYPE}}` 换成 `upskill`.

**`docs/tasks/`** 下的东西全部由 `lesson-smith sync` 生成, 不手写. SYLLABUS 对 upskill 来说只有 `01-upskill` 一段.

**`docs/upskill/`** 下三份 doc 与两个子 skill 都由 `lesson-smith-upskill-forge` 产出. **它要读的规范与模板一份都不在这一层**, 全部在 [00-common/13-forge-shared/](../00-common/13-forge-shared/): [docs-learn](../00-common/13-forge-shared/docs-learn/docs-learn-cn-spec.md), [docs-runbook](../00-common/13-forge-shared/docs-runbook/docs-runbook-cn-spec.md), [docs-quiz](../00-common/13-forge-shared/docs-quiz/docs-quiz-cn-spec.md), 加上两份 SKILL 模板.

**upskill 的 forge 产物和 showcase 完全重合**, 所以那些素材全归通用层, upskill 这一层没有自己的 `forge/` 目录. showcase 只是在同一套之上多两份 (demo 与 publish). 素材里的 `{{TYPE}}` 是占位符, 落地时换成 `upskill`.

那一层**分语种**: 每份 doc 中英各一套 spec 加 template, 子 skill 也是无后缀的英文版与 `-cn` 版各一份. **但 forge 当前只产 `-cn` 那一套**, 因为无后缀的英文课程正文留空, 英文索引只会指向一堆空文件. 英文那一套规范留着, 等多语种模块回来接手.

---

## 5. 与通用标准的关系

upskill 在通用标准之上做了三处特化:

- 把带序号的 branch 收敛成唯一的 `01-upskill`.
- 新增 `examples/` 这一层放 Task 及其索引.
- 新增 `docs/upskill/` 与两个子 skill 这一整套学习工具链.

其余 (特殊文件命名, 多语言后缀, description 的长度与字符约束, `docs/tasks/` 汇总视图, SYLLABUS 生成与校验) 都沿用通用标准, 不在这里重复.
