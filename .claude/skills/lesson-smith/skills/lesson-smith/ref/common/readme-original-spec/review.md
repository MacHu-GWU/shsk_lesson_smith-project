# README-ORIGINAL 语料库评审 (英文版)

评审对象: `corpus/` 下 6 个 repo 的 `README-ORIGINAL.md` (英文版), 以 `-cn.md` 为对照原本, 以 [readme-original-spec.md](../../common/readme-original-spec/readme-original-spec.md) 与 [repo-layout.md](../../repo-layout.md) 第 4 节为判据.

评审重点 (按需求): (1) `description` 与 `github_about` 的长度是否用足预算; (2) 正文英文是否还带翻译腔 (读起来像中文直译, 而不是母语作者写的英文).

评审日期: 2026-08-09. 本文件只做点评, 未改动任何语料文件.

---

## 0. 总体结论

**先说结论: 这批英文不是 chinglish.** 它们是真正的重写, 不是翻译 —— 大量句子在英文里比中文原句更好 (vercel 的 "the first time their work turns into a link they can hand to somebody else", ai_development 的 "you meet the problem before you meet the abstraction that solves it"). 母语读者不会觉得这是从中文来的.

翻译腔的残留是**局部的, 可点名的**, 集中在三类:

1. **逗号同位语堆叠**: 中文习惯用逗号一路串下去, 英文照搬就会出现 `turning a vague prompt, build an app for splitting bills with friends, build a live score feed for a game in progress, into a plan` 这种一眼断不了句的结构. 这是本语料最伤的一类, 也是最容易修的 —— 项目的英文 spec 文件本身就在用 em dash (`—`), 所以英文版用破折号或括号不违反任何规范.
2. **计生硬的 calque (逐词直译)**: `separates nobody` (短期拉不开差距), `a full round of the workflow` (一整轮), `not at a first look at the topic` (不是入门科普), `why every line that isn't got dropped`. 每个都是单点可改.
3. **中文顿号列举变成 60+ 词长句**: github 正文第二段那一句是全语料最长的句子, 直接源于中文那串顿号.

真正的系统性问题反而不在语言, 而在**预算与合规**: 英文 `description` 普遍只用了预算的一半左右, 有一份还漏掉了 spec 明确要求的 "学完有什么收获"; 4/6 的正文段落超过 spec 的 100 词上限; 2/6 的 H1 被改写了.

### 速查表

| repo | desc (EN) | 用量 | EN/CN 倍率 | about (EN) | 正文段落词数 | H1 | 语言评级 |
|---|---|---|---|---|---|---|---|
| ai_development_basic | 376 | 47% | 1.24 | 134 | 86 / 90 / 82 | 掉了 `-project` | A |
| build_resume_matrix | 465 | 58% | 1.90 | 142 | **110 / 116** / 68 | 掉了 `-project` | A- |
| financial_engineer_interview | 458 | 57% | 2.14 | 128 | 77 / 93 / 55 | 正确 | B+ |
| github_basic_v1 | 499 | 62% | 1.60 | 198 | 90 / **159** / 68 | 正确 | C+ |
| system_design | 602 | **75%** | 2.07 | 161 | 97 / **112** / 72 / 8 | 正确 | B |
| vercel_basic_v1 | 523 | 65% | 2.11 | 110 | 91 / **117** / 27 | 正确 | A- |

上限: EN description 800, EN github_about 300, 正文每段 100 词 (加粗 = 超标). "EN/CN 倍率" 是英文字符数除以中文字符数; repo-layout 第 4 节说 400 字符中文重写成英文约需 700 到 900 字符, 即健康倍率约 1.75 到 2.25 —— 只有 ai_development 的 1.24 明显掉队, 说明那一份是**压缩**而不是重写.

---

## 1. 跨语料的共性问题

### 1.1 英文 description 集体没用足预算 (中度)

6 份的英文 description 全部落在 47% 到 75%, 平均 61%. spec 说得很明确: "它是唯一鼓励写长的 description, 可多句, 用足预算写到接近 400 字符", 而 repo-layout 又特意为英文放宽到 800, 理由就是 "英文版是中文版的重写, 不是压缩".

