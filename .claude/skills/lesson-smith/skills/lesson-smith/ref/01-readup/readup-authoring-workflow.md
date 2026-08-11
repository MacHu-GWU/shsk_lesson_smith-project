# Readup 课程创作工作流

这份文档定义如何从零创作一个符合 readup 规范的 repo. 它是整条创作流的骨架: 11 个步骤, 分成 6 个阶段, 每个阶段有一个对应的 step skill 唤醒它.

readup 是纯阅读型仓库: 不带任何 AI 学习工具链 (没有带学, 自测子 skill, 没有给 AI 看的元文档, 也没有出题的 mini task). 所以它比 upskill 和 showcase 少一个锻造工具链的阶段.

前置: 创作者以中文为母语, 遵循创作铁律 (先写 cn, 全部定稿后一次性重写成 en, 见 [ref/rewrite-en-spec.md](../rewrite-en-spec.md)) 和 markdown-style, chinese-english-punctuation 两个 Agent Skill. 整体布局见 [ref/readup/readup-repo-layout.md](readup-repo-layout.md).

---

## 1. 阶段与 step skill 的对应

创作者每到一个新阶段, 敲一次对应的 step skill. 它会把那个阶段要读的规范和要守的红线唤起来.

| 步骤 | 阶段 | step skill | 建议开新 session |
| :--- | :--- | :--- | :--- |
| 1 到 3 | 规划 | `/lesson-smith-readup-author-step-01-to-03-plan` | 跟 author 一起 |
| 4 到 7 | 写 mini task | `/lesson-smith-readup-author-step-04-to-07-write` | |
| 8 | 统稿 | `/lesson-smith-readup-author-step-08-review` | 是 |
| 9 | 写全局中文 | `/lesson-smith-readup-author-step-09-wrap-cn` | 是 |
| 10 | 重写英文 | `/lesson-smith-readup-author-step-10-rewrite-en` | 是 |
| 11 | 出厂 | `/lesson-smith-readup-author-step-11-ship` | 是 |

后四个阶段建议各开一个新 session, 因为它们都要通读整门课, 而前面写作留下的上下文只会挤占注意力. 每个新 session 开头先敲一次 `/lesson-smith-readup-author`, 再敲那一步的 step skill.

---

## 2. 想清楚教什么, 写大背景

> 步骤 1, 属于规划阶段.

先用概括, 笼统的方式想清楚这个 repo 大致要教一个什么东西, 按规范写 `README-ORIGINAL-cn.md` (遵循 [ref/common/readme-original-spec/readme-original-spec.md](../common/readme-original-spec/readme-original-spec.md)). 这是整门课的大背景与电梯陈述, 后面所有内容都长在它之上.

注意这只是一版粗稿种子: 此时 examples 还没写, description 难免粗糙, 也和最终内容对不齐. 等全部内容完工后, 第 9 步会重写整份 `README-ORIGINAL-cn.md`, 让这门 Lesson 的门面和成品对齐. 所以这一步不用抠 description, 先把大方向写出来即可. 也不要写英文版, 英文是第 10 步的事.

---

## 3. 先完成 examples 之外的 "做的部分"

> 步骤 2, 属于规划阶段.

如果这门课除了 examples 之外还有很多代码, 文档, 例子 (即学生真正要去读, 去跑的东西), 先把这些 "做的部分" 全部完成. 从下一步开始, 就默认这些 examples 之外的东西已经写完了. 为什么这一层要放在 examples 而不是 tutorials, 见 [ref/readup/readup-repo-layout.md](readup-repo-layout.md).

---

## 4. 和 AI 讨论, 规划这门课写哪些

> 步骤 3, 属于规划阶段.

和 AI 讨论: 这门课应该写哪些内容, 边界在哪. 把讨论结果写进 `examples/_lm-example-plan.md` (这个文件允许进 git). 它是创作过程中的规划底稿, 会随着后面几步不断精修.

---

## 5. 先写前几篇试水, 锁定风格

> 步骤 4, 属于写 mini task 阶段.

