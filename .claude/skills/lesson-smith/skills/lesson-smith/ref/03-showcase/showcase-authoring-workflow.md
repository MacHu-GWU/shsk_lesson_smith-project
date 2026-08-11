# Showcase 课程创作工作流

这份文档定义如何从零创作一个符合 showcase 规范的 repo. 它是整条创作流的骨架: **14 个步骤, 分成 9 个阶段**, 每个阶段有一个对应的 step skill 唤醒它.

showcase 比 upskill 多两样东西: `examples/` 里多一个 demo 讲故事底稿 Task, 以及整门课学完之后多一个对外 publish 环节 (由 forge 产出的 `showcase-publish-cn` skill 承担, **不是创作流的一步**, 是学生自己后来跑的).

**前置**: 创作者以中文为母语, 全程只写中文 (见 lesson-smith 的创作铁律), 并遵循 `markdown-style` 与 `chinese-english-punctuation` 两个 Agent Skill. 整体布局见 [showcase-repo-layout.md](showcase-repo-layout.md).

---

## 1. 阶段与 step skill 的对应

创作者每到一个新阶段, 敲一次对应的 step skill. 它会把那个阶段要读的规范和要守的红线唤起来.

| 步骤 | 阶段 | step skill | 建议开新 session |
| :--- | :--- | :--- | :--- |
| 1 到 2 | 定题 | `/lesson-smith-showcase-author-step-01-to-02-scope` | 跟 author 一起 |
| 3 到 5 | 规划与试水 | `/lesson-smith-showcase-author-step-03-to-05-plan-and-trial` | |
| 6 | 写主线 | `/lesson-smith-showcase-author-step-06-mainline` | |
| 7 到 8 | 写 quiz | `/lesson-smith-showcase-author-step-07-to-08-quiz` | |
| 9 | 写 demo | `/lesson-smith-showcase-author-step-09-demo` | |
| 10 到 11 | 补两头加统稿 | `/lesson-smith-showcase-author-step-10-to-11-bookends-and-converge` | 是 |
| 12 | 锻造 | `/lesson-smith-showcase-author-step-12-forge` | 是 |
| 13 | 写根目录文档 | `/lesson-smith-showcase-author-step-13-root-docs` | 接着 12 那个 session |
| 14 | 出厂 | `/lesson-smith-showcase-author-step-14-ship` | 是 |

后面几个阶段建议各开一个新 session, 因为它们都要通读整门课, 而前面留下的上下文只会挤占注意力. 每个新 session 开头先敲一次 `/lesson-smith-showcase-author`, 再敲那一步的 step skill.

**第 13 步不要另开 session.** 锻造那一步已经把整套 examples 读进来了, 写根目录文档要的正是同一批素材, 接着写能省一次通读, 而且刚锻造出来的四个子 skill 就在手边, 根 README 里提到它们时可以立刻验证.

阶段这么切, 是因为缝都在真实的地方:

- **定题和规划之间**: 第 1 到 2 步想的是题材和代码, 第 3 步开始想的才是怎么教.
- **规划与试水不分家**: `examples/_lm-example-plan.md` 是第 3 步建的, 第 5 步改的. 把建它和改它切到两个阶段, 等于把一个循环从中间剖开.
- **主线单独成段**: 前面是边写边定风格, 第 6 步风格已经锁死, 剩下的是产量.
- **quiz 和 demo 各自成段**: 它们是两个特殊 Task, 规范, 红线和产出形态都不一样 (一个是题库, 一个是叙事底稿). 一个 Task 一个阶段, 将来加第三个就是加一个阶段, 前后都不用动.
- **补两头和统稿合并**: 两步都要通读全系列, 分开就是读两遍. 而且统稿要查 "规定动作齐不齐", 刚写完的两头正好一起过.

---

## 2. 想清楚教什么, 写大背景

> 步骤 1, 属于定题阶段.

先用概括, 笼统的方式想清楚这个 repo 大致要教一个什么东西, 按规范写 `README-ORIGINAL-cn.md` (遵循 [00-common/02-readme-original-spec](../00-common/02-readme-original-spec/readme-original-cn-spec.md)). 这是整门课的大背景与电梯陈述, 后面所有内容都长在它之上.

注意这**只是一版粗稿种子**: 此时 `examples/` 还没写, description 难免粗糙, 也和最终内容对不齐. 等全部内容完工后, **第 13 步会重写整份** `README-ORIGINAL-cn.md`, 让这门 Lesson 的门面和成品对齐. 所以这一步不用抠 description, 先把大方向写出来即可.

