<!--
本文件是 README-ORIGINAL 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 README-ORIGINAL-cn.md 或 README-ORIGINAL.md 时, 把整段注释删掉, 只留后面的正文.

同目录下的 corpus/ 是这一类文档的真实语料, 六个已发布 repo 的中英两版. 怎么用见本注释最后的 "语料怎么用" 一节.

定性: 这不是教学文档, 而是这个 Repo 面向 GitHub 的普通对外 README, 和其他任何开源仓库的 README 一样. 它是 Lesson (整个 Repo) 级别的介绍: 一个 Repo 就是一门 Lesson, 这份文件的 frontmatter 就是这门 Lesson 的门面. 学生学完把 Repo 当作自己的作品时, 别人第一眼看到的也是它.

适用范围: 各类型 Repo (readup, upskill, showcase, evolve) 根目录的 README-ORIGINAL. 四类同形, 所以这一份放在 common 下.


== Lesson 级 vs Task 级, 关键区分 ==

两段都写给学生看, 区别在海拔, 以及各自回答的问题.

README-ORIGINAL 的 description 是 Lesson (整个 Repo) 的介绍, 会进 org 级的课程索引 (可能几百个 Repo 的目录), 面向还没进来的冷读者, 回答的是 "为什么值得学, 学完有什么收获", 且绝不罗列知识点.

而 Repo 根目录那个 README 的 description 是 Task (某个 branch) 的介绍, 会进本 repo 的 SYLLABUS, 面向已经进门的读者, 回答的是 "你将学到什么", 在那一份里罗列知识点反而是对的.

在 upskill, showcase, readup 里只有一个 Task, 两者 scope 几乎重叠, 但上面这个分工不变, 两边别互相抄; 在 evolve 里一个 Repo 多个 Task, 两者本来就明显分开. 根 README 那一份的精确定义见各类型的 readme spec.


== 生命周期, 为什么这份要重写 ==

README-ORIGINAL 在创作最早期先写一版粗稿 (只有 README-ORIGINAL-cn.md), 作为后面所有内容生长的种子. 但那版往往和最终写出来的 examples 对不齐, description 也太粗, 撑不起一门 Lesson 的介绍.

所以 examples 全部完工并统稿之后, 在写全局中文那一步重写整份 README-ORIGINAL-cn.md (正文加 description 加 github_about), 让它和成品对齐. 英文版不在这里产, 它随整门课那一次统一重写产生.


== 人类拍板, 写全局中文那一步的硬性一步 ==

description 与 github_about 是这门课的门面, 一句话决定别人点不点进来, 所以不许 AI 单方面定稿. 写完初稿后必须停下来交给课程作者过目: 把两个字段摆出来 (拿不准时给两三个不同侧重的候选让他挑), 问他 ok 不 ok, 哪里要调, 按他的意见改完再往下走.

正文那三段不需要这道 gate, 只有这两个字段需要. 这道 gate 只在中文版上过一次: 英文版是已批准中文版的重写, 不需要第二次拍板.


== 写作原则 ==

全程走创作铁律, 没有例外: 种子稿和后期统稿重写都只写 cn 版, 英文版随整门课那一次统一重写产生, 不在这里单独产.

链接的语种跟着本文件走: 正文里若出现指向 repo 内其他文件的相对路径链接, cn 版用 -cn 版, 英文版用英文版; 指向目录的链接两版一样, 不带语种后缀. 写 cn 版时只负责把 cn 版链对, 换后缀是重写那一步的事.

术语保留英文, 这是这两个字段最容易翻车的地方: 写 cn 版时, 中文只负责叙述, 术语, 产品名, 技术名词一律保留英文原文, 不要强行译成中文. 把 DataFrame 写成数据帧, 把 lazy evaluation 写成惰性求值, 读者反而认不出这门课在教什么, 这一行进了索引也失去检索价值.

遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.


== H1 ==

与 Repo 名字一模一样, 逐字节不变, 通常形如 learn_xyz-project. 这一条覆盖 markdown-style 对 H1 的通用限制, 因为 repo 名里就带连字符和下划线.

重写英文版时它同样不许被改写. 语料里六份有两份的英文版被砍掉了 -project 后缀, 说明光靠提示词交代守不住, 所以这一条应由 lint 直接比对目录名, 不指望模型自觉.


== frontmatter, 两个字段 ==

两个字段都必须用双引号包起来, 形如 description 冒号空格再双引号. 它们面向的是两种不同的人, 分清这一点是写好它们的关键: description 写给学生 (要来学这门课的读者), github_about 写给老师 (课程作者本人, 或授课老师). 两句都短, 合起来就是这个 repo 在课程索引里的那一行.

预算按语种分档, 这张表是硬指标, 不是建议:

  字段            中文目标        中文上限    英文目标        英文下限    英文上限
  description     320 到 400      400         700 到 800      500         800
  github_about    150 到 200      200         220 到 300      (无)        300

