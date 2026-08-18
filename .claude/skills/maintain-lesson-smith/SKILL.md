---
name: maintain-lesson-smith
description: "维护 lesson-smith 这个 Agent Skill 插件本身: 改基座 ref/ 下的规范, 改或新增某个 repo type 的 author / step / forge skill, 改 prompts 输入模板, 以及配套的 lint 与 sync package. 在本 repo 里要动 .claude/skills/lesson-smith/ 下任何东西时加载."
argument-hint: "[这次想改什么...]"
---

# maintain-lesson-smith

你是 lesson-smith 插件的维护者搭档. 本 skill 只装三样东西: **这个插件是干什么的, 它按什么规律组织, 改一处要连带改哪儿**. 具体这次要改什么由我在调用之后说.

---

## 1. lesson-smith 是干什么的

**让 AI 结构化地生产课程.** 一个 GitHub Repo 就是一门课 (Lesson), 一个 Task 是携带一对 `README` 与 `TICKET` 的最小单位, 一门课就是一串 Task. 插件把两件事固化下来:

- **写什么样**: 每种特殊文件 (README, TICKET, README-ORIGINAL, SYLLABUS) 该长什么形状, 由基座的 spec 规定, 并由 `lesson-smith lint` 机器校验.
- **按什么顺序写**: 从定题到出厂的一条创作流, 拆成带编号的步骤, 每步一条斜杠命令. 创作者一条条敲下去, 产出一门合规的课.

服务两类人: 创作者 (我) 用它写课, 学生用产出的 repo 学. 所以插件的每次改动都要问一句 "这是让创作更顺, 还是让学生学得更好", 两者都不沾的东西不加.

---

## 2. 地图与命名规律

约定两个简写, 下文不再写全路径: **插件根** = `.claude/skills/lesson-smith/`, **基座** = `<插件根>/skills/lesson-smith/`. 凡 `ref/`, `prompts/`, `SKILL.md` 不特别说明都指基座下的那一份.

**基座是唯一权威.** 那个不带任何后缀的 `lesson-smith` skill 装的是概念模型, 创作铁律, 以及一张 "什么时候该读 `ref/` 下哪一份" 的索引; **真正的规范全部住在 `ref/` 下**. 改规范就是改 `ref/`, 改基座 `SKILL.md` 通常只是改那张索引.

**`ref/` 两层**: `00-common/` 通用层, `01-readup/` `02-upskill/` `03-showcase/` (将来还会更多) 是特化层. 特化层只写差异.

**repo type 是插件的扩展维度.** 每多一类教学仓库, 就在 `ref/` 下多一个特化层, 同时在 `<插件根>/skills/` 下长出一组同构的 skill:

| 角色 | 命名 | 干什么 |
| :--- | :--- | :--- |
| 总入口 | `lesson-smith-<type>-author` | 加载基座与主剧本, 判断创作者在第几步, 告诉他该敲哪条 step 命令. 每个 session 开头敲一次 |
| step invoker | `lesson-smith-<type>-author-step-NN-<slug>` 或 `-step-NN-to-NN-<slug>` | 某一步 (或连着的几步) 的快捷启动: 只唤起那一步要读的规范与红线 |
| forge | `lesson-smith-<type>-forge` | 锻造学习工具链 (docs 与子 skill), 只有带工具链的 type 才有 |

- 每类的**主剧本**是 `ref/<NN-type>/<type>-authoring-workflow.md`, step skill 的编号与它的节一一对应, step skill 自己不重复剧本内容.
- `prompts/run-<skill-name>.md` 是给我填的**输入模板**, 只给决策密度高, AI 猜不出的那几次调用配 (目前是各 author 入口与各 forge). 模板顶部带用法说明和那条要敲的命令, 我把里面的 "无" 换成内容, 整份发出去.
- **一次性或过渡性的 skill** (如 `lesson-smith-retrofit`) 自包含: 主剧本与 prompts 放自己目录下, 不进基座, 用完整个目录删掉, 基座不留痕迹.
- 插件之外, 同一个 repo 里的 Python package `shsk_lesson_smith/` 提供 `lesson-smith lint` 与 `sync`, 是这套规范里机器可验证的那一半.

---

## 3. 分层铁律

维护时最容易破的就是这几条:

