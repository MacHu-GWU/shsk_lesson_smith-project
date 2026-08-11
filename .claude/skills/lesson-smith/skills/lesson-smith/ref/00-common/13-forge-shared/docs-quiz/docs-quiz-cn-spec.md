# docs/{{TYPE}}/03-{{TYPE}}-quiz-cn.md 规范, 中文版

**适用范围**: {{TYPE}} 类型 repo 的 `docs/{{TYPE}}/03-{{TYPE}}-quiz-cn.md`, 由 `lesson-smith-{{TYPE}}-forge` 生成, 给 `{{TYPE}}-quiz-cn` skill 消费.

**配套骨架**: [docs-quiz-cn-template.md](docs-quiz-cn-template.md).

**当前只产这一套**: 英文版规范与骨架就在同目录下, 但 forge 现在只产 `-cn`.

**链接一律指 `-cn`**: 题库指针必须指向 `README-cn.md`. 指到无后缀那一版就是指到一个空文件, 而且 `{{TYPE}}-quiz-cn` 不会报错, 它会以为这门课没有题.

---

## 1. 它是什么

**quiz 的薄壳.** 它本身**不出题**.

题目, 考察点, 参考回答, 深入解读全在 quiz 那个 Task 的 README 里, 规范见 [11-quiz-readme-spec](../../11-quiz-readme-spec/quiz-readme-cn-spec.md).

这份 doc 只做两件事: **指出题库在哪**, 以及**记录人类对考法的自定义要求**.

---

## 2. 两个部分

**第一部分, 题库位置.** 用 markdown 链接指向 quiz 那个 Task 的 `README-cn.md` (即题库真身), 让 `{{TYPE}}-quiz-cn` skill 知道去哪读题.

这部分容易, forge 按固定目录名 `NN-prove-i-get-it` 就能定位. 一句话说清是哪个 Task, 顺带给出题量.

**第二部分, 考法自定义 (可选).** 人类在这里写对 `{{TYPE}}-quiz-cn` 行为的特殊要求和说明. 例如: 默认抽几道, 是否按主题分组考, 哪些题偏重, 用什么口吻, 有没有时间限制, 及格线怎么算.

没有特殊要求就写一句 "没有特殊要求, 按 skill 默认来".

---

## 3. 写作原则

- **不要把题目本身复制到这里**, 避免和题库真身两处漂移. 这里只放指针和自定义说明.
- 指向文件用 markdown 链接, 定位用 header 或关键字, 不用 line no.
- 遵循 markdown-style 与 chinese-english-punctuation 两个 Agent Skill, **但 H2 之间不加分隔线**.
- 那条分隔线的豁免是有意的, 不是漏了: `docs/<type>/` 下这几份是给 skill 读的机器文件, 没有 frontmatter, 不进 lint, 也没人会从头念一遍. 配套 template 里因此一条分隔线都没有, 照抄即可. 全套里只有这一类文件是这样, 别拿它去套别处的 spec.
