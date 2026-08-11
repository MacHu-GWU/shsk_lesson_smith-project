# Readup 课程创作工作流

这份文档定义如何从零创作一个符合 readup 规范的 repo. 它是整条创作流的骨架: **10 个步骤, 分成 6 个阶段**, 每个阶段有一个对应的 step skill 唤醒它.

readup 是纯阅读型仓库: 不带任何 AI 学习工具链 (没有带学, 自测子 skill, 没有给 AI 看的元文档, 也没有出题的 Task). 所以它比 upskill 和 showcase 少一个锻造工具链的阶段.

**前置**: 创作者以中文为母语, 全程只写中文 (见 lesson-smith 的创作铁律), 并遵循 `markdown-style` 与 `chinese-english-punctuation` 两个 Agent Skill. 整体布局见 [readup-repo-layout.md](readup-repo-layout.md).

---

## 1. 阶段与 step skill 的对应

创作者每到一个新阶段, 敲一次对应的 step skill. 它会把那个阶段要读的规范和要守的红线唤起来.

| 步骤 | 阶段 | step skill | 建议开新 session |
| :--- | :--- | :--- | :--- |
| 1 到 2 | 定题 | `/lesson-smith-readup-author-step-01-to-02-scope` | 跟 author 一起 |
| 3 到 5 | 规划与试水 | `/lesson-smith-readup-author-step-03-to-05-plan-and-trial` | |
| 6 | 写主线 | `/lesson-smith-readup-author-step-06-mainline` | |
| 7 到 8 | 补两头加统稿 | `/lesson-smith-readup-author-step-07-to-08-bookends-and-converge` | 是 |
| 9 | 写根目录文档 | `/lesson-smith-readup-author-step-09-root-docs` | 是 |
| 10 | 出厂 | `/lesson-smith-readup-author-step-10-ship` | 是 |

后三个阶段建议各开一个新 session, 因为它们都要通读整门课, 而前面写作留下的上下文只会挤占注意力. 每个新 session 开头先敲一次 `/lesson-smith-readup-author`, 再敲那一步的 step skill.

阶段这么切, 是因为缝都在真实的地方:

- **定题和规划之间**: 第 1 到 2 步想的是题材和代码, 第 3 步开始想的才是怎么教.
- **规划与试水不分家**: `examples/_lm-example-plan.md` 是第 3 步建的, 第 5 步改的. 把建它和改它切到两个阶段, 等于把一个循环从中间剖开.
- **补两头和统稿合并**: 两步都要通读全系列, 分开就是读两遍. 而且统稿要查 "规定动作齐不齐", 刚写完的两头正好一起过.

---

## 2. 想清楚教什么, 写大背景

> 步骤 1, 属于定题阶段.

先用概括, 笼统的方式想清楚这个 repo 大致要教一个什么东西, 按规范写 `README-ORIGINAL-cn.md` (遵循 [00-common/02-readme-original-spec](../00-common/02-readme-original-spec/readme-original-cn-spec.md)). 这是整门课的大背景与电梯陈述, 后面所有内容都长在它之上.

注意这**只是一版粗稿种子**: 此时 `examples/` 还没写, description 难免粗糙, 也和最终内容对不齐. 等全部内容完工后, **第 9 步会重写整份** `README-ORIGINAL-cn.md`, 让这门 Lesson 的门面和成品对齐. 所以这一步不用抠 description, 先把大方向写出来即可.

---

## 3. 先完成 examples 之外的 "做的部分"

> 步骤 2, 属于定题阶段.

如果这门课除了 `examples/` 之外还有很多代码, 文档, 例子 (即学生真正要去读, 去跑的东西), 先把这些 "做的部分" 全部完成. 从下一步开始, 就默认这些 examples 之外的东西已经写完了.

**很多课压根没有这一块.** 纯讲解型的课, 要学的东西全在 `examples/` 里, 那就直接跳到下一步, 不用为了凑一个步骤去造点什么出来.

为什么这一层要放在 `examples/` 而不是 tutorials, 见 [readup-repo-layout.md](readup-repo-layout.md) 第 1 节.

---

## 4. 和 AI 讨论, 规划这门课写哪些

> 步骤 3, 属于规划与试水阶段.

和 AI 讨论: 这门课应该写哪些内容, 边界在哪. 把讨论结果写进 `examples/_lm-example-plan.md` (这个文件允许进 git). 它是创作过程中的规划底稿, 会随着后面几步不断精修.

**这一步和第 5 步是一对.** 现在写的是纸上的计划, 第 5 步会拿写过三篇之后的手感回来改它. 所以这里不用抠细节, 把范围和分组的大方向定下来就行.