---

## 3. 先完成 examples 之外的 "做的部分"

> 步骤 2, 属于定题阶段.

如果这门课除了 `examples/` 之外还有很多代码, 文档, 例子 (即学生真正要去读, 去跑的东西), 先把这些 "做的部分" 全部完成. 从下一步开始, 就默认这些 examples 之外的东西已经写完了.

**很多课压根没有这一块.** 纯讲解型的课, 要学的东西全在 `examples/` 里, 那就直接跳到下一步, 不用为了凑一个步骤去造点什么出来.

不过 showcase 是三类里**最可能有这一块的**: 它的终点是学生把这个 repo 当自己的作品拿出去讲, 而一个只有教程没有产物的 repo 讲不出故事.

为什么这一层要放在 `examples/` 而不是 tutorials, 见 [showcase-repo-layout.md](showcase-repo-layout.md) 第 1 节.

---

## 4. 和 AI 讨论, 规划这门课写哪些

> 步骤 3, 属于规划与试水阶段.

和 AI 讨论: 这门课应该写哪些内容, 边界在哪. 把讨论结果写进 `examples/_lm-example-plan.md` (这个文件允许进 git). 它是创作过程中的规划底稿, 会随着后面几步不断精修.

**这一步和第 5 步是一对.** 现在写的是纸上的计划, 第 5 步会拿写过三篇之后的手感回来改它. 所以这里不用抠细节, 把范围和分组的大方向定下来就行.

---

## 5. 先写前几篇试水, 锁定风格

> 步骤 4, 属于规划与试水阶段.

很难一次性写出完美的计划, 也很难凭空定好文章的深浅和风格. 所以先写前几篇试试水.

**从 02 开始写.** 01 那个位置留给索引 Task, 它是整门课的地图, 只能在路修完之后画, 属于第 10 步的活.

所以这里从 `examples/02-title/` 起手, 一般写到 04 左右:

- **02 是综述**, 交代话题本身的背景: 这个领域怎么来的, 现在什么局面, 学生进来之前该知道什么. 长短取决于话题需要多少铺垫, 可以很长.
- **03, 04 是最前面两篇主线**, 真正开始教东西.

位置约定见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 4.2 节.

写过这三篇, 心里才会清楚整个系列该怎么写.

---

## 6. 精修前几篇, 更新计划, 进入快速迭代

> 步骤 5, 属于规划与试水阶段. **最容易被跳过的一步.**

写完 02, 03, 04 基本心里有数了. 回到 `examples/_lm-example-plan.md` 更新一版, 顺手精修这几篇. 从这里开始进入快速迭代模式.

此时对后面的教学系列也大致有谱了: 分成几个组, 每组几篇. 这个不必定死, 但有个大概想法, 最终差别不会太大. 把这些都写进 plan.

跳过这一步的代价是, **前几篇的风格没锁死就一路写到底**, 最后统稿时要返工的量比现在停下来精修大得多.

---

## 7. 一步步往后写

> 步骤 6, 属于写主线阶段.

从 05 开始 (具体从第几篇取决于前面写了几篇) 一步步往后推进, 把主线写完.

**这一阶段单独成段**, 因为它和前面两个阶段的性质不同: 前面是边写边定风格, 这里风格已经锁死, 剩下的是产量. 它也是全流程最长的一段.

---

## 8. 规划 quiz

> 步骤 7, 属于写 quiz 阶段.

主线的最后一篇写完之后, 开始准备 quiz 材料.

**动笔写题之前先规划.** 扫一遍之前写过的全部主线 Task 和其它教学相关文件, 定出一个问题清单和题量, 写进 `examples/_lm-quiz-plan.md`. AI 提建议, 创作者也给反馈, 讨论几轮, 把题量和方向锁定.

quiz 是 `examples/` 里靠后的一个 Task, 目录固定命名 `NN-prove-i-get-it` (视角是学生自己检查自己). 它排在主线之后, **demo 之前** (位置约定见 [00-common/01-repo-layout.md](../00-common/01-repo-layout.md) 第 4.2 节).

---

## 9. 写 quiz 并精修

> 步骤 8, 属于写 quiz 阶段.

按 [00-common/11-quiz-readme-spec](../00-common/11-quiz-readme-spec/quiz-readme-cn-spec.md) 写这个 Task 的 README, 也就是题库真身 (每题四段: 问题, 考察点, 参考回答, 深入解读).

