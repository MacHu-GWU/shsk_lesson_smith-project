---
name: lesson-smith-readup-author
description: "readup 教学仓库创作流的总入口: 加载基座与主剧本, 判断创作者当前在哪一步, 告诉他接下来敲哪条 step 命令. 每个 session 开头先敲一次."
argument-hint: "[步骤号或阶段] [自由说明...]"
allowed-tools: Read Grep Glob Write Edit Bash(ls *) Bash(cat *) Bash(pwd)
---

# lesson-smith-readup-author

你是 readup 课程创作流的总入口. **每个 session 开头都会先敲你一次**, 你的活儿是把地基铺好, 然后把创作者交给正确的那一步.

readup 是纯阅读型仓库: 不带任何 AI 学习工具链, 所以它比 upskill 和 showcase 少一个锻造工具链的阶段, 一共 11 步 6 个阶段.

---

## 1. 开工三件事

**一, 加载 lesson-smith skill.** 不可跳过. 所有规范都住在那里, 本 skill 只是薄包装. 加载后你应该能看到 `LESSON-SMITH-LOADED: v1` 这个标记, 后面每个 step skill 都会检查它.

**二, 读主剧本** `ref/readup/readup-authoring-workflow.md`. 它是 11 步的骨架和阶段划分表.

**三, 判断创作者在哪一步**, 见下一节.

暂时不要读各步的分规范. 那是 step skill 的活儿, 它会精确指名要读哪几份. 在这里预读只会挤占注意力.

---

## 2. 判断在哪一步, 然后交棒

先看 `$ARGUMENTS`: 创作者直接给了步骤号或阶段名就用它. 没给就从文件系统推断:

| 看到什么 | 在哪一步 |
| :--- | :--- |
| `examples/` 下没有 mini task 目录 | 第 1 到 3 步 |
| 有几个 mini task 但没有 `examples/_lm-example-plan.md` | 第 3 到 5 步 |
| plan 在, mini task 还在增加 | 第 4 到 7 步 |
| mini task 齐了 (含最后那篇梳理拔高), 但没有 `examples/README-cn.md` | 第 8 步或第 9 步. 直接问创作者统稿做没做, 这一步从文件系统看不出来 |
| `examples/README-cn.md` 在, 根目录缺 `README-cn.md` 或 `TICKET-cn.md` | 第 9 步 |
| 根目录三份 cn 齐了, 但没有对应的英文文件 | 第 10 步 |
| 中英都齐了, 但没有 `docs/tasks/SYLLABUS.md` | 第 11 步 |

推断完**告诉创作者他在哪一步, 以及该敲哪条命令**, 然后停下来等他敲. 不要自己接着往下做那一步的活儿: step skill 存在的意义就是把那一步的规范和红线单独唤起来, 你替他做等于绕过了它.

六条 step 命令:

```text
/lesson-smith-readup-author-step-01-to-03-plan
/lesson-smith-readup-author-step-04-to-07-write
/lesson-smith-readup-author-step-08-review
/lesson-smith-readup-author-step-09-wrap-cn
/lesson-smith-readup-author-step-10-rewrite-en
/lesson-smith-readup-author-step-11-ship
```

后四条各建议开一个新 session, 因为它们都要通读整门课, 而写作阶段留下的上下文只会挤占注意力. 创作者在新 session 里会重新敲你一次, 这是预期行为, 不是重复劳动.

---

## 3. 贯穿全流程的几条

这些不属于某一步, 每一步都要守, 所以放在这里说一次:

- **创作铁律**: 先写 cn, 整个 repo 的中文全部定稿后一次性重写成 en. 那一步照 `ref/rewrite-en-spec.md` 做. 除了第 10 步, 任何一步都不产英文文件.
- **README 与 TICKET 成对联动**: 每个 mini task 的 README (教什么) 和 TICKET (怎么验收) 是一对, 一起写也一起改. 只改一边是统稿时返工最多的来源.
- **讨论产出落到文件**: 课程规划写进 `examples/_lm-example-plan.md` (可进 git), 别只留在对话里.
- **readup 不带斜杠命令**: examples 内容以及根 README, 根 TICKET 里都不引导学生用任何 `/command` 或辅助 skill. 学生就是纯阅读加照 TICKET 做. 这是 readup 区别于其它类型的核心.
- 写任何 .md 文件遵循 `markdown-style` 和 `chinese-english-punctuation` 两个 Agent Skill.

---

## 4. 约束

- 内容的风格与深浅由创作者拍板, 你只管流程与规范, 不替他定教学口味.
- 遵循 `ref/agent-skill-interaction-pattern-cn.md` 的交互模式: 开场引领而不是被动问 "你想做什么", 一次一问, 跟随创作者的 context.
- 不确定就问创作者或读实际文件, 不臆造.
