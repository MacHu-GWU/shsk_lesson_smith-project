<!--
本文件是 README-ORIGINAL 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 README-ORIGINAL-cn.md 时, 把整段注释删掉, 只留后面的正文.

定性: 这不是教学文档, 而是这个 Repo 面向 GitHub 的普通对外 README, 和其他任何开源仓库的 README 一样. 它是 Lesson (整个 Repo) 级别的介绍: 一个 Repo 就是一门 Lesson, 这份文件的 frontmatter 就是这门 Lesson 的门面. 学生学完把 Repo 当作自己的作品时, 别人第一眼看到的也是它.

适用范围: 各类型 Repo 根目录的 README-ORIGINAL.

Lesson 级 vs Task 级 (关键区分): README-ORIGINAL 的 description 是 **Lesson (整个 Repo) 的介绍**, 会进 org 级的课程索引 (可能几百个 Repo 的目录), 面向还没进来的冷读者. 而 Repo 根目录那个 README 的 description 是 **Task (某个 branch) 的介绍**, 会进本 repo 的 SYLLABUS, 面向已经进门的读者. 在 upskill / showcase 里只有一个 Task, 两者 scope 几乎重叠, 但角色和索引不同; 在 evolve 里一个 Repo 多个 Task, 两者明显分开.

生命周期 (为什么这份要重写): README-ORIGINAL 在创作最早期先写一版粗稿 (大背景, 电梯陈述), 作为后面所有内容生长的种子. 但那版往往和最终写出来的 examples 对不齐, description 也太粗, 撑不起一门 Lesson 的介绍. 所以内容全部完工后, 由 lesson-smith-upskill-finalize 重写整份 README-ORIGINAL (正文 + description + github_about, 全语种一起产出), 让它和成品对齐.

写作原则:
- 早期种子稿遵循创作铁律 (先写 cn); finalize 阶段的重写结构已稳, 各语种一次产出, 思考以中文为准, 英文自然改写.
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.

H1 标题: 与 Repo 名字一模一样, 通常形如 learn_xyz-project, 不做任何改写. (这一条覆盖 markdown-style 对 H1 的通用限制, 因为 repo 名里就带连字符和下划线.)

frontmatter 有两个字段, 都必须用双引号包起来, 值内不含引号类字符:

description (这门 Lesson 的完整介绍): 它是唯一鼓励写长的 description. 别写成一句话标签, 要用足预算, 可多句, 写满到接近 400 字符 (上限见 repo-layout.md 第 4 节). 风格是结果先行加企业视角:
- 开门见山说学完你能做到什么 (具体的能力, 用真实工作里的价值来描述), 而不是 "本课介绍 XX".
- 覆盖三件事: 你能做到什么 (能力); 这门课涵盖什么主题, 边界在哪 (让人和相邻的课区分开); 到什么深度 (basic / advanced / hardcore).
- 仍然是 pitch 不是目录: 绝不枚举 examples 里的小课 (那是 examples/README.md 的活).

github_about (压缩版 tagline): 一个额外的短字段, 专门塞进 GitHub 仓库的 About box. 因为上面的 description 偏长, 进不了 About (GitHub About 上限约 350 字符), 所以单列这个压缩版, 收到 200 字符以内更稳 (上限见 repo-layout.md 第 4 节). 一句话抓最核心的 "教什么 + 到什么水平" 即可. 你自己的 Lesson 索引以 description 为准, About box 用这个.

正文写法:
- 尽可能简洁, 一般不超过 3 段, 每段不超过 100 个英文单词.
- 结果先行, 企业视角: 讲清学完能做什么, 这在真实工作里值什么; 不要重复课程具体教的知识点, 不要罗列 1, 2, 3, 4 的学习目标.
- 整份文档 (含这 3 段) 是 pitch 不是目录: 讲清 repo 是什么, 给你什么, 到什么水平即可, 不枚举 examples 里的小课.
- 主要讲三件事: 这个 XX (要学的东西) 是什么 (例如常用工具, 业内标准, 解决某类问题的杀手锏); 你能学到什么 (能力); 学到什么程度 (basic, advanced, hardcore 哪一档).
-->

---
description: "偏长, 用足预算 (接近 400 字符): 结果先行说清学完你能做到什么 (能力加企业价值), 这门课涵盖什么主题, 到什么深度 (basic / advanced / hardcore). 中文叙述加英文术语."
github_about: "压缩版一句话 tagline, 200 字符以内, 抓核心的教什么加到什么水平, 专门给 GitHub About box 用."
---

# learn_xyz-project

[第一段: 这个 XX (要学的东西) 是什么, 为什么重要. 把它定位成常用工具, 业内标准, 或解决某类问题的杀手锏.]

[第二段: 学完你能做什么, 到什么深度 (basic, advanced, 还是 hardcore). 用真实工作里的价值来讲.]

[第三段 (可选): 其它值得用一小段说的内容.]
