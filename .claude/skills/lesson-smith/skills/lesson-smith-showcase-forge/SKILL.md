---
name: lesson-smith-showcase-forge
description: "为当前 showcase 教学仓库锻造学习与展示工具链: 产出 docs/showcase 五份文档 (learn, runbook, quiz, demo, publish) 与四个子 skill (showcase-learn, showcase-quiz, showcase-demo, showcase-publish). 课程内容写完后手动跑一次."
disable-model-invocation: true
argument-hint: "[init | refresh | learn | runbook | quiz | demo | publish] [自由说明...]"
allowed-tools: Read Grep Glob Write Edit Bash(ls *) Bash(cat *) Bash(pwd) Bash(git rev-parse *) Bash(uvx *)
---

# lesson-smith-showcase-forge

你是 showcase 工具链的锻造者. 对着当前这个 showcase 教学仓库跑一次, 产出两样东西:

1. `docs/showcase/` 下 5 份文档 (学习索引 + 跑起来 + quiz 薄壳 + demo 薄壳 + publish 清单).
2. `.claude/skills/` 下 4 个子 skill (showcase-learn, showcase-quiz, showcase-demo, showcase-publish).

产出后, 创作者与任何学员都能用 `/showcase-learn` 带着学, `/showcase-quiz` 自测, `/showcase-demo` 排练怎么讲这段经历, `/showcase-publish` 把 repo 抹去教学痕迹发布成作品.

## 第 0 步: 先加载 lesson-smith skill (不可跳过)

所有规范都住在 **lesson-smith** skill 里, 本 skill 只是薄包装, 自己不复制规范. 这是所有 `lesson-smith-*` skill 的通例: 默认先加载 lesson-smith, 再附带自己这一层的东西. 开工前先加载 lesson-smith skill, 之后从它的 `ref/` 按需读规范.

## 必读规范 (都在 lesson-smith skill 的 ref/ 下)

按用途从 lesson-smith skill 读这些文件, 不要一次全读:

- `ref/showcase/showcase-repo-layout.md` — showcase 的目录结构特化, 先读它对齐整体布局.
- `ref/showcase/docs-showcase-learn-spec.md` — 写 `01-showcase-learn.md` 的规范.
- `ref/showcase/docs-showcase-runbook-spec.md` — 写 `02-showcase-runbook.md` 的规范.
- `ref/showcase/docs-showcase-quiz-spec.md` — 写 `03-showcase-quiz.md` 的规范.
- `ref/showcase/docs-showcase-demo-spec.md` — 写 `04-showcase-demo.md` 的规范.
- `ref/showcase/docs-showcase-publish-spec.md` — 写 `05-showcase-publish.md` 的规范 (自包含 publish 清单).
- `ref/showcase/showcase-examples-quiz-readme-spec.md` — 题库真身 (quiz mini task 的 README) 的格式, 用来定位它并写好 `03` 的指针.
- `ref/showcase/showcase-examples-demo-readme-spec.md` — 讲故事底稿 (demo mini task 的 README) 的格式, 用来定位它并写好 `04` 的指针.
- `ref/showcase/showcase-learn.SKILL.md`, `ref/showcase/showcase-quiz.SKILL.md`, `ref/showcase/showcase-demo.SKILL.md`, `ref/showcase/showcase-publish.SKILL.md` — 四个子 skill 的近乎静态模板, 直接拷.
- `ref/agent-skill-interaction-pattern.md` — 通用交互模式 (英文权威版), 生成子 skill 时拷一份进各自的 ref/ 下.

## 参数

把 `$ARGUMENTS` 解析成 `<mode> < 自由说明...>`. 第一个 token 若是下列 mode 就用它, 否则整段当自由说明, mode 默认 init.

- (空) 或 `init`: 全量生成. 若 `docs/showcase/` 已有目标文件, 停下让用户改用 refresh.
- `refresh`: 覆盖式重跑 (先跟用户确认).
- `learn` | `runbook` | `quiz` | `demo` | `publish`: 只重生成那一份 doc (以及对应的 skill, 若有).

自由说明是创作者对本次生成的额外指示 (例如 "学习素材以 src/ 下的代码为主", "quiz 偏重 concurrency", "publish 时保留 examples/03 作为作品主线"). 有的话在 Phase 3 一并采纳.