按 [00-common/12-quiz-ticket-spec](../00-common/12-quiz-ticket-spec/quiz-ticket-cn-spec.md) 写它的 TICKET, 内容固定极简: 读一遍题库, 再用 quiz 那个子 skill 测到 70% 通过.

写完精修一遍. **每道题都要能在 repo 里找到出处**, 编不出出处的题就是超纲题.

**quiz 只考技术知识.** 关于这段经历和方法的元问题 (为什么选这个技能, AI 生成的东西你真懂吗) 归下一步的 demo, 别混进题库.

---

## 10. 写 demo 讲故事底稿

> 步骤 9, 属于写 demo 阶段. **这一步是 showcase 相对 upskill 多出来的.**

写 `examples/NN-how-i-build-this/`, 目录名固定. 它排在 quiz 之后, 收尾之前.

按 [showcase-demo-readme-spec](showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md) 写它的 README: 把**默认七幕主线**用这个 repo 的真实经历填实 (具体是什么技能, 什么领域, 调研了什么, 大纲长什么样, 例子是哪些, 最后投入到哪个真实问题), 再补常见追问和按听众裁剪.

按 [showcase-demo-ticket-spec](showcase-demo-ticket-spec/showcase-demo-ticket-cn-spec.md) 写它的 TICKET: 读一遍底稿, 再用 demo 那个子 skill 排练到能流畅讲完并接住追问.

**为什么排在 quiz 之后**: 七幕里有一幕是 "在 AI 陪伴下学完并验收", 它要指向 quiz 那个 Task 当产物. quiz 还没写, 那一幕就没有东西可指.

**这份底稿是教学痕迹, 将来会被删掉.** 学生跑 publish 时, 这个 Task, 对应的 doc 和 demo 子 skill 都会一起清掉. 所以它的价值在**排练**, 不在留存: 真正带走的是学生脑子里那套能讲的故事. 写的时候就按这个前提写.

---

## 11. 回头补开头和结尾

> 步骤 10, 属于补两头加统稿阶段. **建议开新 session.**

主线, quiz, demo 都写完了, 现在补两头. 两个都写完, `examples/` 才算齐.

**结尾: 收尾 Task.** 放在最后一个位置, 在 demo 之后. 它梳理这门课学了什么, 学完应该达到什么水平; 如果还想更进一步, 给出拔高方向: 可以搜索引擎搜哪些关键字, 以及一句话的话题, 方便学生直接复制粘贴去喂给 AI, 深挖, 拓宽边界.

**拔高只提, 决不能教.** 一旦为某个拔高方向单独展开写教程, 就和这个 repo 的主线冲突, 而且没完没了. 真想教就把它变成一个正式的主线 Task, 不走拔高这个口子.

**开头: 索引 Task.** 放在 `examples/01-title/`, 位置固定在 01, 目录名随课程而定. 它给刚进来的人一张地图: 这门课有哪些 Task, 怎么分组, 该按什么顺序读. 规范见 [00-common/05-overview-readme-spec](../00-common/05-overview-readme-spec/overview-readme-cn-spec.md) 与 [00-common/06-overview-ticket-spec](../00-common/06-overview-ticket-spec/overview-ticket-cn-spec.md).

**为什么放在这一步而不是最前面**: 地图只能在路修完之后画. 一开始就写索引, 写出来的一定是计划而不是成品的地图, 而计划在第 5, 6 步里还会变.

索引里给 Task 分组时, **quiz, demo, 收尾各自单独成组**, 一个占一个 group, 不许几个挤一组, 也不许混进主线 Task 的列表.

---

## 12. 统稿

> 步骤 11, 属于补两头加统稿阶段. **接着第 10 步做, 同一个 session.**

到这里 `examples/` 下全部 Task 都写完了, 但它们是一篇篇分头写出来的, 合起来未必是一条线. 这一步通读全系列, 一半纠错 (术语与表达不一致, 前后矛盾, 承上启下断掉), 一半给改稿建议 (头重脚轻, 该拆该并, 规定动作齐不齐).

做法见 [00-common/08-series-converge-spec.md](../00-common/08-series-converge-spec.md).

**这一步是主线成文的判据**: 过了它, 这门课的教学内容才算定稿. 后面三步 (锻造, 根目录文档, 出厂) 全都拿 `examples/` 当素材, 素材不稳就白做.

