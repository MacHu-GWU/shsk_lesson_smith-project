# 教学仓库目录结构标准

这是通用层. evolve, readup, upskill, showcase 四类教学仓库共享这一套术语, 命名, 目录与 frontmatter 标准.

各类型在此之上特化. 特化文档只写差异, 不重复本文件; 本文件也不写任何一类的特有结构.

---

## 1. 术语

三个词, 全套规范里只用这三个, 不要另造同义词:

- **Lesson**: 一个 Repo 就是一门课.
- **Task**: 一门课里的一个任务. 它是**携带一对 README 与 TICKET 的最小单位**.
- **特殊文件**: `README`, `TICKET`, `README-ORIGINAL`, `SYLLABUS` 这四个有专属规范的文档.

关于 Task, 三条要记住:

- **README 与 TICKET 必然成对.** 有 Task 就有这两份, 一份说教什么, 一份说怎么验收.
- **Task 只是一个位置无关的单位.** 它可能落在 branch 根目录 (evolve), 也可能落在 `examples/NN-title/` 下 (readup, upskill, showcase). 落在哪里由类型的特化文档定, 规范本身是同一份.
- **人类嘴里的别名, 都映射回 Task.** 口头怎么说都行, 但**写进 spec 一律用 Task**, 否则各 spec 之间会对不上, 读的人以为是两种东西.
  - **tutorial**: 指一个 Task 里 `README` 那份教学.
  - **example**, **mini task**: 指 readup, upskill, showcase 三类里 `examples/NN-title/` 下那个 Task 的 `README`.

---

## 2. 语种

- **当前只写中文.** 正文全部落在 `-cn` 版上, 工作流里没有任何翻译或重写环节.
- **英文版文件仍然存在, 只是留空.** 布局不变, 每份 `-cn` 都有一个无后缀的同名文件占位, 现在里面没有内容. 等多语种作为独立模块单独做的时候才填.
- **所以英文那一套约束不许删.** 长度预算, 字符集这些规则照旧写在规范里 (见第 6 节), 只是暂时不生效. 删掉的代价是多语种模块接手时得重新推导一遍.
- 支持哪些语种由 skill 根目录的 `supported-languages.json` 声明, 目前只有 `cn`.

---

## 3. 命名约定

- **Branch name**: 两位数序号打头, 连字符分隔, 全部小写. 例如 `01-branch-name`, `02-branch-name`.
- **特殊文件**: 名字主体一律大写. 例如 `README-ORIGINAL-cn.md`.
- **语种后缀**: 加在名字主体之后, lang 小写. 例如 `README-cn.md`.
- **机器可读的配置或清单**: 一律小写. 例如 `lm.json`.
- **目录名永远不带语种后缀.** 各语种的文件都落在同一个目录下, 目录本身没有语种之分. 撞见带 `-cn` 的目录名, 那是存量错误, 报给创作者去改目录名.

为什么全小写加连字符, 为什么特殊文件全大写: 都是为了减少认知负担. 不用记大小写规范就更容易保持统一, 而全大写的名字一眼就能认出这是特殊文件.

---

## 4. 目录结构

### 4.1 根目录与 branch 快照

```text
lm.json
README.md                              留空
README-cn.md
README-ORIGINAL.md                     留空
README-ORIGINAL-cn.md
TICKET.md                              留空
TICKET-cn.md
docs/tasks/
docs/tasks/SYLLABUS.md                 生成
docs/tasks/SYLLABUS-cn.md              生成
docs/tasks/01-branch-name/
docs/tasks/01-branch-name/README.md
docs/tasks/01-branch-name/README-cn.md
docs/tasks/01-branch-name/TICKET.md
docs/tasks/01-branch-name/TICKET-cn.md
docs/tasks/02-branch-name/
```

readup, upskill, showcase 还会在这之上多一层 `examples/`, 见下一小节.

### 4.2 `examples/` 下的位置约定

带 `examples/` 的三类 repo (readup, upskill, showcase) **共用同一套位置约定**. evolve 没有这一层.

