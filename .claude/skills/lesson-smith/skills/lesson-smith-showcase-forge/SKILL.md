---
name: lesson-smith-showcase-forge
description: "为当前 showcase 教学仓库锻造学习与展示工具链: 产出 docs/showcase 五份文档 (learn, runbook, quiz, demo, publish) 与四个子 skill. 统稿之后手动跑一次."
argument-hint: "[init | refresh | learn | runbook | quiz | demo | publish] [自由说明...]"
allowed-tools: Read Grep Glob Write Edit Bash(ls *) Bash(cat *) Bash(pwd) Bash(git rev-parse *) Bash(uvx *)
---

# lesson-smith-showcase-forge

你是 showcase 工具链的锻造者. 对着当前这个 showcase 教学仓库跑一次, 产出两样东西:

1. `docs/showcase/` 下 5 份文档: 学习索引, 跑起来的操作, quiz 薄壳, demo 薄壳, publish 清单.
2. `.claude/skills/` 下 4 个子 skill: `showcase-learn-cn`, `showcase-quiz-cn`, `showcase-demo-cn`, `showcase-publish-cn`.

产出后, 创作者与任何学员都能用 `/showcase-learn-cn` 带着学, `/showcase-quiz-cn` 自测, `/showcase-demo-cn` 排练怎么讲这段经历, `/showcase-publish-cn` 把 repo 抹去教学痕迹发布成作品.

这一步对应创作工作流的**第 12 步**. 跑完别急着关 session, 第 13 步 (写根目录文档) 接着用同一批素材.

## 第 0 步: 先加载 lesson-smith skill (不可跳过)

所有规范都住在 **lesson-smith** skill 里, 本 skill 只是薄包装, 自己不复制规范. 这是所有 `lesson-smith-*` skill 的通例: 默认先加载 lesson-smith, 再附带自己这一层的东西. 开工前先加载 lesson-smith skill, 之后从它的 `ref/` 按需读规范.

## 必读规范 (都在 lesson-smith skill 的 ref/ 下)

按用途读, 不要一次全读. **forge 要的东西分两处**: 和 upskill 共用的三份在 `ref/00-common/13-forge-shared/`, showcase 独有的两份在 `ref/03-showcase/forge/`. 每份 doc 一个目录, 里面中英各一套 spec 加 template.

- `ref/03-showcase/showcase-repo-layout.md`: showcase 的目录结构特化, 先读它对齐整体布局.
- `ref/00-common/13-forge-shared/docs-learn/docs-learn-cn-spec.md`: 写 `01-showcase-learn-cn.md` 的规范, 配套 template 在同目录.
- `ref/00-common/13-forge-shared/docs-runbook/docs-runbook-cn-spec.md`: 写 `02-showcase-runbook-cn.md` 的规范.
- `ref/00-common/13-forge-shared/docs-quiz/docs-quiz-cn-spec.md`: 写 `03-showcase-quiz-cn.md` 的规范.
- `ref/03-showcase/forge/docs-showcase-demo/docs-showcase-demo-cn-spec.md`: 写 `04-showcase-demo-cn.md` 的规范, showcase 独有.
- `ref/03-showcase/forge/docs-showcase-publish/docs-showcase-publish-cn-spec.md`: 写 `05-showcase-publish-cn.md` 的规范, showcase 独有, 自包含的 publish 清单.
- `ref/00-common/13-forge-shared/{learn,quiz}-cn.SKILL.md` 与 `ref/03-showcase/forge/showcase-{demo,publish}-cn.SKILL.md`: 四个子 skill 的近乎静态模板, 直接拷.
- `ref/agent-skill-interaction-pattern-cn.md`: 通用交互模式中文版, 生成子 skill 时拷一份进各自的 `ref/` 下.
- `ref/00-common/11-quiz-readme-spec/` 与 `ref/03-showcase/showcase-demo-readme-spec/`: 题库真身与讲故事底稿的格式, 用来核对定位到的那两个 Task 对不对.

### 素材里的 `{{TYPE}}` 是占位符

`13-forge-shared/` 那一层被 upskill 与 showcase 共用, 所以里面的类型名一律写成 `{{TYPE}}`. **拷过去之后必须全部替换成 `showcase`**, 路径, skill 名, frontmatter 里的 `name` 与 `description` 全算.

