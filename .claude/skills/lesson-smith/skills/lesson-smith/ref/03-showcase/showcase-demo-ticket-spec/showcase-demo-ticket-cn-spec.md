# Showcase demo Task 的 TICKET 规范, 中文版

**适用范围**: 仅 showcase 类型 repo 里 demo 那个 Task 的 `TICKET-cn.md`, 目录固定命名 `examples/NN-how-i-build-this`.

它**沿用**通用 [04-task-ticket-spec](../../00-common/04-task-ticket-spec/task-ticket-cn-spec.md) 的三段式结构, 只是内容固定且极简. **通用规范其余部分仍以那一份为准**, 尤其是受控词汇, H1, frontmatter 与链接四条, 不要在这里另立一套.

**配套骨架**: [showcase-demo-ticket-cn-template.md](showcase-demo-ticket-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么

demo 那个 Task 的验收清单. 配套的讲故事底稿 README 另有规范, 见 [showcase-demo-readme-spec](../showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md).

**内容是固定的**, 不需要按课程重新设计: 把底稿通读一遍, 再用 `/showcase-demo-cn` 排练到能流畅讲完并接住常见追问. 不同课程可以微调措辞, 意思固定.

---

## 2. 两条判据不许删

措辞可按课程微调, 但下面两条是这个 Task 存在的理由, 删掉它就只剩一个空壳:

- **读一遍底稿**: 默认七幕主线和常见追问都过一遍.
- **排练到能流畅讲完并接住追问**: 用 `/showcase-demo-cn` 练到不看稿能把主线讲顺.

这两条对应第 2 节的两个步骤. 第 3 节比它们多一条: 排练结果拆成 "能流畅讲完" 和 "接得住追问" 两个 checkbox, 因为讲得顺和答得住是两种能力, 合成一条容易蒙混过去.

---

## 3. 交付前自检

- 三个 H2, 编号连续, 之间有分隔线, 文字逐字等于受控词汇
- 第 3 节三个 checkbox: 读完底稿, 能流畅讲完, 接得住追问
- 第 2 节末尾有预计用时那一行, 且逐字等于 `30 到 60 分钟` (六档里的第 4 档)
- 全文没有相对路径链接
- frontmatter 的 description 在, 值用双引号包着 (见 [00-common/01-repo-layout.md](../../00-common/01-repo-layout.md) 第 6 节)
