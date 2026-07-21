<!--
本文件是 docs/showcase/01-showcase-learn.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

定性: 这是 "学习资料索引", 由 lesson-smith-showcase-forge 生成, 给 showcase-learn skill 消费. 它不铺开讲知识 (知识在 examples 和素材本身里), 只回答三件事: 要学的东西有哪些, 在哪, 按什么顺序过. 它是索引, 不是完整的知识清单.

适用范围: showcase 类型 repo 的 docs/showcase/01-showcase-learn.md. 这是给 AI/skill 看的元文件, 人类读的是真正的教程正文 (examples 下的), 不读这个; 所以它产出内容全英文, 不走 cn-first 铁律. 因此下面的正文模板本身就是英文的.

学习资料分两类, 正文就是这两部分:

Part 1 学习素材 (study material): repo 里除 examples 渐进序列以外, 要学的东西 (根目录代码, 其它文档, 配置文件等). 这部分需要人类说清, 因为它不像 examples 那样自明. 两种情况:
- 情况 A, 教程本身就是要学的东西 (偏阅读, 内容都在 examples 里): 这部分很薄, 甚至只写一句 no extra material, it is all in the guided path.
- 情况 B, 真东西 (通常是代码) 在 repo 别处, examples 只是带你一步步走一遍: 这部分是主菜, 要把散落的素材梳理全.
每条素材给出: 一个 markdown 链接 (定位到文件, 需要时精确到某个 header 或关键字, 不用 line no), 一句话说学什么, 一句话说为什么重要或有什么坑.

Part 2 引导路径 (guided path): examples/01, 02 ... 的渐进序列就是学生要走的路, showcase-learn skill 按它往前推. 这部分 forge 扫一遍 examples 目录就能得到, 容易. 这里只概述整条线怎么推进 (分成几段, 每段学到什么), 并点向 examples/README 和 docs/tasks/SYLLABUS; 对情况 B, 标明每一段路径覆盖 Part 1 的哪些素材. 引导路径讲的是教学 mini task 的推进, 不含结尾的 quiz 与 demo 两个特殊 mini task (它们各由 showcase-quiz 与 showcase-demo skill 负责, 不在带学路径里). 不要逐条复述每个 example 的正文.

写作原则:
- 全程用 markdown 链接溯源, 定位一律用 header 或关键字, 不用 line no (line no 会随代码漂移).
- 这份 doc 可被直接编辑修正, 也可以重新 forge 刷新. 素材列错了直接改这里.
-->

# [Course Name] Learning Index

> What there is to learn in this course, where it lives, and in what order to go through it. The showcase-learn skill walks you along this index.

## 1. Study Material

[List what there is to learn outside the examples progression. In case A this can be thin; in case B it is the main course, so gather the scattered code and docs. Each entry: a link, what to learn, and why it matters or a gotcha.]

- [some_module at the repo root](../../some_module/) — [what to learn] — [why it matters, or a gotcha]
- [a section of some doc](../../docs/some-doc.md) — [what to learn] — [what to watch out for]
- [the tasks section of mise.toml](../../mise.toml) — [the common commands] — [for running things, see docs/showcase/02-showcase-runbook.md]

## 2. Guided Path

[The examples/01, 02 ... progression is the path the student walks. Summarize how the whole line advances; point at the index and the syllabus; do not restate each example. Stop at the teaching mini tasks; the trailing quiz and demo tasks are handled by their own skills.]

The whole line breaks into a few stretches:

- [First stretch theme]: examples/01 to examples/0X — [what this stretch teaches] (covers study material: [which Part 1 entries])
- [Second stretch theme]: examples/0X onward — [what this stretch teaches] (covers study material: [which Part 1 entries])

See the [examples theme index](../../examples/README.md) and the [SYLLABUS](../tasks/SYLLABUS.md).