漏掉一个的后果是产出一条指向不存在的路径的链接, 而且不报错. **替换是纯机械的**: `{{TYPE}}` 一律换成 `showcase`, 没有例外, 不用判断上下文.

所以 Phase 6 有一条硬检查: **生成的文件里 grep `{{`, 必须 0 命中.** 用 `{{` 而不是完整的占位符去 grep, 是因为万一拼错了 (写成 `{TYPE}` 或 `{{type}}`) 那样也能抓到.

`13-forge-shared/` 之外的两份 (demo 与 publish) 写死 `showcase`, 不带占位符, 照常直接拷.

## 语种: 只产 `-cn` 那一套

上面每份 doc 都有中英两套 spec 与 template, 四个子 skill 也有中英两版. **当前只产 `-cn` 那一套.**

理由是 `examples/` 下无后缀的英文课程正文是**留空的占位符**, 英文索引只会指向一堆空文件. 英文那一套规范原地留着, 等多语种模块回来接手. **这是预期状态, 不是欠账.**

由此推出一条贯穿全流程的硬规则:

> **读 `examples/` 时只读 `-cn.md`.** 无后缀的那一版是空的. 读到空文件不会报错, 你会以为这门课没有内容然后开始编.

examples 之外的脚本, 数据, 配置等没有语种之分, 照常通读.

## 参数

把 `$ARGUMENTS` 解析成 `<mode> < 自由说明...>`. 第一个 token 若是下列 mode 就用它, 否则整段当自由说明, mode 默认 init.

- (空) 或 `init`: 全量生成. 若 `docs/showcase/` 已有目标文件, 停下让用户改用 refresh.
- `refresh`: 覆盖式重跑 (先跟用户确认).
- `learn` | `runbook` | `quiz` | `demo` | `publish`: 只重生成那一份 doc (以及对应的 skill, 若有).

自由说明是创作者对本次生成的额外指示 (例如 "学习素材以 src/ 下的代码为主", "quiz 偏重 concurrency", "publish 时保留 examples/03 作为作品主线"). 有的话在 Phase 3 一并采纳.

## 工作流

### Phase 1: Preflight (不可跳过)

1. 确认是 showcase repo: 读根目录 `lm.json`, `type` 必须是 `showcase`; `examples/` 必须存在. 不满足就停下问用户.
2. 定课程名. 从 `README-ORIGINAL-cn.md` 取, 它从第 1 步起就存在; **根 `README-cn.md` 这时候还没写**, 那是第 13 步的产物.
3. **确认统稿已经过了.** 这一步从文件系统看不出来, 直接问创作者. 统稿之前跑的代价见本文末尾那一节.
4. 列出 `docs/showcase/` 现有内容. init 模式下若目标文件已存在, 停下让用户确认改用 refresh.

### Phase 2: 扫 examples (轻量, 不派 Explore subagent)

showcase 的内容是创作者手写的 Task, 不用像扫陌生代码那样重. 直接:

- 读各 `examples/NN-title/README-cn.md` 顶部的 description (或 `docs/tasks/SYLLABUS-cn.md`), 拼出**引导路径** (learn 文档的第 2 节).
- **按固定目录名定位两个特殊 Task**: quiz 是 `NN-prove-i-get-it`, demo 是 `NN-how-i-build-this`. 名字是硬的, 直接找就行. 特征匹配只在名字找不到时当兜底, 兜不住就停下问, 别猜.
- **demo 按名字找, 不按位置找.** 它后面还有一个收尾 Task, 它不是 `examples/` 的最后一个.
- 顺带记下 examples 之外看起来是学习素材的东西 (根目录代码, 其它文档, `mise.toml`), 作为学习素材的候选.
- **为写 publish 清单, 扫一遍当前 repo 的真实文件树**: 把铁律删除的 glob 展开成真实路径, 分清哪一版有内容哪一版是空壳, 并记下可用于 commit plan 的真实文件与依赖顺序.

`examples/` 的位置约定 (01 索引, 02 综述, 03 往后主线, 然后 quiz, 然后 demo, 最后收尾) 见 `ref/00-common/01-repo-layout.md` 第 4.2 节. **引导路径讲的是主线**; 索引与收尾各自是一个 Task, quiz 与 demo 分别归 `03` 和 `04` 那两份薄壳管.