**为什么这一层叫 examples 而不是 tutorials**: 如果这个 repo 最终要拿去给外面看, tutorials 给人的感觉是 "别人在教这个学生", 而 examples 给人的感觉是 "这个学生在教别人, 在展示自己怎么学会的". 后者视角更主动, 更适合展示, 所以统一用 examples.

编号两位数打头, **从 01 连续, 不许跳号** (lint 查这条). 每个位置的角色是固定的:

| 位置 | 是什么 | 谁有 |
| :--- | :--- | :--- |
| `01` | **索引 Task**, 整门课的地图 | 三类 |
| `02` | **综述 Task**, 话题本身的背景 | 三类, 一般都有 |
| `03` 到 `N` | **主线教学 Task** | 三类 |
| `N+1` 往后 | **特殊 Task**, 目录名固定 | 类型专属, 见下表 |
| 最后一个 | **收尾 Task**, 梳理这门课并给拔高方向 | 三类 |

各类型有哪些特殊 Task:

| 类型 | 特殊 Task (按顺序) |
| :--- | :--- |
| readup | 无 |
| upskill | `NN-prove-i-get-it` (quiz) |
| showcase | `NN-prove-i-get-it` (quiz), `NN-how-i-build-this` (demo) |

**`01` 索引和 `02` 综述不是一回事**, 别合并:

- **索引**梳理这门课有哪些 Task, 怎么分组, 该按什么顺序读. 它短, 是一张地图.
- **综述**交代话题本身: 这个领域是怎么来的, 现在什么局面, 学生进来之前该知道哪些背景. 它可以很长, 取决于话题需要多少铺垫.

**收尾排在所有特殊 Task 之后**, 这是硬的. 两条理由:

- 收尾要说 "你现在应该能做到什么", 而 quiz 和 demo 正是证明这件事的两个动作, **它得在两者之后才说得出口**, 而且要在正文里提到它们.
- 收了尾又冒出两个 Task, 读起来很怪.

**写的顺序不等于摆的顺序.** `01` 索引摆在最前, 但它是**最后写的** (路修完才能画地图); `02` 综述摆在第二, 但和最早的几篇主线一起写. 各类型的创作工作流会说清各自的写作顺序.

### 4.3 哪些硬, 哪些软

| 约定 | 硬度 | lint 查不查 |
| :--- | :--- | :--- |
| 编号从 01 连续 | 硬 | **查** |
| 每个 `NN-title/` 下有 README 与 TICKET | 硬 | **查** |
| quiz 那个 Task 存在且目录名是 `NN-prove-i-get-it` | 硬, forge 与 publish 按名字找它 | **查** (upskill 与 showcase) |
| demo 那个 Task 存在且目录名是 `NN-how-i-build-this` | 硬, 同上 | **查** (仅 showcase) |
| demo 紧跟 quiz, 且后面还有 Task | 硬 | **查** (仅 showcase, 见下) |
| `01` 是索引 | 硬 | 不查 |
| 最后一个是收尾 | 硬 | 不查 (showcase 间接查到, 见下) |
| `02` 是综述 | 惯例, 几乎总有 | 不查 |
| 索引与收尾的目录名 | 软, 随课程而定 | 不查 |

**lint 只认得出名字固定的那几个角色.** 索引与收尾的目录名随课程而定, 所以在 lint 眼里它们和主线 Task 长得一样, 整个漏掉也不报. 这是明确接受的代价: 缺席很响 (谁打开 `examples/` 都立刻发现没有入口), 而且统稿那一步的 "规定动作齐不齐" 本来就是拿这张表对着人工核的.

**showcase 多查到一层, 是白捡的.** demo 的目录名是固定的, 而规范要求收尾排在它后面, 所以 "demo 不是最后一个" 这一条不用认出收尾是谁就能判: 后面那个必然是它. 于是 showcase 漏写收尾会被 lint 抓到, 而 upskill 与 readup 不会. **这个不对称是能力所限, 不是规则不同**: 三类的收尾都是硬要求, 只是另外两类没有一个固定名字可以当锚点.

