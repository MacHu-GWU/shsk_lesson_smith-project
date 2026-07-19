<!--
本文件是 examples/README 系列索引的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 examples/README-cn.md 时, 把整段注释删掉, 只留后面的正文.

放置位置说明: 这个 spec 由 upskill 和 showcase 两种类型共用 (两者的 examples 布局一模一样). 目前物理上放在 ref/upskill 下; showcase 的规范应引用本文件, 不要复制一份.

定性: examples/README 是系列索引, 给刚进入 repo 的人一眼看清这门课有哪些 mini task, 以及它们是怎么组织的. 它不是教学文档 (教程在各 mini task 的 README 里).

适用范围: upskill 和 showcase 类型 repo 根目录下的 examples/README(-lang).md. 它不遵循 readme-spec (那是给单个 task 的教学 README 用的).

和 SYLLABUS 的区别 (这是本 spec 的核心): SYLLABUS 由脚本生成, 是无脑的平铺罗列, 一个 task 一段, 按 01, 02, 03 顺序排下来, 谁都不挨着谁. examples/README 恰恰相反, 是人手写的 "梳理": 把若干个 mini task 按主题聚成几个 group, 每个 group 一个大主题, 体现出结构, 分类与递进, 读起来是 "这门课分成这么几块, 每块解决什么", 而不是 "这里有 8 个东西". 两者海拔和目的都不同, 因此并存不冲突.

不带 frontmatter: 它是索引不是特殊文件, 不带 description frontmatter (那是 README, TICKET, README-ORIGINAL 才有的). lesson-smith lint 对它只查存在性和语种完整性, 不查内容; 内容质量靠人和本 spec 保证.

写作原则:
- 以 examples/README-cn.md 中文版为准: 先写中文, 定稿后用 translate-to-en 生成英文 examples/README.md.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.
- group 的数量与主题都随课程本身而定, 灵活机动; 下面的分组和用词只是示例.

结构:
- 开头一段: 说清这门课是什么, 以及 mini task 大致分成哪几块 (给读者一张地图).
- 中间若干个 group: 每个 group 一个编号 H2 (markdown-style 要求 H2 从 1 连续编号), 标题是这一组的主题; H2 下先一句话点出这组在讲什么, 再用 bullet 列出该组的 mini task, 每条给出目录链接和一句话说明.
- 结尾一段小结: 把这几块串起来, 说清学完整条线能得到什么.

链接: 指向各 mini task 的 README, 用相对路径 (例如 01-title/README-cn.md), 语种和本文件保持一致.
-->

# [课程名] 系列索引

[开头: 一段话说清这门课是什么, 以及下面的 mini task 大致分成哪几块, 给读者一张地图.]

## 1. [第一组主题]

[一句话点出这一组在解决什么.]

- [01-title](01-title/README-cn.md): [一句话说明这个 mini task.]
- [02-title](02-title/README-cn.md): [一句话说明这个 mini task.]

---

## 2. [第二组主题]

[一句话点出这一组在解决什么.]

- [03-title](03-title/README-cn.md): [一句话说明这个 mini task.]
- [04-title](04-title/README-cn.md): [一句话说明这个 mini task.]

---

## 3. 小结

[把上面几组串起来, 说清学完整条线你能得到什么.]
