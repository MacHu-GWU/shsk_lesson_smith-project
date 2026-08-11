# Upskill 根 README 规范, 中文版

**适用范围**: 仅 upskill 类型 repo **根目录**的 `README-cn.md`. 它不遵循 [03-task-readme-spec](../../00-common/03-task-readme-spec/task-readme-cn-spec.md), 那是给 `examples/` 下单个教学 Task 用的.

**配套骨架**: [upskill-readme-cn-template.md](upskill-readme-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么

**这门课的操作总入口.** 它同时是唯一 branch `01-upskill` 的 Task README 和仓库总览, 面向准备开始学的学生, 回答 "**怎么用这个 repo 学**".

它不是三样别的东西, 分清楚才写得对:

- 不是教学正文. 教程在各个 Task 自己的 README 里.
- 不是对外 pitch. pitch 在 `README-ORIGINAL` 里.
- 不是内容地图. 地图在 `examples/` 的第一个 Task 里.

**多链接, 少复述.** pitch 一句话带过并链到 `README-ORIGINAL-cn.md`, 内容一句话带过并链到 `examples/`, 绝不重复它们已经讲清的东西.

**篇幅是入口不是教程**, 软上限约 60 到 80 行. 超了通常是把 pitch 或内容地图又抄了一遍.

---

## 2. 两条固定内容

**写死两个 skill.** `/upskill-learn` 与 `/upskill-quiz` 由 `lesson-smith-upskill-forge` 必然产出, 所以 "怎么学" 一节固定提及它们, 措辞近乎静态.

**不提 runbook.** 正文不引导环境 setup, 也不提 `docs/upskill/02-upskill-runbook.md` (那是给 AI 看的元文件). setup 只在开始那一下和中途偶发, 交给 `/upskill-learn` 在学生真遇到麻烦时智能介入, 根 README 不必唠叨.

---

## 3. frontmatter, description

它是 **Task (这个 branch) 级**的介绍, 回答 "**你将学到什么**": 这个 branch 教的具体是哪些东西, 学完手上多了哪些能力.

和 `README-ORIGINAL` 那段的区别在海拔:

| | `README-ORIGINAL` 的 description | 这一份 |
| :--- | :--- | :--- |
| 海拔 | Lesson, 整个 Repo | Task, 这个 branch |
| 回答 | 为什么值得学, 学完有什么收获 | 你将学到什么 |
| 重点 | 动机与收获 | 内容与能力 |

upskill 只有一个 branch, 所以这一行看起来像在讲整个 Repo, 其实讲的仍是这个 Task, 只不过它底下装了很多 Task. 两段覆盖范围几乎重叠, **但别把 `README-ORIGINAL` 那段抄过来**. 反过来说, "为什么要学" 在这一份里不重要, 不用写.

**罗列在这里不是毛病, 但只限这一行.** 挑几个有代表性的 examples 主题串出来, 再加一句这门课要学的到底是什么, 恰恰是对的写法. 不必列全, 挑得出这门课的分量即可.

为什么这一行可以罗列而正文不可以: 这一行会被 `lesson-smith sync` 汇进 SYLLABUS, 将来也会进课程索引, **那时它是脱离 repo 单独出现的**, 读者点不进 `examples/`, 只能靠它自己把内容讲出来. 正文不一样, 读者已经站在 repo 里了, 一个链接就能到.

形态与长度见 [01-repo-layout.md](../../00-common/01-repo-layout.md) 第 6 节.

---

## 4. 正文结构

三个 H2, 按 markdown-style 从 1 连续编号, 相邻小节之间用分隔线隔开.

**第 1 节 这门课是什么.** 极简 2 到 3 句说清教什么, 外加 3 到 4 行 "这是 upskill 教学仓库, 该怎么用" 的元概念说明 (学生可能不懂这个概念), 想要完整定位就链到 `README-ORIGINAL`. **不写方法论长文.**

**第 2 节 怎么学.** 全文的篇幅重心. 讲三件事:

- 学的顺序: 进 `examples/`, 从 01 开始按编号一篇篇刷, 每个都照它自己的 TICKET 做完再往下. `examples/` 的第一个 Task 就是索引, 会给出整门课的地图.
- 两个帮手: `/upskill-learn` 带学, `/upskill-quiz` 自测.
- 学到什么算成: 用 `/upskill-quiz` 测到 70% 且思路清晰.

**第 3 节 学完你能做到什么.** 收尾一句, 呼应顶部 description 说的那些.

**没有单独的 "课程内容" 一节.** 目录本身就是索引, 谁点进 `examples/` 都知道从 01 顺着看, 再单开一节说一遍是纯复述.

---

## 5. 写作原则

- **术语保留英文.** 中文只负责叙述, 术语, 产品名, 技术名词一律保留英文原文. 把 lazy evaluation 写成惰性求值, 读者反而认不出这门课在教什么, 这一行进了 SYLLABUS 也失去检索价值.
- **链接**: 指向 repo 内**文件**的相对路径链接用 `-cn` 版; 指向**目录**的链接不带语种后缀.
- H1 只用字母, 数字, 文字, 以及逗号, 冒号, 句号. 禁 emoji, 引号, 双引号, 方括号, 三种破折号.
- 遵循 `markdown-style` 与 `chinese-english-punctuation` 两个 Agent Skill.

---

## 6. 交付前自检

- 两个 skill 都提到了, runbook 一个字没提
- 三个 H2, 编号连续, 之间有分隔线
- pitch 和内容都是一句话带过加一个链接, 没有整段复述
- description 写的是 "你将学到什么", 不是 `README-ORIGINAL` 那段的复制
- description 里罗列了几个有代表性的主题, 而正文里没有罗列
- 全文行数在 80 行以内