`02` 综述与主线 Task 走通用的 [03-task-readme-spec](03-task-readme-spec/task-readme-cn-spec.md) 与 [04-task-ticket-spec](04-task-ticket-spec/task-ticket-cn-spec.md). 三个角色 Task 各有补充:

| Task | README 走 | TICKET 走 |
| :--- | :--- | :--- |
| `01` 索引 | [05-overview-readme-spec](05-overview-readme-spec/overview-readme-cn-spec.md) | [06-overview-ticket-spec](06-overview-ticket-spec/overview-ticket-cn-spec.md) |
| quiz | [11-quiz-readme-spec](11-quiz-readme-spec/quiz-readme-cn-spec.md) | [12-quiz-ticket-spec](12-quiz-ticket-spec/quiz-ticket-cn-spec.md) |
| demo (showcase) | [showcase-demo-readme-spec](../03-showcase/showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md) | [showcase-demo-ticket-spec](../03-showcase/showcase-demo-ticket-spec/showcase-demo-ticket-cn-spec.md) |
| 最后一个 收尾 | [14-wrap-up-readme-spec](14-wrap-up-readme-spec/wrap-up-readme-cn-spec.md) | 通用 `04` |

---

## 5. 各文件说明

每个特殊文件的规范是一个目录, 里面一份 spec (规范, 权威) 加一份 template (骨架, 原样复制). 唯一的例外是 `14-wrap-up-readme-spec/`, 它只有 spec, 骨架直接用 `03` 那一份. 格式详见 skill 根目录的 `spec-file-format.md`.

- **`README.md`**: 教学文档, 给学生阅读. 教学内容的结构随课程本身而定, 只有少量硬标准. 见 [03-task-readme-spec](03-task-readme-spec/task-readme-cn-spec.md).
- **`TICKET.md`**: 任务目标与验收 checklist, 给学生阅读, 同时作为 Kanban 里 Ticket body 的正文. 见 [04-task-ticket-spec](04-task-ticket-spec/task-ticket-cn-spec.md).
- **`README-ORIGINAL.md`**: 整个 Repo 逻辑意义上的长介绍. 因为各 branch 的 `README.md` 都归它那个 Task 用了, Repo 自身的介绍才另起这个文件. 见 [02-readme-original-spec](02-readme-original-spec/readme-original-cn-spec.md).
- **`SYLLABUS.md`**: 整个 Repo 所有 Task 的清单索引. **不手写**, 由脚本从各 Task `README.md` 的 frontmatter `description` 汇总生成. 见 [07-syllabus-spec.md](07-syllabus-spec.md).
- **`lm.json`**: Repo 根目录的机器可读清单. 它不是文档, 不走上面的 spec 加注释格式. 目前三个字段:

  | 字段 | 谁写 | 是什么 |
  | :--- | :--- | :--- |
  | `type` | 人手写 (第 1 步) | `evolve` \| `showcase` \| `upskill` \| `readup`, 声明这个 repo 属于哪一类. 校验脚本按它分支处理不同布局 |
  | `estimated_hours_lower` | `lesson-smith sync` | 整个 Repo 的时间下限, 单位小数小时 |
  | `estimated_hours_upper` | `lesson-smith sync` | 整个 Repo 的时间上限, 单位小数小时 |

  后两个是 **Repo 级** (不是 branch 级) 的时间预算: 把 `docs/tasks/<branch>/TICKET-cn.md` 每个 branch 的分钟区间下限加下限, 上限加上限, 最后一次性换算成小时, 四舍五入到 2 位小数. **不手写**, 由 sync 生成, 由 lint 校验有没有漂. 规则见 [04-task-ticket-spec](04-task-ticket-spec/task-ticket-cn-spec.md) 第 8.2 节.

  ```json
  {
      "type": "readup",
      "estimated_hours_lower": 6.42,
      "estimated_hours_upper": 11.67
  }
  ```

  为什么从 `docs/tasks/` 算而不是从工作区算: 那是唯一一处**所有 branch 同时可见**的地方, 工作区任何时刻只 checkout 了一个 branch. 也因此 evolve 暂时没有这两个字段, sync 还不支持它的多 branch 快照.

