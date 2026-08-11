# Showcase 根 README 规范, 中文版

**适用范围**: 仅 showcase 类型 repo **根目录**的 `README-cn.md`. 它不遵循 [03-task-readme-spec](../../00-common/03-task-readme-spec/task-readme-cn-spec.md), 那是给 `examples/` 下单个教学 Task 用的.

**配套骨架**: [showcase-readme-cn-template.md](showcase-readme-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么

**这门课的操作总入口.** 它同时是唯一 branch `01-showcase` 的 Task README 和仓库总览, 面向准备开始学的学生, 回答 "**怎么用这个 repo 学, 学完怎么对外展示**".

它不是三样别的东西, 分清楚才写得对:

- 不是教学正文. 教程在各个 Task 自己的 README 里.
- 不是对外 pitch. pitch 在 `README-ORIGINAL` 里.
- 不是内容地图. 地图在 `examples/` 的第一个 Task 里.

**和 upskill 的关键差异就体现在这份 README 上**: upskill 学会即止, 根 README 只讲 "怎么学"; showcase 学完还要抹去教学痕迹拿去展示, 所以在 "怎么学" 之外**多一节 "学完之后: 展示与发布"**.

**多链接, 少复述.** pitch 一句话带过并链到 `README-ORIGINAL-cn.md`, 内容一句话带过并链到 `examples/`, 绝不重复它们已经讲清的东西.

**篇幅是入口不是教程**, 软上限约 70 到 90 行.

---

## 2. 两条固定内容

**写死四个 skill.** `/showcase-learn`, `/showcase-quiz`, `/showcase-demo`, `/showcase-publish` 由 `lesson-smith-showcase-forge` 必然产出, 所以对应小节固定提及它们, 措辞近乎静态. learn 与 quiz 属 "怎么学", demo 与 publish 属 "学完怎么展示发布".

**不提 runbook.** 正文不引导环境 setup, 也不提 `docs/showcase/02-showcase-runbook.md` (那是给 AI 看的元文件). setup 交给 `/showcase-learn` 在学生真遇到麻烦时智能介入.

---

## 3. frontmatter, description

它是 **Task (这个 branch) 级**的介绍, 回答 "**你将学到什么**": 这个 branch 教的具体是哪些东西, 学完手上多了哪些能力.

和 `README-ORIGINAL` 那段的区别在海拔:

| | `README-ORIGINAL` 的 description | 这一份 |
| :--- | :--- | :--- |
| 海拔 | Lesson, 整个 Repo | Task, 这个 branch |
| 回答 | 为什么值得学, 学完有什么收获 | 你将学到什么 |
| 重点 | 动机与收获 | 内容与能力 |

showcase 只有一个 branch, 所以这一行看起来像在讲整个 Repo, 其实讲的仍是这个 Task, 只不过它底下装了很多 Task. 两段覆盖范围几乎重叠, **但别把 `README-ORIGINAL` 那段抄过来**. 反过来说, "为什么要学" 在这一份里不重要, 不用写.

**罗列在这里不是毛病, 但只限这一行.** 挑几个有代表性的 examples 主题串出来, 再加一句这门课要学的到底是什么, 恰恰是对的写法. 不必列全, 挑得出这门课的分量即可.

为什么这一行可以罗列而正文不可以: 这一行会被 `lesson-smith sync` 汇进 SYLLABUS, 将来也会进课程索引, **那时它是脱离 repo 单独出现的**, 读者点不进 `examples/`, 只能靠它自己把内容讲出来. 正文不一样, 读者已经站在 repo 里了, 一个链接就能到.

形态与长度见 [01-repo-layout.md](../../00-common/01-repo-layout.md) 第 6 节.

---

## 4. 正文结构

四个 H2, 按 markdown-style 从 1 连续编号, 相邻小节之间用分隔线隔开.

**第 1 节 这门课是什么.** 极简 2 到 3 句说清教什么, 外加 3 到 4 行 "这是 showcase 教学仓库, 该怎么用" 的元概念说明, **点明学完可以抹去教学痕迹当作品展示**. 想要完整定位就链到 `README-ORIGINAL`. 不写方法论长文.

**第 2 节 怎么学.** 讲三件事:

- 学的顺序: 进 `examples/`, 从 01 开始按编号一篇篇刷, 每个都照它自己的 TICKET 做完再往下. `examples/` 的第一个 Task 就是索引, 会给出整门课的地图.
- 两个帮手: `/showcase-learn` 带学, `/showcase-quiz` 自测.
- 学到什么算成: 用 `/showcase-quiz` 测到 70% 且思路清晰.

**第 3 节 学完之后: 展示与发布.** showcase 特有, 也是它的落点: 把这段经历讲出去, 并把 repo 变成作品. 两个帮手:

- `/showcase-demo` 陪你排练 "我是怎么做出这个的" 这段故事, 含接住追问.
- `/showcase-publish` 把 repo 抹去教学痕迹, 转成可放上自己 GitHub 的 portfolio repo.

**顺序要点明**: 先排练 demo, 再跑 publish. publish 会把 demo 底稿本身也一并清掉.

**第 4 节 学完你能做到什么.** 收尾一句, 呼应顶部 description, 并点出能把它作为一件作品讲出来.

**没有单独的 "课程内容" 一节.** 目录本身就是索引, 谁点进 `examples/` 都知道从 01 顺着看, 再单开一节说一遍是纯复述.

---

## 5. 写作原则

- **术语保留英文.** 中文只负责叙述, 术语, 产品名, 技术名词一律保留英文原文. 把 lazy evaluation 写成惰性求值, 读者反而认不出这门课在教什么, 这一行进了 SYLLABUS 也失去检索价值.
- **链接**: 指向 repo 内**文件**的相对路径链接用 `-cn` 版; 指向**目录**的链接不带语种后缀.
- H1 只用字母, 数字, 文字, 以及逗号, 冒号, 句号. 禁 emoji, 引号, 双引号, 方括号, 三种破折号.
- 遵循 `markdown-style` 与 `chinese-english-punctuation` 两个 Agent Skill.

---

## 6. 交付前自检

- 四个 skill 都提到了, 且 demo 在 publish 之前, runbook 一个字没提
- 四个 H2, 编号连续, 之间有分隔线
- 第 1 节点明了 "学完可以当作品展示" 这件事
- pitch 和内容都是一句话带过加一个链接, 没有整段复述
- description 写的是 "你将学到什么", 不是 `README-ORIGINAL` 那段的复制
- description 里罗列了几个有代表性的主题, 而正文里没有罗列
- 全文行数在 90 行以内
