# 出厂规范

创作流的最后一步: 生成 SYLLABUS 与 `docs/tasks/` 快照, 跑 lint 把整仓过一遍, 修到通过.

适用范围: readup, upskill, showcase 三类通用. 位置在英文重写之后 (upskill 与 showcase 还要在 forge 之后), 因为 sync 快照的是 README 与 TICKET 的**全部语种**, lint 也校验语种完整性. 英文还没产出就跑, sync 会快照一半, lint 会报一堆语种缺失.

**这一步不写内容.** 不碰 examples, 不碰根目录那几份, 不碰 `docs/upskill` 或 `docs/showcase`. lint 报出来的问题如果需要改正文, 那是回到对应步骤去改, 不是在这里顺手补.

---

## 1. 先确认前置齐了

跑之前核一遍, 缺了就停下来告诉创作者该回哪一步, 不要硬着头皮往下跑:

- `examples/` 下每个 mini task 的 README 与 TICKET 都有 cn 与英文两份.
- 根目录 `README`, `TICKET`, `README-ORIGINAL` 也都有两份.
- upskill 与 showcase: `docs/<type>/` 下的 doc 与 `.claude/skills/<type>-*/` 子 skill 都在 (那是 forge 的产物).

---

## 2. sync

在 repo 根目录跑:

```bash
uvx --from shsk-lesson-smith==<version> lesson-smith sync -p .
```

`<version>` 取当前最新发布版, uvx 与 pin 版本的理由见 [ref/repo-layout.md](repo-layout.md) 第 6 节. 本地已装好该 package 时直接 `lesson-smith sync` 亦可.

它生成 `docs/tasks/SYLLABUS` 与 `docs/tasks/<branch>/` 下的 README, TICKET 快照.

**SYLLABUS 与快照一律不手写.** 命令不可用或报错就如实告诉创作者, 不要自己拼一份出来: 手写的那份下次 sync 会被覆盖, 而在被覆盖之前它会一直看起来是对的.

---

## 3. lint

```bash
uvx --from shsk-lesson-smith==<version> lesson-smith lint -p .
```

它只读, 校验目录结构, 命名, 语种完整性, frontmatter 的 description 与 github_about, H1 字符集, SYLLABUS 内容是否与各 README 的 description 一致.

按报告逐条修到通过. 常见的几类, 以及该回哪一步修:

| lint 报什么 | 通常是哪一步欠的账 |
| :--- | :--- |
| description 超长 | 写全局中文那步 (README-ORIGINAL 最常见), 或英文重写没压住 |
| description 没加双引号, 或值里有引号 | 英文重写时 frontmatter 走形 |
| H1 字符集 | 英文重写把标题写成了带连字符的形式 |
| README-ORIGINAL 的 H1 不等于 repo 名 | 英文重写把 repo 名当标题重写了, 改回去即可 |
| 语种缺失 | 英文重写漏了文件, 或根本没跑 |
| SYLLABUS 对不上 | 改过 README 的 description 之后没重跑 sync |

改完正文之后要**重跑 sync 再重跑 lint**, 因为 SYLLABUS 是从 description 生成的.

---

## 4. 汇报

跑完告诉创作者:

1. sync 创建或更新了哪些文件.
2. lint 报了什么, 各自怎么修的.
3. 这门课到此收尾完成, 可以从根目录 README 进入开始学.
