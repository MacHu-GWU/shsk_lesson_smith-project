# ref 维护指南

**这份文件不给 Agent Skill 读, 是给维护 `ref/` 的人本人看的.** 它说清四件事: 这一堆规范为什么长成现在这个形状, 按什么结构组织, 该按什么顺序写, 以及现在还欠什么.

---

## 1. 为什么是这个形状: 三类同构

`ref/` 的分层不是为了看着整齐, 是照着教学仓库本身的形状切的.

readup, upskill, showcase 三类底层是**同一个东西**: 一个 branch, 加 `examples/` 下一串 Task. 它们的目录结构一样, 特殊文件一样, 连创作流程的骨架都一样:

> 定题 → 规划与试水 → 写主线 → 补两头加统稿 → 写根目录文档 → 出厂

差别只在**节奏**: 主线之后插几个特殊 Task, 统稿之后加不加一步锻造.

| | readup | upskill | showcase |
| :--- | :--- | :--- | :--- |
| 步骤 / 阶段 | 10 / 6 | 13 / 8 | 14 / 9 |
| 特殊 Task | 无 | quiz | quiz, demo |
| forge 锻造出的工具链 | 无 | 3 份 doc, 2 个子 skill | 5 份 doc, 4 个子 skill |
| 学完之后 | 读完就完 | 学完就完 | 多一个对外 publish 环节 |

**readup 是 upskill 的子集, upskill 是 showcase 的子集.** 每往右一格是加东西, 不是换一套.

所以 `ref/` 就照这个分: **一层通用, 三层特化.** 通用层承担那个共同骨架, 特化层只写各自多出来的那几格. 三个特化层内部的文件构成也刻意保持一致 (一份 layout, 一份 workflow, 一对根 README 与 TICKET spec, 加各自的特殊 Task 与 forge), 这样从一类跳到另一类, 找东西的路径不用重学.

evolve 是第四类, 它没有 `examples/` 那一层, 不在这个同构关系里, 规范也还没立起来.

---

## 2. 一条原则: 先通用, 后特化

- **通用层写完并稳定了, 才动特化层.** 顺序反过来的直接后果是同一条规则被四类各写一遍, 然后各自漂移.
- **特化层只写差异.** 一条规则在通用层已经说过, 特化层不许重复, 只留一句指过去.
- **反向也成立.** 在特化层里发现某条其实四类都适用, 把它提回通用层, 不要复制四份.
- **判断一条规则属于哪一层**, 就问它换一个 repo 类型还成不成立. 成立就是通用层的, 不成立才是特化的.

维护者本人写的时候也走这个顺序: 先把通用层想透, 特化层才有东西可以 "只写差异".

---

## 3. 目录结构

```text
ref/
  ref-maintainer-README.md              本文件, 给人看, 不给 skill 读
  agent-skill-interaction-pattern.md    通用交互模式, 英文版
  agent-skill-interaction-pattern-cn.md 中文版
  00-common/                            通用层
    01-repo-layout.md                       标准
    02-readme-original-spec/                文档 spec, 人写
    03-task-readme-spec/
    04-task-ticket-spec/
    05-overview-readme-spec/
    06-overview-ticket-spec/
    07-syllabus-spec.md                     文档 spec, 脚本生成
    08-series-converge-spec.md              流程步骤: 统稿
    09-root-docs-spec.md                    流程步骤: 写根目录文档
    10-ship-spec.md                         流程步骤: 出厂
  01-readup/                            特化层
    readup-repo-layout.md
    readup-authoring-workflow.md
    readup-readme-spec/                     根 README
    readup-ticket-spec/                     根 TICKET
  02-upskill/
    upskill-repo-layout.md
    upskill-authoring-workflow.md
    upskill-readme-spec/
    upskill-ticket-spec/
    upskill-quiz-readme-spec/               特殊 Task: quiz
    upskill-quiz-ticket-spec/
    forge/                                  分组目录, 见第 4 节
  03-showcase/
    showcase-repo-layout.md
    showcase-authoring-workflow.md
    showcase-readme-spec/
    showcase-ticket-spec/
    showcase-quiz-readme-spec/              特殊 Task: quiz
    showcase-quiz-ticket-spec/
    showcase-demo-readme-spec/              特殊 Task: demo
    showcase-demo-ticket-spec/
    forge/
  evolve/                               还没立
```

