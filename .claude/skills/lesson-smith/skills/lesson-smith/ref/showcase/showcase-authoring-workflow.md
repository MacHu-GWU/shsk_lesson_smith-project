# Showcase 课程创作工作流

这份文档定义如何从零创作一个符合 showcase 规范的 repo, 主要是 examples 下那一整套课程内容怎么一步步做出来, 直到能对外展示发布. 它由 lesson-smith-showcase-author skill 加载, AI 按这份剧本带着创作者往前走.

前置: 创作者以中文为母语, 遵循创作铁律 (先写 cn, 定稿后 translate-to-en) 和 markdown-style, chinese-english-punctuation 两个 Agent Skill. 整体布局见 [ref/showcase/showcase-repo-layout.md](showcase-repo-layout.md).

showcase 与 upskill 的差别集中在收尾: showcase 多一个 demo 讲故事底稿 (examples 的最后一个 mini task), 并在整门课之后有对外 publish 环节. 下面的步骤据此安排.

## 1. 想清楚教什么, 写大背景

先用概括, 笼统的方式想清楚这个 repo 大致要教一个什么东西, 按规范写 README-ORIGINAL-cn.md (遵循 [ref/readme-original-spec.md](../readme-original-spec.md)). 这是整门课的大背景与电梯陈述, 后面所有内容都长在它之上.

注意这只是一版粗稿种子: 此时 examples 还没写, description 难免粗糙, 也和最终内容对不齐. 等全部内容完工后, 最后一步的 finalize 会重写整份 README-ORIGINAL (正文, description, github_about, 全语种), 让这门 Lesson 的门面和成品对齐. 所以这一步不用抠 description, 先把大方向写出来即可.

---

## 2. 先完成 examples 之外的 "做的部分"

如果这门课除了 examples 之外还有很多代码, 文档, 例子 (即学生真正要去读, 去跑的东西), 先把这些 "做的部分" 全部完成. 从下一步开始, 就默认这些 examples 之外的东西已经写完了. 为什么这一层要放在 examples 而不是 tutorials, 见 [ref/showcase/showcase-repo-layout.md](showcase-repo-layout.md).

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

## 7. 教学系列收尾: 拔高只提不教

教学系列写完后, 如果想给学生指个拔高方向 (学了 A, 相关的 B, C, D 也值得知道), 可以在最后一篇教学 mini task 里加一小节点一下: 给几个搜索关键字, 加一句话的话题, 方便学生直接复制粘贴去喂给 AI 深挖. 红线: 拔高只能提, 决不能为它单独展开写教程. 一旦开口教就和这个 repo 的教学系列冲突, 没完没了; 要教就直接作为正式 mini task, 不走拔高这个口子.

---

## 8. 规划 quiz

教学系列写完后, 开始准备 quiz 材料. quiz 是 examples 里靠后的一个 mini task, 目录固定命名为 NN-prove-i-get-it (视角是学生自己检查自己). 动笔写题之前, 先扫描之前写过的全部教程和其它教学相关文件, 规划一个 quiz 问题清单和问题数量, 写进 examples/_lm-quiz-plan.md. 这一步 AI 给建议, 人类也给反馈和意见, 讨论几轮, 锁定题目数量和清单方向.

---

## 9. 写 quiz 并精修

按 [ref/showcase/showcase-examples-quiz-readme-spec.md](showcase-examples-quiz-readme-spec.md) 写这个 mini task 的 README (题库, 每题四段: 问题, 考察点, 参考回答, 深入解读), 按 [ref/showcase/showcase-examples-quiz-ticket-spec.md](showcase-examples-quiz-ticket-spec.md) 写它固定的 TICKET (读一遍题库 + 用 /showcase-quiz 测到 70% 通过), 然后精修.

---

## 10. 写 demo 讲故事底稿 (examples 最后一个 mini task)

写 examples 的最后一个 mini task: demo 讲故事底稿, 目录固定命名为 how-i-build-this. 按 [ref/showcase/showcase-examples-demo-readme-spec.md](showcase-examples-demo-readme-spec.md) 写它的 README (把默认七幕主线用这个 repo 的真实经历填实: 具体是什么技能, 什么领域, 调研了什么, 大纲长什么样, 例子是哪些, 最后投入到哪个真实问题; 再补常见追问和按听众裁剪), 按 [ref/showcase/showcase-examples-demo-ticket-spec.md](showcase-examples-demo-ticket-spec.md) 写它固定的 TICKET (读一遍底稿 + 用 /showcase-demo 排练到能流畅讲完并接住追问), 然后精修.

这一步是 showcase 相对 upskill 多出来的. 它服务于学完之后的对外展示: 学生靠这份底稿把 "我是怎么做出这个的" 排练好. 注意这份底稿本身是教学痕迹, 之后 publish 时会被删掉, 所以它的价值在排练, 不在留存.

---

## 11. 写 examples/README 系列索引

写 examples/README.md 做梳理, 按 [ref/showcase/showcase-examples-readme-spec.md](showcase-examples-readme-spec.md) 来. 重点是避免陈列 (不是无脑罗列 mini task), 而是按主题分组梳理, 结尾把 quiz 与 demo 两个收尾 mini task 交代清楚. 人类主要在前后插入个性化的内容和观点.

---

## 12. 批量翻译成英文

到此为止所有正文都是 cn 版. 用 translate-to-en Agent Skill 启动多个 agent, 批量并行把各 mini task 的 README-cn.md, TICKET-cn.md 以及 examples/README-cn.md 翻译成对应的英文文件.

---

## 13. 交给 forge 产出学习与展示工具链

用 /lesson-smith-showcase-forge 完成 docs/showcase/ 下五份 doc (learn, runbook, quiz, demo, publish) 以及 .claude/skills/showcase-*/SKILL.md 四个子 skill 的产出. 这个过程中人类需要兜底做决策 (哪些是学习素材, runbook 的隐性步骤, quiz 考法, demo 排练自定义, publish 清单的取舍等). 为方便编辑那次调用的输入, 用模板 [prompts/run-lesson-smith-showcase-forge.md](../../prompts/run-lesson-smith-showcase-forge.md).

---

## 14. 交给 finalize 收尾定型

到这一步 examples 内容和学习工具链都齐了, 最后给整门课收尾. 用 /lesson-smith-showcase-finalize 完成: 重写 README-ORIGINAL (整个 Repo 也就是这门 Lesson 的对外门面, 让 description 与 github_about 和最终内容对齐, 遵循 [ref/readme-original-spec.md](../readme-original-spec.md)); 写出根目录的 README (仓库总览加操作入口, 覆盖怎么学与学完怎么展示发布, 遵循 [ref/showcase/showcase-readme-spec.md](showcase-readme-spec.md)) 与 TICKET (整门课的验收清单, 遵循 [ref/showcase/showcase-ticket-spec.md](showcase-ticket-spec.md)). 这几份结构固定, 由 finalize 一次性产出全部语种, 不再走 cn-first 分两步. 随后 finalize 会跑 lesson-smith sync 生成 SYLLABUS 与快照, 再跑 lesson-smith lint 把关. 为方便编辑那次调用的输入, 用模板 [prompts/run-lesson-smith-showcase-finalize.md](../../prompts/run-lesson-smith-showcase-finalize.md).

到此整门 showcase 课创作完成. 学生学完后, 可以用 /showcase-demo 排练怎么讲这段经历, 再用 /showcase-publish 把 repo 抹去教学痕迹, 发布成自己 GitHub 上的 portfolio repo.
