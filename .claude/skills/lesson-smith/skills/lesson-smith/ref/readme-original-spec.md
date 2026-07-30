<!--
本文件是 README-ORIGINAL 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 README-ORIGINAL-cn.md 时, 把整段注释删掉, 只留后面的正文.

定性: 这不是教学文档, 而是这个 Repo 面向 GitHub 的普通对外 README, 和其他任何开源仓库的 README 一样. 它是 Lesson (整个 Repo) 级别的介绍: 一个 Repo 就是一门 Lesson, 这份文件的 frontmatter 就是这门 Lesson 的门面. 学生学完把 Repo 当作自己的作品时, 别人第一眼看到的也是它.

适用范围: 各类型 Repo 根目录的 README-ORIGINAL.

Lesson 级 vs Task 级 (关键区分): README-ORIGINAL 的 description 是 **Lesson (整个 Repo) 的介绍**, 会进 org 级的课程索引 (可能几百个 Repo 的目录), 面向还没进来的冷读者. 而 Repo 根目录那个 README 的 description 是 **Task (某个 branch) 的介绍**, 会进本 repo 的 SYLLABUS, 面向已经进门的读者. 在 upskill / showcase / readup 里只有一个 Task, 两者 scope 几乎重叠, 但角色和索引不同; 在 evolve 里一个 Repo 多个 Task, 两者明显分开.

生命周期 (为什么这份要重写): README-ORIGINAL 在创作最早期先写一版粗稿, 作为后面所有内容生长的种子. 但那版往往和最终写出来的 examples 对不齐, description 也太粗, 撑不起一门 Lesson 的介绍. 所以内容全部完工后, 由对应类型的 finalize skill (readup 是 lesson-smith-readup-finalize, upskill 是 lesson-smith-upskill-finalize, showcase 是 lesson-smith-showcase-finalize) 重写整份 README-ORIGINAL (正文加 description 加 github_about, 全语种一起产出), 让它和成品对齐.

人类拍板 (finalize 阶段的硬性一步): description 与 github_about 是这门课的门面, 一句话决定别人点不点进来, 所以不许 AI 单方面定稿. finalize 写完初稿后必须停下来交给课程作者过目: 把 description 与 github_about 摆出来 (两句都拿不准时, 给两三个不同侧重的候选让他挑), 问他 ok 不 ok, 哪里要调, 按他的意见改完再进下一步. 正文那 3 段不需要这道 gate, 只有这两个字段需要.

写作原则:
- 早期种子稿遵循创作铁律 (先写 cn); finalize 阶段的重写结构已稳, 各语种一次产出, 思考以中文为准, 英文自然改写.
- 术语保留英文 (这两个字段最容易翻车的地方): 写 cn 版时, 中文只负责叙述, 术语, 产品名, 技术名词一律保留英文原文, 不要强行译成中文. 把 DataFrame 写成数据帧, 把 lazy evaluation 写成惰性求值, 读者反而认不出这门课在教什么, 这一行进了索引也失去检索价值.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.

H1 标题: 与 Repo 名字一模一样, 通常形如 learn_xyz-project, 不做任何改写. (这一条覆盖 markdown-style 对 H1 的通用限制, 因为 repo 名里就带连字符和下划线.)

frontmatter 有两个字段, 都必须用双引号包起来, 值内不含引号类字符. 它们面向的是两种不同的人, 分清这一点是写好它们的关键: description 写给学生 (要来学这门课的读者), github_about 写给老师 (课程作者本人, 以及同行). 两句都短, 合起来就是这个 repo 在课程索引里的那一行.

description (写给学生的那段话): 黄金标准是, 你把课程链接丢给一个学生时, 这段话可以原样复制粘贴发给他. 所以它不是摘要, 不是目录, 是你对着一个具体的人说的话. 它是唯一鼓励写长的 description, 可多句, 用足预算写到接近 400 字符 (上限见 repo-layout.md 第 4 节).

内容是两段式, 两件事都要有, 且要分得清:
1. 概述: 这门课学的是什么. 让他知道这是关于什么的一门课, 一句人话就够.
2. 为什么值得学, 学完有什么收获. 注意这是两件不同的事, 别只写一个: "为什么学" 是动机 (这东西在真实工作或学习里值什么, 不会它会怎样), "有什么收获" 是结果 (学完他手上多了什么能力). 深浅档位 (basic, advanced, hardcore) 如果要提, 自然融进这一点, 不单列成一项去凑.

红线, 绝不罗列知识点: 最常见也最要命的失败, 是把各 mini task 或各 branch 的知识点用几个词串成一串, 读起来像目录. 一旦写出 "涵盖 A, B, C, D" 这种句式就已经跑偏, 哪怕前面加了 "学完你能" 也一样. 主题的边界靠一句人话交代, 不靠枚举; 枚举是 examples/README.md 的活. 同理别写成 "本课介绍 XX" 这种第三人称课程简介口吻, 那不是能发给学生的话.

github_about (写给老师的那句话): 一个额外的短字段, 专门塞进 GitHub 仓库的 About box. 因为上面的 description 偏长, 进不了 About (GitHub About 上限约 350 字符), 所以单列这个压缩版, 收到 200 字符以内更稳 (上限见 repo-layout.md 第 4 节).

它的受众和 description 不同: 看它的是课程作者本人和其他老师, 在 GitHub 的 About box 或课程索引里扫一眼, 望文生义就知道这个 repo 大概教什么. 所以它只回答一件事, 这是教什么的; 学完有什么收获在这里不重要, 不用写. 一句话, 越直白越好.

正文写法:
- 尽可能简洁, 一般不超过 3 段, 每段不超过 100 个英文单词.
- 结果先行, 企业视角: 讲清学完能做什么, 这在真实工作里值什么; 不要重复课程具体教的知识点, 不要罗列 1, 2, 3, 4 的学习目标.
- 整份文档 (含这 3 段) 是 pitch 不是目录: 讲清 repo 是什么, 给你什么, 到什么水平即可, 不枚举 examples 里的小课.
- 主要讲三件事: 这个 XX (要学的东西) 是什么 (例如常用工具, 业内标准, 解决某类问题的杀手锏); 你能学到什么 (能力); 学到什么程度 (basic, advanced, hardcore 哪一档).
-->

---
description: "写给学生, 能原样复制粘贴发给他的一段话, 用足预算 (接近 400 字符). 先一句人话说清这门课学的是什么, 再说清为什么值得学 (动机) 以及学完有什么收获 (能力). 绝不罗列知识点. 中文叙述加英文术语."
github_about: "写给老师, 一句话说清这个 repo 教什么, 200 字符以内, 望文生义即可, 不写收获. 专门给 GitHub About box 用."
---

# learn_xyz-project

[第一段: 这个 XX (要学的东西) 是什么, 为什么重要. 把它定位成常用工具, 业内标准, 或解决某类问题的杀手锏.]

[第二段: 学完你能做什么, 到什么深度 (basic, advanced, 还是 hardcore). 用真实工作里的价值来讲.]

[第三段 (可选): 其它值得用一小段说的内容.]