- **`00-common` 里的序号就是维护顺序, 也是阅读顺序.** 它排在最前不是因为最重要, 而是因为后面三层都建立在它之上.
- **`00-common` 的号分三段: `01` 是标准, `02` 到 `07` 是文档 spec, `08` 到 `10` 是流程步骤.** 数字连着排是为了有个确定的阅读顺序, 不代表它们是同一种东西.
- **`00-common` 的判据是 "被多个 repo type 共享", 不是 "四类都有".** 比如 `05` 与 `06` 那个索引 Task 只有 examples 系的三类有, evolve 没有, 但三类共享就够格放这儿. 各文件自己的适用范围写在各自开头.
- **特化层内部不排号.** 那里不是一条阅读顺序, 是按 "谁要读" 摆的: 写根 README 的去找 `<type>-readme-spec/`, 跑 forge 的只进 `forge/`. 排号反而会暗示一个并不存在的先后.
- **两份 `agent-skill-interaction-pattern` 放在 `ref/` 根**, 因为它不限教学仓库, 任何互动 skill 都能加载. 它也是唯一一份中英都活着且内容对等的文件, **改一版必须同步另一版**.
- `evolve/` 还没排号, 因为这一类的规范还没正式立起来.

---

## 4. 三种文件形态

**spec 目录**, 形如 `<name>-spec/`. 用在有固定产物的文档上, 每个语种两份文件:

- `<name>-<lang>-spec.md`: 规范. 普通 markdown, 有编号 H2, 有表格, 有分隔线, 能渲染, 能被别的文档用锚点链过来. 权威在这.
- `<name>-<lang>-template.md`: 骨架. frontmatter 加 `[方括号]` 占位, **一个注释都没有**, 起草时整份复制过去填空.

spec 与 template **每个语种各一套**, 各写各的, 不是同一份的翻译. **目录下不放语料库.**

**分不分语种的判据只有一条: 带 template 的分, 不带的不分.** 所以 `01`, `07`, `08`, `09`, `10` 那几份单文件都不带语种后缀. 完整理由 (以及为什么不再把规范塞进顶部注释) 见 skill 根目录的 `spec-file-format.md`.

**单文件**, 形如 `<name>.md`. 用在没有固定产物的东西上, 比如目录布局标准, 工作流规范. 就是一份普通的 markdown, 没有配套 template.

**分组目录**, 目前只有两个 `forge/`. 它把**同一个消费者**要读的东西收在一处: `lesson-smith-upskill-forge` 与 `lesson-smith-showcase-forge` 跑一次要读七八份规范, 摊在特化层根下会把那一层淹掉. 分组目录不是 spec 目录, 它只是在 spec 目录外面加了一层, "一个 spec 一个目录" 那条规矩不变:

```text
02-upskill/forge/
  docs-upskill-learn/                   spec 目录, 中英各一套
  docs-upskill-runbook/
  docs-upskill-quiz/
  upskill-learn.SKILL.md                子 skill 模板, 近乎全静态, 直接拷
  upskill-learn-cn.SKILL.md
  upskill-quiz.SKILL.md
  upskill-quiz-cn.SKILL.md
```

那四份 `*.SKILL.md` 是本层唯一的**第三种东西**: 既不是 spec 也不是 template, 是可以整份拷成一个真 skill 的成品. 它们不进 spec 目录, 因为它们没有配套规范, 拷过去改个路径就能用.

---

## 5. 写一份新 spec 的顺序

1. **先去读真实写过的文件.** 从已发布的 repo 里翻出几份同类的, 尽量覆盖不同题材. 读完就走, 不要往 ref 里拷贝.
2. **再从里面归纳规范.** 找的是重复出现的分寸: 哪一节到什么程度就该收, 哪一类写法每次都翻车.
3. **最后才写 template.**

顺序不能反. 先拍脑袋定规范再回头找例子印证, 出来的规范一定和实际写法对不上, 而且对不上的地方要等到真去写一门课才暴露.

一条经验判据: 一份 spec 里如果风格类的话不到十行, 那它基本上只是在描述骨架, 还没有到能约束人的程度.

