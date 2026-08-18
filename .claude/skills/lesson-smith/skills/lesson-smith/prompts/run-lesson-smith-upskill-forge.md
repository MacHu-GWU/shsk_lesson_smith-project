# 运行 /lesson-smith-upskill-forge 的输入

> 用法: 把下面每个 "无" 换成你的内容, 然后把整份内容连同 /lesson-smith-upskill-forge 一起发出去. forge 会据此收集信息, 产出 `docs/upskill/` 下三份 `-cn` doc 与 `upskill-learn-cn`, `upskill-quiz-cn` 两个子 skill. 过程中它会向你确认, 你兜底做决策.

> 前置: 这是创作流的**第 12 步**, 统稿之后才能跑. 统稿之前跑, 产出的链接和锚点会全部指在还会变的东西上, 而且没有任何检查会报出来. 跑完接着做第 13 步 (写根目录文档), 不要另开 session.

/lesson-smith-upskill-author-step-12-forge

请按 /lesson-smith-upskill-forge 中的规范, 先收集信息, 再产出对应的 doc 与子 skill.

## 1. examples 之外的学习素材

> 这门课除 examples 外, 学生还要读或跑哪些东西? 每类列出路径, 一句话说学什么. 没有的类别写 "无".

**源代码:**

无

**配置文件:**

无

**文档:**

无

**Agent Skill:**

无

## 2. examples 教程里值得单说的点

> 推进 examples 时有哪些隐性操作 (注册账号, 浏览器里 setup, cd, 环境变量) 或值得单拎出来的步骤? 这些会进 runbook. 没有写 "无".

前期 setup 的时候,  configure credential, 配置 ~/.aws/config, credentials 文件, 用 mise.toml 里安装 CLI, 如果不是 mac 电脑怎么做, 这个部分, 我认为是很容易踩坑的, 一旦过了就好办了, 所以这里可能要想到用户可能会卡壳, 你看怎么帮助学生

## 3. quiz 考法要求

> 对 upskill-quiz-cn 的特殊要求 (例如偏重哪块, 默认抽几道, 是否按主题分组考, 用什么口吻, 及格线怎么算). 这一段会原样落进 `docs/upskill/03-upskill-quiz-cn.md` 的 "考法自定义" 那一节. 没有写 "无", 按默认.

quiz 里的核心是概念, 是这种, 先把 AWS cli, boto3 API 跑通, 跑通后建立一种学习方法, 这么多服务, 以后未来就是转向每一个 AWS Service (甚至其他公司的 Service) 学的时候几乎都是, 看 API, 搞清楚有哪些 Resource 以及有哪些 Action, 配合官方解决的问题. 我们希望这一门课能把这个思路建立起来. 因为每个具体的 Service 都可以在 AI 的帮助下快速学会

## 4. 其他要求

> 对本次生成的额外指示 (例如学习素材以哪部分为主). 没有写 "无".

无