很难一次性写出完美的计划, 也很难凭空定好文章的深浅和风格. 所以先写前几篇试试水. 01 一般是一个开头: overview, 综述, 讲清这门课的意义, 背景, 目标等基本科普信息, 结构较固定. 再写 02, 03 之类, 写过之后心里才会清楚整个 examples 系列该怎么写.

---

## 6. 精修前几篇, 更新计划, 进入快速迭代

> 步骤 5, 属于写 mini task 阶段. **最容易被跳过的一步.**

写完 01, 02, 03 基本心里有数了. 回到 `examples/_lm-example-plan.md` 更新一版, 顺手精修 01, 02, 03. 从这里开始进入快速迭代模式. 此时对后面的教学系列也大致有谱了: 分成几个组, 每组几篇. 这个不必定死, 但有个大概想法, 最终差别不会太大. 把这些都写进 plan.

跳过这一步的代价是, 前三篇的风格没锁死就一路写到底, 最后统稿时要返工的量比现在停下来精修大得多.

---

## 7. 一步步往后写

> 步骤 6, 属于写 mini task 阶段.

从 04 开始 (具体从第几篇取决于前面写了几篇) 一步步往后推进, 把教学系列写完.

---

## 8. 写最后一篇: 梳理与拔高

> 步骤 7, 属于写 mini task 阶段.

最后写最后一个 mini task. 它梳理这门课学了什么, 学完应该达到什么水平; 如果还想更进一步, 给出拔高方向: 可以搜索引擎搜哪些关键字, 以及一句话的话题, 方便学生直接复制粘贴去喂给 AI, 深挖, 拓宽边界.

readup 没有单独的出题 mini task: 每篇 mini task 自己的 TICKET 就是自查手段, 整门课的核对再由根目录 TICKET 汇总, 不需要额外的题库.

---

## 9. 统稿

> 步骤 8. **建议开新 session.**

到这里各篇 mini task 都写完了, 但它们是一篇篇分头写出来的, 合起来未必是一条线. 这一步通读全系列, 把不一致, 矛盾, 遗漏, 断掉的承上启下找出来并修掉. 做法见 [ref/review-spec.md](../review-spec.md).

这一步是主干成文的判据: 过了它, 这门课的中文教学内容才算定稿, 才能进第 9 步去写那些拿全系列当素材的全局文档.

---

## 10. 写全局中文

> 步骤 9. **建议开新 session.**

统稿之后, examples 是稳定的素材, 这一步基于它们写四份全局文档的中文版:

- `examples/README-cn.md` 系列索引
- 根目录 `README-cn.md` 与 `TICKET-cn.md`
- 重写 `README-ORIGINAL-cn.md`

全部只写 cn 版, 英文是下一步的事. 完整做法见 [ref/readup/readup-wrap-cn-spec.md](readup-wrap-cn-spec.md), 里面含一道必须停下来让创作者拍板的 gate.

---

## 11. 一次性重写成英文

> 步骤 10. **建议开新 session.**

到此为止整个 repo 的正文都是 cn 版. 这一步一次性把它们重写成英文.

完整规范见 [ref/rewrite-en-spec.md](../rewrite-en-spec.md), 照它做即可, 不要在这里重新推导. 那份规范定死了用哪条命令, 处理哪些文件 (六组 glob, 含根目录那三份), 要额外交代哪两条 lint 硬约束, 链接怎么分文件和目录处理, 以及跑完要修什么.

**不要问创作者要文件清单.** 创作者手工在新会话里发起时, 用自包含的模板 [prompts/run-rewrite-en.md](../../prompts/run-rewrite-en.md).

---

## 12. 出厂

> 步骤 11. **建议开新 session.**

跑 `lesson-smith sync` 生成 SYLLABUS 与 `docs/tasks/` 快照, 再跑 `lesson-smith lint` 把整仓过一遍, 有问题修到通过. 做法见 [ref/ship-spec.md](../ship-spec.md).

过了 lint, 这门 readup 课创作完成.
