<!--
本文件是 docs/upskill/01-upskill-learn.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

定性: 这是 "学习资料索引", 由 lesson-smith-upskill-forge 生成, 给 upskill-learn skill 消费, 学生也能直接读. 它不铺开讲知识 (知识在 examples 和素材本身里), 只回答三件事: 要学的东西有哪些, 在哪, 按什么顺序过. 它是索引, 不是完整的知识清单.

适用范围: upskill 类型 repo 的 docs/upskill/01-upskill-learn.md. 语言遵循创作铁律 (先写 cn, 定稿后 translate-to-en), 或按 repo 的语言约定.

学习资料分两类, 正文就是这两部分:

Part 1 学习素材 (study material): repo 里除 examples 渐进序列以外, 要学的东西 (根目录代码, 其它文档, 配置文件等). 这部分需要人类说清, 因为它不像 examples 那样自明. 两种情况:
- 情况 A, 教程本身就是要学的东西 (偏阅读, 内容都在 examples 里): 这部分很薄, 甚至只写一句 "无额外素材, 内容都在引导路径里".
- 情况 B, 真东西 (通常是代码) 在 repo 别处, examples 只是带你一步步走一遍: 这部分是主菜, 要把散落的素材梳理全.
每条素材给出: 一个 markdown 链接 (定位到文件, 需要时精确到某个 header 或关键字, 不用 line no), 一句话说学什么, 一句话说为什么重要或有什么坑.

Part 2 引导路径 (guided path): examples/01, 02 ... 的渐进序列就是学生要走的路, upskill-learn skill 按它往前推. 这部分 forge 扫一遍 examples 目录就能得到, 容易. 这里只概述整条线怎么推进 (分成几段, 每段学到什么), 并点向 examples/README (主题梳理) 和 docs/tasks/SYLLABUS (清单); 对情况 B, 标明每一段路径覆盖 Part 1 的哪些素材. 不要逐条复述每个 example 的正文.

写作原则:
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.
- 全程用 markdown 链接溯源, 定位一律用 header 或关键字, 不用 line no (line no 会随代码漂移).
- 这份 doc 可被直接编辑修正; 也可以重新 forge 刷新. 素材列错了直接改这里.
-->

# [课程名] 学习索引

> 这门课要学的东西有哪些, 在哪, 按什么顺序过. upskill-learn skill 按这份索引带你走.

## 1. 学习素材

[列出 examples 渐进序列之外, 你要学的东西. 情况 A 可以很薄; 情况 B 是主菜, 把散落的代码与文档梳理全. 每条: 链接 + 学什么 + 为什么重要或有什么坑.]

- [根目录的 some_module](../../some_module/) — [学什么] — [为什么重要, 或有什么坑]
- [某篇文档的某一节](../../docs/some-doc.md) — [学什么] — [注意什么]
- [mise.toml 的 tasks 段](../../mise.toml) — [有哪些常用命令] — [跑起来看 docs/upskill/02-upskill-runbook.md]

## 2. 引导路径

[examples/01, 02 ... 的渐进序列就是你要走的路. 这里概述整条线怎么推进, 点向索引与清单, 不逐条复述每个 example.]

整条线大致分成几段:

- [第一段主题]: examples/01 到 examples/0X — [这一段学到什么] (对应素材: [Part 1 的哪几条])
- [第二段主题]: examples/0X 往后 — [这一段学到什么] (对应素材: [Part 1 的哪几条])

详见 [examples 主题索引](../../examples/README.md) 与 [SYLLABUS](../tasks/SYLLABUS.md).