- **规范只有一个副本.** 所有 `lesson-smith-*` skill 都是薄包装, 只准指向基座 `ref/`, 不准复制规范正文.
- **先通用, 后特化.** 判据: 一条规则换一个 repo type 还成不成立. 成立就归 `00-common/`, 不成立才进特化层. 在特化层发现某条其实通用, 提回通用层, 不要复制多份.
- **三类是子集关系**: readup ⊂ upskill ⊂ showcase, 往右是加环节而不是换一套. evolve 不在这个同构关系里.
- **共享的代价是占位符**: 多类共用的素材里类型名写 `{{TYPE}}`, 落地时机械替换, 产出里 grep `{{` 必须 0 命中.
- **只写中文** (`-cn.md`), 无后缀的英文文件留空占位. 这是主动推迟的多语种模块, 不是欠账. 唯一中英对等且**改一版必须同步另一版**的是 `ref/agent-skill-interaction-pattern[-cn].md`.
- **`00-common/` 的序号是阅读顺序**, 新东西往后接, 不往中间插.

动手之前先读 `ref/ref-maintainer-README.md` (写给维护者本人, 讲清 `ref/` 为什么长成这样, 以及当前状态与欠账). 要新增或改动 spec 文件的形态, 再读基座的 `spec-file-format.md`.

---

## 4. 常见改动与它的连带面

漏掉连带面是这个插件最主要的返工来源, 因为多数不一致 lint 查不出来.

| 我要做的事 | 先读 | 改动落在 | 别忘了同步 |
| :--- | :--- | :--- | :--- |
| 改一条已有规范 | 基座 SKILL.md 的 ref 索引 | `ref/` 下那一份 | 确认它在对的那一层; 有没有哪个 skill 正文重复了这条 (有就删成指针) |
| 新增一份 spec | `spec-file-format.md` | 新 spec 目录 (spec 加 template) | 基座 SKILL.md 的索引; 用到它那一步的 step skill 的 "要读的规范" |
| 改某一步的做法 | 那一类的 authoring workflow | workflow 的那一节 | 对应 step skill; 那一步若有 prompt 模板 |
| 增删一个步骤 | 那一类的 authoring workflow | 步骤号与阶段划分表 | **所有引用步骤号的地方**: author 入口的判断表与命令清单, 各 step skill 开头, forge 的 "对应第 N 步", prompts 顶部那条命令 |
| 新增一个 repo type | `ref-maintainer-README.md` 第 1 节 | `ref/` 新特化层, 加一组同构 skill | 先把能共享的部分留在 `00-common/`; package 要认新 type (`linter_for_*.py`, `repo_for_*.py` 与 tests) |
| 改 lint 或 sync 规则 | package `shsk_lesson_smith/` | linter 或 sync 加 tests | 和 `ref/` 里对应那条规范对齐, 两边不许各说各的 |
| 改通用交互模式 | `ref/agent-skill-interaction-pattern-cn.md` | 中英两份一起改 | forge 会把它拷进生成的子 skill, 改完提醒我对已有 repo 跑 refresh |

---

## 5. 怎么和我协作

- 我调用之后会直接说要改什么. **先按上表定位到最小的那个改动面, 只读要读的那几份**, 不要通读 `ref/`.
- 改动跨多处时, 先把连带清单列给我确认再动手, 不要边改边扩散.
- 拿不准一条规则该进通用层还是特化层, 该进规范还是该进 skill 正文, 停下来问. 两边都写是最坏的结果.
- 改完汇报三样: 动了哪几份, 哪些引用被同步了, 哪些是故意没动的.
- 写任何 .md 遵循 `markdown-style` 与 `chinese-english-punctuation`; 写或改 SKILL.md 本身可以借 `author-agent-skill`.
- **版本号与发布不归这里管** (bump `plugin.json`, 打 tag, 更新 marketplace), 走 `maintain-claude-plugins`.
- 基座下的 `tmp/` 是历史工作记录, `archive/` 是已作废的规范 (中译英那一套). **两者都不是权威**, 不要当规范读, 也不要顺手更新.

---

## 6. 这次要改的

$ARGUMENTS

没给就按通用交互模式开场: 先说一句你看到的当前状态, 再问我这次想动哪一块, 一次一问.
