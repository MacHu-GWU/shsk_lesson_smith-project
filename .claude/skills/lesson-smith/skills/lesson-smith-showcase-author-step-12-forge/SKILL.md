---
name: lesson-smith-showcase-author-step-12-forge
description: "第 12 步: 锻造学习与展示工具链, 产出 docs/showcase 五份 doc 与四个子 skill"
argument-hint: "[自由说明...]"
disable-model-invocation: true
---

# showcase 创作流 第 12 步

你在 **showcase 创作工作流的第 12 步**: 锻造学习与展示工具链.

主剧本是 `lesson-smith` skill 的 `ref/03-showcase/showcase-authoring-workflow.md`, 本步对应它的第 13 节. 先读那一节接上上下文, 再按下面动手.

---

## 1. 先确认基座在场

在上下文里找 `LESSON-SMITH-LOADED: v1` 这个标记. **找不到就先加载 `lesson-smith` skill 再回来.**

按约定每个 session 开头都会敲一次 `/lesson-smith-showcase-author`, 所以通常你已经看得到它. 但没有基座就动手, 产出会违反一堆你根本不知道存在的规范, 而且要拖到出厂那步跑 lint 才炸.

---

## 2. 这一步怎么做

**这一步的活儿由 `/lesson-smith-showcase-forge` 完成**, 不在这里手写. 它产出两样东西:

- `docs/showcase/` 下五份 doc: 学习索引, 跑起来的操作, quiz 薄壳, demo 薄壳, publish 清单.
- `.claude/skills/` 下四个子 skill: `showcase-learn-cn`, `showcase-quiz-cn`, `showcase-demo-cn`, `showcase-publish-cn`.

规范与模板都在 `ref/03-showcase/forge/` 下, 由那个 skill 自己去读, 你不用预读.

为方便编辑那次调用的输入, 用模板 `prompts/run-lesson-smith-showcase-forge.md`.

---

## 3. publish 那一份要额外认真

另外四份产歪了大不了重生成, **publish 清单指导的是删文件, 而且删的是学生自己那份 repo**. 两处最容易出人命:

- **语种收敛**: 留下有内容的那一版 (`-cn`), 删掉留空的占位符, 再去掉后缀. **判断哪一版是占位符必须去读文件内容, 不许看后缀就下结论.** 做反了就是把整门课删光, 留下一棵空文件的树, 而且后面没有任何一步会发现.
- **删除区间**: quiz, demo, 收尾三个连着排在 `examples/` 最末, 一起删. 排在 quiz 之前的主线 Task 是作品内容, 要保留, 归待定项让学生自己判断.

清单里的 glob 都要**在生成时对着真实的树展开成路径**, 留着 glob 等于把展开的活推给一个将来没有上下文的 session.

---

## 4. 这一步的红线

- **统稿没过不许跑.** forge 产出的是索引和指针, 指向 `examples/` 里的文件与标题, 而统稿会改标题, 会拆篇并篇, 甚至调编号. 早跑一步, 链接和锚点全指在会变的东西上, 而且没有任何检查会报出来.
- **只产 `-cn` 那一套.** 英文规范和骨架就在 `forge/` 目录里, 但当前不产出, 因为无后缀的英文课程正文留空, 英文索引只会指向一堆空文件.
- **有五件事机器猜不出, 必须停下来问创作者**: 哪些算学习素材 (以及这门课是情况 A 还是 B), runbook 里有哪些隐性步骤, quiz 想怎么考, demo 想怎么排练, publish 清单里哪些算待定项.
- **别在这里出题, 也别在这里写故事.** 题库真身是第 8 步写的, 讲故事底稿是第 9 步写的, forge 只负责定位它们并写好那两份薄壳的指针.
- **demo 按名字找, 不按位置找.** `NN-how-i-build-this` 后面还有一个收尾 Task, 它不是 `examples/` 的最后一个.
- 跑完**别急着关 session**: 第 13 步接着在这个 session 里做, 它要的正是刚读进来的这批素材.

---

## 5. 自由说明

`$ARGUMENTS` 是创作者对这一步的额外指示. 有就一并采纳, 没有按规范默认.
