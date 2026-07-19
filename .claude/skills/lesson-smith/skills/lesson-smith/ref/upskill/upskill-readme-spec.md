<!--
本文件是 upskill 类型 repo 根目录 README 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 README-cn.md 与 README.md 时, 把整段注释删掉, 只留后面的正文.

定性: 根目录 README 是这门课的操作总入口. 它同时是唯一 branch 01-upskill 的 Task README 和仓库总览, 面向准备开始学的学生, 回答的是 "怎么用这个 repo 学". 它不是教学正文 (教程在各 mini task 的 README 里), 不是对外 pitch (pitch 在 README-ORIGINAL 里), 也不是内容地图 (地图在 examples/README 里).

适用范围: 仅 upskill 类型 repo 根目录的 README(-lang).md. 它不遵循 [ref/readme-spec.md](../readme-spec.md) (那是给单个 mini task 的教学 README 用的).

写作原则:
- 这份文档结构固定, 低歧义, 由 lesson-smith-upskill-finalize 一次性产出全部语种 (英文版加 supported-languages.json 里每个语种), 不走 "先写 cn 再 translate-to-en" 的分两步. 但思考口径仍以中文为准, 英文版自然改写而非逐字直译.
- 多链接, 少复述: pitch 一句话带过并链到 README-ORIGINAL, 内容一句话带过并链到 examples/README, 绝不重复它们已经讲清的东西.
- 篇幅是入口不是教程, 软上限约 60 到 80 行. 超了通常是把 pitch 或内容地图又抄了一遍.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.

不提 runbook: 正文不引导环境 setup, 也不提 docs/upskill/02-upskill-runbook.md (那是给 AI 看的元文件). setup 只在开始那一下和中途偶发, 交给 /upskill-learn 在学生真遇到麻烦时智能介入, 根 README 不必唠叨.

写死两个 skill: /upskill-learn 与 /upskill-quiz 由 lesson-smith-upskill-forge 必然产出, 所以 "怎么学" 一节固定提及它们, 措辞近乎静态.

H1 标题: 只用字母, 数字, 文字, 以及逗号, 冒号, 句号; 禁止 emoji, 引号, 双引号, 破折号等特殊符号 (理由同 readme-spec: H1 常被当字符串引用, 引号要转义).

顶部 frontmatter 的 description 是这门课的 "承诺": 一行说清学完你能做到什么 (获得的能力, 或能回答的问题), 而不是罗列教了哪些点. 它会被 lesson-smith sync 汇进 SYLLABUS. 长度与字符约束见 repo-layout.md 第 4 节.

正文结构 (四个 H2, 按 markdown-style 从 1 连续编号, 相邻小节之间用分隔线隔开):
- 第 1 节 这门课是什么: 极简 2 到 3 句说清教什么, 外加 3 到 4 行 "这是 upskill 教学仓库, 该怎么用" 的元概念说明 (学生可能不懂这个概念), 想要完整定位就链到 README-ORIGINAL. 不写方法论长文.
- 第 2 节 怎么学: 全文的篇幅重心. 讲读的顺序 (先看 examples/README 的系列索引, 再按编号顺序刷 examples 下的 mini task), 两个帮手 (/upskill-learn 带学, /upskill-quiz 自测), 以及学到什么算成 (用 /upskill-quiz 测到 70% 且思路清晰).
- 第 3 节 课程内容: 一句话加一个指向 examples/README 的链接, 不重复罗列 mini task.
- 第 4 节 学完你能做到什么: 收尾一句, 呼应顶部 description 的承诺.
-->

---
description: 一行, 这门课的承诺 (学完你能做到什么). 中文叙述加英文术语, 最多 400 字符.
---

# [课程名] 总览

> 一句话: 这门课教什么. 想先了解全貌, 看 [README-ORIGINAL-cn.md](README-ORIGINAL-cn.md).

## 1. 这门课是什么

[极简 2 到 3 句: 这门课教什么, 有意思在哪.]

这是一个 upskill 类型的教学仓库: 整个 repo 就是一门课, 内容拆成 [examples/](examples/) 下一个个按编号排列的 mini task, 学会即止. 你不需要把它当作从头读到尾的教材, 而是照下面 "怎么学" 的路子走一遍.

---

## 2. 怎么学

1. 先读 [examples/README-cn.md](examples/README-cn.md) 的系列索引, 对整门课有张地图.
2. 按编号顺序刷 examples 下的 mini task (01, 02, ...), 每个都照它自己的 TICKET 做完再往下.
3. 学的过程中有两个帮手随叫随到: `/upskill-learn` 是带学教练 (要地图, 要某一处讲透, 要决定下一步, 或卡住了都找它, 环境 setup 也由它带); `/upskill-quiz` 是面试式自测, 检验你是不是真的学懂了 (know-what 和 know-why).
4. 学到什么算成: 用 `/upskill-quiz` 测到 70% 的题都能思路清晰地答出来.

---

## 3. 课程内容

全部 mini task 按主题梳理在 [examples/README-cn.md](examples/README-cn.md) 里, 从那儿进入.

---

## 4. 学完你能做到什么

[收尾一句: 走完这门课你获得的能力, 呼应顶部 description 的承诺.]
