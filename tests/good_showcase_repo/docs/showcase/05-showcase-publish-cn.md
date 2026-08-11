# GitHub 基础协作 发布清单

> showcase-publish-cn skill 靠这份文档把这个教学 repo 转成作品 repo. 机器友好: 路径和表格, 不写散文. 针对这一棵树生成, 里面的 glob 已经展开成真实路径.

## 1. 铁律删除

下面每一项都一眼暴露教学来源, 发布前必删.

- path: `README-ORIGINAL-cn.md`, `README-ORIGINAL.md`
  reason: 对外的课程电梯陈述, 只有教学 repo 才有
  detected_by: 文件名匹配
- path: `lm.json`, `docs/tasks/`, `docs/showcase/`
  reason: lesson-smith 的清单与它生成的汇总视图
  detected_by: 文件与目录存在性
- path: `.claude/skills/showcase-learn-cn/`, `.claude/skills/showcase-quiz-cn/`, `.claude/skills/showcase-demo-cn/`, `.claude/skills/showcase-publish-cn/`
  reason: 四个生成的子 skill
  detected_by: 目录存在性
- path: `examples/01-overview/` (整个目录)
  reason: 索引 Task, 是教学阶段的地图而不是作品内容
  detected_by: 固定在 01 这个位置
- path: `examples/06-prove-i-get-it/`, `examples/07-how-i-build-this/`, `examples/08-level-up/` (整个目录)
  reason: 自测, 讲故事, 回顾, 都不是作品本身. 这三个连着排在最末. 只有排在 quiz 之前的技术 Task 保留, 那些归第 3 节处理
  detected_by: 从 quiz Task 的位置往后
- path: `TICKET.md`, `TICKET-cn.md`, `examples/02-create-repo/TICKET.md`, `examples/02-create-repo/TICKET-cn.md`, `examples/03-edit-files/TICKET.md`, `examples/03-edit-files/TICKET-cn.md`, `examples/04-git-branch/TICKET.md`, `examples/04-git-branch/TICKET-cn.md`, `examples/05-merge-branch/TICKET.md`, `examples/05-merge-branch/TICKET-cn.md`
  reason: 教学任务卡, 根目录和每个 Task 下都有
  detected_by: 文件名匹配
- path: 无
  reason: 这个 repo 里没有 `examples/_lm-*.md` 创作底稿
  detected_by: 文件名匹配

## 2. 语种收敛

作品 repo 只带一个语种. 这棵树里**内容全在 `-cn` 那一版**, 无后缀的英文文件是留空的占位符, 已经逐个打开确认过大小为 0.

- 保留的语种: `-cn`, 因为内容在那一版
- 删除 (留空的英文占位符, 真实路径):
- `README.md`
- `examples/02-create-repo/README.md`
- `examples/03-edit-files/README.md`
- `examples/04-git-branch/README.md`
- `examples/05-merge-branch/README.md`
- 删完再改名:
- `README-cn.md` 改成 `README.md`
- `examples/02-create-repo/README-cn.md` 改成 `examples/02-create-repo/README.md`
- `examples/03-edit-files/README-cn.md` 改成 `examples/03-edit-files/README.md`
- `examples/04-git-branch/README-cn.md` 改成 `examples/04-git-branch/README.md`
- `examples/05-merge-branch/README-cn.md` 改成 `examples/05-merge-branch/README.md`

**先删后改名**, 否则改名会覆盖掉刚留下的文件. 各 TICKET 与 README-ORIGINAL 已在第 1 节整组删掉, 不进这一节.

## 3. 待定项

- path: 排在 quiz 之前的技术教学 Task, 即 `examples/02-create-repo/` 到 `examples/05-merge-branch/`
  reason: 这是作品内容, 但这门课全程在浏览器里走, 没有代码产物, 所以这几个 Task 就是全部内容. 留下它们意味着要把那股教学口吻改写掉, 顺带重新想想还叫不叫 `examples/`. 另一个选项是发布你当时真正练手的那个 GitHub repo, 把这一个留成 private
  default: ask

_(除了那些 Task 之外没有别的, 这个 repo 里没有 `tmp/`, 没有草稿笔记.)_

## 4. 按依赖排序的 commit 计划

| # | 文件 | 建议的 commit message (第一人称过去时) | 理由 |
| :- | :--- | :--- | :--- |
| 1 | `mise.toml` | Set up the project root | 根配置, 其余都长在它上面 |
| 2 | 改写后的 `examples/02-create-repo/README.md` | Write up how I created the repository | 第一步, 不依赖别的 |
| 3 | 改写后的 `examples/03-edit-files/README.md` | Write up committing changes from the web editor | 依赖上一条建好的 repo |
| 4 | 改写后的 `examples/04-git-branch/README.md` | Write up isolating work on a branch | 依赖已经有 commit 历史 |
| 5 | 改写后的 `examples/05-merge-branch/README.md` | Write up reviewing and merging a Pull Request | 依赖上一条的 branch |
| 6 | `README.md` | Write the project README | 门面, 最后写 |

## 5. README 大纲

- 语种: 问学生一次. 公开作品用英文很常见, 哪怕课程内容是中文的
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

- 铁律删除物残留 (HIGH): glob `README-ORIGINAL*`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET*.md`. 报出确切路径.
- 还留着带语种后缀的文件 (HIGH): glob `**/*-cn.md`. 作品 repo 不该有语种体系.
- README 里的教学口吻 (HIGH): grep README 与根目录 `*.md`, 找 "本教程", "这门课", "我们学过", "作为学生".
- commit message 里的教学口吻 (MEDIUM): 同一套措辞过 `git log --all --format="%s%n%b"`.
- git ref 暴露课程来源 (MEDIUM): `git tag --list` 与 `git branch --all`, 找 `01-showcase`, `tutorial-base`, `from-course`, `original`.
- 残留的子 skill 目录 (HIGH): 任何还在的 `.claude/skills/showcase-*` 或 `docs/showcase/`.
- 卫生问题 (LOW): `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/`.
- 可疑的雷同 (MEDIUM): 多个文件同模板生成的注释横幅或结构. 报出来即可, 不强制改.
