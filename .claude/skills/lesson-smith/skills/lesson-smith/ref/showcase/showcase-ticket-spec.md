<!--
本文件是 showcase 类型 repo 根目录 TICKET 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 TICKET-cn.md 与 TICKET.md 时, 把整段注释删掉, 只留后面的正文.

定性: 根目录 TICKET 是整门课 (唯一 branch 01-showcase) 的验收清单, 主要给学生自查用. 各 mini task 自己的 TICKET 负责单个 task 的验收; 这一份站在整门课的高度, 汇总成一张 "我是不是把这门课学完学透, 并且能把它作为作品展示出去" 的核对表.

适用范围: 仅 showcase 类型 repo 根目录的 TICKET(-lang).md. 它在通用 ref/ticket-spec.md 的三段式之上, 多加一个 H2 (关键能力); 通用规范其余部分仍以它为准.

showcase 与 upskill 的关键差异 (体现在这份 TICKET 上): showcase 的验收不止 "学会", 还包含 "能讲 (demo) 与能发布 (publish)". 所以 "要做的事情" 的路径末尾多两步 (排练 demo, 跑 publish 抹痕迹), "检查清单" 里也多相应两条. 是否把 publish 真正跑通计入验收由创作者定; 至少要把 "能讲清这段经历" 列入.

写作原则:
- 这份文档结构固定, 低歧义, 由 lesson-smith-showcase-finalize 一次性产出全部语种 (英文版加 supported-languages.json 里每个语种), 不走分两步翻译. 思考口径以中文为准, 英文版自然改写.
- 沿用 ticket-spec 的三段式 (目标, 要做的事情, 检查清单), 再加第 4 个 H2 (关键能力). 四个 H2 按 markdown-style 从 1 连续编号, 之间用分隔线隔开.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.

链接约定 (沿用通用 ticket-spec 的规则, 这里因为要频繁提到 mini task 而再强调一次): 禁止指向 repo 内文件或目录的相对路径链接 (在 GitHub Issue 里点不动); 绝对 URL (形如 https://domain/href) 则照常可用. 需要指向 examples 的某个 mini task, 系列索引, 或某个 skill 时, 用文字提及 (直接说是 examples 里第几个 task, 说系列索引, 说 showcase-quiz 等), 不写相对路径链接. 第 4 节 "关键能力" 尤其如此: 纯文字 bullet.

H1 任务标题: 规则同 ticket-spec (只用字母, 数字, 文字, 逗号, 冒号, 句号; 禁 emoji, 引号, 双引号, 破折号; 且标题里不放 repo 名字作为通用前缀).

顶部 frontmatter 的 description 是整门课的 "完成判据": 一句话说清走完整门课, 做出什么或能当场演示什么才算完成. 它和根 README 那句承诺是同一门课的两张脸 (README 说学完能做到什么, 这句说做出什么才算完). description 的值必须用双引号包起来, 长度, 字符与该约束见 repo-layout.md 第 4 节.

四个 H2 各写什么:
- 第 1 节 目标: 一段, 整门课级别的 Definition of Done (走完这门课要建立起什么整体能力或体感, 并能把它作为一件作品讲出来).
- 第 2 节 要做的事情: 有序的学习加展示路径. 大致是: 先读根目录 README, 再读 examples 的系列索引, 然后按编号顺序刷完全部 mini task (每个照它自己的 TICKET 做), 用 showcase-quiz 测到 70% 且思路清晰, 再用 showcase-demo 排练怎么讲这段经历, 最后 (可选计入验收) 用 showcase-publish 把 repo 抹去教学痕迹发布出去. 末尾给一个整门课的预计用时.
- 第 3 节 检查清单: 固定的 markdown todo 骨架 (带 checkbox). 覆盖: 全部 mini task 完成 (各自 TICKET 逐项打勾), showcase-quiz 达到 70%, 能不看教程独立复现, 能用自己的话讲清核心概念, 能流畅讲出这段经历 (demo). publish 那条视创作者要求决定是否列入. 视课程增删.
- 第 4 节 关键能力: 从各 mini task 的 TICKET 里萃取出最重要的能力, 汇成一张纯 bullet 清单 (不带 checkbox, 因为逐项打勾的活第 3 节和各 mini task 已经做过; 它是让学员对照 "我是不是真掌握了这些" 的能力核对). 硬性要求取舍: 控制在 10 条以内, 不是每个 mini task 都值得列, 挑最能代表这门课的能力, 每条一句话.
-->

---
description: "一句话, 走完整门课, 做出什么或能演示什么才算完成. 中文叙述加英文术语."
---

# 完成 [课程名] 全部课程

## 1. 目标

[一段: 走完本课程全部 mini task, 要建立起什么整体能力或体感, 并且能把这段学习经历作为一件作品讲给别人听.]

---

## 2. 要做的事情

1. 先读根目录的 README, 明白这门课怎么学, 学完怎么展示.
2. 读 examples 的系列索引, 对整门课有张地图.
3. 按编号顺序刷完 examples 下全部 mini task, 每个都照它自己的 TICKET 逐项确认.
4. 全部刷完后, 用 showcase-quiz 自测, 测到 70% 的题都能思路清晰地答出来.
5. 用 showcase-demo 排练 "我是怎么做出这个项目的" 这段故事, 练到能流畅讲完并接住常见追问.
6. (可选) 用 showcase-publish 把 repo 抹去教学痕迹, 发布成自己 GitHub 上的 portfolio repo.

**预计用时:** [X 到 Y] [小时 / 一个周末]

---

## 3. 检查清单

- [ ] **全部 mini task 完成**: examples 下每个 task 的 TICKET 检查清单都已逐项打勾.
- [ ] **自测达标**: 用 showcase-quiz 测到 70% 的题都能思路清晰地答出来.
- [ ] **能独立复现**: 不看教程, 能把这门课的核心流程从头独立走一遍.
- [ ] **能讲清概念**: 能用自己的话解释这门课几个核心概念各自解决什么问题.
- [ ] **能讲出这段经历**: 用 showcase-demo 排练过, 能流畅讲完 "我是怎么做出这个的" 并接住追问.

---

## 4. 关键能力

[从各 mini task 的 TICKET 里挑最重要的能力汇成 bullet, 10 条以内, 取舍, 每条一句. 纯 bullet, 不带 checkbox, 也不带相对路径链接.]

- [关键能力一.]
- [关键能力二.]
- [关键能力三.]
