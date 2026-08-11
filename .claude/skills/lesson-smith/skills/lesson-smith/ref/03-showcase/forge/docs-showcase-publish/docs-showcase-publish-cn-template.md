# [课程名] 发布清单

> showcase-publish-cn skill 靠这份文档把这个教学 repo 转成作品 repo. 机器友好: 路径和表格, 不写散文. 针对这一棵树生成, 里面的 glob 已经展开成真实路径.

## 1. 铁律删除

[下面每一项都一眼暴露教学来源, 发布前必删. 每个 glob 都展开, 真实匹配一条条列出来.]

- path: `README-ORIGINAL-cn.md` (及其余各语种)
  reason: 对外的课程电梯陈述, 只有教学 repo 才有
  detected_by: 文件名匹配
- path: `lm.json`, `docs/tasks/`, `docs/showcase/`
  reason: lesson-smith 的清单与它生成的汇总视图
  detected_by: 文件与目录存在性
- path: `.claude/skills/showcase-learn*/`, `.claude/skills/showcase-quiz*/`, `.claude/skills/showcase-demo*/`, `.claude/skills/showcase-publish*/`
  reason: 四个生成的子 skill
  detected_by: 目录存在性
- path: `examples/01-title/` (整个目录)
  reason: 索引 Task, 是教学阶段的地图而不是作品内容
  detected_by: 固定在 01 这个位置
- path: `examples/NN-prove-i-get-it/`, `examples/NN-how-i-build-this/`, 以及最后那个收尾 Task (整个目录)
  reason: 自查, 讲故事, 回顾, 都不是作品本身. 这三个连着排在最末. 只有排在 quiz 之前的技术 Task 保留, 那些归第 3 节处理
  detected_by: 从 quiz Task 的位置往后
- path: `**/TICKET*.md`
  reason: 教学任务卡, 根目录和每个 Task 下都有
  detected_by: 文件名匹配
- path: `examples/_lm-*.md`
  reason: 创作底稿
  detected_by: 文件名匹配

## 2. 语种收敛

[作品 repo 只带一个语种. 先定哪一版留下, 删掉其余各版, 最后去掉后缀. 判断哪个是占位符要去读文件内容, 不许只看后缀.]

- 保留的语种: [例如 `-cn`, 因为内容在那一版]
- 删除 (留空的占位符与其余各版, 列真实路径, 不留 glob):
- [README.md]
- [examples/02-title/README.md]
- [...]
- 删完再改名:
- [README-cn.md] 改成 [README.md]
- [examples/02-title/README-cn.md] 改成 [examples/02-title/README.md]
- [...]

## 3. 待定项

[不是明显教学但值得再看一眼的. 交给学生判断, 不要自己删.]

- path: 排在 quiz 之前的技术教学 Task
  reason: 这是作品内容, 但那股教学口吻以及 `examples/` 这个命名可能要改写得不像教程
  default: ask
- path: [例如 `tmp/`, `notes/`, `*.draft.md`]
  reason: [看着像本地草稿]
  default: [keep 或 ask]

_(除了那些 Task 之外没有别的, 就写: 这个 repo 里没有.)_

## 4. 按依赖排序的 commit 计划

[最不依赖别人的先提交, 让 history 读起来像自然长出来的. 用这个 repo 的真实路径. 最后一条永远是手写的 README.]

| # | 文件 | 建议的 commit message (第一人称过去时) | 理由 |
| :- | :--- | :--- | :--- |
| 1 | [根配置, 例如 mise.toml, pyproject.toml, .gitignore] | Set up the toolchain | 根配置, 其余全都长在它上面 |
| 2 | [共用骨架或工具函数] | Add the base structure | 后面的东西依赖它 |
| ... | [内容文件, 一个 commit 一个] | [Add / Wire up / Document ...] | [谁依赖谁] |
| N | README.md | Write the project README | 门面, 最后写 |

## 5. README 大纲

[publish skill 陪学生共写 README 时 follow 的结构. 干净的作品口吻: 绝不出现 "教程", "本课", "我们学过". 全文 250 到 500 词.]

- 语种: [问学生一次. 公开作品用英文很常见, 哪怕课程内容是中文的]
- section: 项目是什么
  goal: 这是个什么东西, 谁会在乎, 用学生自己的话说
  prompts: ["一句话, 这是个什么?", "谁会在乎它?", "它让你能做到什么?"]
  length: 60 到 100 词
- section: 怎么装怎么跑
  goal: 从 clone 到跑出东西的最短路径
  prompts: ["最短的一串命令是什么, 跑完能出结果?"]
  length: 40 到 80 词
- section: 我做了什么, 它怎么工作
  goal: 这活的形状, 加一个值得说的设计取舍
  prompts: ["主要有哪几块?", "有哪个决定是你现在还觉得做对了的?"]
  length: 80 到 140 词
- section: 我学到了什么
  goal: 具体的东西, 不是套话
  prompts: ["什么事让你意外?", "最难的是哪一段, 你怎么过去的?"]
  length: 60 到 120 词
- section: 下一步 (可选)
  goal: 一个诚实的下一步
  prompts: ["再给你一周, 你会加什么?"]
  length: 40 到 80 词

## 6. 敌意扫描规则

[假设读者就是在找破绽. 每一类给探测方式和严重度.]

- 铁律删除物残留 (HIGH): glob `README-ORIGINAL*`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET*.md`. 报出确切路径.
- 还留着带语种后缀的文件 (HIGH): glob `**/*-<locale>.md`. 作品 repo 不该有语种体系.
- README 里的教学口吻 (HIGH): grep README 与根目录 `*.md`, 找 "本教程", "这门课", "我们学过", "作为学生".
- commit message 里的教学口吻 (MEDIUM): 同一套措辞过 `git log --all --format="%s%n%b"`.
- git ref 暴露课程来源 (MEDIUM): `git tag --list` 与 `git branch --all`, 找 `01-showcase`, `tutorial-base`, `from-course`, `original`.
- 残留的子 skill 目录 (HIGH): 任何还在的 `.claude/skills/showcase-*` 或 `docs/showcase/`.
- 卫生问题 (LOW): `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/`.
- 可疑的雷同 (MEDIUM): 多个文件同模板生成的注释横幅或结构. 报出来即可, 不强制改.
