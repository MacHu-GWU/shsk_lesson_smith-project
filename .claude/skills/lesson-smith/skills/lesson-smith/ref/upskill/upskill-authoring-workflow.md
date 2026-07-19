# Upskill 课程创作工作流

这份文档定义如何从零创作一个符合 upskill 规范的 repo, 主要是 examples 下那一整套课程内容怎么一步步做出来. 它由 lesson-smith-upskill-author skill 加载, AI 按这份剧本带着创作者往前走.

前置: 创作者以中文为母语, 遵循创作铁律 (先写 cn, 定稿后 translate-to-en) 和 markdown-style, chinese-english-punctuation 两个 Agent Skill. 整体布局见 [ref/upskill/upskill-repo-layout.md](upskill-repo-layout.md).

## 1. 想清楚教什么, 写大背景

先用概括, 笼统的方式想清楚这个 repo 大致要教一个什么东西, 按规范写 README-ORIGINAL-cn.md (遵循 [ref/readme-original-spec.md](../readme-original-spec.md)). 这是整门课的大背景与电梯陈述, 后面所有内容都长在它之上.

---

## 2. 先完成 examples 之外的 "做的部分"

如果这门课除了 examples 之外还有很多代码, 文档, 例子 (即学生真正要去读, 去跑的东西), 先把这些 "做的部分" 全部完成. 从下一步开始, 就默认这些 examples 之外的东西已经写完了. 为什么这一层要放在 examples 而不是 tutorials, 见 [ref/upskill/upskill-repo-layout.md](upskill-repo-layout.md).

---

## 3. 和 AI 讨论, 规划这门课写哪些

和 AI 讨论: 这门课应该写哪些内容, 边界在哪. 把讨论结果写进 examples/_lm-example-plan.md (这个文件允许进 git). 它是创作过程中的规划底稿, 会随着后面几步不断精修.

---

## 4. 先写前几篇试水, 锁定风格

很难一次性写出完美的计划, 也很难凭空定好文章的深浅和风格. 所以先写前几篇试试水. 01 一般是一个开头: overview, 综述, 讲清这门课的意义, 背景, 目标等基本科普信息, 结构较固定. 再写 02, 03 之类, 写过之后心里才会清楚整个 examples 系列该怎么写.

---

## 5. 精修前几篇, 更新计划, 进入快速迭代

写完 01, 02, 03 基本心里有数了. 回到 examples/_lm-example-plan.md 更新一版, 顺手精修 01, 02, 03. 从这里开始进入快速迭代模式. 此时对后面的教学系列也大致有谱了: 分成几个组, 每组几篇. 这个不必定死, 但有个大概想法, 最终差别不会太大. 把这些都写进 plan.

---

## 6. 一步步往后写

从 04 开始 (具体从第几篇取决于前面写了几篇) 一步步往后推进, 把教学系列写完.

---

## 7. 写到最后一篇教程后, 规划 quiz

教程系列的最后一篇写完后, 开始准备 quiz 材料. quiz 是 examples 里靠后的一个 mini task, 目录固定命名为 NN-prove-i-get-it (视角是学生自己检查自己). 动笔写题之前, 先扫描之前写过的全部教程和其它教学相关文件, 规划一个 quiz 问题清单和问题数量, 写进 examples/_lm-quiz-plan.md. 这一步 AI 给建议, 人类也给反馈和意见, 讨论几轮, 锁定题目数量和清单方向.

---

## 8. 写 quiz 并精修

按 [ref/upskill/examples-quiz-spec.md](examples-quiz-spec.md) 写 quiz 题库 (每题四段: 问题, 考察点, 参考回答, 深入解读), 然后精修.

---

## 9. 写最后一篇: 梳理与拔高

最后写最后一个 mini task. 它梳理这门课学了什么, 学完应该达到什么水平; 如果还想更进一步, 给出拔高方向: 可以搜索引擎搜哪些关键字, 以及一句话的话题, 方便学生直接复制粘贴去喂给 AI, 深挖, 拓宽边界.

---

## 10. 写 examples/README 系列索引

写 examples/README.md 做梳理, 按 [ref/upskill/examples-readme-spec.md](examples-readme-spec.md) 来. 重点是避免陈列 (不是无脑罗列 mini task), 而是按主题分组梳理. 人类主要在前后插入个性化的内容和观点.

---

## 11. 批量翻译成英文

到此为止所有正文都是 cn 版. 用 translate-to-en Agent Skill 启动多个 agent, 批量并行把各 mini task 的 README-cn.md, TICKET-cn.md 以及 examples/README-cn.md 翻译成对应的英文文件.

---

## 12. 交给 forge 产出学习工具链

用 /lesson-smith-upskill-forge 完成 docs/upskill/ 下的文档以及 .claude/skills/upskill-*/SKILL.md 的产出. 这个过程中人类需要兜底做决策 (哪些是学习素材, runbook 的隐性步骤, quiz 考法等). 为方便编辑那次调用的输入, 用模板 [prompts/run-lesson-smith-upskill-forge.md](../../prompts/run-lesson-smith-upskill-forge.md).

---

## 13. 后续

还有第 13 步及以后, 不过对应的 skill 都还没准备好, 等之后再说.
