<!--
本文件是 TICKET 任务卡片的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 TICKET-cn.md 时, 把整段注释删掉, 只留后面的正文.

定性: 这是任务卡片 (GitHub Project Issue). 给学生看 (主要), 也给导师或验收者看. 用途是告诉学生要做什么, 怎么做, 怎么检查和提交, 同时为验收者提供验收标准.

适用范围: 教学用的 Task 或 mini task 级 TICKET, 位置标准与 README 一致. 在 upskill 和 showcase 类型的 Repo 里, 是 examples/XY-title-here/TICKET-cn.md. 在 evolve 类型的 Repo 里, 就在 Repo 根目录下.

写作原则:
- 以 TICKET-cn.md 中文版为准: 先写中文, 定稿后用 translate-to-en 生成英文 TICKET.md.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.
- 三段式结构 (必须遵守): 目标, 要做的事情, 检查清单. 三个 H2 按 markdown-style 从 1 连续编号, 之间用 markdown 分隔线隔开.

H1 任务标题: 规则与 README 相同 (只用字母, 数字, 文字, 逗号, 冒号, 句号; 禁 emoji, 引号, 双引号, 破折号). 额外一条: 标题里不许出现 repo 名字作为通用前缀. (为什么: 凡是能用程序批量生成的一律不手写, repo 前缀这类交给程序.)

链接约定: TICKET 正文最终会被程序放进 GitHub Issue, 所以对链接有讲究.
- 禁止指向 repo 内文件或目录的相对路径链接 (形如指向 ../ 或 ./ 某个文件的 markdown 链接). 相对路径在 GitHub Issue 里是死的, 点不动. 要指向 repo 里某个文件, 目录或 mini task 时, 用文字提及 (直接说文件名或位置), 不写成链接.
- 允许绝对 URL: 形如 https://domain/href 的绝对链接完全可以照常用.
- 另外不手写指向本教程或本 Issue 自身的 GitHub 链接: 生成 Issue 时程序会确定性地拼出来, 不手写.

顶部 frontmatter 的 description 是这个 Task 的 "完成判据": 一句话说清做出什么, 或能当场演示什么, 才算完成 (Definition of Done 压成一句). 它出现在看板 / Issue 列表里, 面向判断 "这活儿是啥, 达没达标" 的人. 和 README 那句是同一个 Task 的两张脸: README 句说学完能做到什么 (承诺), 这句说做出什么才算完 (判据). 纯知识型 Task 就写成可当场检验的理解 (你能解释清楚 X). description 的值必须用双引号包起来 (形如 description 冒号空格再双引号), 长度与该约束见 repo-layout.md 第 4 节.
-->

---
description: "一句话, 做出什么或能演示什么才算这个 Task 完成. 中文叙述 + 英文术语."
---

# [任务标题]

## 1. 目标

[简述要完成什么, 以及为什么.]

---

## 2. 要做的事情

1. [第一件事, 要具体.]
2. [第二件事.]
3. [第三件事.]

**预计用时:** [X 到 Y] 分钟

---

## 3. 检查清单

- [ ] **[条目标题]**: [完成标准的简述.]
- [ ] **[条目标题]**: [完成标准的简述.]
- [ ] **[条目标题]**: [完成标准的简述.]
