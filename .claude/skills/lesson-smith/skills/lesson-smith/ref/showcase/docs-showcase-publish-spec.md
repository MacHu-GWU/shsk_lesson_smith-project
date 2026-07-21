<!--
本文件是 docs/showcase/05-showcase-publish.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

本文件独立成篇, 不引用 ref/upskill/ 下任何文件; 需要引用时只引 ref/ 根目录的通用 spec.

定性: 这是 publish 清单, 由 lesson-smith-showcase-forge 生成, 给 showcase-publish skill 消费. publish 是 showcase 独有的对外环节: 把这个教学 repo 就地转成一个可以放上学生自己 GitHub 的 portfolio repo, 且一个敌意读者看不出它源自教学. 这份 doc 就是 "在这个具体 repo 里, 什么算教学痕迹, 怎么删, 怎么攒 commit, 怎么重写 README, 怎么做敌意扫描" 的针对性清单. 它没有 examples mini task 撑, 是自包含的 (quiz 与 demo 各自有 examples 撑, publish 没有).

适用范围: showcase 类型 repo 的 docs/showcase/05-showcase-publish.md. 这是给 AI/skill 看的元文件, 不给人类当教程读; 所以它产出内容全英文, 不走 cn-first 铁律. 因此下面的正文模板本身就是英文的. 它由 forge 针对当前 repo 生成, 里面的 glob 要在生成时对这个 repo 展开成真实文件清单, commit plan 要引真实文件路径, 不要停留在通用占位.

正文是五块, 就是下面五个 H2:

1. Cardinal deletes (铁律删除, 永不可发布). 每一项都是一眼就暴露 "这来自教学" 的文件或目录, 发布前必删. showcase 里通常包括: 各语种本地化 README (形如 README-cn.md, 任意深度, 用 glob 声明再展开成真实清单); README-ORIGINAL 及其语种; lesson-smith 的清单与汇总视图 (lm.json, docs/tasks 整个目录含 SYLLABUS 与快照, docs/showcase 整个目录); 四个生成的子 skill (.claude/skills 下的 showcase-learn, showcase-quiz, showcase-demo, showcase-publish); demo 那个 mini task (examples 下的 how-i-build-this 整个目录); quiz 那个 mini task (examples 下的 prove-i-get-it 整个目录); 各级 TICKET 及其语种 (根目录与每个 example 下的 TICKET, 是教学任务卡); 以及创作底稿 (examples 下的 _lm 开头的 plan 文件). 每项写清 path, reason, detected_by 三个字段.

2. Borderline items (待定项, 问学生). 对这个具体 repo 扫一遍, 找那些不是明显教学但可疑的东西, 交给学生判断而不是自动删. showcase 尤其要处理教学 example 本身: examples 下那些教学 mini task 是作品内容的载体, 通常保留, 但它们的教学口吻 README (以及 examples 这层的命名) 可能要改写得不像教程. 其它常见待定项: tmp 目录, 草稿笔记, 半成品. 每项写 path, reason, default (keep 或 ask).

3. Dependency ordered commit plan (按依赖排序的 commit 计划). 原则是最不依赖别人的先提交, 让 git history 读起来像自然长出来的. 针对这个 repo 的真实文件生成一张逐条表, 每条给 commit 号, 要 stage 的真实文件, 建议的 commit message (第一人称过去时), 一句 rationale. 最后一条永远是手写的 README. 通常 10 到 15 条起.

4. README co-write outline (英文, 分节). 这是 publish skill 陪学生共写 README 时 follow 的结构. showcase 的 README 要讲出这段作品的故事 (和 demo 的七幕主线一脉相承), 但用干净的 portfolio 口吻, 绝不出现 "这是个教程" "本课" "我们在这门课里" 之类. 每节给 section name, goal (一句), question prompts (2 到 4 个 publish skill 会问学生的问题), length target. 常见分节: Project description, Install and run, What I built and how it works, What I learned, What is next (可选). 整份 README 只用英文, 目标长度 250 到 500 词.

5. Hostile scan rules (敌意扫描规则, 供 audit 用). 假设一个敌意读者拿着 "这是不是来自教程" 的问题扫这个 repo. 给出规则类别加明确的探测方式, 每类标严重度: file pattern flags (文件名或目录名信号, 例如任意深度的 README locale 后缀文件, README-ORIGINAL, docs/tasks, docs/showcase, .claude/skills 下的 showcase 子 skill), README phrase flags (发布出的 README 里暴露教学口吻的措辞, 例如 this tutorial, this course, in this lesson, as a student, we learned), commit message phrase flags (同一套措辞用在 commit subject 与 body), git ref flags (tag 或 branch 名里暴露教学来源的, 例如 01-showcase, tutorial-base, from-course, original), residual directory flags (任何残留的 showcase 子 skill 目录或 docs/showcase), hygiene flags (.DS_Store, __pycache__, .venv, *.egg-info, .idea 等, 非教学特有但难看), suspicious symmetry flags (多个文件明显同模板生成的雷同注释或结构). 每类给严重度提示: HIGH RISK 一经命中即致命 (铁律删除物残留, 残留子 skill, 教学口吻 README); MEDIUM RISK 可恢复但显眼 (commit message 口吻, 难看的 hygiene, 雷同模板); LOW RISK 纯外观 (OS 垃圾文件, 缺 gitignore 条目).

