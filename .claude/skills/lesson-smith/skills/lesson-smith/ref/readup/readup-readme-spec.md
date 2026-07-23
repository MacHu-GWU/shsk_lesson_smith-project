<!--
本文件是 readup 类型 repo 根目录 README 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 README-cn.md 与 README.md 时, 把整段注释删掉, 只留后面的正文.

定性: 根目录 README 是这门课的阅读总入口. 它同时是唯一 branch 01-readup 的 Task README 和仓库总览, 面向准备开始读的学生, 回答的是 "怎么用这个 repo 学". 它不是教学正文 (教程在各 mini task 的 README 里), 不是对外 pitch (pitch 在 README-ORIGINAL 里), 也不是内容地图 (地图在 examples/README 里).

适用范围: 仅 readup 类型 repo 根目录的 README(-lang).md. 它不遵循 [ref/readme-spec.md](../readme-spec.md) (那是给单个 mini task 的教学 README 用的).

写作原则:
- 这份文档结构固定, 低歧义, 由 lesson-smith-readup-finalize 一次性产出全部语种 (英文版加 supported-languages.json 里每个语种), 不走 "先写 cn 再 translate-to-en" 的分两步. 但思考口径仍以中文为准, 英文版自然改写而非逐字直译.
- 多链接, 少复述: pitch 一句话带过并链到 README-ORIGINAL, 内容一句话带过并链到 examples/README, 绝不重复它们已经讲清的东西.
- 篇幅是入口不是教程, 软上限约 50 到 70 行. 超了通常是把 pitch 或内容地图又抄了一遍.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.

不提任何斜杠命令 (readup 的立身之本): readup 是纯阅读型仓库, 面向还不知道 AI Agent Skill 是什么的读者, 整门课不带任何辅助 skill. 所以正文绝不出现 /upskill-learn, /upskill-quiz 之类的斜杠命令; 也不引导环境 setup, 不提任何给 AI 看的元文档. 学生要做什么, 怎么自查, 全靠一篇篇 mini task 自己的 README 与 TICKET. 这一条是 readup 区别于其它类型的核心, 写 README 时优先守住.

H1 标题: 只用字母, 数字, 文字, 以及逗号, 冒号, 句号; 禁止 emoji, 引号, 双引号, 破折号等特殊符号 (理由同 readme-spec: H1 常被当字符串引用, 引号要转义).

顶部 frontmatter 的 description 是这门课的 "承诺": 一行说清读完你能做到什么 (获得的能力, 或能回答的问题), 而不是罗列教了哪些点. 它会被 lesson-smith sync 汇进 SYLLABUS. description 的值必须用双引号包起来, 长度, 字符与该约束见 repo-layout.md 第 4 节.

正文结构 (四个 H2, 按 markdown-style 从 1 连续编号, 相邻小节之间用分隔线隔开):
- 第 1 节 这门课是什么: 极简 2 到 3 句说清教什么, 外加 2 到 3 行 "这是 readup 教学仓库, 该怎么用" 的元概念说明 (整个 repo 就是一门课, 内容拆成 examples 下按编号排列的 mini task, 顺着读即可; 学生可能连这个概念都不熟). 不写方法论长文.
- 第 2 节 怎么读: 全文的篇幅重心. 讲读的顺序 (先看 examples/README 的系列索引, 再按编号顺序一篇篇读 examples 下的 mini task, 每篇先读 README 再照它的 TICKET 做), 以及读到什么算成 (每个 mini task 的 TICKET 都能逐项打勾, 能不看教程独立复现). 全程不提任何斜杠命令或辅助工具.
- 第 3 节 课程内容: 一句话加一个指向 examples/README 的链接, 不重复罗列 mini task.
- 第 4 节 读完你能做到什么: 收尾一句, 呼应顶部 description 的承诺.
-->

---
description: "一行, 这门课的承诺 (读完你能做到什么). 中文叙述加英文术语, 最多 400 字符."
---

# [课程名] 总览

> 一句话: 这门课教什么. 想先了解全貌, 看 [README-ORIGINAL-cn.md](README-ORIGINAL-cn.md).

## 1. 这门课是什么

[极简 2 到 3 句: 这门课教什么, 有意思在哪.]

这是一个 readup 类型的教学仓库: 整个 repo 就是一门课, 内容拆成 [examples/](examples/) 下一个个按编号排列的 mini task. 你不用把它当成一本从头读到尾的大部头, 只要照下面 "怎么读" 的路子, 一篇篇顺着读下来, 边读边照每篇的 TICKET 做, 就能学会.

---

## 2. 怎么读

1. 先读 [examples/README-cn.md](examples/README-cn.md) 的系列索引, 对整门课有张地图.
2. 按编号顺序读 examples 下的 mini task (01, 02, ...): 每个 mini task 目录里, 先读 README (这一篇教什么, 带你做什么), 再照它的 TICKET 把 "要做的事情" 逐项做完, 用 "检查清单" 自查是不是真的做到了.
3. 一篇读完再读下一篇, 直到读完最后一篇 (它会帮你梳理学到了什么, 并指出想更进一步可以往哪走).
4. 读到什么算成: 每个 mini task 的 TICKET 检查清单都能逐项打勾, 且能不看教程自己把核心流程走一遍.

---

## 3. 课程内容

全部 mini task 按主题梳理在 [examples/README-cn.md](examples/README-cn.md) 里, 从那儿进入.

---

## 4. 读完你能做到什么

[收尾一句: 走完这门课你获得的能力, 呼应顶部 description 的承诺.]
