# 教学仓库 Retrofit 工作流 (旧 repo 改造)

这份文档定义如何把一个内容已经够好, 但不符合 lesson-smith 规范的旧 repo, 改造成一个合规的新 repo. 它由 lesson-smith-retrofit skill 加载, AI 按这份剧本带着创作者往前走.

它随 lesson-smith-retrofit skill 自包含 (住在这个 skill 自己的 `ref/` 下), 不放进基座 lesson-smith. 因为 retrofit 是过渡性的: 旧 repo 全部改造完之后, 整个 lesson-smith-retrofit 目录直接删掉即可, 基座不留痕迹. 但下面提到的各类 spec 仍以基座 lesson-smith 的 `ref/` 为准, 本文档不复制它们.

retrofit 与从零创作的关系: **retrofit 就是 author, 不是别的东西**. 区别在于从零创作时那一段是创作者一篇篇构思写出来的, 而这里 90% 的内容早就写在旧 repo 里了, 所以 AI 的主要活儿变成 "知道去哪找到旧材料, 再把它映射进新布局", 剩下的判断交给创作者拍板. 也因此 retrofit 只覆盖内容那一段, 精修做完就结束: 统稿往后决策密度高, 必须创作者亲自跑.

三种类型 (readup, upskill, showcase) 共用这一份剧本. 差异只有两处, 分别收在第 5 步和第 6 步的表里.

前置: 创作者以中文为母语, 遵循创作铁律 (先写 cn, 全部定稿后一次性重写成 en, 见 rewrite-en-spec.md) 和 markdown-style, chinese-english-punctuation 两个 Agent Skill.

## 1. 认清类型与两个 repo

全程有两个 repo, 角色分明, 不要搞混:

- **新 repo**: retrofit 在这里跑 (当前工作目录), 所有产物都落在这里. 它已经 clone 好, 脚手架与 `lm.json` 就绪, retrofit 不负责初始化它.
- **旧 repo**: 创作者给的本地绝对路径, 已 clone 到本地. **全程只读**, 唯一的例外是第 2 步的 checkout. 绝不在旧 repo 里写文件, 提交, 或丢弃创作者的未提交改动.

目标类型读新 repo 根目录的 `lm.json`, `type` 字段就是唯一真相, 不要从 repo 名字或目录结构猜.

以下任一条不满足就停下问创作者, 不要硬着头皮往下走: 新 repo 没有 `lm.json`; `type` 不是 readup, upskill, showcase 三者之一 (例如 `evolve`, 目前 retrofit 不支持); 创作者没给旧 repo 路径; 那个路径不存在或不是一个 git repo.

---

## 2. 把旧 repo 切到最大的教学 branch

列出旧 repo 的全部 branch (含 remote), **只看序号在 50 以下的那些**, 取序号最大的一个 checkout 过去, **然后才开始探索**.

顺序不能反. 不同 branch 的教程内容不一样, 序号越大的 branch 内容越全; 在错的 branch 上探索会漏掉后面几课.

为什么以 50 划线: 序号 50 及以上 (例如 98, 99) 留给归档, 实验这类非教学用途的 branch, 它们不是课程内容.

旧 repo 的 branch 名可能带大小写 (例如 `08-Control-Output-Format`), 挑选时只看开头那两位数序号, 不要被大小写干扰. 如果有未提交的改动导致切不过去, 停下告诉创作者, 不要自作主张 stash 或丢弃.

---

## 3. 探索旧 repo, 定位要迁移的材料

### 3.1 先判断旧 repo 是哪种形态

| 形态 | 判据 (只看序号 < 50 的 branch) | 课程材料在 | 截图在 |
| :--- | :--- | :--- | :--- |
| learn-this-project | 只有一个, 名为 `01-Learn-This-Project` (大小写不敏感) | `examples/NN-title/` 与 `docs/learn-this-project/` | 通常已在各 mini task 目录内 |
| 多 branch 教程 | 有 `01`, `02`, ... 多个 | `docs/tutorials/NN-Title/` | `img/NN-Title/` |

learn-this-project 是要被 showcase 取代的那套旧规范, 它的布局已经接近新规范, 迁移主要是重命名与补齐. 多 branch 形态离新规范远一些, 迁移动作更大.

