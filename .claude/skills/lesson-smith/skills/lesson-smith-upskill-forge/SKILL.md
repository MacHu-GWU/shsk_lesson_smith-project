---
name: lesson-smith-upskill-forge
description: 为当前这个 upskill 教学仓库锻造出 "学这门课" 的工具链. 扫一遍 examples 渐进序列, 向创作者问清学习素材与考法, 写出 docs/upskill/ 下的 3 份文档 (learn, runbook, quiz), 并落下 upskill-learn 与 upskill-quiz 两个子 skill. 接手或刷新一个 upskill repo 的学习工具时用. 关键词, forge upskill, 生成 upskill 学习 skill, 刷新 upskill 文档.
disable-model-invocation: true
argument-hint: [init | refresh | learn | runbook | quiz] [自由说明...]
allowed-tools: Read Grep Glob Write Edit Bash(ls *) Bash(cat *) Bash(pwd) Bash(git rev-parse *)
---

# lesson-smith-upskill-forge

你是 upskill 学习工具链的锻造者. 对着当前这个 upskill 教学仓库跑一次, 产出两样东西:

1. `docs/upskill/` 下 3 份文档 (学习索引 + 跑起来 + quiz 薄壳).
2. `.claude/skills/` 下 2 个子 skill (upskill-learn, upskill-quiz).

产出后, 创作者与任何学员都能用 `/upskill-learn` 带着学, `/upskill-quiz` 自测.

## 第 0 步: 先加载 lesson-smith skill (不可跳过)

所有规范都住在 **lesson-smith** skill 里, 本 skill 只是薄包装, 自己不复制规范. 这是所有 `lesson-smith-*` skill 的通例: 默认先加载 lesson-smith, 再附带自己这一层的东西. 开工前先加载 lesson-smith skill, 之后从它的 `ref/` 按需读规范.

## 必读规范 (都在 lesson-smith skill 的 ref/ 下)

按用途从 lesson-smith skill 读这些文件, 不要一次全读:

- `ref/upskill/upskill-repo-layout.md` — upskill 的目录结构特化, 先读它对齐整体布局.
- `ref/upskill/docs-upskill-learn-spec.md` — 写 `01-upskill-learn.md` 的规范.
- `ref/upskill/docs-upskill-runbook-spec.md` — 写 `02-upskill-runbook.md` 的规范.
- `ref/upskill/docs-upskill-quiz-spec.md` — 写 `03-upskill-quiz.md` 的规范.
- `ref/upskill/examples-quiz-readme-spec.md` — 题库真身 (quiz mini task 的 README) 的格式, 用来定位它并写好 `03` 的指针.
- `ref/upskill/upskill-learn.SKILL.md`, `ref/upskill/upskill-quiz.SKILL.md` — 两个子 skill 的近乎静态模板, 直接拷.
- `ref/agent-skill-interaction-pattern.md` — 通用交互模式 (英文权威版), 生成子 skill 时拷一份进各自的 ref/ 下.

## 参数

把 `$ARGUMENTS` 解析成 `<mode> < 自由说明...>`. 第一个 token 若是下列 mode 就用它, 否则整段当自由说明, mode 默认 init.

- (空) 或 `init`: 全量生成. 若 `docs/upskill/` 已有目标文件, 停下让用户改用 refresh.
- `refresh`: 覆盖式重跑 (先跟用户确认).
- `learn` | `runbook` | `quiz`: 只重生成那一份 doc (以及对应的 skill).

自由说明是创作者对本次生成的额外指示 (例如 "学习素材以 src/ 下的代码为主", "quiz 偏重 concurrency"). 有的话在 Phase 3 一并采纳.

## 工作流

### Phase 1 — Preflight (不可跳过)

1. 确认是 upskill repo: 读根目录 `lm.json`, `type` 必须是 `upskill`; `examples/` 必须存在. 不满足就停下问用户.
2. 定课程名 (从 `README-ORIGINAL.md` 或根 `README.md`).
3. 列出 `docs/upskill/` 现有内容. init 模式下若目标文件已存在, 停下让用户确认改用 refresh.

### Phase 2 — 扫 examples (轻量, 不派 Explore subagent)

upskill 的内容是创作者手写的 mini task, 不用像扫陌生代码那样重. 直接:

