---
name: lesson-smith-upskill-finalize
description: 给一个 upskill 教学仓库收尾定型. 重写 README-ORIGINAL (Lesson 门面), 写出根目录的 README 与 TICKET (仓库总览加整门课验收清单, 一次产出全部语种), 再跑 lesson-smith sync 生成 SYLLABUS 与快照, 最后跑 lesson-smith lint 把关. 创作流的最后一步, examples 与 forge 都做完之后用. 关键词, finalize upskill, 重写 README-ORIGINAL, 写根 README TICKET, 生成 SYLLABUS, upskill 收尾.
disable-model-invocation: true
argument-hint: [init | refresh] [自由说明...]
allowed-tools: Read Grep Glob Write Edit Bash(ls *) Bash(cat *) Bash(pwd) Bash(git rev-parse *) Bash(git branch *) Bash(lesson-smith *)
---

# lesson-smith-upskill-finalize

你是 upskill 教学仓库的收尾定型者. 对着当前这个 upskill repo 跑一次, 把最外层的几份文件和汇总视图补齐, 让整门课成为一个结构合规, 可交付的成品:

1. 重写 `README-ORIGINAL` (整个 Repo 也就是这门 Lesson 的对外门面), 让它和最终内容对齐, 一次产出全部语种.
2. 根目录 `README` 与 `TICKET` (仓库总览加整门课验收清单), 一次产出全部语种.
3. 跑 `lesson-smith sync` 生成 `docs/tasks/SYLLABUS` 与 `docs/tasks/01-upskill/` 快照.
4. 跑 `lesson-smith lint` 把关整仓结构.

这是创作流的最后一步: 默认 examples 已全部写完, 且 `/lesson-smith-upskill-forge` 已产出 `docs/upskill/` 与两个子 skill.

## 第 0 步: 先加载 lesson-smith skill (不可跳过)

所有规范都住在 **lesson-smith** skill 里, 本 skill 只是薄包装, 自己不复制规范. 这是所有 `lesson-smith-*` skill 的通例: 默认先加载 lesson-smith, 再附带自己这一层的东西. 开工前先加载 lesson-smith skill, 之后从它的 `ref/` 按需读规范.

## 必读规范 (都在 lesson-smith skill 的 ref/ 下)

按用途读, 不要一次全读:

- `ref/upskill/upskill-repo-layout.md` — upskill 的目录结构, 先读它对齐整体布局与各文件归属.
- `ref/readme-original-spec.md` — 重写 README-ORIGINAL 的规范加模板 (含 description 与 github_about 两个字段).
- `ref/upskill/upskill-readme-spec.md` — 写根目录 README 的规范加模板.
- `ref/upskill/upskill-ticket-spec.md` — 写根目录 TICKET 的规范加模板.
- `ref/syllabus-spec.md` — SYLLABUS 的格式 (它由 sync 生成, 也被 lint 校验), 读它以便核对 sync 产物.

## 参数

把 `$ARGUMENTS` 解析成 `<mode> < 自由说明...>`. 第一个 token 若是下列 mode 就用它, 否则整段当自由说明, mode 默认 init.

- (空) 或 `init`: 全量产出. 若根目录 README 或 TICKET 已存在, 停下让用户确认改用 refresh.
- `refresh`: 覆盖式重跑 (先跟用户确认).

自由说明是创作者对本次产出的额外指示, 通常来自输入模板 `prompts/run-lesson-smith-upskill-finalize.md` 的三处: TICKET 关键能力清单的取舍侧重, 整门课预计用时, 以及其他口径要求. 有的话在对应 Phase 一并采纳; 没给的按规范默认.

## 工作流

### Phase 1 — Preflight (不可跳过)

1. 确认是 upskill repo: 读根目录 `lm.json`, `type` 必须是 `upskill`; `examples/` 必须存在. 不满足就停下问用户.
2. 确认前置步骤已完成: `docs/upskill/` 下三份 doc 与 `.claude/skills/upskill-learn`, `.claude/skills/upskill-quiz` 都在. 缺了就提醒用户 finalize 是最后一步, 应先跑 `/lesson-smith-upskill-forge`, 再问是否仍要继续.
3. init 模式下若根目录 README 或 TICKET 已存在, 停下让用户确认改用 refresh.

### Phase 2 — 采集素材 (轻量, 不派 Explore subagent)