---

## 5. 先写前几篇试水, 锁定风格

> 步骤 4, 属于规划与试水阶段.

很难一次性写出完美的计划, 也很难凭空定好文章的深浅和风格. 所以先写前几篇试试水.

**从 02 开始写.** 01 那个位置留给索引 Task, 它是整门课的地图, 只能在路修完之后画, 属于第 7 步的活.

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

## 8. 回头补开头和结尾

> 步骤 7, 属于补两头加统稿阶段. **建议开新 session.**

主线写完了, 现在补两头. 两个都要写完, `examples/` 才算齐.

**结尾: 收尾 Task.** 放在最后一个位置. 它干两件事: 回望 (梳理这门课学了什么, 学完该到什么水平) 和拔高 (往哪走, 给搜索关键字与可粘贴的话题). 规范见 [00-common/14-wrap-up-readme-spec](../00-common/14-wrap-up-readme-spec/wrap-up-readme-cn-spec.md), 那里有一条红线: **拔高只提, 决不能教.**

**开头: 索引 Task.** 放在 `examples/01-title/`, 位置固定在 01, 目录名随课程而定. 它给刚进来的人一张地图: 这门课有哪些 Task, 怎么分组, 该按什么顺序读. 规范见 [00-common/05-overview-readme-spec](../00-common/05-overview-readme-spec/overview-readme-cn-spec.md) 与 [00-common/06-overview-ticket-spec](../00-common/06-overview-ticket-spec/overview-ticket-cn-spec.md).

**为什么放在这一步而不是最前面**: 地图只能在路修完之后画. 一开始就写索引, 写出来的一定是计划而不是成品的地图, 而计划在第 5, 6 步里还会变.

readup 没有单独的出题 Task: 每个 Task 自己的 TICKET 就是自查手段, 整门课的核对再由根目录 TICKET 汇总, 不需要额外的题库.

---

## 9. 统稿

> 步骤 8, 属于补两头加统稿阶段. **接着第 7 步做, 同一个 session.**

到这里 `examples/` 下全部 Task 都写完了, 但它们是一篇篇分头写出来的, 合起来未必是一条线. 这一步通读全系列, 一半纠错 (术语与表达不一致, 前后矛盾, 承上启下断掉), 一半给改稿建议 (头重脚轻, 该拆该并, 规定动作齐不齐).

做法见 [00-common/08-series-converge-spec.md](../00-common/08-series-converge-spec.md).

**为什么和第 7 步同一个 session**: 补两头本来就要通读全系列 (索引要按顺序和分组画地图, 收尾要说清整门课学了什么), 统稿要的是同一次通读. 分成两个 session 就是把同一批内容读两遍. 而且统稿第 3 节要查 "规定动作齐不齐", 刚写完的两头正好一起过.

**这一步是主线成文的判据**: 过了它, 这门课的教学内容才算定稿, 才能进下一步去写那些拿全系列当素材的根目录文档.

---

## 10. 写根目录文档

> 步骤 9. **建议开新 session.**

统稿之后 `examples/` 是稳定的素材, 这一步基于它们写 repo 根目录那三份:

- `README-cn.md` 阅读总入口
- `TICKET-cn.md` 整门课的验收清单
- 重写 `README-ORIGINAL-cn.md`

完整做法见 [00-common/09-root-docs-spec.md](../00-common/09-root-docs-spec.md), 里面含**一道必须停下来让创作者拍板的 gate**.

---

## 11. 出厂

> 步骤 10. **建议开新 session.**

跑 `lesson-smith sync` 生成 SYLLABUS 与 `docs/tasks/` 快照, 再跑 `lesson-smith lint` 把整仓过一遍, 有问题修到通过. 做法见 [00-common/10-ship-spec.md](../00-common/10-ship-spec.md).

过了 lint, 这门 readup 课创作完成.

---

## 附: 中译英 (当前跳过)

整门课的中文定稿之后, 原本还有一步一次性重写成英文, 那份规范已经归档在 [archive/rewrite-en-spec.md](../../archive/rewrite-en-spec.md).

**这一步当前不做, 直接跳过.** 原因是重写出来的英文质量不过关 (chinglish, 内容被压缩, 术语跨篇分叉). 与其产出一批迟早要返工的英文, 不如先把这个问题解决, 之后再作为独立的多语种模块回来做. 在那之前, 无后缀的英文文件保持留空.

所以走到出厂那一步时, repo 里只有 `-cn` 版有内容. **这是预期状态, 不是欠账**, lint 也不检查英文.
