<!--
本文件是 docs/showcase/02-showcase-runbook.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

本文件独立成篇, 不引用 ref/upskill/ 下任何文件; 需要引用时只引 ref/ 根目录的通用 spec.

定性: 这是 "把课程跑起来的操作手册", 由 lesson-smith-showcase-forge 生成, 给 showcase-learn skill 消费. 它只管 "怎么把要学的东西跑起来", 不讲知识 (知识在 examples 和素材里), 也不做索引 (那是 01-showcase-learn.md 的活). 它没有对应的独立 skill, 由 showcase-learn 在学生遇到 setup 或运行麻烦时读取.

适用范围: showcase 类型 repo 的 docs/showcase/02-showcase-runbook.md. 这是给 AI/skill 看的元文件, 人类读的是真正的教程正文 (examples 下的), 不读这个; 所以它产出内容全英文, 不走 cn-first 铁律. 因此下面的正文模板本身就是英文的.

内容分两块:

第一块, 开始 examples 之前的一次性 setup: 前置工具与版本, 首次 setup 的命令. 这些命令大多已经在 mise.toml 里 (tasks 与工具版本), 原样引过来, 不改写.

第二块, 推进 examples 过程中的操作: 一切和 "把例子, 要学的东西跑起来" 相关的动作, 例如切目录 (cd), 设环境变量, 起服务, 以及跳出命令行的操作 (注册某个账号, 在浏览器里 setup 某个东西).

核心原则 (这份 doc 的价值所在): 把导师默认懂, 但学生 follow 时不懂的隐性操作显式写清. 导师做的时候有经验, 一看目录结构就知道该 cd 到哪, 该先跑哪个命令, 往往不会显式说; 学生照着 examples 走却会卡住. 凡是这类 "没写出来但必须做" 的步骤, 都要在这里补明白.

精炼原则: examples/01, 02 ... 如果只是标准地一个个往前推, 没有额外操作, 就用一两句概括整体节奏, 不要逐个 example 枚举. 只有某一步需要跳出常规 (注册账号, 浏览器 setup, 切到某个特殊目录等), 才把那一步单拎出来单独说.

写作原则:
- 命令原样可跑, 逐字照抄, 不要转述或改写.
- 需要指向文件时用 markdown 链接, 定位用 header 或关键字, 不用 line no.
- 没有内容的小节保留标题, 写一句占位 (例如 none yet, fill in as you hit them), 不要整节删掉.
-->

# [Course Name] Runbook

> How to run this course: how to set up before you start, and which environment / command / operational steps come up as you go. When something will not run, look here first.

## 1. Environment Setup

[A one-time setup before the examples begin. Most commands live in mise.toml; copy them verbatim.]

- Prerequisites: [tools and versions, from [mise.toml](../../mise.toml)]
- First-time setup:
1. [command one, runnable as-is]
2. [command two]

## 2. Operations Along the Way

[Do not enumerate examples/01, 02 ... one by one; a sentence or two on the overall rhythm is enough. Make explicit the implicit steps a mentor takes for granted but a following student does not know; then call out the steps worth singling out.]

Overall rhythm: [one line, e.g. most examples are read-the-README-and-follow, no extra operation; only the spots below step off the beaten path.]

Steps worth singling out:

- At [examples/0X]: [the extra operation, e.g. register some account, enable some setting in the browser, cd into some dir, set some env var]
- At [examples/0Y]: [the extra operation]

## 3. Common Snags

[Known footguns and fixes. If none, write none yet, fill in as you hit them.]