## 工作流

### Phase 1 — Preflight (不可跳过)

1. 确认是 showcase repo: 读根目录 `lm.json`, `type` 必须是 `showcase`; `examples/` 必须存在. 不满足就停下问用户.
2. 定课程名 (从 `README-ORIGINAL.md` 或根 `README.md`).
3. 列出 `docs/showcase/` 现有内容. init 模式下若目标文件已存在, 停下让用户确认改用 refresh.

### Phase 2 — 扫 examples (轻量, 不派 Explore subagent)

showcase 的内容是创作者手写的 mini task, 不用像扫陌生代码那样重. 直接:

- 读 `examples/README` 与各 `examples/NN-title/README` 顶部的 description (或 `docs/tasks/SYLLABUS`), 拼出**引导路径** (即 learn 文档的 #2).
- 按 `showcase-examples-quiz-readme-spec.md` 的特征定位那个 **quiz 环节 mini task** (`NN-prove-i-get-it`), 按 `showcase-examples-demo-readme-spec.md` 的特征定位那个 **demo 讲故事底稿 mini task** (`how-i-build-this`, examples 最后一个).
- 顺带记下 examples 之外看起来是学习素材的东西 (根目录代码, 其它文档, `mise.toml`), 作为 **#1 学习素材** 的候选.
- 为写 publish 清单, 扫一遍当前 repo 的实际文件: 把 cardinal 删除的 glob (各语种 README, examples/README, quiz 起及之后的 mini task, 各级 TICKET 等) 对这个 repo 展开成真实清单; 记下可用于 commit plan 的真实文件与依赖顺序.

读 examples 时只读英文版 (无后缀的 `.md`), **跳过本地化变体** `examples/*-<lang>.md` 与 `examples/*/*-<lang>.md`: 它们内容和英文版一致. 但 examples 之外的脚本, 数据, 配置等要照常通读, 不受此限.

### Phase 3 — 问创作者 (交互 gate, 机器猜不出的部分)

把下面几样问清, 回显确认后再动笔:

- **学习素材 (#1)**: 把 Phase 2 找到的候选列出来, 请创作者确认或增删, 并说清是情况 A (教程本身就是要学的东西) 还是情况 B (真东西在 examples 之外).
- **runbook 隐性步骤**: 开始前的一次性 setup, 以及推进中导师默认懂, 学生却不懂的操作 (cd, 环境变量, 注册账号, 浏览器里 setup 等).
- **quiz 考法自定义**: `03-showcase-quiz.md` 里对 showcase-quiz 行为的特殊要求 (没有就按默认).
- **demo 排练自定义**: `04-showcase-demo.md` 里对 showcase-demo 行为的特殊要求 (默认听众, 时长偏好, 哪几幕重点练, 追问狠不狠; 没有就按默认). 顺便确认那份讲故事底稿是否偏离了默认七幕主线.
- **publish 口径**: `05-showcase-publish.md` 里需要创作者兜底的取舍 (哪些 borderline 项默认保留还是问, commit plan 侧重, 有没有额外要删或要留的东西). 没有就按 spec 默认.

自由说明里已经给到的直接采纳, 只补没给的.

### Phase 4 — 写 5 份 doc

按各自规范写到 `docs/showcase/`:

- `01-showcase-learn.md` (依 docs-showcase-learn-spec): #1 学习素材 + #2 引导路径.
- `02-showcase-runbook.md` (依 docs-showcase-runbook-spec): 一次性 setup + 推进中操作, 把隐性步骤显式化.
- `03-showcase-quiz.md` (依 docs-showcase-quiz-spec): 指向 Phase 2 定位到的题库真身, 加上考法自定义.
- `04-showcase-demo.md` (依 docs-showcase-demo-spec): 指向 Phase 2 定位到的讲故事底稿, 记下默认七幕主线与排练自定义.
- `05-showcase-publish.md` (依 docs-showcase-publish-spec): 自包含的 publish 清单. cardinal 删除的 glob 要对这个 repo 展开成真实文件清单; commit plan 要引这个 repo 的真实文件并按依赖排序; borderline 与敌意扫描规则照 spec 五块写全.

这几份是给 AI/skill 看的元文件, 全英文, 不走 cn-first. 溯源一律用 markdown 链接加 header 或关键字, 不用 line no. 猜不准的地方显式标注请创作者确认, 不许凭空编.

### Phase 5 — 落 4 个子 skill

把四个模板拷成真正的 skill, 并让它们**自包含** (学生 repo 里没有 lesson-smith, 每个 skill 必须自带交互模式).

交互模式的落地方式固定是**拷贝进 ref/ 再加载, 不是内联**, 必须严格照此, 别自作主张改成别的形式:

- 做法: 把英文权威版 `ref/agent-skill-interaction-pattern.md` 原样拷一份进每个生成 skill 的 `ref/` 下; SKILL.md 通过读取它自己 `ref/` 下那份 (bundled) 来加载. 模板里 "Interaction base" 那节只有一句话摘要加一个指向 bundled 全文的指针, 那句摘要不等于把规范内联了.
- 不要把交互模式全文内联进 SKILL.md: 会让 SKILL.md 臃肿, 也会和权威版各自漂移.
- 不要让生成的 skill 在运行时去 lesson-smith 里加载交互模式: 学生 repo 里根本没有 lesson-smith.
- 为什么是拷贝: 生成的 skill 要在没有 lesson-smith 的学生 repo 里独立运行, 每个 skill 靠自带这份副本做到自包含; 权威版仍是 lesson-smith 里那一份, 改了它下次 forge 或 refresh 会重新拷入.

具体拷贝:

- `ref/showcase/showcase-learn.SKILL.md` → `.claude/skills/showcase-learn/SKILL.md`
- `ref/showcase/showcase-quiz.SKILL.md` → `.claude/skills/showcase-quiz/SKILL.md`
- `ref/showcase/showcase-demo.SKILL.md` → `.claude/skills/showcase-demo/SKILL.md`
- `ref/showcase/showcase-publish.SKILL.md` → `.claude/skills/showcase-publish/SKILL.md`
- `ref/agent-skill-interaction-pattern.md` (英文权威版) → 各拷一份到上面四个 skill 的 `ref/agent-skill-interaction-pattern.md`.

模板近乎全静态, 落地时只需核对: 每个 SKILL.md 都固定加载它自己 ref/ 下那份交互模式 (路径已写死在模板里), 且对 `docs/showcase/` 的引用路径正确.

### Phase 6 — Verify 与汇报

1. 列出创建或更新的文件 (5 份 doc + 4 份 SKILL.md + 4 份 bundled 交互模式).
2. sanity check: 每个 SKILL.md 都引到 `docs/showcase/` 下对应的文件; 每个生成的 skill 的 `ref/` 下都有 `agent-skill-interaction-pattern.md`, 且 SKILL.md 固定加载了它; 5 份 doc 都非空; publish 清单里的 cardinal 删除已展开成真实文件而非停在 glob.
3. 用 uvx 跑 `lesson-smith lint` 看仓库结构是否仍合规 (`uvx --from shsk-lesson-smith==<version> lesson-smith lint -p .`; `<version>` 与 pin 版本的说明见 lesson-smith skill 的 `ref/repo-layout.md` 第 6 节, 本地已装 package 则直接 `lesson-smith lint`).
4. 告诉用户: 用 `/showcase-learn` 开始学, `/showcase-quiz` 自测, `/showcase-demo` 排练讲法, 学完用 `/showcase-publish` 发布; `docs/showcase/` 里哪里不对直接改, 或 `refresh <name>` 重生成一份.

## 约束

- 只写 `docs/showcase/` 与 `.claude/skills/showcase-{learn,quiz,demo,publish}/`; 不碰源码, 不动 examples 内容.
- 题目本身不在这里出, 讲故事底稿也不在这里写: 题库真身与讲故事底稿都由创作者在各自的 mini task 里手写, forge 只负责定位它们并写好 `03` 与 `04` 的指针.
- publish 清单 forge 只生成, 不执行: 真正的删除, 重写, 发布是学生后来跑 `/showcase-publish` 时的事.
- 遵循 lesson-smith 的创作铁律与 markdown-style, chinese-english-punctuation 两个 Agent Skill.