### Phase 3: 问创作者 (交互 gate, 机器猜不出的部分)

把下面五样问清, 回显确认后再动笔:

- **学习素材**: 把 Phase 2 找到的候选列出来, 请创作者确认或增删, 并说清是情况 A (教程本身就是要学的东西) 还是情况 B (真东西在 examples 之外). 这一条决定 learn 文档第 1 节是薄薄一句还是主菜.
- **runbook 隐性步骤**: 开始前的一次性 setup, 以及推进中导师默认懂, 学生却不懂的操作 (cd, 环境变量, 注册账号, 浏览器里 setup 等).
- **quiz 考法自定义**: 对 `showcase-quiz-cn` 行为的特殊要求 (没有就按默认).
- **demo 排练自定义**: 对 `showcase-demo-cn` 行为的特殊要求 (默认听众, 时长偏好, 哪几幕重点练, 追问狠不狠). 顺便确认那份讲故事底稿**有没有偏离默认七幕主线**, 偏了要在 `04` 里一句话说清偏在哪.
- **publish 口径**: 哪些待定项默认保留还是问创作者, commit plan 的侧重, 有没有额外要删或要留的东西.

自由说明里已经给到的直接采纳, 只补没给的.

### Phase 4: 写 5 份 doc

按各自规范写到 `docs/showcase/`, 全部带 `-cn` 后缀:

- `01-showcase-learn-cn.md`: 学习素材加引导路径.
- `02-showcase-runbook-cn.md`: 一次性 setup 加推进中操作, 把隐性步骤显式化.
- `03-showcase-quiz-cn.md`: 指向 Phase 2 定位到的题库真身, 加上考法自定义.
- `04-showcase-demo-cn.md`: 指向 Phase 2 定位到的讲故事底稿, 记下默认七幕主线与排练自定义.
- `05-showcase-publish-cn.md`: 自包含的 publish 清单, 六节写全.

**这五份里所有指向 `examples/` 与 repo 内文档的链接都写 `-cn.md`.** 指到无后缀那一版就是指到空文件.

溯源一律用 markdown 链接加 header 或关键字, **不用 line no**. 猜不准的地方显式标注请创作者确认, 不许凭空编.

#### publish 那一份要额外认真

另外四份产歪了大不了重生成. **publish 清单指导的是删文件, 而且删的是学生自己那份 repo.** 三处最容易出人命:

- **语种收敛**: 作品 repo 只带一个语种. 留下有内容的那一版 (`-cn`), 删掉留空的占位符, 再去掉后缀. **判断哪一版是占位符必须去读文件内容, 不许看后缀就下结论.** 做反了就是把整门课删光, 留下一棵空文件的树, 而且后面没有任何一步会发现.
- **删除区间**: quiz, demo, 收尾三个连着排在 `examples/` 最末, 一起删. 排在 quiz 之前的主线 Task 是作品内容, 要保留, 归待定项让学生自己判断.
- **glob 必须展开**: 清单里每个 glob 都要对着真实的树展开成路径. 留着 glob 等于把展开的活推给一个将来没有上下文的 session.

### Phase 5: 落 4 个子 skill

把四个模板拷成真正的 skill, 并让它们**自包含** (学生 repo 里没有 lesson-smith, 每个 skill 必须自带交互模式).

交互模式的落地方式固定是**拷贝进 `ref/` 再加载, 不是内联**, 必须严格照此, 别自作主张改成别的形式:

- 做法: 把 `ref/agent-skill-interaction-pattern-cn.md` 原样拷一份进每个生成 skill 的 `ref/` 下; SKILL.md 通过读取它自己 `ref/` 下那份来加载. 模板里 "交互基座" 那节只有一句话摘要加一个指向全文的指针, 那句摘要不等于把规范内联了.
- **不要把交互模式全文内联进 SKILL.md**: 会让 SKILL.md 臃肿, 也会和权威版各自漂移.
- **不要让生成的 skill 在运行时去 lesson-smith 里加载交互模式**: 学生 repo 里根本没有 lesson-smith.
- 为什么是拷贝: 生成的 skill 要在没有 lesson-smith 的学生 repo 里独立运行, 每个 skill 靠自带这份副本做到自包含. 权威版仍是 lesson-smith 里那一份, 改了它下次 forge 或 refresh 会重新拷入.

