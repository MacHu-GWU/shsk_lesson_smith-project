# [课程名] 发布清单

> showcase-publish-cn skill 靠这份文档把这个教学 repo 转成作品 repo. 机器友好: 路径和表格, 不写散文. 针对这一棵树生成, 里面的 glob 已经展开成真实路径.

## 1. 铁律删除

[下面每一项都一眼暴露教学来源, 发布前必删. 每个 glob 都展开, 真实匹配一条条列出来.]

- path: `README-cn.md`, `README-ORIGINAL-cn.md` (及其余各语种, 根目录所有 `README*.md` 除了发布时新写的那份 `README.md`)
  reason: 教学入口与对外的课程电梯陈述, 只有教学 repo 才有
  detected_by: 文件名匹配
- path: `lm.json`, `docs/tasks/`, `docs/showcase/`
  reason: lesson-smith 的清单与它生成的汇总视图
  detected_by: 文件与目录存在性
- path: `.claude/skills/showcase-learn*/`, `.claude/skills/showcase-quiz*/`, `.claude/skills/showcase-demo*/`, `.claude/skills/showcase-publish*/`, 以及 `.agents/skills/` 下的同名四个
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
- 根目录 README 这一族不参与收敛: [根 `README.md` 现在是空占位符还是已有内容 (读过文件确认). 新 README 由 skill 发布时写进这个位置. 教学版 `README-cn.md` 走第 1 节直接删, 不改名]
- 删除 (留空的占位符与其余各版, 列真实路径, 不留 glob, 根目录 README 除外):
- [examples/02-title/README.md]
- [docs/some-doc.md]
- [...]
- 删完再改名:
- [examples/02-title/README-cn.md] 改成 [examples/02-title/README.md]
- [docs/some-doc-cn.md] 改成 [docs/some-doc.md]
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

[最不依赖别人的先提交, 让 history 读起来像自然长出来的. 用这个 repo 的真实路径. 最后一条永远是 README.]

| # | 文件 | 建议的 commit message (第一人称过去时) | 理由 |
| :- | :--- | :--- | :--- |
| 1 | [根配置, 例如 mise.toml, pyproject.toml, .gitignore] | Set up the toolchain | 根配置, 其余全都长在它上面 |
| 2 | [共用骨架或工具函数] | Add the base structure | 后面的东西依赖它 |
| ... | [内容文件, 一个 commit 一个] | [Add / Wire up / Document ...] | [谁依赖谁] |
| N | README.md | Write the project README | 门面, 最后提交 |

## 5. README 素材线索

[只写这个 repo 特有的素材在哪, 给 skill 当入口. 不是大纲: 信息块, 语气, 语种都在发布时按学生的意愿定. 以发布时读到的文件为准.]

- 故事在哪: [demo 讲故事底稿的真实路径, 以及它偏离默认七幕的地方 (若有)]
- 定位在哪: [`README-ORIGINAL-cn.md` 与根 `TICKET-cn.md` 的真实路径]
- 保留的主线 Task: [真实目录, 各一句话主题]
- 真实可跑的命令: [从 mise.toml, pyproject.toml 等读到的安装与运行命令, 只列读到的]
- 值得画成图的东西: [这个 repo 里真实存在的模块, 服务, 数据流, 各自在哪]
- 已有的视觉素材: [截图, 图片, 终端录屏的真实路径; 没有就写: 这个 repo 里没有]
- 徽章可用的事实: [语言与版本, 许可证, CI workflow 文件是否存在]

## 6. 敌意扫描规则

[假设读者就是在找破绽. 每一类给探测方式和严重度.]

- 铁律删除物残留 (HIGH): glob `README-ORIGINAL*`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `.agents/skills/showcase-*`, `**/TICKET*.md`. 报出确切路径.
- 根目录 README 不止一份 (HIGH): glob 根目录 `README*.md`, 只该剩一份 `README.md`.
- 还留着带语种后缀的文件 (HIGH): glob `**/*-<locale>.md`. 作品 repo 不该有语种体系.
- README 顶部还挂着 frontmatter (HIGH): `README.md` 第一行是 `---`.
- README 里的教学口吻 (HIGH): grep README 与根目录 `*.md`, 中英两套都找: "本教程", "这门课", "我们学过", "作为学生", tutorial, course, lesson, curriculum, syllabus, exercise, quiz, 以及 `showcase-`, `TICKET`, `lesson-smith`.
- README 里的死链与破图 (HIGH): `README.md` 里每个相对链接与本地图片路径都要解析得到; 指向 `.github/workflows/` 的徽章, 那个文件要存在.
- 选了英文却留着汉字 (HIGH): 只在学生选英文时查, Grep 搜 `\p{Han}` 查 `README.md`, 必须 0 命中.
- commit message 里的教学口吻 (MEDIUM): 同一套措辞过 `git log --all --format="%s%n%b"`.
- git ref 暴露课程来源 (MEDIUM): `git tag --list` 与 `git branch --all`, 找 `01-showcase`, `tutorial-base`, `from-course`, `original`.
- 残留的子 skill 目录 (HIGH): 任何还在的 `.claude/skills/showcase-*`, `.agents/skills/showcase-*` 或 `docs/showcase/`.
- 卫生问题 (LOW): `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/`.
- 可疑的雷同 (MEDIUM): 多个文件同模板生成的注释横幅或结构. 报出来即可, 不强制改.
