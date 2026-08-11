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

- **README 与 TICKET 必然成对.** 有 Task 就有这两份, 一份说教什么, 一份说怎么验收. 只写一份就是欠账, 统稿时一定返工.
- **Task 只是一个位置无关的单位.** 它可能落在 branch 根目录 (evolve), 也可能落在 `examples/NN-title/` 下 (readup, upskill, showcase). 落在哪里由类型的特化文档定, 规范本身是同一份.
- **不再用 tutorial, mini task 这类叫法.** 它们指的都是 Task. 混着用的直接后果是各 spec 之间对不上, 读的人以为是两种东西.

---

## 2. 语种

- **当前只写中文.** 一门课的全部文档都是 `-cn` 版, 工作流里没有任何翻译或重写环节.
- **语种后缀的位置仍然保留.** 中文写作 `-cn`, 无后缀那个位置留给英文. 多语种以后作为独立模块单独做, 不在现在这条线里.
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

```text
lm.json
README-cn.md
README-ORIGINAL-cn.md
TICKET-cn.md
docs/tasks/
docs/tasks/SYLLABUS-cn.md
docs/tasks/01-branch-name/
docs/tasks/01-branch-name/README-cn.md
docs/tasks/01-branch-name/TICKET-cn.md
docs/tasks/02-branch-name/
```

readup, upskill, showcase 还会在这之上多一层 `examples/`, 见各自的特化文档.

---

## 5. 各文件说明

每个特殊文件的规范与模板合在同一个 spec 文件里: 规范写在顶部 `<!-- -->` 注释, 正文即可直接套用的模板. 格式详见 skill 根目录的 `spec-file-format.md`.

- **`README.md`**: 教学文档, 给学生阅读. 教学内容的结构随课程本身而定, 只有少量硬标准. 见 [02-task-readme-spec](02-task-readme-spec/task-readme-spec.md).
- **`TICKET.md`**: 任务目标与验收 checklist, 给学生阅读, 同时作为 Kanban 里 Ticket body 的正文. 见 [03-task-ticket-spec](03-task-ticket-spec/task-ticket-spec.md).
- **`README-ORIGINAL.md`**: 整个 Repo 逻辑意义上的长介绍. 因为各 branch 的 `README.md` 都归它那个 Task 用了, Repo 自身的介绍才另起这个文件. 见 [04-readme-original-spec](04-readme-original-spec/readme-original-spec.md).
- **`SYLLABUS.md`**: 整个 Repo 所有 Task 的清单索引. **不手写**, 由脚本从各 Task `README.md` 的 frontmatter `description` 汇总生成. 见 `syllabus-spec.md` (尚未迁入本目录).
- **`lm.json`**: Repo 根目录的机器可读清单. 它不是文档, 不走上面的 spec 加注释格式. 目前 schema 只有一个字段 `type`, 取值 `evolve` | `showcase` | `upskill` | `readup`, 声明这个 repo 属于哪一类. 以后可以往里加更多结构化字段, 也方便校验脚本按 `type` 分支处理不同布局.

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

| 字段 | 出现在 | 下限 | 上限 |
| :--- | :--- | ---: | ---: |
| `description` | `README.md`, `TICKET.md` | 无 | 400 |
| `description` | `README-ORIGINAL.md` | 200 | 400 |
| `github_about` | `README-ORIGINAL.md` | 无 | 200 |

- **紧度按海拔分档.** Task 级的 `README` 与 `TICKET` 要紧, 1 到 2 句. Lesson 级的 `README-ORIGINAL` 是整门课的门面, 会进 org 级课程索引, 允许多句写长.
- **上限是硬线, 不是靶心.** 内容说完就停, 一段 280 字的 description 完全可以比一段 395 字的更好.
- **`README-ORIGINAL` 的下限只用来挡敷衍.** 概述, 动机, 收获三件事都认真写清楚, 自然就过线, 不需要盯着字数凑.
- **`github_about` 的上限性质不同.** description 的上限是我们自己定的风格预算; 这一条是外部限制, GitHub 的 About box 约 350 字符就截断, 而且不分语种. 所以它没有下限, 短是优点.

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
- `lint`: 只读校验. 目录结构, 语种完整性, frontmatter 的 description 与 github_about, H1 字符集, SYLLABUS 内容是否与各 README 的 description 一致.
- `<version>` 填创作时的最新发布版本 (当前是 0.3.0; 最新版见 https://pypi.org/pypi/shsk-lesson-smith).
- **pin 死版本**是为了让校验规范可复现, 不随新版悄悄漂移.
- 本地已经装好这个 package 时, 直接跑 `lesson-smith sync` 与 `lesson-smith lint` 效果相同.