---

## 6. frontmatter

`README.md`, `TICKET.md`, `README-ORIGINAL.md` 三份顶部都带 YAML frontmatter.

### 6.1 有哪些字段

- `description`: 三份都有.
- `github_about`: **只有 `README-ORIGINAL.md` 有**, 由 lint 强制存在.

### 6.2 形态, lint 全都卡

- 值保持**一行**, 不含换行.
- 值必须用**双引号**包起来, 形如 `description: "..."`.
- 值里**不许出现**: 双引号, 反引号, 以及四个弯引号 (成对的那些).
- 值里**允许出现 ASCII 撇号** (`'`). 值本身已经被双引号包住, 撇号在里面不产生歧义, 而英文的 `it's`, `GitHub's` 这类写法少不了它.
- 长度只算双引号内的内容, 不含包裹的那两个字符.

两条为什么:

- **为什么必须一行**: 它要被程序读取, 拼成 SYLLABUS 里 "一行一个" 的条目, 或表格里的一个 cell. 多于一行就很难排版.
- **为什么必须双引号**: 值里不含双引号, 所以包上绝不会有歧义; 却能让 YAML 编辑器不把值中的冒号误当成映射, 也让 "这是一整行字符串" 一目了然.

### 6.3 长度预算

单位是字符, 只算双引号内的内容.

| 字段 | 出现在 | 中文下限 | 中文上限 | 英文下限 | 英文上限 |
| :--- | :--- | ---: |---------:| ---: | ---: |
| `description` | `README.md`, `TICKET.md` | 无 |      400 | 无 | 800 |
| `description` | `README-ORIGINAL.md` | 200 |      400 | 400 | 800 |
| `github_about` | `README-ORIGINAL.md` | 无 |      150 | 无 | 300 |

- **上限由 lint 卡死, 下限只给人看.** 下限没有任何工具检查它, 它只用来挡明显敷衍的一句话交差.
- **英文那几档现在是备用的.** 英文文件留空, 所以这几个数字暂时不生效; 留在表里是因为多语种模块接手时要照这个预算写, 不该让它重新推导一遍.
- **紧度按海拔分档.** Task 级的 `README` 与 `TICKET` 要紧, 1 到 2 句. Lesson 级的 `README-ORIGINAL` 是整门课的门面, 会进 org 级课程索引, 允许多句写长.
- **上限是硬线, 不是靶心.** 内容说完就停, 一段 280 字的 description 完全可以比一段 395 字的更好.
- **`README-ORIGINAL` 的中文下限只用来挡敷衍.** 概述, 动机, 收获三件事都认真写清楚, 自然就过线, 不需要盯着字数凑.
- **英文上限为什么翻倍.** 一个字符在不同书写系统里承载的信息量差得远, 400 字符的中文写成英文大约要 700 到 900 字符. 一个全局上限要么卡死每一份英文, 要么让中文永远用不满.
- **`README-ORIGINAL` 的英文下限则是防压缩.** 英文版是重写不是压缩, 如果它只比中文版长一点点, 基本可以断定内容被砍过.
- **`github_about` 的上限性质不同.** description 的上限是我们自己定的风格预算; 这一条是外部限制, GitHub 的 About box 约 350 字符就截断, 而且不分语种. 所以英文只给一点余量, 不像 description 那样翻倍, 也没有下限, 短是优点.

### 6.4 各自回答什么

三份 description 目的完全不同, 精确定义见各自的 spec:

- **`README`**: 承诺. 学完你能做到什么.
- **`TICKET`**: 判据. 做出什么才算完.
- **`README-ORIGINAL`**: 发给学生的那段话. 这门课学什么, 为什么值得学, 学完有什么收获; 标准是能原样复制粘贴发给一个学生, 且绝不罗列知识点.

