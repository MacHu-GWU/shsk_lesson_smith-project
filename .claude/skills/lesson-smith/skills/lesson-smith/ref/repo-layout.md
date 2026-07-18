# 教学仓库目录结构标准

所有不同类型的教学仓库共享这套目录与命名标准. 本文档尚未完稿: 各文件的 spec 与 template 文件, 以及校验脚本, 都还没写.

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

`README.md`, `TICKET.md`, `README-ORIGINAL.md` 顶部都带 YAML frontmatter, 其中 `description` 是一行, 最多 400 字符, 最多 2 句, 供索引拼成一条 bullet. 这些约束由校验脚本 lint (为什么必须一行: 它要被程序读取, 拼成 "一行一个" 的 bullet 或表格里的一个 cell; 多于一行就很难排版). 三个文件的 description 目的各不相同: README 是 "承诺" (学完能做到什么), TICKET 是 "完成判据" (做出什么才算完), README-ORIGINAL 是 "电梯陈述" (整个 repo 是什么, 到什么水平); 精确定义见各自的 spec.

---

## 5. docs/tasks 汇总视图

`docs/tasks/` 位于 `main` branch, 汇总所有 Task 的快照, 给整门课一个单一视图. 每个 `docs/tasks/NN-branch-name/` 下只保存该 Task 的 `README.md` 和 `TICKET.md` 副本 (含多语言版本). 假设当前在 `03` branch, `docs/tasks/` 会包含 01, 02, 03 之前所有的教程和任务副本, 也就是越靠后的 branch, 这里的信息越全.

---

## 6. 校验脚本

维护 `docs/tasks/` 以及校验命名与语种完整性的脚本在 `scripts/` 下 (待完工). 用法待补.