- 读 `examples/README` 与各 `examples/NN-title/README` 顶部的 description (或 `docs/tasks/SYLLABUS`), 拼出**引导路径** (即 learn 文档的 #2).
- 按 `examples-quiz-readme-spec.md` 的特征 (H1 下有固定句, 每题一个 H2, 四段结构) 定位那个 **quiz 环节 mini task** (通常在倒数第 2 到第 3).
- 顺带记下 examples 之外看起来是学习素材的东西 (根目录代码, 其它文档, `mise.toml`), 作为 **#1 学习素材** 的候选.

读 examples 时只读英文版 (无后缀的 `.md`), **跳过本地化变体** `examples/*-<lang>.md` 与 `examples/*/*-<lang>.md` (例如 `-cn.md`): 它们内容和英文版一致, 两份都读是浪费 token; 反正产出都是英文文件, 索引的也是英文文件. 但 examples 之外的脚本, 数据, 配置等要照常通读, 不受此限.

### Phase 3 — 问创作者 (交互 gate, 机器猜不出的部分)

把下面三样问清, 回显确认后再动笔:

- **学习素材 (#1)**: 把 Phase 2 找到的候选列出来, 请创作者确认或增删, 并说清是情况 A (教程本身就是要学的东西) 还是情况 B (真东西在 examples 之外).
- **runbook 隐性步骤**: 开始前的一次性 setup, 以及推进中导师默认懂, 学生却不懂的操作 (cd, 环境变量, 注册账号, 浏览器里 setup 等).
- **quiz 考法自定义**: `03-upskill-quiz.md` 里对 upskill-quiz 行为的特殊要求 (没有就按默认).

自由说明里已经给到的直接采纳, 只补没给的.

### Phase 4 — 写 3 份 doc

按各自规范写到 `docs/upskill/`:

- `01-upskill-learn.md` (依 docs-upskill-learn-spec): #1 学习素材 + #2 引导路径.
- `02-upskill-runbook.md` (依 docs-upskill-runbook-spec): 一次性 setup + 推进中操作, 把隐性步骤显式化.
- `03-upskill-quiz.md` (依 docs-upskill-quiz-spec): 指向 Phase 2 定位到的题库真身, 加上考法自定义.

溯源一律用 markdown 链接加 header 或关键字, 不用 line no. 先写 cn, 定稿后按创作铁律 translate-to-en. 猜不准的地方显式标注请创作者确认, 不许凭空编.

### Phase 5 — 落 2 个子 skill

把两个模板拷成真正的 skill, 并让它们**自包含** (学生 repo 里没有 lesson-smith, 每个 skill 必须自带交互模式):

- `ref/upskill/upskill-learn.SKILL.md` → `.claude/skills/upskill-learn/SKILL.md`
- `ref/upskill/upskill-quiz.SKILL.md` → `.claude/skills/upskill-quiz/SKILL.md`
- `ref/agent-skill-interaction-pattern.md` (英文权威版) → 各拷一份到 `.claude/skills/upskill-learn/ref/agent-skill-interaction-pattern.md` 和 `.claude/skills/upskill-quiz/ref/agent-skill-interaction-pattern.md`.

模板近乎全静态, 落地时只需核对: 每个 SKILL.md 都固定加载它自己 ref/ 下那份交互模式 (路径已写死在模板里), 且对 `docs/upskill/` 的引用路径正确.

### Phase 6 — Verify 与汇报

1. 列出创建或更新的文件 (3 份 doc + 2 份 SKILL.md).
2. sanity check: 每个 SKILL.md 都引到 `docs/upskill/` 下的文件; 每个生成的 skill 的 `ref/` 下都有 `agent-skill-interaction-pattern.md`, 且 SKILL.md 固定加载了它; 3 份 doc 都非空.
3. 跑 `lesson-smith lint` 看仓库结构是否仍合规.
4. 告诉用户: 用 `/upskill-learn` 开始学, `/upskill-quiz` 自测; `docs/upskill/` 里哪里不对直接改, 或 `refresh <name>` 重生成一份.

## 约束

- 只写 `docs/upskill/` 与 `.claude/skills/upskill-{learn,quiz}/`; 不碰源码, 不动 examples 内容.
- 题目本身不在这里出: 题库真身由创作者在 quiz mini task 里手写 (可另有 skill 辅助), forge 只负责定位它并写好 `03` 的指针.
- 遵循 lesson-smith 的创作铁律与 markdown-style, chinese-english-punctuation 两个 Agent Skill.
