# docs/showcase/04-showcase-demo-cn.md 规范, 中文版

**适用范围**: showcase 类型 repo 的 `docs/showcase/04-showcase-demo-cn.md`, 由 `lesson-smith-showcase-forge` 生成, 给 `showcase-demo-cn` skill 消费.

**配套骨架**: [docs-showcase-demo-cn-template.md](docs-showcase-demo-cn-template.md).

**当前只产这一套**: 英文版规范与骨架就在同目录下, 但 forge 现在只产 `-cn`.

**链接一律指 `-cn`**: 底稿指针必须指向 `README-cn.md`. 指到无后缀那一版就是指到一个空文件, 而 `showcase-demo-cn` 不会报错, 它会以为这个 repo 没有故事.

---

## 1. 它是什么

**它是指针, 不是故事.** 底稿真身 (七幕主线, 常见追问, 按听众裁剪) 全在 demo 那个 Task 的 README 里, 规范见 [showcase-demo-readme-spec](../../showcase-demo-readme-spec/showcase-demo-readme-cn-spec.md).

这份 doc 做三件事: **指出底稿在哪**, **把默认主线每幕一句记一遍** (让 skill 不必每次重推), 以及**记录人类对排练方式的要求**.

---

## 2. 三个部分

**底稿位置.** 一个 markdown 链接指向 demo 那个 Task 的 `README-cn.md`. forge 按固定目录名 `ZZ-how-i-build-this` 定位, 它是 `examples/` 的最后一个 Task.

**默认主线.** 七幕, 每幕一句. 默认故事讲的是方法论本身: 我如何用 AI 快速把一个技能学会并投入实战. 它既是作品叙事, 又顺带证明了 AI 协作能力.

这个 repo 的底稿如果偏离了默认主线, **一句话说清偏在哪**; 没偏离也要明说没偏离, 不要让读的人自己猜.

**排练自定义 (可选).** 人类对 `showcase-demo-cn` 的特殊要求: 默认听众是谁, 按多长的场子练, 哪几幕要重点练, 追问要不要更狠.

---

## 3. 写作原则

- **不要把整份底稿复制到这里**, 避免和底稿真身两处漂移. 这里只放指针, 默认骨架和自定义说明.
- 指向文件用 markdown 链接, 定位用 header 或关键字, 不用 line no.
- 遵循 markdown-style 与 chinese-english-punctuation 两个 Agent Skill.