上面是常见落点, 不是铁律. 判完形态仍要实际列一遍目录确认材料真在那里; 找不到就问创作者, 不要猜一个路径继续往下走.

### 3.2 无论哪种形态, 都要额外探这三处

这三处不属于课程正文, 但很可能要一起迁过去:

1. **源代码**: 读旧 repo 的 `pyproject.toml` 取包名, 然后看 `<package_name>/**/*.py` 与 `tests/**/*.py`. **包名在新 repo 通常不一样, 迁的时候必须一并改写**: 目录名, import 语句, `pyproject.toml` 里的 name, 以及测试里的引用.
2. **mise.toml**: 和新 repo 的那份对比一下, 旧 repo 可能有额外的依赖或 task 要搬过来. 是补差集, 不是整份覆盖.
3. **AI 配置**: `.claude/agents/`, `.claude/skills/`, `.claude/prompts/` 下的东西也可能要复制. 新 repo 已有同名的就跳过, 不要覆盖.

旧 repo 的 `README-ORIGINAL` 和旧的 Syllabus 只读来理解课程定位, 不迁 (理由见 4.2 最后一条).

### 3.3 产出一张迁移清单

探索完不要直接动手. 先把清单摆给创作者过目: 旧 repo 停在哪个 branch, 判成哪种形态, 每个旧 tutorial 或 mini task 映射到新 repo 的哪个路径, 截图有几张各归到哪, 源代码与 AI 配置各要搬什么.

清单写进新 repo 的 `examples/_lm-example-plan.md` (可进 git), 复用 author 那套约定. 创作者点头之后再进第 4 步.

---

## 4. 迁徙

这一步把旧 repo 已有的内容整体合并进新 repo. 走完之后, 课程主线就算告一段落.

### 4.1 先问清人类把关的几件事

下面这几件事机器猜不出, 必须问. 创作者可能在调用时就主动说了 (见本 skill 自带的输入模板 `prompts/run-lesson-smith-retrofit.md`), 说了的直接采纳, 没说的照通用交互模式一次问一件, 能给选项就给选项:

- **是不是全部保留**: 旧 repo 的每一课都要迁吗, 有没有过时的, 太窄的, 或和新 repo 定位不符的要砍掉.
- **顺序要不要调整**: 迁过来之后照旧编号, 还是重排.
- **要不要增加新内容**: 有没有旧 repo 里没有, 这次想补上的课.
- **截图怎么处理**: 默认复制到对应的 `examples/NN-title/` 下 (映射规则见 4.2), 创作者另有要求就照他的.
- **除课程内容以外的内容怎么处理**: 把 3.2 探到的源代码, `mise.toml` 差集, AI 配置逐项确认搬还是不搬.

### 4.2 映射规则

- **目录名全部转小写**: 旧的 `05-Mastering-Artifacts` 变成新的 `examples/05-mastering-artifacts`. 新规范里 branch 名与目录名一律小写加连字符.
- **一课一目录**: 旧的一个 tutorial 或 mini task 目录, 对应新的一个 `examples/NN-title/`, 里面是 `README.md`, `README-cn.md`, `TICKET.md`, `TICKET-cn.md`.
- **语种补齐**: 旧 repo 常常只有单语 (例如只有 `TICKET.md` 没有 `TICKET-cn.md`), 新 repo 要按 `supported-languages.json` 补齐. 照创作铁律, 缺中文就先补中文, 再据此产出英文.
- **链接跟着语种走**: 迁过来的正文里指向 repo 内其他**文件**的相对路径链接, `-cn.md` 里一律链 `-cn` 版, 英文文件里一律链英文版; 指向**目录**的链接不带语种后缀, 两边一样. 旧 repo 常常只有单语链接, 补语种时要顺手把后缀改对. 后面产英文版时这条由重写管线自己兜底 (见基座的 `ref/rewrite-en-spec.md` 第 5 节), 不用再显式交代. 顺带: 旧 repo 里若有目录名带 `-cn`, 那是命名错误, 迁过来时改掉.
- **截图跟着课走**: 旧的 `img/05-Mastering-Artifacts/05-Mastering-Artifacts-1.png` 变成新的 `examples/05-mastering-artifacts/img/05-mastering-artifacts-1.png`, 文件名一并转小写; 正文里的引用改成 `./img/...` 的相对路径.
- **正文不是原样照抄**: 迁过来的内容要按基座的 `ref/00-common/03-task-readme-spec/` 与 `ref/00-common/04-task-ticket-spec/` 重整 (补 frontmatter 的 description, H2 从 1 连续编号并加分隔线, H1 的字符限制等), 还要按创作者在 4.1 里给的 "更新" 口径改内容.
- **旧的索引类文件不搬**: 旧 repo 的 `docs/tutorials/Syllabus.md`, `about.md`, `about-cn.md`, 以及旧的 `README-ORIGINAL` 都不迁. 它们的角色在新规范里分别由 sync 生成的 SYLLABUS 和后面那一步重写的 README-ORIGINAL 接管, 现在搬过去也只会被覆盖.