现在的实际情况是: 中文那边用到 54% 到 78% (也没用满), 英文那边又在中文的基础上按 1.2 到 2.1 倍展开. 两级缩水叠加, 结果是这些 description 进 org 级课程索引时, 比它们**被允许的**样子要瘦一圈. 只有 system_design 一份把预算当回事.

建议: 这不是逐份修文的事, 而是 rewrite-en 那一步该显式交代的 —— 英文 description 的目标区间给一个下限 (例如不低于 500 字符 / 不低于中文字符数的 1.7 倍), 让重写管线知道 "扩写是任务本身", 而不是默认求短.

### 1.2 正文 100 词段落上限, 4/6 超标 (需要改 spec, 而不是改文)

spec 写的是 "每段不超过 100 个英文单词". 中文版全部远低于此, 英文版有 4 份超标, 其中 github 第二段 159 词. 这不是作者不守规矩, 而是**规则本身没分语种**: 同一段内容, 中文 100 字对应英文往往就是 130 到 160 词. description 已经按语种分档了 (400 / 800), 正文的词数上限却没有, 这是 spec 的一个漏洞.

建议: 要么把上限改成分语种 (中文段 ≤ 200 字, 英文段 ≤ 140 词), 要么明说这条只约束中文版, 英文版按 "不超过中文段的自然展开量" 走. 现状是这条规则实际上处于半失效状态 —— 4/6 违反且没人纠正, 这种规则比没有更糟.

唯一真正该按现有标准修的是 github 的第二段 (159 词, 且其中一句 60+ 词), 那一段确实读起来累, 见 §2.4.

### 1.3 语气 (voice) 分裂成两派 (轻度但明显)

按正文 contraction 使用量分:

