# Upskill quiz Task 的 TICKET 规范, 中文版

**适用范围**: 仅 upskill 类型 repo 里 quiz 那个 Task 的 `TICKET-cn.md`, 目录固定命名 `examples/NN-prove-i-get-it`.

它**沿用**通用 [04-task-ticket-spec](../../00-common/04-task-ticket-spec/task-ticket-cn-spec.md) 的三段式结构, 只是内容固定且极简. **通用规范其余部分仍以那一份为准**, 尤其是受控词汇, H1, frontmatter 与链接四条, 不要在这里另立一套.

**配套骨架**: [upskill-quiz-ticket-cn-template.md](upskill-quiz-ticket-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么

quiz 那个 Task 的验收清单. 配套的题库真身 README 另有规范, 见 [upskill-quiz-readme-spec](../upskill-quiz-readme-spec/upskill-quiz-readme-cn-spec.md).

**内容是固定的**, 不需要按课程重新设计: 把题库通读一遍, 再用 `/upskill-quiz-cn` 抽测到 70% 通过. 不同课程可以微调措辞, 意思固定.

---

## 2. 两条判据不许删

措辞可按课程微调, 但下面两条是这个 Task 存在的理由, 删掉它就只剩一个空壳:

- **读一遍题库**: 每题先自己答, 再对照参考回答与深入解读.
- **测到 70% 通过**: 用 `/upskill-quiz-cn` 反复抽测, 正确率稳定在 70% 以上.

两条对应第 2 节的两个步骤, 也对应第 3 节的两个 checkbox.

---

## 3. 交付前自检

- 三个 H2, 编号连续, 之间有分隔线, 文字逐字等于受控词汇
- 第 2 节的两个步骤和第 3 节的两个 checkbox 一一对应
- 第 2 节末尾有预计用时那一行
- 全文没有相对路径链接
- frontmatter 的 description 在, 值用双引号包着 (见 [00-common/01-repo-layout.md](../../00-common/01-repo-layout.md) 第 6 节)
