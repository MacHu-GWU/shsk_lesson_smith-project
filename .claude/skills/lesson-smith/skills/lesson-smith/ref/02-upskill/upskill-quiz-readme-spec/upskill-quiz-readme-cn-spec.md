# Upskill quiz Task 的 README 规范, 中文版

**适用范围**: 仅 upskill 类型 repo 里 quiz 那个 Task 的 `README-cn.md`, 目录固定命名 `examples/NN-prove-i-get-it`.

它住在 `examples/` 下, 但**不走** [00-common/03-task-readme-spec](../../00-common/03-task-readme-spec/task-readme-cn-spec.md) 的教学正文结构, 而走下面这套问答结构. **frontmatter, H1 与链接三条仍以通用规范为准**, 不要在这里另立一套.

**配套骨架**: [upskill-quiz-readme-cn-template.md](upskill-quiz-readme-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么

**题库真身.** 题目, 考察点, 参考回答, 深入解读全部写在这里.

`docs/upskill/03-upskill-quiz-cn.md` 只是一层指过来的薄壳, `/upskill-quiz-cn` 抽题也是抽这里的题. 题不写在这份文件里, 那两处就是空的.

写这份文件时 AI 提建议, **创作者拍板定题**. 视角是学生自己检查自己 (所以目录叫 `prove-i-get-it`), 便于对外展示.

配套的 TICKET 另有规范, 见 [upskill-quiz-ticket-spec](../upskill-quiz-ticket-spec/upskill-quiz-ticket-cn-spec.md).

---

## 2. 位置

主线教学 Task 全部写完之后, **收尾 Task 之前** (位置约定见 [00-common/01-repo-layout.md](../../00-common/01-repo-layout.md) 第 4.2 节).

理由是它要考的东西必须先教过. 位置不像索引 Task 那样硬性固定在某个编号, 但目录名 `NN-prove-i-get-it` 是固定的, forge 靠这个名字定位它.

---

## 3. 整体结构

- **H1 下固定跟一句话**, 说明本文档是对整门课学到的东西的一次验证, 看你是否知其然知其所以然. 措辞可调, 意思不变.
- **每道题一个 H2.** 题量按 repo 复杂度而定, **20 到 50 题是常态**.
- H2 标题是这道题的**一句话主题** (短), 真正的问法写在下面的 "问题" 里.
- H2 按 markdown-style 从 1 连续编号, 相邻题之间用分隔线隔开.

---

## 4. 每道题的四段结构

四段的**顺序固定**, 每段的格式也固定:

1. 单独一行**加粗的 short title** (例如加粗的 "问题" 二字, 不带冒号)
2. 空一行
3. 一个 markdown blockquote (每行以 `>` 开头) 承载这一段的内容

用 blockquote 而不是冒号后直接跟一行, 是因为参考回答与深入解读常常有多句甚至多段, blockquote 能整段包住, 排版更清楚, 也和题面视觉上分开.

四段依次是:

| 段 | 写什么 |
| :--- | :--- |
| **问题** | 面试官会直接问你的那句话, 1 到 3 句, 长短按题目复杂度自己定. **题一定是 repo 里教过, 有据可查的东西.** |
| **考察点** | 一段话讲这题的潜台词, 想通过它看你会不会某种东西, 而不是复述题面. |
| **参考回答** | 面试里 1 到 3 分钟能说出口的话, 相对精炼, 是知其然的部分. |
| **深入解读** | 旁白式把这个知识讲透, 比参考回答更冗长 (为帮助理解, 允许冗余), 偏知其所以然. |

两条容易做偏的:

- **考察点不要过度阴谋论.** 有的题就是个纯知识点, 那就简洁地说考的就是题面, 不强行拔高.
- **深入解读必须用 markdown 链接溯源**, 指到哪个文件的哪个部分. 定位一律用 header 或关键字, **不用 line no**.

---

## 5. 交付前自检

- H1 下那句话在, 每道题一个 H2, 编号连续, 之间有分隔线
- 每道题四段齐全, 顺序正确, 每段都是加粗 short title 加 blockquote
- 每道题都能在 repo 里找到出处
- 每道深入解读都带至少一条溯源链接, 且链接活的
- frontmatter 的 description 在, 值用双引号包着 (见 [00-common/01-repo-layout.md](../../00-common/01-repo-layout.md) 第 6 节)