**为什么和第 10 步同一个 session**: 补两头本来就要通读全系列 (索引要按顺序和分组画地图, 收尾要说清整门课学了什么), 统稿要的是同一次通读. 分成两个 session 就是把同一批内容读两遍. 而且统稿第 3 节要查 "规定动作齐不齐", 刚写完的两头正好一起过.

---

## 13. 锻造学习与展示工具链

> 步骤 12. **建议开新 session.**

用 `/lesson-smith-showcase-forge` 产出两样东西:

- `docs/showcase/` 下五份 doc: 学习索引, 跑起来的操作, quiz 薄壳, demo 薄壳, publish 清单.
- `.claude/skills/` 下四个子 skill: `showcase-learn-cn`, `showcase-quiz-cn`, `showcase-demo-cn`, `showcase-publish-cn`.

规范与模板分两处: 和 upskill 共用的三份在 [00-common/13-forge-shared/](../00-common/13-forge-shared/) (里面的 `<type>` 落地时换成 `showcase`), showcase 独有的 demo 与 publish 在 [forge/](forge/). 每份中英各一套, **当前只产 `-cn` 那一套**.

这一步 AI 猜不出的部分要创作者兜底拍板: 哪些算学习素材, runbook 里有哪些隐性步骤, quiz 想怎么考, demo 想怎么排练, publish 清单里哪些算待定项. 为方便编辑那次调用的输入, 用模板 [prompts/run-lesson-smith-showcase-forge.md](../../prompts/run-lesson-smith-showcase-forge.md).

**publish 那一份要特别认真.** 另外四份产歪了大不了重生成, 而 publish 清单指导的是**删文件**, 而且删的是学生自己那份 repo. 尤其是语种收敛那一节: 留下有内容的那一版, 删掉留空的占位符, 判断哪版是占位符必须去读文件.

**为什么卡在统稿之后**: forge 产出的是索引和指针, 它们指向 `examples/` 里的文件与标题. 统稿会改标题, 会拆篇并篇, 甚至会调整编号. 统稿之前跑, 产出的链接和锚点全都指在会变的东西上, 而且没有任何检查会报出来.

---

## 14. 写根目录文档

> 步骤 13. **建议开新 session.**

这一步基于定稿的 `examples/` 写 repo 根目录那三份:

- `README-cn.md` 仓库总览加操作入口, 覆盖怎么学以及学完怎么展示发布
- `TICKET-cn.md` 整门课的验收清单
- 重写 `README-ORIGINAL-cn.md`

完整做法见 [00-common/09-root-docs-spec.md](../00-common/09-root-docs-spec.md), 里面含**一道必须停下来让创作者拍板的 gate**.

**为什么排在 forge 之后**: 根 README 要指名道姓提到四个子 skill, 根 TICKET 的检查清单里也有 "用 quiz 测到 70%". forge 先跑完, 写这几句的时候命令是真能敲的, 而不是照着规范默写一个还不存在的东西.

---

## 15. 出厂

> 步骤 14. **建议开新 session.**

跑 `lesson-smith sync` 生成 SYLLABUS 与 `docs/tasks/` 快照, 再跑 `lesson-smith lint` 把整仓过一遍, 有问题修到通过. 做法见 [00-common/10-ship-spec.md](../00-common/10-ship-spec.md).

lint 会检查 forge 的产物, 所以它必须排在第 12 步之后.

过了 lint, 这门 showcase 课创作完成.

学生学完之后, 用 demo 那个子 skill 排练怎么讲这段经历, 再用 publish 那个把 repo 抹去教学痕迹, 发布成自己 GitHub 上的作品仓库. **那两步不属于创作流**, 是学生自己后来跑的.

---

## 附: 中译英 (当前跳过)

整门课的中文定稿之后, 原本还有一步一次性重写成英文, 那份规范已经归档在 [archive/rewrite-en-spec.md](../../archive/rewrite-en-spec.md).

**这一步当前不做, 直接跳过.** 原因是重写出来的英文质量不过关 (chinglish, 内容被压缩, 术语跨篇分叉). 与其产出一批迟早要返工的英文, 不如先把这个问题解决, 之后再作为独立的多语种模块回来做. 在那之前, 无后缀的英文文件保持留空.

所以走到出厂那一步时, repo 里只有 `-cn` 版有内容. **这是预期状态, 不是欠账**, lint 也不检查英文.