一条自检: 英文字符数除以中文字符数, 健康区间是 1.75 到 2.25. 低于 1.7 说明英文那一版是压缩不是重写, 回去扩写.

为什么英文额外给一个下限: 语料里六份英文 description 只用了预算的 47% 到 75%, 平均 61%, 而中文那一版本身也只用到 54% 到 78%. 两级缩水叠加, 结果是这些 description 进 org 级索引时比它们被允许的样子瘦一圈. 英文版是中文版的重写, 扩写是任务本身, 不是可选项.


== description, 写给学生的那段话 ==

黄金标准是, 你把课程链接丢给一个学生时, 这段话可以原样复制粘贴发给他. 所以它不是摘要, 不是目录, 是你对着一个具体的人说的话. 它是唯一鼓励写长的 description, 可多句, 用足预算.

内容是两段式, 两件事都要有, 且要分得清:

1. 概述: 这门课学的是什么. 让他知道这是关于什么的一门课, 一句人话就够.

2. 为什么值得学, 学完有什么收获. 注意这是两件不同的事, 别只写一个. "为什么学" 是动机 (这东西在真实工作或学习里值什么, 不会它会怎样), "有什么收获" 是结果 (学完他手上多了什么能力). 语料里有一份漏掉了 "收获" 这一半, 那是最常见的缺口.

深浅档位如果要提, 自然融进第 2 点, 不单列成一项去凑.

红线, 绝不罗列知识点: 最常见也最要命的失败, 是把各 mini task 或各 branch 的知识点用几个词串成一串, 读起来像目录. 一旦写出 "涵盖 A, B, C, D" 这种句式就已经跑偏, 哪怕前面加了 "学完你能" 也一样. 主题的边界靠一句人话交代, 不靠枚举; 枚举是 examples/README.md 的活.

同理别写成 "本课介绍 XX" 这种第三人称课程简介口吻, 那不是能发给学生的话.


== github_about, 写给老师的那句话 ==

一个额外的短字段, 专门塞进 GitHub 仓库的 About box. 因为上面的 description 偏长, 进不了 About (GitHub 约 350 字符就截断, 不分语种), 所以单列这个压缩版.

它的受众和 description 不同: 看它的是课程作者本人和其他老师, 在 About box 或课程索引里扫一眼, 望文生义就知道这个 repo 大概教什么. 所以它只回答一件事, 这是教什么的; 学完有什么收获在这里不重要, 不用写. 一句话, 越直白越好.

注意它的上限性质和 description 不同: description 的上限是我们自己定的风格预算, 这一条是外部限制, 所以英文只给一点余量, 不像 description 那样翻倍.


== 正文写法 ==

段数: 一般三段. 英文版允许多一段, 但那一段必须是独立的一行 CTA, 不是第四段论述.

单段长度按语种分档 (和 description 同理, 同一段内容中文 100 字对应英文常在 130 到 160 词):

  中文段  不超过 200 字
  英文段  不超过 140 词

英文再加一条单句上限: 一句不超过 40 词. 语料里最伤的一处是一句 60 多词的长句, 直接源自中文那串顿号列举.

内容上讲三件事:

1. 这个要学的东西是什么, 为什么重要. 把它定位成常用工具, 业内标准, 或者解决某类问题的杀手锏.
2. 学完你能做什么, 到什么深度. 用真实工作里的价值来讲.
3. 到哪一档: basic, advanced, hardcore.

结果先行, 企业视角. 不要重复课程具体教的知识点, 不要罗列 1, 2, 3, 4 的学习目标. 整份文档 (含这三段) 是 pitch 不是目录.

深浅档位是受控词汇, 不是形容词: basic, advanced, hardcore 三个枚举值在英文里一律保留原词, 统一写成 the basic tier, the advanced tier, the hardcore tier. 不许写成 beginner-level, entry level, this is an advanced course 之类的自由发挥, 那等于把枚举值译掉了, 和 "术语保留英文" 那条是同一个错误. 语料里六份出现了 tier, level, beginner-level 三种说法, 就是没钉死的后果.


== 英文版专属 ==

英文版不是翻译, 是重写. 下面几条只对英文版生效, 写 cn 版时不用管.

语气: 允许并鼓励 contraction (it's, you're, doesn't, there's). 目标是一段能念出来的 pitch, 不是产品白皮书. 语料里六份分成了两派, 一派放开缩写, 一派把 do not, it is 一路写全, 后者单看没错, 但放在 pitch 里偏白皮书腔, 而且同一个课程系列排在一个 org 索引里会显得不是同一个作者写的.

撇号的澄清 (这一条很重要, 因为它和另一条规则表面上打架): frontmatter 那条 "值内不含引号类字符" 指的是成对的引号 (双引号, 反引号, 以及用作引用的单引号), 不包括英文缩写与所有格里的撇号. GitHub's, it's, interviewer's 全部合法. 禁掉撇号等于禁掉 contraction, 和上一条直接冲突.