- **口语派**: ai_development (6 处: It's / doesn't / There's / That's / don't), build_resume_matrix (6 处: you're / It's / isn't / what's)
- **正式派**: financial_engineer (0 处), system_design (0 处), vercel (0 处, `somebody's` `Vercel's` 是所有格不是缩写), github (1 处所有格)

正式派把 `do not` `does not` `it is` `you are` 一路写全, 单看没有错, 但放在一份 pitch 里就偏白皮书腔, 少一分 "对着一个学生说话" 的感觉 —— 而 spec 对 description 的黄金标准恰恰是 "你把课程链接丢给一个学生时, 这段话可以原样复制粘贴发给他". 更重要的是, 同一个课程系列里六个 repo 用两种语气, 排在同一个 org 索引里会显得不是同一个作者写的.

这几乎肯定是不同批次重写留下的痕迹. 建议在 rewrite-en-spec 里把语气钉死一句 (例如: 允许并鼓励 contraction, 目标是能念出来的 pitch, 不是产品白皮书), 而不是让每次重写自己发挥.

### 1.4 深浅档位的英文说法不统一 (轻度)

spec 要求正文交代 basic / advanced / hardcore 哪一档. 六份的说法是: `That's the basic tier` (ai_dev) / `This is the advanced tier` (resume) / `That is the advanced tier` (fin_eng) / `The course stays at the basic level` (github) / `pitched at senior and staff` (system_design) / `a beginner-level course` (vercel).

`tier` `level` `beginner-level` 三种译法混用. 档位是这套体系里的**受控词汇** (basic, advanced, hardcore 是枚举值, 不是形容词), 英文里应该统一保留原词, 比如一律 `the basic tier` / `the advanced tier`. vercel 的 `beginner-level` 把枚举值译掉了, 恰好踩中 spec 里 "术语保留英文" 那条 (把 lazy evaluation 写成惰性求值的英文版本).

### 1.5 两份 H1 被改写了 (硬性违规, lint 应该抓)

spec: "H1 是 repo 名, 逐字节不变. 重写英文版时它也不许被改写, 这一条要在调用重写管线时显式交代."

- `learn_ai_development_basic-project` → 英文版写成 `learn_ai_development_basic`
- `learn_build_resume_matrix-project` → 英文版写成 `learn_build_resume_matrix`

其余四份正确. 两份都是被砍掉了 `-project` 后缀 —— 这正是重写模型"觉得后缀多余"时最容易做的手脚, 说明这条约束在实际调用里没有被显式交代到位, 或者交代了但没被执行. 建议由 lint 直接比对目录名, 不指望提示词.

### 1.6 frontmatter 里出现了撇号 (可能触发 lint)

repo-layout 第 4 节: description 与 github_about 的值 "永远不含引号类字符 (单双引号, 反引号都被禁)". 英文写作里的撇号 `'` 就是 U+0027 单引号:

- `build_resume_matrix` description: `an interviewer's follow-up questions`, `It's the only part`
- `github_basic_v1` description: `GitHub's basic workflow`; github_about: `GitHub's basic workflow`

YAML 层面无害 (双引号里放单引号完全合法), 但如果 lint 是按字符类粗暴匹配的, 这三处会报错; 如果 lint 不报, 那就是规则文本写得比实际检查严. 无论哪种, 这条规则需要澄清一句 "英文缩写与所有格的撇号不在此列", 否则英文版几乎无法写出自然语气 —— 禁掉撇号等于禁掉 contraction, 直接和 §1.3 想要的语气冲突.

---

## 2. 逐份点评

### 2.1 learn_ai_development_basic — 正文最好, description 最弱

**description (376 / 800, 47%)** — 全语料唯一不到一半的, 也是唯一**内容缺项**的.

spec 要求 description 是两段式, 且明说 "为什么值得学" 和 "有什么收获" 是两件不同的事, 别只写一个. 中文版两件都有:

> ...学完你能独立搭出一个基于自己资料的 AI 应用骨架, 看得懂业内那些 AI 产品背后到底是怎么搭起来的, 也知道自己下一步该往哪儿深入.

英文版把这整块**删掉了**, 换成一句讲教法的收尾:

> This course builds that layer from scratch, in Python you can run and break on the spot.

于是英文 description 变成 "概述 + 动机 + 教法", 收获整块缺席. 这是本次评审里唯一的内容性缺失 (其余都是长度或语言问题). 而且预算还剩一半没用, 补回来毫无代价 —— 把正文第二段那句 "It talks to models from more than one vendor... It calls tools to..." 压成一句放进去, 就能到 550 左右且信息完整.

**github_about (134 / 300)** — 好. `Intro to AI app development with LangChain and Strands Agents. From raw API calls to RAG and agents, every concept as runnable Python.` 望文生义, 技术栈在, 边界在, 不写收获, 完全对路.

**正文语言 — A, 全语料最自然的一份.** 没有翻译腔, 而且有明显的英文原生写作痕迹:

- `It's getting hard to find a software job that doesn't touch AI somewhere` —— 中文原句是 "已经从少数团队的实验, 变成了几乎每个软件岗位都会碰到的日常", 英文没有硬跟, 换了一个母语者会用的说法.
- `putting your own documents where the model can see them` —— 比中文 "把公司自己的资料喂给它" 更准.
- `so you meet the problem before you meet the abstraction that solves it, and only then does the framework come in and delete the boilerplate` —— 中文只说 "再看框架替你省掉了什么", 英文把因果讲透了, 是升级不是翻译.
- 第二段那串 `It talks to... It hands back... It answers... It calls...` 的短句排比是刻意的修辞, 母语感很强.

可挑的只有一处: `but neither one shows up as magic` 略别扭, 母语更可能写 `but neither is treated as a black box` (中文原文就是 "不把框架当黑盒", 反而是英文自己绕远了).

**其它**: H1 掉了 `-project` (见 §1.5).

**判决**: 正文可以直接当范文用; description 需要补写 "学完有什么收获" 并扩到 550 左右.

---

### 2.2 learn_build_resume_matrix — 正文很好, description 有一句读不动

**description (465 / 800, 58%)** — 长度尚可, 但结构有问题. 第二句是这样的:

> You take a thin-sounding internship or class project and build it up until it holds under an interviewer's follow-up questions, compress it into bullets and a Summary that reward digging, then keep all of it in one bloated master resume you cut each application down from, one version per job.

一句 50 词, 三个动作串联, 结尾 `one bloated master resume you cut each application down from, one version per job` 是一个悬垂介词的定语从句再挂一个同位语 —— 读者读到 `from` 才知道前面那个名词是什么角色, 这是全语料第二难读的句子.

更关键的是**顺序反了**: 中文版先立概念 (维护一份 master resume 当素材库, 按方向做减法派生), 再讲收获; 英文版先讲怎么打磨 bullets, 最后才蹦出 master resume. 冷读者 (spec 强调 description 面向 "还没进来的冷读者") 前 40 个词不知道 resume matrix 是什么. 建议拆成三句, 并把 master resume 提到第二句开头.

**github_about (142 / 300)** — 句子本身干净: `Build a 1+N resume matrix: one master resume, N versions cut from it, plus agent skills for gap analysis, project design, and writing bullets.`

但比中文版丢了两个检索锚点: 中文有 "面向美国求职市场" 和 "十个 agent skill", 英文只剩 `agent skills`. github_about 是给老师在索引里扫一眼用的, `US job market` 这五个字符正是同行判断要不要点进去的关键 —— 预算还剩一半, 没有理由省掉.

**正文语言 — A-, 第二好.** 亮点:

- `You keep one master resume, bloated on purpose and never sent to anyone` —— `bloated on purpose` 精准接住了中文 "长得离谱".
- `bullets that reward the digging instead of collapsing under it` —— 全语料最好的一句, 中文 "经得起深挖" 在英文里被写成了一个有画面的对仗.
- `Point them at any background and any job description and they still work.` —— 母语句法.

翻译腔 / 语法残留两处:

- `It's being able to say why every line is on the page and why every line that isn't got dropped.` —— `why every line that isn't got dropped` 语法上勉强成立 (`that isn't [on the page]` + `got dropped`), 但读起来是花园小径句, 大多数母语读者要回读一次. 母语写法: `...and why the ones that aren't were cut.`
- `This has become the practical approach because titles no longer draw clean lines around anything.` —— 中文是 "在 AI 时代这是刚需", 英文把 "AI 时代" 这个时代锚点丢了, 换成一个撑得有点勉强的隐喻 (`draw clean lines around anything` 到底是什么在画线?). 动机的力度弱于中文.

**其它**: H1 掉了 `-project`; 第一, 二段 110 / 116 词超 spec 上限 (但见 §1.2, 我认为该改的是 spec).

---

### 2.3 learn_financial_engineer_interview — 结构最合规, 语气最拘谨

**description (458 / 800, 57%)** — 内容完整 (概述 + 动机 + 教法 + 收获四件都在), 结尾 `By the end you can explain why a model holds and where it breaks.` 收得干净. 长度还剩四成, 中文版结尾那个对比 (`而不是只会往公式里代数字`) 被删了, 完全可以补回来做收尾, 会更有力.

**github_about (128 / 300)** — 全语料最标准的一份. `264 quant interview questions across Entry, Mid-Level, and Senior, each with a full write-up, plus an AI agent to drill against.` 一句话, 只说教什么, 数字与档位都在, 不写收获. 可以当模板.

**正文语言 — B+, 干净但偏正式.**

好的地方:

- `or quant work as everyone actually calls it` —— 中文 "业内更常叫 Quant" 的地道对应.
- `Get through it and an unfamiliar model stops being a wall` —— 比中文 "面对一个陌生的模型问题" 生动.
- `name the assumption that breaks first` —— 比中文 "假设在哪里会断" 更利落.
- `enough to hold your own on your first real project once you are in the seat` —— `in the seat` 用得好.

问题只有一个, 但是全篇性的: **零 contraction**. `Nobody asks you for a definition` 后面跟 `that kind of judgment does not come from...`, `That is the advanced tier`, `once you are in the seat`, `the bank is plain Markdown`. 逐句都对, 合起来的调子是行业报告, 不是 spec 想要的 "发给一个学生的话". 这份的内容本来是六份里张力最强的 (面试, 露馅, 当场拆题), 语气却是最平的, 反差可惜.

一处小的: `that kind of judgment does not come from reading around the subject` —— `reading around the subject` 偏英式书面语, 中文原意 "靠零散看书攒不出来" 更口语, `does not come from reading a few books here and there` 更贴.

**其它**: 段落 77 / 93 / 55 词全部合规, H1 正确, frontmatter 无撇号 —— **六份里唯一零硬性违规的**.

---

### 2.4 learn_github_basic_v1 — 问题最集中的一份

**description (499 / 800, 62%) — 踩了 spec 的红线.**

spec 的红线原文: "绝不罗列知识点. 最常见也最要命的失败, 是把各 mini task 或各 branch 的知识点用几个词串成一串, 读起来像目录. 一旦写出 '涵盖 A, B, C, D' 这种句式就已经跑偏, 哪怕前面加了 '学完你能' 也一样."

现在的英文 description:

> By the end of this course you can run GitHub's basic workflow on your own: create a repository, edit files and commit, branch off to experiment safely, and merge back into main with a Pull Request. You also take control of access (public vs private, collaborators, access tokens), move the whole workflow onto your own machine with GitHub Desktop, and learn to find shared repos inside an organization.

这就是 "学完你能" + 目录, 一字不差地命中红线. 而且**根因在中文版** —— 中文那份同样是从头列到尾, 英文只是忠实照做. 所以这一份要修, 得回到 `-cn.md` 重写 description, 英文再跟着重写, 单改英文没有意义.

真正该留的东西其实已经在文件里了, 只是被埋在最后: `The habit matters most: put all of your work on GitHub.` 加上正文第三段 "AI 时代, 一份无法造假的长期记录比自我标榜更有说服力" —— 那才是这门课的动机, 应该占 description 的主体, 而不是当补语.

唯一亮点: 收尾 `For absolute beginners, no command line.` 干脆利落, 该留.

**github_about (198 / 300) — 同样是目录.**

> Learn GitHub's basic workflow from scratch: create a repo, edit and commit, branch and merge, public vs private, collaborators and access tokens, GitHub Desktop, and repo ownership. No command line.

八个条目. spec 对 github_about 的要求是 "一句话, 越直白越好", "只回答一件事, 这是教什么的". 现在它试图把整个 syllabus 塞进 About box. 198 字符也是六份里最长的 (中文版 170 也是最长). 压到 `Learn GitHub from scratch in the browser: repos, commits, branches, Pull Requests, access control, and GitHub Desktop. No command line.` 之类, 100 字符出头就够, 信息密度反而更高.

**正文语言 — C+, 六份里最差, 但坏在结构不在词句.**

第二段 159 词, 超 spec 上限六成, 其中一句:

> You can also tell public from private, invite a collaborator to work alongside you, use an access token to let a program act on your behalf, move the whole workflow onto your own machine with GitHub Desktop, and recognize that every repository belongs to some owner, which is what tells you to look inside an organization for the things other people have shared with you.

62 词, 五个并列动词 + 一个关系从句尾巴. 这是**中文顿号列举直接搬进英文**的典型后果 —— 中文里 "也能分清..., 邀请..., 用..., 把..., 并认清..." 靠逗号轻快带过没问题, 英文里同样的并列会把读者的短期记忆撑爆. 而且句尾 `which is what tells you to look inside an organization for the things other people have shared with you` 逻辑绕: "认清每个 repo 有 owner" 和 "去 organization 里找" 之间的因果, 中文原句本来就跳, 英文照跳就成了读不懂. 应当拆成两到三句, 并把 owner → organization 那层因果明说出来.

其它单点:

- `get you through a full round of the workflow on your own` —— `a full round of the workflow` 是 "一整轮" 的逐词直译, 英文不这么说, 应为 `one full pass through the workflow` 或 `one complete cycle`.
- `makes keeping that kind of long term record effortless` —— `long term` 作定语缺连字符, 应为 `long-term`. 纯校对问题.
- `Code, documentation, notes, anything that exists as words: GitHub gives all of it version history` —— 三个名词加一个总括再加冒号, 断句别扭; 英文更自然的是把 `anything that exists as words` 用破折号引出.

第三段反而是全篇最好的: `a record that builds up day after day, that anyone can check, and that cannot be faked says more about you than anything you can say about yourself` —— 三个 that 从句的排比很有力, 且比中文原句更响. 说明作者写得动好英文, 只是前两段被中文的列举结构绑住了.

**判决**: 这一份的 description, github_about, 第二段都需要回到中文版重做, 不是英文层面的修补. 六份里唯一需要**返工**而不是**打磨**的.

---

### 2.5 learn_system_design — 预算用得最好, 开头一句读不通

**description (602 / 800, 75%) — 长度是六份里的标杆**, 内容也完整 (是什么 + 为什么值得学 + 收获 + 深度). 但第一句有严重的可读性问题:

> System design is the skill of turning a vague prompt, build an app for splitting bills with friends, build a live score feed for a game in progress, into a plan that holds up under real traffic.

`turning a vague prompt, ..., ..., into a plan` —— 两个例子用逗号插在 `turning X into Y` 的中间, 读者读到第二个 `build` 时会以为遇到了并列的祈使句, 直到 `into a plan` 才发现要回头重新断句. 这是全语料**唯一一句需要回读才能理解**的话, 而它偏偏是这门课门面的第一句.

中文版没这个毛病, 因为中文用 "比如" 显式引出了例子 ("比如设计一个朋友分账 App 或一个赛事比分实时推送系统"). 英文把 "比如" 省了, 同位语就失去了标记. 三种修法任选:

- 破折号: `turning a vague prompt — build an app for splitting bills with friends, build a live score feed for a game in progress — into a plan that...` (项目的英文 spec 文件本身就在用 em dash, 不违规)
- 括号同上
- 补回 `like`: `turning a vague prompt like "build an app for splitting bills" into a plan that...` (但引号被 frontmatter 规则禁, 所以只能不带引号)

后半段很好: `You leave with a framework you can run on a problem you have never seen, not a set of memorized answers, and the nerve to defend your calls while someone keeps pushing.` —— `the nerve to defend your calls` 比中文 "底气" 还准.

**github_about (161 / 300)** — 好. `one reusable framework, ten problems from warm-up to hard, a method for debriefing interviews, and an agent to practice against` 结构清楚, `from warm-up to hard` 比中文 "由浅入深" 更具体.

**正文语言 — B, 有三处明确的 calque.**

- `It is the kind of skill that separates nobody in the short run and sets your ceiling in the long run.` —— `separates nobody` 是 "短期拉不开差距" 的逐词直译, 英文里 `separate` 不这么用 (要说 `separates nobody from anybody` 才勉强成立, 但也不地道). 母语写法: `makes no difference in the short run and sets your ceiling in the long run` —— 而且这样前后两个动词还能形成对仗.
- `The depth is pitched at senior and staff interviews and real design reviews, not at a first look at the topic.` —— `not at a first look at the topic` 是 "不是入门科普" 的硬译. 母语: `not at an introduction to the subject`.
- `Ten problems of rising difficulty walk that line end to end.` —— `walk that line` 与英文成语 `walk the line` (循规蹈矩) 撞车, 读者会先激活错的义项. 前一句已经用了 `line of attack`, 这里换个词就好, 例如 `Ten problems of rising difficulty run it end to end.`

其余相当好: `Production problems are never clean.` `every decision is squeezed by cost, deadlines, and the size of the team` `Interviews carve system design into its own round because it exposes judgment in a way an algorithm question never will` —— 尤其最后这句, 比中文原句更有说服力.

**其它**:

- 正文 4 段, spec 说 "一般不超过 3 段". 第四段只有 8 个词 (`The course itself lives in [examples/README.md](examples/README.md). Start there.`), 中文版是把它并进第三段的. 我认为**英文这样拆更好** —— 独立的一行 CTA 比藏在段尾的链接有效得多. 建议不是改文件, 而是在 spec 里给这个 CTA 明确开个口子 (允许末尾一行独立的 "从哪儿开始读").
- 链接语种正确: 中文版链 `examples/README-cn.md`, 英文版链 `examples/README.md` ✓ 这是六份里唯一有内部文件链接的, 规则守住了.
- 北美语境守住了: `consumer products anyone in North America will recognize` ✓
- 第二段 112 词超上限 (见 §1.2).

---

### 2.6 learn_vercel_basic_v1 — 稳, 无硬伤

**description (523 / 800, 65%)** — 内容完整, 收尾 `Most of it carries over to other platforms.` 干净. 一处小问题: `The bar for writing code keeps falling, and the last stretch, getting the work online, is what actually stops people.` 又是逗号同位语 (`the last stretch, getting the work online, is`), 但这个是规范的同位语用法, 能一次读懂, 不像 system_design 那句会断错. 可接受, 换成破折号会更利落.

**github_about (110 / 300)** — 最短的一份, 也最干脆: `Vercel basics: deploy a site, ship changes safely with Preview deployments, debug with Build and Runtime Logs.` `ship changes safely` 三个词概括了中文 "用 branch 与 Preview 安全改动", 很好.

丢了一个信息: 中文版结尾的 "不教 app 代码". 这是这门课**最重要的边界声明** (正文第二段专门用一句讲它), 老师在索引里扫到 `Vercel basics` 时最想知道的恰恰是 "那它教不教 Next.js". 预算还剩 190 字符, 加一句 `Platform only, not app code.` 零成本.

**正文语言 — A-.** 第一段几乎是范文:

> Getting a website onto the internet used to be somebody's full-time job: buy a server, configure the environment, open the right ports, request a certificate and remember to renew it, write the deploy scripts, and dig through the logs by hand when something broke.

这里同样是长列举 (对应中文那串顿号), 但因为前面有冒号做显式标记, 且每项都是短动词短语, 读起来是有节奏的排比而不是负担 —— 和 github 第二段形成了鲜明对照, 可以直接拿来当 "同样的中文列举, 英文该怎么处理" 的正反例.

其它亮点:

- `Vercel collapsed that whole chain into a few clicks.` —— `collapsed` 用得好.
- `for a lot of people it is the first time their work turns into a link they can hand to somebody else` —— 中文是 "第一次把自己的作品交到别人手上", 英文加了 `turns into a link` 这个具体意象, **比中文原句好**.
- `How fast that loop turns is what sets the pace of your project` —— 干净.
- `When the two disagree, [Vercel's official documentation](https://vercel.com/docs) wins.` —— `wins` 一个词解决 "以...为准", 母语感强.

可挑的:

- `a beginner-level course` —— 应该保留档位原词 `basic` (见 §1.4).
- 零 contraction: `It will not teach you how to write app code.` `the logic underneath them will not change.` 中文原文 "它不教你" 是很口语的, 英文全写成 `will not` 就端起来了. 这一份的语气问题比 fin_eng 轻, 因为句子本身够短.
- 第二段 117 词超上限 (见 §1.2).

---

## 3. 该怎么行动 (按性价比排序)

**A. 改 spec, 不改文 (影响所有未来的 repo)**

1. 正文段落词数上限分语种 (§1.2) —— 现在这条规则 4/6 违反且无人纠正, 属于半失效状态.
2. 英文 description 给一个**下限** (不低于 500 字符或中文的 1.7 倍), 并在 rewrite-en-spec 里明说 "扩写是任务本身, 不是可选项" (§1.1).
3. 钉死英文语气: 鼓励 contraction, 目标是能念出来的 pitch (§1.3); 同时澄清 frontmatter 的 "禁引号" 不包括英文撇号 (§1.6) —— 这两条现在互相打架.
4. 档位 basic / advanced / hardcore 在英文里保留原词, 统一 `the X tier` (§1.4).
5. 英文版允许末尾一行独立的 CTA 段 (§2.5).
6. H1 逐字节一致改由 lint 比对目录名, 不指望提示词 (§1.5).

**B. 返工 (一份)**

- `learn_github_basic_v1`: description 与 github_about 踩红线 (罗列知识点), 正文第二段 159 词. **必须从中文版重做**, 只改英文是治标.

**C. 打磨 (点状, 可各自单独修)**

- `learn_ai_development_basic`: description 补 "学完有什么收获" 并扩到 ~550; H1 补回 `-project`.
- `learn_system_design`: description 第一句加破折号或括号; 正文 `separates nobody` / `not at a first look at the topic` / `walk that line` 三处换词.
- `learn_build_resume_matrix`: description 拆句并把 master resume 提前; 正文 `why every line that isn't got dropped` 改写; github_about 补回 US job market; H1 补回 `-project`.
- `learn_financial_engineer_interview`: 全篇放开 contraction; description 补一句收尾用足预算.
- `learn_vercel_basic_v1`: github_about 补 `Platform only, not app code.`; `beginner-level` → `basic tier`; 适度放开 contraction.

**D. 可以当范文用的**

- 正文英文: `learn_ai_development_basic` 全篇, `learn_vercel_basic_v1` 第一段 (中文顿号列举的正确英文处理).
- github_about: `learn_financial_engineer_interview` (一句话, 只说教什么, 数字与档位齐全).
- description 长度与结构: `learn_system_design` (除第一句的断句问题外).