---

## 6. 术语

- 全套规范只用三个词: **Lesson** (一个 repo), **Task** (携带一对 README 与 TICKET 的最小单位), **特殊文件**. 定义见 [00-common/01-repo-layout.md](00-common/01-repo-layout.md) 第 1 节.
- **不要再用 tutorial 或 mini task.** 它们指的都是 Task. 改术语的时候连带 spec 的目录名一起改, 别只改正文.
- 流程步骤也有固定叫法: **统稿** (不叫 review), **收尾** (不叫梳理拔高), **主线** (不叫主干).

---

## 7. 语种

当前**只写中文**. 工作流里没有翻译, 也没有中译英的重写环节; 产出英文的那部分以后作为独立的多语种模块单独做. 但英文文件本身仍然存在, 只是留空.

维护 ref 时因此有三条:

- **砍的是工作流, 不是规范.** "英文版专属" 那种教你怎么重写的小节可以走, 因为现在没有重写这一步.
- **但按语种分档的预算, 字符集这类硬约束要留着.** 一份英文文件该长什么样, 规范里还得说得清. 删掉的代价是多语种模块接手时要重新推导一遍.
- **`forge/` 下的英文 spec 与 template 是例外, 它们已经写好了.** 那几份不是翻译, 是照着中文版的意思用英文重新写的, 属于多语种模块提前落位的一块. 当前 forge 只产 `-cn` 那一套, 英文那套躺着等接手.

---

## 8. 当前状态

**结构上已经完工.** 从通用层到三个特化层, 从 spec 到 workflow 到 SKILL 到 step skill, 一路都按上面几节的规矩落地了:

- `00-common/` 十份齐了: `01` 标准, `02` 到 `07` 文档 spec, `08` 到 `10` 流程三件套 (统稿, 根目录文档, 出厂).
- spec 目录全面改成两文件制 (一份 spec 加一份 template), 顶部注释与 `corpus/` 那两套已作废.
- 三个特化层的 layout, workflow, 根 README 与 TICKET spec, 特殊 Task spec 全部落位; 两个 `forge/` 分组目录中英各一套.
- 运行时那一侧同步跟上: `SKILL.md` 的 ref 索引与工作流步骤都已重指, 三条 author 命令加对应的 step skill 全部到位, `finalize` 那一套已删.
- lint 加了按语种开关 (`constants.py` 的 `LINT_ENABLED_BY_LANG`), 英文当前关着, 所以留空的英文占位文件不拖垮整仓.

**唯一的大欠账是多语种.** 它是被主动推迟的, 不是漏掉的:

- 英文正文全部留空, lint 对英文整个跳过.
- 中译英那一步已经从三份 workflow 里整步移除, `rewrite-en-spec.md` 与 `run-rewrite-en.md` 都进了 skill 根目录的 `archive/`. 三份 workflow 末尾各留一节 `附: 中译英 (当前跳过)` 记着这件事.
- 接手时要做的是三件: 打开 `LINT_ENABLED_BY_LANG` 里的英文, 把英文正文填进去, 让 forge 中英两套都产 (`forge/` 下的英文 spec 已经备好).

**两处还没对上, 都不大**:

- **撇号**: `constants.py` 的 `DESCRIPTION_FORBIDDEN_CHARS` 里还含 ASCII 单引号 (U+0027), 而 [00-common/01-repo-layout.md](00-common/01-repo-layout.md) 第 6.2 节已经改成允许 (值本身被双引号包着, 撇号不产生歧义). 要把它从这个集合里去掉. 注意 `H1_FORBIDDEN_CHARS` 里也有一个, 但 H1 不带包裹的引号, 理由不通用, 那一个要单独决定动不动.
- **`03-task-readme-spec/` 的风格层最薄**. 它是从旧 `readme-spec.md` 忠实迁过来的, 而那一份关于 "怎么写才算写好" 只有零星几句. 三份里就数它最需要照第 5 节回去读真实的教学 README 再补一层.

**明确推迟, 不算欠账**: `evolve/` 这一类的规范一直没立. 它不带 `examples/`, 和三类同构关系不一样, 要立就是从 layout 开始重新推一遍, 不是补几份 spec 的事.
