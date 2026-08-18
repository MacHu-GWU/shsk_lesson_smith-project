# Upskill 根 TICKET 规范, 中文版

**适用范围**: 仅 upskill 类型 repo **根目录**的 `TICKET-cn.md`.

它在通用 [04-task-ticket-spec](../../00-common/04-task-ticket-spec/task-ticket-cn-spec.md) 的三段式之上**多加一个 H2 (关键能力)**. **通用规范其余部分仍以那一份为准**, 尤其是受控词汇, H1, frontmatter 与链接四条, 不要在这里另立一套.

**配套骨架**: [upskill-ticket-cn-template.md](upskill-ticket-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么

**整门课 (唯一 branch `01-upskill`) 的验收清单**, 主要给学生自查用.

各个 Task 自己的 TICKET 负责单个 Task 的验收; 这一份站在整门课的高度, 汇总成一张 "我是不是把这门课学完学透了" 的核对表.

它和根 README 那句 description 是同一门课的两张脸: README 说学完能做到什么 (承诺), 这句说做出什么才算完 (判据).

---

## 2. 和 readup 的关键差异

**upskill 的验收里有一件 readup 没有的事: 用自测工具证明自己学会了.**

所以:

- "要做的事情" 的路径末尾**多一步**: 用 `/upskill-quiz-cn` 测到 70% 且思路清晰.
- "检查清单" 里也多相应的条目.
- 提到那个 skill 时用文字提及, 不写成链接 (见第 4 节).

---

## 3. 四个 H2 各写什么

**第 1 节 目标.** 一段, 整门课级别的 Definition of Done: 走完这门课要建立起什么整体能力或体感.

**第 2 节 要做的事情.** 有序的学习路径. 大致是: 先读根目录 README 明白这门课怎么学, 再进 `examples/` 从 01 开始按编号刷完全部 Task (每个照它自己的 TICKET 做), 最后用 `/upskill-quiz-cn` 测到 70% 且思路清晰. 末尾给一个整门课的预计用时, **由各个 Task 加总得出 (下限加下限, 上限加上限), 写法见 [04-task-ticket-spec](../../00-common/04-task-ticket-spec/task-ticket-cn-spec.md) 第 8.1 节**.

**第 3 节 检查清单.** markdown todo 骨架, 带 checkbox. 覆盖: 全部 Task 完成 (各自 TICKET 逐项打勾), `/upskill-quiz-cn` 达到 70%, 能不看教程独立复现, 能用自己的话讲清核心概念. 视课程增删.

**第 4 节 关键能力.** 从各个 Task 的 TICKET 里萃取出最重要的能力, 汇成一张**纯 bullet 清单**.

- **不带 checkbox.** 逐项打勾的活第 3 节和各个 Task 已经做过了; 这一节是让学员对照 "我是不是真掌握了这些" 的能力核对.
- **硬性要求取舍: 10 条以内.** 不是每个 Task 都值得列 (它们各自 TICKET 里都说过了), 挑最能代表这门课的能力, 每条一句话.
- 纯文字, 不带任何相对路径链接.

---

## 4. 链接约定

沿用通用 spec 的规则, 这里因为要频繁提到别的 Task 而再强调一次:

- **禁止指向 repo 内文件或目录的相对路径链接**, 在 GitHub Issue 里点不动.
- 绝对 URL (形如 `https://domain/href`) 照常可用.
- 需要指向 `examples/` 下某个 Task 或 `/upskill-quiz-cn` 时**用文字提及**, 不写成链接. 第 4 节尤其如此.
- 提到子 skill 的写法 (正文用反引号加斜杠, frontmatter 里裸写不加反引号) 见通用 spec 第 6.1 节, 不要在这里另立一套.

---

## 5. 交付前自检

- 四个 H2, 编号连续, 之间有分隔线, 前三个的文字逐字等于受控词汇
- 全文没有相对路径链接
- 第 4 节是纯 bullet, 不带 checkbox, 10 条以内
- 第 2 节末尾有预计用时那一行, 且等于 `examples/` 下各 Task 的加总 (下限加下限, 上限加上限), 后面括号里附小时换算
- description 写的是判据, 不是承诺
