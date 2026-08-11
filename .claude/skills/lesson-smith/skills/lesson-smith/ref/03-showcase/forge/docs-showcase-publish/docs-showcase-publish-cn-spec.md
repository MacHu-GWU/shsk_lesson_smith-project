# docs/showcase/05-showcase-publish-cn.md 规范, 中文版

**适用范围**: showcase 类型 repo 的 `docs/showcase/05-showcase-publish-cn.md`, 由 `lesson-smith-showcase-forge` 生成, 给 `showcase-publish-cn` skill 消费.

**配套骨架**: [docs-showcase-publish-cn-template.md](docs-showcase-publish-cn-template.md).

**当前只产这一套**: 英文版规范与骨架就在同目录下, 但 forge 现在只产 `-cn`.

**自包含**: 和 quiz, demo 不一样, publish 在 `examples/` 下没有对应的 Task 撑着. skill 需要的一切都在这一份文件里.

---

## 1. 它是什么

**一份为这一个 repo 量身裁的清单.** publish 把教学 repo 就地转成学生可以放上自己 GitHub 的作品 repo, 而且一个带着敌意的读者看不出它源自教学.

这份 doc 回答的是, 在**这个** repo 里: 什么算教学痕迹, 怎么删, commit 怎么攒, README 怎么写, 最后怎么自查.

**要对着真实的树生成.** 每个 glob 都展开成实际匹配到的路径, commit 计划里引真实文件. 一份全是占位符的清单没人能照着执行.

---

## 2. 六个部分

skill 是按编号读这几节的, 所以**六节都要在, 顺序不能变**. 某一节在这个 repo 里确实没内容, 保留标题写一句 "这个 repo 里没有", 不要整节删掉.

### 2.1 铁律删除

一眼就暴露教学来源的文件与目录, 发布前必删, 没有商量. 每项写清 `path`, `reason`, `detected_by` 三个字段.

showcase 通常包括:

| 删什么 | 为什么 |
| :--- | :--- |
| `README-ORIGINAL` 及各语种 | 对外的课程电梯陈述, 只有教学 repo 才有 |
| `lm.json`, `docs/tasks/`, `docs/showcase/` | lesson-smith 的清单与它生成的汇总视图 |
| `.claude/skills/` 下四个生成的子 skill | learn, quiz, demo, publish |
| `examples/01-*/` 索引 Task | 教学阶段的地图, 不是作品内容 |
| quiz Task 及其之后的全部 Task | `NN-prove-i-get-it`, `NN-how-i-build-this`, 收尾 Task. 三个连着排在最末, 是自查, 讲故事和回顾, 都不是作品本身 |
| 各级 `TICKET` 及各语种 | 教学任务卡, 根目录和每个 Task 下都有 |
| `examples/_lm-*.md` | 创作底稿 |

只有排在 quiz **之前**的技术教学 Task 保留, 它们归下面的待定项处理.

### 2.2 语种收敛

**作品 repo 只带一个语种.** 一棵每个文件都有 "无后缀" 和 "带后缀" 两版的树, 本身就是 lesson-smith 的签名; 而留空的占位文件更糟, 看上去像烂尾.

所以清单必须写清三件事:

1. **哪个语种留下来.** 内容实际在哪一版就留哪一版. 中文单语种的 repo 里就是 `-cn`, 无后缀的英文文件是留空的占位符.
2. **其余各版全删**, 包括那些空占位符. 列成真实路径, 不要留 glob.
3. **留下来的那版去掉后缀.** `README-cn.md` 变 `README.md`, `docs/some-doc-cn.md` 变 `docs/some-doc.md`. **先删后改名**, 免得覆盖掉刚留下的文件.

**这一步做反了, 后果是把整门课删光, 留下一棵空文件的树, 而且后面没有任何一步会发现.** 所以判断哪个是占位符时**要去读文件内容**, 不许只看后缀就下结论.

### 2.3 待定项

不是明显教学但值得再看一眼的东西. **交给学生判断, 不要自动删.** 每项写 `path`, `reason`, `default` (keep 或 ask).

保留下来的教学 Task 永远在这张单子上: 它们是作品内容的载体, 但那股教学口吻, 以及 `examples/` 这个命名本身, 可能要改写得不像教程. 其它常见的: `tmp/`, 草稿笔记, 半成品.

### 2.4 按依赖排序的 commit 计划

最不依赖别人的先提交, 让 git history 读起来像自然长出来的, 而不是一坨砸下来的. 对着这个 repo 的真实文件生成一张逐条表: commit 号, 要 stage 的文件, 建议的 commit message (第一人称过去时), 一句 rationale.

最后一条永远是手写的 README. 通常 10 到 15 条起.

### 2.5 README 大纲

publish skill 陪学生共写 README 时 follow 的结构. README 要讲出和 demo 底稿一脉相承的故事, 但用干净的作品口吻: **绝不出现 "教程", "本课", "我们在这门课里" 这类措辞.**

每节给: 名字, 一句话目标, 2 到 4 个 skill 会问学生的问题, 长度目标. 常见分节是项目是什么, 怎么装怎么跑, 我做了什么以及它怎么工作, 我学到了什么, 以及可选的下一步. 全文 250 到 500 词.

**要写清 README 用什么语种.** 这件事不是自动的: 学生完全可能想在一个中文内容的 repo 上放一份英文 README, 那是合理的选择, 应该问他一次, 而不是替他定了.

### 2.6 敌意扫描规则

假设一个读者就是在找破绽. 每一类给出探测方式和严重度.

| 类别 | 严重度 | 怎么探测 |
| :--- | :--- | :--- |
| 铁律删除物残留 | HIGH | glob `README-ORIGINAL*`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET*.md` |
| 还留着带语种后缀的文件 | HIGH | glob `**/*-<locale>.md`. 作品 repo 不该有语种体系 |
| README 里的教学口吻 | HIGH | grep README 与根目录 `*.md`, 找 "本教程", "这门课", "我们学过", "作为学生" |
| commit message 里的教学口吻 | MEDIUM | 同一套措辞过一遍 `git log --all --format="%s%n%b"` |
| git ref 暴露课程来源 | MEDIUM | `git tag --list` 与 `git branch --all`, 找 `01-showcase`, `tutorial-base`, `from-course`, `original` |
| 残留的子 skill 目录 | HIGH | 任何还在的 `.claude/skills/showcase-*` 或 `docs/showcase/` |
| 卫生问题 | LOW | `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/` |
| 可疑的雷同 | MEDIUM | 多个文件同模板生成的注释横幅或结构. 报出来即可, 不强制改 |

**HIGH 一经命中即致命.** MEDIUM 可恢复但显眼. LOW 纯外观.

---

## 3. 写作原则

- **机器友好.** 表格, 列表, 真实路径. 这份文件是给 skill 读的, 没人会把它念出来. skill 模板已经覆盖的散文解释不要重复写.
- **空的小节也保留.** 这个 repo 没有 `tmp/`, 没有待定项, 也要留着标题写 "这个 repo 里没有". skill 期望六节都在.
- 每个 glob 都在生成时展开. 这份文件的意义就在于它是针对一个具体 repo 的.
- 遵循 markdown-style 与 chinese-english-punctuation 两个 Agent Skill.
