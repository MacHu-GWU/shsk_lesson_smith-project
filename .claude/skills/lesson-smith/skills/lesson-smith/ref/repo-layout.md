# 教学仓库目录结构标准

所有不同类型的教学仓库共享这套目录与命名标准. 各类型在此基础上特化, 特化说明放在 ref 下对应的子目录里 (upskill 见 upskill/upskill-repo-layout.md; showcase, evolve 待补).

## 1. 命名约定

- Branch name: 两位数序号打头, 连字符分隔, 全部小写. 例如 `01-branch-name`, `02-branch-name`. (全小写加连字符是为了减少认知负担: 不用记大小写规范, 更容易保持统一.)
- 特殊文件 (README, TICKET, README-ORIGINAL, SYLLABUS) 的名字主体一律大写. (全大写好记, 一眼就能认出这是特殊文件, 同样是为了减少认知负担.)
- 多语言版本在名字主体后加 `-<lang>` (lang 小写), 英文版无后缀. 例如 `README-cn.md`. 支持哪些语种见 skill 根目录的 `supported-languages.json`.
- 机器可读的配置 / 清单文件用小写, 例如 `lm.json`. (大写规则只针对上面那些文档类特殊文件.)

---

## 2. 目录结构

```
lm.json
README.md
README-<lang>.md
README-ORIGINAL.md
README-ORIGINAL-<lang>.md
TICKET.md
TICKET-<lang>.md
docs/tasks/
docs/tasks/SYLLABUS.md
docs/tasks/SYLLABUS-<lang>.md
docs/tasks/01-branch-name/
docs/tasks/01-branch-name/README.md
docs/tasks/01-branch-name/README-<lang>.md
docs/tasks/01-branch-name/TICKET.md
docs/tasks/01-branch-name/TICKET-<lang>.md
docs/tasks/02-branch-name/
```

---

## 3. 各文件说明

每个特殊文件的规范与模板合在同一个 spec 文件里 (规范写在顶部 `<!-- -->` 注释, 正文即可直接套用的模板; 详见 skill 根目录的 `spec-file-format.md`).

`README.md` 是教学文档, 给学生阅读. 教学内容的结构随课程本身而定, 只有少量硬标准. 规范与模板详见 `readme-spec.md`.

`TICKET.md` 是任务目标与验收 checklist, 给学生阅读, 同时作为 Kanban 系统中 Ticket body 的正文. 规范与模板详见 `ticket-spec.md`.

`README-ORIGINAL.md` 是整个 Repo 逻辑意义上的长介绍. 因为各 branch 的 `README.md` 都归它那个 Task 用了, 所以 Repo 自身的介绍另起这个文件. 规范与模板详见 `readme-original-spec.md`.

`SYLLABUS.md` 是整个 Repo 所有 Task 的清单索引. 它不手写, 而是由脚本从各 Task 的 `README.md` 顶部 frontmatter 的 `description` 解析汇总而成. 规范与模板详见 `syllabus-spec.md`.

`lm.json` 是 Repo 根目录的机器可读清单 (manifest), 记录这个 repo 的结构化字段. 它不是文档, 不走上面的 spec 加注释格式. 目前 schema 只有一个字段: `type`, 取值 `evolve` | `showcase` | `upskill`, 声明这个 repo 属于哪一类. 以后可以往里加更多结构化字段, 也方便校验脚本按 `type` 分支处理不同布局.

---

## 4. 一行摘要 frontmatter

`README.md`, `TICKET.md`, `README-ORIGINAL.md` 顶部都带 YAML frontmatter, 其中 `description` 是一行 (不含换行), 最多 400 字符 (不含包裹的双引号), 供索引拼成一条 bullet. 句数按海拔分档: Task 级的 `README.md` 与 `TICKET.md` 的 description 要紧, 1 到 2 句; Lesson 级的 `README-ORIGINAL.md` 的 description 是整门课的门面, 会进 org 级课程索引, 鼓励写长, 用足预算到接近 400 字符, 详见 [readme-original-spec.md](readme-original-spec.md). 这些约束由校验脚本 lint (为什么必须一行: 它要被程序读取, 拼成 "一行一个" 的 bullet 或表格里的一个 cell; 多于一行就很难排版).

`README-ORIGINAL.md` 额外多带一个 `github_about` 字段: 压缩版 tagline, 一行, 最多 200 字符, 专门给 GitHub 仓库的 About box 用 (About 上限约 350, 收到 200 更稳; 长的 description 进不了 About, 所以单列这个). 只有 README-ORIGINAL 有这个字段, 由 lint 强制存在与校验.

`description` 与 `github_about` 的值都必须用双引号包起来, 形如 `description: "..."`. 因为值里永远不含引号类字符 (单双引号, 反引号都被禁), 用双引号包裹绝不会有歧义, 却能让 YAML 编辑器不把值中的冒号误当成映射, 也让 "这是一整行字符串" 一目了然. 这一条同样由 lint 强制: 未加双引号或用单引号都会报错. 长度只算双引号内的内容. 三个文件的 description 目的各不相同: README 是 "承诺" (学完能做到什么), TICKET 是 "完成判据" (做出什么才算完), README-ORIGINAL 是 "电梯陈述" (整个 repo 是什么, 到什么水平); 精确定义见各自的 spec.

---

## 5. docs/tasks 汇总视图

`docs/tasks/` 位于 `main` branch, 汇总所有 Task 的快照, 给整门课一个单一视图. 每个 `docs/tasks/NN-branch-name/` 下只保存该 Task 的 `README.md` 和 `TICKET.md` 副本 (含多语言版本). 假设当前在 `03` branch, `docs/tasks/` 会包含 01, 02, 03 之前所有的教程和任务副本, 也就是越靠后的 branch, 这里的信息越全.

---

## 6. 校验与同步工具

维护 `docs/tasks/` 以及校验命名, 语种完整性, description 规范的逻辑在本项目的 `shsk_lesson_smith` Python package 里, CLI 入口是 `lesson-smith`:

```bash
lesson-smith sync   # 快照当前 branch 的 README / TICKET 到 docs/tasks/<branch>/, 并重建 SYLLABUS
lesson-smith lint   # 只读校验: 目录结构, 语种完整性, frontmatter description, SYLLABUS 内容
```