根 README 与 TICKET 的内容几乎都能从既有文件推导, 直接读:

- `README-ORIGINAL` — 课程定位与 "承诺" 的依据.
- `examples/README` — 内容地图, 以及 mini task 的编号与顺序.
- 各 `examples/NN-title/TICKET` 顶部的 description 与正文 — 萃取根 TICKET 第 4 节 "关键能力" 的原料.

读 examples 时只读英文版 (无后缀的 `.md`), 跳过本地化变体 (例如 `-cn.md`): 内容一致, 两份都读是浪费 token. 因为根 README 与 TICKET 结构固定, 各语种是同一结构的改写, 从英文素材推导即可.

### Phase 3 — 重写 README-ORIGINAL (全部语种)

按 `readme-original-spec.md` 重写整份 README-ORIGINAL (正文加 description 加 github_about), 一次产出全部语种. 早期那版 README-ORIGINAL 是内容还没写时的粗稿, description 太粗, 也和最终 examples 对不齐; 现在内容齐了, 重写它让这门 Lesson 的对外门面和成品对齐.

要点: description 是 Lesson (整个 Repo) 级的介绍, 结果先行加企业视角, 用足预算写到接近 400 字符, 覆盖 "学完能做什么, 涵盖什么主题, 到什么深度", 不枚举 examples; github_about 是压缩版 tagline, 200 字符以内, 给 GitHub About box 用; 两个字段都用双引号包起来. H1 保持与 repo 名一模一样, 不改. 正文是 3 段 pitch, 保持简洁.

### Phase 4 — 写根目录 README (全部语种)

按 `upskill-readme-spec.md` 写, 一次产出英文版加 `supported-languages.json` 里每个语种 (目前是 `README.md` 与 `README-cn.md`). 这份结构固定, 低歧义, 直接产全部语种, 不走 "先 cn 再 translate-to-en" 的分两步; 思考口径以中文为准, 英文版自然改写.

要点: 操作总入口, 多链接少复述 (pitch 链到 README-ORIGINAL, 内容地图链到 examples/README); 固定提及 `/upskill-learn` 与 `/upskill-quiz`; 不提 runbook; 篇幅软上限约 60 到 80 行. 顶部 frontmatter 的 description 是这门课的承诺, 会流进 SYLLABUS.

### Phase 5 — 写根目录 TICKET (全部语种)

按 `upskill-ticket-spec.md` 写, 同样一次产出全部语种.

要点: 三段式 (目标, 要做的事情, 检查清单) 加第 4 个 H2 (关键能力). 第 4 节从各 mini task 的 TICKET 萃取, 纯 bullet, 不带 checkbox, 10 条以内且必须取舍 (按自由说明给的侧重, 没给就自行挑最能代表这门课的). 预计用时用自由说明给的值, 没给就保守估计或省略. **不写指向 repo 内文件或目录的相对路径链接** (TICKET 会进 GitHub Issue, 相对路径点不动; 绝对 URL 可以), 提到 mini task, 系列索引, upskill-quiz 一律用文字提及.

### Phase 6 — 生成 SYLLABUS 与快照

跑 `lesson-smith sync` (它生成 `docs/tasks/SYLLABUS` 与 `docs/tasks/01-upskill/` 下的 README, TICKET 快照). 若命令不可用或报错, 如实告诉用户, 不要手写这些生成物.

### Phase 7 — Verify 与汇报

1. 跑 `lesson-smith lint` 看整仓结构是否合规; 有问题按报告修到通过.
2. 列出创建或更新的文件 (README-ORIGINAL, 根 README 与 TICKET 各语种, SYLLABUS 与快照).
3. sanity check: README-ORIGINAL 的 description 与 github_about 都在且 H1 等于 repo 名; 根 README 提及了两个子 skill 且没提 runbook; 根 TICKET 有第 4 节关键能力且无相对路径链接.
4. 告诉用户: 这门 upskill 课到此收尾完成, 可以从根目录 README 进入开始学.

## 约束

- 只写 README-ORIGINAL 与根目录的 README, TICKET (各语种), 并触发 sync 与 lint; 不碰源码, 不动 examples 内容, 不改 docs/upskill 与两个子 skill (那是 forge 的活).
- SYLLABUS 与 docs/tasks 快照由 sync 生成, 一律不手写.
- 遵循 lesson-smith 的规范与 markdown-style, chinese-english-punctuation 两个 Agent Skill.