同一份 `README-ORIGINAL` 里那两个字段面向的是两种人:

- **`description` 写给学生**, 也就是要来学这门课的读者.
- **`github_about` 写给老师**, 也就是课程作者本人与同行. 它只说清这个 repo 教什么, 不写收获.

两句都短, 合起来就是这个 repo 在课程索引里的那一行.

---

## 7. docs/tasks 汇总视图

- 位置在 `main` branch, 汇总所有 Task 的快照, 给整门课一个单一视图.
- 每个 `docs/tasks/NN-branch-name/` 下只保存该 Task 的 `README` 与 `TICKET` 副本.
- 内容随 branch 累积: 当前在 `03` branch 时, 这里会包含 01, 02, 03 的副本. 越靠后的 branch, 这里的信息越全.
- 全部由脚本生成, 不手写.

---

## 8. 校验与同步工具

维护 `docs/tasks/` 以及校验命名, 语种完整性, description 规范的逻辑在 `shsk_lesson_smith` 这个 Python package 里 (已发布到 PyPI, 项目名 `shsk-lesson-smith`), CLI 入口是 `lesson-smith`, 两个子命令 `sync` 与 `lint`.

教学仓库自己不依赖这个 package, 所以在教学 repo 根目录下用 uvx 临时拉一个 pin 死的版本来跑, 不必预装:

```bash
uvx --from shsk-lesson-smith==<version> lesson-smith sync -p .
```

```bash
uvx --from shsk-lesson-smith==<version> lesson-smith lint -p .
```

- `sync`: 快照当前 branch 的 README 与 TICKET 到 `docs/tasks/<branch>/`, 并重建 SYLLABUS.
- `lint`: 只读校验. 目录结构, 语种完整性, 唯一那个带序号 branch 的名字对不对 (`01-<type>`), 特殊 Task 的目录名与位置 (见第 4.3 节那张表), forge 产物在不在 (upskill 与 showcase), frontmatter 的 description 与 github_about, H1 字符集, TICKET 里有没有相对路径链接, SYLLABUS 内容是否与各 README 的 description 一致.
- **lint 按语种开关.** 只有开着的语种才被检查, 关掉的整个跳过 (既不要求存在, 内容也不检查). 英文当前是关的, 所以留空的英文占位文件不会报错. 开关在 package 的 `constants.py` 里.
- `<version>` 填创作时的最新发布版本 (当前是 0.3.0; 最新版见 https://pypi.org/pypi/shsk-lesson-smith).
- **pin 死版本**是为了让校验规范可复现, 不随新版悄悄漂移.
- 本地已经装好这个 package 时, 直接跑 `lesson-smith sync` 与 `lesson-smith lint` 效果相同.

---

## 9. H1

四类 repo 的每份特殊文件都只有一个 H1, 字符集由 lint 卡死.

### 9.1 通用规则

- 只用字母, 数字, 文字, 以及逗号, 冒号, 句号.
- 禁 emoji, 引号, 双引号, 方括号, 以及三种破折号 (em dash, en dash, ASCII hyphen).
- **不许拿 repo 名字当通用前缀.** 凡是能用程序批量生成的一律不手写.

**为什么禁引号类**: H1 常被当成裸字符串出现在别处 (看板标题, Issue 标题, 索引里的一行), 带引号就要转义. 逗号和冒号在字符串里是安全的, 予以保留.

**最容易翻车的是带连字符的术语.** `from-scratch mode` 这类词在正文里合法, 写进 H1 就报错. 改成不带连字符的写法或者换个词, **不要把连字符换成任何一种破折号**, 那三种全在禁用集里.

### 9.2 README-ORIGINAL 是例外

`README-ORIGINAL` 的 H1 **逐字节等于 repo 目录名**, 通常形如 `learn_xyz-project`, 所以它不受 9.1 的字符集约束 (repo 名里就带连字符和下划线). lint 对它改为直接比对目录名.

最常见的走样是觉得 `-project` 后缀多余顺手砍掉, 而这种错是静默的, 事后抽查很容易看漏.
