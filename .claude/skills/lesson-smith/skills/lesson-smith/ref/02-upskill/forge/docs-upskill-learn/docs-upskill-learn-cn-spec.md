# docs/upskill/01-upskill-learn-cn.md 规范, 中文版

**适用范围**: upskill 类型 repo 的 `docs/upskill/01-upskill-learn-cn.md`, 由 `lesson-smith-upskill-forge` 生成, 给 `upskill-learn-cn` skill 消费.

**配套骨架**: [docs-upskill-learn-cn-template.md](docs-upskill-learn-cn-template.md).

**当前只产这一套**: 英文版规范与骨架就在同目录下, 但 forge 现在只产 `-cn`. 理由是 `examples/` 下无后缀的英文课程正文留空, 英文索引只会指向一堆空文件.

**链接一律指 `-cn`**: 这份索引里所有指向 `examples/` 与 repo 内文档的链接都写 `-cn.md`. 指到无后缀那一版就是指到空文件.

---

## 1. 它是什么

**学习资料索引.** 它不铺开讲知识 (知识在 `examples/` 和素材本身里), 只回答三件事: 要学的东西有哪些, 在哪, 按什么顺序过.

**它是索引, 不是完整的知识清单.**

---

## 2. 两个部分

正文就是下面两部分, 一一对应两个 H2.

### 2.1 学习素材

repo 里除 `examples/` 渐进序列以外, 要学的东西: 根目录代码, 其它文档, 配置文件等.

**这部分需要人类说清**, 因为它不像 `examples/` 那样自明. 分两种情况:

| 情况 | 说明 | 这一节的厚度 |
| :--- | :--- | :--- |
| **A** | 教程本身就是要学的东西 (偏阅读, 内容都在 `examples/` 里) | 很薄, 甚至只写一句 "没有额外素材, 全在引导路径里" |
| **B** | 真东西 (通常是代码) 在 repo 别处, `examples/` 只是带你一步步走一遍 | 这部分是主菜, 要把散落的素材梳理全 |

每条素材给出三样: 一个 markdown 链接 (定位到文件, 需要时精确到某个 header 或关键字), 一句话说学什么, 一句话说为什么重要或有什么坑.

### 2.2 引导路径

`examples/01, 02 ...` 的渐进序列就是学生要走的路, `upskill-learn-cn` skill 按它往前推.

这部分 forge 扫一遍 `examples/` 目录就能得到, 容易. **只概述整条线怎么推进** (分成几段, 每段学到什么), 并点向 `examples/01` 那个索引 Task 和 `docs/tasks/SYLLABUS-cn.md`.

- 对情况 B, 标明每一段路径覆盖第 1 节的哪些素材.
- **不要逐条复述每个 Task 的正文.**

---

## 3. 写作原则

- 全程用 markdown 链接溯源, 定位一律用 header 或关键字, **不用 line no** (line no 会随代码漂移).
- 遵循 markdown-style 与 chinese-english-punctuation 两个 Agent Skill.
- 这份 doc **可被直接编辑修正**, 也可以重新 forge 刷新. 素材列错了直接改这里.