具体拷贝:

```text
ref/00-common/13-forge-shared/learn-cn.SKILL.md     ->  .claude/skills/showcase-learn-cn/SKILL.md
ref/00-common/13-forge-shared/quiz-cn.SKILL.md      ->  .claude/skills/showcase-quiz-cn/SKILL.md
ref/03-showcase/forge/showcase-demo-cn.SKILL.md     ->  .claude/skills/showcase-demo-cn/SKILL.md
ref/03-showcase/forge/showcase-publish-cn.SKILL.md  ->  .claude/skills/showcase-publish-cn/SKILL.md
ref/agent-skill-interaction-pattern-cn.md           ->  上面四个 skill 各自的 ref/agent-skill-interaction-pattern-cn.md
```

模板近乎全静态, 落地时只有四件事要做: 把 learn 与 quiz 那两份里的 `{{TYPE}}` 全部换成 `showcase` (demo 与 publish 那两份写死 `showcase`, 不带占位符), 让 frontmatter 的 `name` 等于目录名, 让每个 SKILL.md 都固定加载它自己 `ref/` 下那份交互模式, 且对 `docs/showcase/` 的引用路径带 `-cn`.

### Phase 6: Verify 与汇报

1. 列出创建或更新的文件 (5 份 doc, 4 份 SKILL.md, 4 份随附的交互模式).
2. sanity check:
   - 每个 SKILL.md 的 `name` 等于它的目录名.
   - 每个 SKILL.md 都引到 `docs/showcase/` 下对应的 `-cn` 文件.
   - 每个生成的 skill 的 `ref/` 下都有交互模式, 且 SKILL.md 加载了它.
   - **产出的文件里 grep `{{`, 必须 0 命中.** 有命中就是共享模板的占位符没换干净, 那会产出一条指向不存在路径的链接.
   - 5 份 doc 都非空, 且里面指向 `examples/` 的链接都是 `-cn` 的.
   - **publish 清单里的铁律删除已经展开成真实路径, 不是停在 glob**, 且语种收敛那一节写明了哪一版留哪一版删.
3. 用 uvx 跑 `lesson-smith lint` 看仓库结构是否仍合规 (`uvx --from shsk-lesson-smith==<version> lesson-smith lint -p .`; `<version>` 与 pin 版本的说明见 `ref/00-common/01-repo-layout.md` 第 8 节, 本地已装 package 则直接 `lesson-smith lint`).
4. 告诉用户: 用 `/showcase-learn-cn` 开始学, `/showcase-quiz-cn` 自测, `/showcase-demo-cn` 排练讲法, 学完用 `/showcase-publish-cn` 发布; `docs/showcase/` 里哪里不对直接改, 或 `refresh <name>` 重生成一份. **接着做第 13 步, 不要另开 session.**

## 为什么卡在统稿之后

forge 产出的是**索引和指针**, 它们指向 `examples/` 里的文件与标题.

统稿会改标题, 会拆篇并篇, 甚至会调整编号. 统稿之前跑, 产出的链接和锚点全都指在会变的东西上, 而且**没有任何检查会报出来**: lint 只查 `docs/showcase/` 那几份**在不在**, 不查里面的链接和锚点指向哪. 学生要等到 `/showcase-learn-cn` 带着他点进一个不存在的文件才发现.

publish 那一份更糟: 它记的是**要删哪些真实路径**. 对着一棵还会变的树生成的删除清单, 将来照着跑就是删错东西.

## 约束

- 只写 `docs/showcase/` 与 `.claude/skills/showcase-{learn,quiz,demo,publish}-cn/`; 不碰源码, 不动 examples 内容.
- **题目本身不在这里出, 讲故事底稿也不在这里写**: 题库真身 (第 8 步) 与讲故事底稿 (第 9 步) 都由创作者手写, forge 只负责定位它们并写好 `03` 与 `04` 的指针.
- **publish 清单 forge 只生成, 不执行.** 真正的删除, 改名, 重写 README 是学生后来跑 `/showcase-publish-cn` 时的事. 什么时候发布由他自己决定.
- 遵循 lesson-smith 的创作铁律与 `markdown-style`, `chinese-english-punctuation` 两个 Agent Skill.
