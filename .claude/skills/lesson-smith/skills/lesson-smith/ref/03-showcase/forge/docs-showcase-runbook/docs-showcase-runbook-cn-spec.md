# docs/showcase/02-showcase-runbook-cn.md 规范, 中文版

**适用范围**: showcase 类型 repo 的 `docs/showcase/02-showcase-runbook-cn.md`, 由 `lesson-smith-showcase-forge` 生成, 给 `showcase-learn-cn` skill 消费.

**配套骨架**: [docs-showcase-runbook-cn-template.md](docs-showcase-runbook-cn-template.md).

**当前只产这一套**: 英文版规范与骨架就在同目录下, 但 forge 现在只产 `-cn`.

**链接一律指 `-cn`**: 指向 repo 内文档的链接都写 `-cn.md`. 指向代码与配置文件 (`mise.toml`, `.py` 之类) 不受此限, 它们没有语种.

---

## 1. 它是什么

**把课程跑起来的操作手册.**

它只管 "怎么把要学的东西跑起来":

- 不讲知识 (知识在 `examples/` 和素材里).
- 不做索引 (那是 `01-showcase-learn-cn.md` 的活).

---

## 2. 核心原则

**把导师默认懂, 但学生 follow 时不懂的隐性操作显式写清.** 这是这份 doc 的价值所在.

导师做的时候有经验, 一看目录结构就知道该 cd 到哪, 该先跑哪个命令, 往往不会显式说; 学生照着 `examples/` 走却会卡住. 凡是这类 "**没写出来但必须做**" 的步骤, 都要在这里补明白.

---

## 3. 两块内容

**第一块, 开始 `examples/` 之前的一次性 setup**: 前置工具与版本, 首次 setup 的命令. 这些命令大多已经在 `mise.toml` 里 (tasks 与工具版本), **原样引过来, 不改写**.

**第二块, 推进 `examples/` 过程中的操作**: 一切和 "把例子, 把要学的东西跑起来" 相关的动作. 例如切目录 (`cd`), 设环境变量, 起服务, 以及跳出命令行的操作 (注册某个账号, 在浏览器里 setup 某个东西).

**精炼原则**: `examples/` 如果只是标准地一个个往前推, 没有额外操作, 就**用一两句概括整体节奏, 不要逐个枚举**. 只有某一步需要跳出常规 (注册账号, 浏览器 setup, 切到某个特殊目录等), 才把那一步单拎出来单独说.

---

## 4. 写作原则

- **命令原样可跑, 逐字照抄**, 不要转述或改写. 命令本身不翻译.
- 需要指向文件时用 markdown 链接, 定位用 header 或关键字, 不用 line no.
- **没有内容的小节保留标题**, 写一句占位 (例如 "暂时没有, 遇到了再补"), 不要整节删掉.
- 遵循 markdown-style 与 chinese-english-punctuation 两个 Agent Skill.