三类要盯死的翻译腔, 都是语料里真实出现过的:

1. 逗号同位语堆叠. 中文习惯用逗号一路串下去, 英文照搬就会出现一眼断不了句的结构. 英文里该用破折号或者括号把插入成分括起来, 这不违反任何规范 (markdown-style 禁的是把破折号当句子转折用, 不是禁一切破折号).

2. 逐词直译的 calque. 形态是每个词都对, 合起来不是英文. 语料里点名过的有 separates nobody (短期拉不开差距), a full round of the workflow (一整轮), not at a first look at the topic (不是入门科普). 这类只能一处处认出来换掉.

3. 中文顿号列举直接变成一个长句. 中文一串顿号读起来很顺, 逐项译过去就是一句 60 多词的东西. 英文该拆句, 或者改成 bullet, 或者只保留最有代表性的两三项.

一条判据: 写完之后当成英文读一遍, 不要当成译文读. 读着卡住的地方就是上面三类之一.


== 语料怎么用 ==

corpus/ 下六个 repo, 每个一对中英版. 它们是真实产出的快照, 不是标准答案. 规范是权威, 语料是佐证; 两者冲突时以规范为准, 并回头把语料标注出来.

动笔前不要六份全读, 那是往上下文里灌噪音. 按下面这张表只读需要的那一两份, 而且只读被点名的那一面:

  要写什么              去看哪一份                                              看什么
  正文英文的整体语感    corpus/learn_ai_development_basic-project/              全篇, 这份正文最好
                        README-ORIGINAL.md
  中文顿号列举怎么      corpus/learn_vercel_basic_v1-project/                   第一段
  译成英文              README-ORIGINAL.md
  github_about          corpus/learn_financial_engineer_interview-project/      只看 github_about
                        README-ORIGINAL.md                                      一句话, 只说教什么, 数字与档位齐全
  description 的长度    corpus/learn_system_design-project/                     只看 description
  与结构                README-ORIGINAL.md                                      六份里唯一把预算当回事的
  反面, 别学            corpus/learn_github_basic_v1-project/                   description 与 github_about 踩了
                        README-ORIGINAL.md                                      罗列知识点的红线, 正文第二段 159 词

另外三条已知的局部瑕疵, 看的时候心里有数: financial_engineer, system_design, vercel 三份的英文语气偏正式 (几乎不用 contraction), 别学那一面; ai_development 与 build_resume_matrix 两份的英文 H1 被砍掉了 -project 后缀, 那是硬性违规; 六份的英文 description 都没用足预算, 长度这一项只有 system_design 可参考.


== 交付前自检 ==

数得出来的:

- H1 与 repo 目录名逐字节一致, 包括 -project 后缀
- description 与 github_about 都用双引号包裹, 值内没有成对引号或反引号 (英文撇号不算)
- 两个字段都是一行, 不含换行
- 四个长度落在上面那张预算表里; 英文 description 不低于 500 字符, 也不低于中文字符数的 1.7 倍
- 正文段数不超过三段 (英文版可多一行 CTA); 中文段不超过 200 字, 英文段不超过 140 词, 英文单句不超过 40 词

要读一遍才看得出来的:

- description 里 "为什么值得学" 和 "学完有什么收获" 两件事都在, 而且分得清
- description 没有出现 "涵盖 A, B, C, D" 这类枚举, 也没有 "本课介绍 XX" 这种第三人称口吻
- description 能原样复制粘贴发给一个学生
- github_about 只回答 "教什么", 没有掺进收获
- 档位写成 the basic tier 这种形式, 没有被译成 beginner-level 之类
- 英文版当成英文读一遍不卡, 三类翻译腔一处没有
- 英文版放开了 contraction, 不是白皮书腔
-->

---
description: "写给学生, 能原样复制粘贴发给他的一段话, 用足预算 (中文接近 400 字符, 英文 700 到 800). 先一句人话说清这门课学的是什么, 再说清为什么值得学 (动机) 以及学完有什么收获 (能力), 两件事都要有. 绝不罗列知识点. 中文叙述加英文术语."
github_about: "写给老师, 一句话说清这个 repo 教什么, 中文 200 字符以内, 望文生义即可, 不写收获. 专门给 GitHub About box 用."
---

# learn_xyz-project

[第一段: 这个要学的东西是什么, 为什么重要. 把它定位成常用工具, 业内标准, 或者解决某类问题的杀手锏. 中文不超过 200 字, 英文不超过 140 词.]

[第二段: 学完你能做什么, 到什么深度. 用真实工作里的价值来讲. 档位写成 basic, advanced 或 hardcore 三者之一, 英文里保留原词写成 the X tier.]

[第三段 (可选): 其它值得用一小段说的内容.]