### 4.3 迁完交给创作者逐篇读

迁徙不是一锤子买卖. 一遍过完之后, 创作者会一篇篇读你改出来的东西, 边读边改, 也可能顺手加新课. 你的活儿是配合他改, 直到他说主线可以了, 再进第 5 步.

---

## 5. 精修

旧 repo 里通常没有, 且人类重度参与的那些环节, 在这一步补齐:

| type | 精修要补的环节 |
| :--- | :--- |
| readup | 开头篇, 结尾的梳理与拔高篇, 各 mini task 之间的承上启下 |
| upskill | 上面三项, 外加 quiz 题库 mini task (`examples/NN-prove-i-get-it`) |
| showcase | 上面三项, 外加 quiz 题库, 以及 demo 讲故事底稿 mini task (`examples/NN-how-i-build-this`, 排在 quiz 之后, 收尾之前) |

开头篇一般是 overview, 综述, 讲清这门课的意义, 背景与怎么学; 结尾篇梳理学了什么, 学完到什么水平, 并给出拔高方向 (几个搜索关键字加一句话话题, 方便创作者的学生直接喂给 AI 深挖). 承上启下是把各 mini task 之间的衔接补顺, 让它读起来是一条线而不是一堆独立文章.

各环节照本类型的 spec 写, 全部到基座 lesson-smith 的 `ref/` 下读:

- 开头篇与结尾篇是普通教学 mini task, 走 `ref/00-common/03-task-readme-spec/` 与 `ref/00-common/04-task-ticket-spec/`.
- quiz 题库走 upskill 的 `ref/02-upskill/upskill-quiz-readme-spec/` 或 showcase 的 `ref/03-showcase/showcase-quiz-readme-spec/`, 它的 TICKET 走同目录下对应的 quiz-ticket-spec.
- demo 底稿走 `ref/03-showcase/showcase-demo-readme-spec/`, 它的 TICKET 走 `ref/03-showcase/showcase-demo-ticket-spec/`.
- `examples/README` 系列索引走本类型的 examples-readme-spec, 迁徙改完编号顺序之后要重写它.

这一步 AI 提建议, 人类拍板. quiz 的题目清单尤其要先讨论几轮再动笔, 做法照本类型 authoring workflow 里 quiz 那一步 (规划写进 `examples/_lm-quiz-plan.md`).

---

## 6. 收尾: 交回创作流的后半段

精修做完, retrofit 的活儿就结束了. **后面那几步一律不要替创作者跑**: 统稿, 锻造, 写根目录文档决策密度高, 必须他亲自过, 自动化只会产出对不上的东西.

收尾时告诉创作者接下来敲哪条 step 命令:

| type | 接下来 |
| :--- | :--- |
| readup | `/lesson-smith-readup-author-step-07-to-08-bookends-and-converge` |
| upskill | `/lesson-smith-upskill-author-step-09-to-10-bookends-and-converge` |
| showcase | `/lesson-smith-showcase-author-step-10-to-11-bookends-and-converge` |

往后各自还有锻造 (upskill 与 showcase 才有), 写根目录文档, 出厂三步, 由那条线自己的 author skill 带.

顺带提醒两件事: SYLLABUS 与 `docs/tasks/` 快照由出厂那一步的 sync 生成, 现在不要手写; 根目录的 README, TICKET 与 README-ORIGINAL 归写根目录文档那一步, retrofit 全程不碰.