格式与详略: 这份 doc 给 skill 消费, 不朗读给人听, 所以机器友好 (表格, 列表, 明确路径), 少写 skill 模板已经覆盖的散文解释. 某一块在这个 repo 确实没有内容 (没有 tmp, 没有待定项等) 也保留小节标题, 写 none found in this repo, 别整节删掉, publish skill 期望每节都在.
-->

# [Course Name] Publish Checklist

> The showcase-publish skill uses this doc to turn this teaching repo into a publish-ready portfolio repo. Machine-facing: paths and tables, not prose. Generated for this specific repo; globs below are expanded against the actual tree.

## 1. Cardinal Deletes — Never Publishable

[Every entry unambiguously signals a teaching origin and must go before publishing. Expand each glob against this repo and list real matches individually.]

- path: `**/README-<locale>.md`
  reason: locale README, a teaching-language counterpart to the English one
  detected_by: filename match (expand to every real hit, e.g. README-cn.md, examples/01-title/README-cn.md, ...)
- path: `README-ORIGINAL.md` (and locales)
  reason: outward lesson pitch, only exists for teaching repos
  detected_by: filename match
- path: `lm.json`, `docs/tasks/`, `docs/showcase/`
  reason: lesson-smith manifest and generated teaching views
  detected_by: dir / file presence
- path: `.claude/skills/showcase-learn/`, `.claude/skills/showcase-quiz/`, `.claude/skills/showcase-demo/`, `.claude/skills/showcase-publish/`
  reason: the four generated child skills
  detected_by: dir presence
- path: `examples/ZZ-how-i-build-this/`
  reason: the demo story mini task (pure teaching-process meta)
  detected_by: dir presence
- path: `examples/NN-prove-i-get-it/`
  reason: the quiz mini task (self-test bank)
  detected_by: dir presence
- path: `**/TICKET.md` (and locales)
  reason: teaching task cards at the root and in each example
  detected_by: filename match
- path: `examples/_lm-*.md`
  reason: authoring plan drafts
  detected_by: filename match

## 2. Borderline Items — Ask the User

[Bootstrap-time scan of this specific repo for not-obviously-teaching but suspicious content. Flag for the user's judgment; do not auto-delete.]

- path: `examples/` teaching mini tasks (the surviving example content)
  reason: this is the portfolio content, but the teaching-voice README and the examples/ naming may need rewriting so it does not read like a course
  default: ask
- path: [e.g. `tmp/`, `notes/`, `*.draft.md`]
  reason: [looks like local scratch]
  default: [keep | ask]

_(If none beyond the examples, write: none found in this repo.)_

## 3. Dependency-Ordered Commit Plan

[Least-dependent first, so history reads as a natural buildup. Real paths from this repo. Last commit is the hand-written README.]

| # | Files | Suggested message (first-person past tense) | Rationale |
| :- | :--- | :--- | :--- |
| 1 | [root config, e.g. mise.toml, pyproject.toml, .gitignore] | Set up the toolchain | root config; everything builds on it |
| 2 | [shared skeleton / utilities] | Add the base structure | depended on by the rest |
| ... | [individual content files, one per commit] | [Add / Wire up / Document ...] | [what depends on what] |
| N | README.md | Write the project README | the front door, written last |

## 4. README Co-write Outline (English)

[Section-by-section structure the publish skill co-writes with the user. Clean portfolio voice; never "tutorial" / "course" / "we learned". 250 to 500 words total.]

- section: Project description
  goal: what this is and who cares, in the user's own voice
  prompts: ["In one sentence, what is this?", "Who would care about it?", "What does it let you do?"]
  length: 60 to 100 words
- section: Install and run
  goal: minimum path from clone to running output
  prompts: ["What is the shortest command sequence to a working run?"]
  length: 40 to 80 words
- section: What I built and how it works
  goal: the shape of the work and one interesting design point
  prompts: ["What are the main pieces?", "What is one choice you are glad you made?"]
  length: 80 to 140 words
- section: What I learned
  goal: specific, not filler
  prompts: ["What surprised you?", "What was the hardest part and how did you get past it?"]
  length: 60 to 120 words
- section: What is next (optional)
  goal: one honest next step
  prompts: ["If you spent another week, what would you add?"]
  length: 40 to 80 words

## 5. Hostile-Scan Rules

[Assume a hostile reader asking "did this come from a tutorial?". Each category with detection and a severity tier.]

- File-pattern flags (HIGH): any `**/README-<locale>.md`, `README-ORIGINAL.md`, `docs/tasks/`, `docs/showcase/`, `.claude/skills/showcase-*`, `**/TICKET.md`. Glob and report exact paths.
- README phrase flags (HIGH): "this tutorial", "this course", "in this lesson", "as a student", "we learned", first-person-plural learning prose. Grep README.md and any root `*.md`.
- Commit-message phrase flags (MEDIUM): same phrase set over `git log --all --format="%s%n%b"`.
- Git ref flags (MEDIUM): `git tag --list` and `git branch --all` for names like `01-showcase`, `tutorial-base`, `from-course`, `original`.
- Residual directory flags (HIGH): any surviving `.claude/skills/showcase-*` or `docs/showcase/`.
- Hygiene flags (LOW): `.DS_Store`, `__pycache__/`, `.venv/`, `*.egg-info/`, `.idea/`.
- Suspicious symmetry flags (MEDIUM): identical comment banners or docstring shapes across many files (heuristic, surface not enforce).
