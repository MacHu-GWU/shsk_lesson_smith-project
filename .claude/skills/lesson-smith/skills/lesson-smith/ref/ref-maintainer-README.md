# ref 维护指南

**这份文件不给 Agent Skill 读, 是给维护 `ref/` 的人本人看的.** 它说清三件事: 这一堆文件按什么结构组织, 该按什么顺序写, 以及现在还欠什么.

---

## 1. 一条原则: 先通用, 后特化

- **通用层写完并稳定了, 才动特化层.** 顺序反过来的直接后果是同一条规则被四类各写一遍, 然后各自漂移.
- **特化层只写差异.** 一条规则在通用层已经说过, 特化层不许重复, 只留一句指过去.
- **反向也成立.** 在特化层里发现某条其实四类都适用, 把它提回通用层, 不要复制四份.
- **判断一条规则属于哪一层**, 就问它换一个 repo 类型还成不成立. 成立就是通用层的, 不成立才是特化的.

维护者本人写的时候也走这个顺序: 先把通用层想透, 特化层才有东西可以 "只写差异".

---

## 2. 目录结构

```text
ref/
  ref-maintainer-README.md      本文件, 给人看, 不给 skill 读
  00-common/                    通用层
    01-repo-layout.md               标准
    02-readme-original-spec/        文档 spec, 人写
    03-task-readme-spec/
    04-task-ticket-spec/
    05-overview-readme-spec/
    06-overview-ticket-spec/
    07-syllabus-spec.md             文档 spec, 脚本生成
    08-series-converge-spec.md      流程步骤
    09-ship-spec.md
  01-readup/                    特化层
  02-upskill/
  03-showcase/
  evolve/
```

- **目录与文件的序号就是维护顺序, 也是阅读顺序.** `00-common` 排在最前不是因为它最重要, 而是因为后面三个都建立在它之上.
- `00-common` 里的号还分三段: **01 是标准, 02 到 07 是文档 spec, 08 往后是流程步骤.** 数字连着排是为了有个确定的阅读顺序, 不代表它们是同一种东西.
- **`00-common` 的判据是 "被多个 repo type 共享", 不是 "四类都有".** 比如 `05` 与 `06` 那个索引 Task 只有 examples 系的三类有, evolve 没有, 但三类共享就够格放这儿. 各文件自己的适用范围写在各自开头.
- `evolve` 还没排号, 因为这一类的规范还没正式立起来.

---

## 3. 两种文件形态

**spec 目录**, 形如 `NN-<name>-spec/`. 用在有固定产物的文档上, 每个语种两份文件:

- `<name>-<lang>-spec.md`: 规范. 普通 markdown, 有编号 H2, 有表格, 有分隔线, 能渲染, 能被别的文档用锚点链过来. 权威在这.
- `<name>-<lang>-template.md`: 骨架. frontmatter 加 `[方括号]` 占位, **一个注释都没有**, 起草时整份复制过去填空.

spec 与 template **每个语种各一套**, 各写各的, 不是同一份的翻译. **目录下不放语料库.**

**分不分语种的判据只有一条: 带 template 的分, 不带的不分.** 所以 `01`, `07`, `08`, `09` 那几份单文件都不带语种后缀. 完整理由 (以及为什么不再把规范塞进顶部注释) 见 skill 根目录的 `spec-file-format.md`.

**单文件**, 形如 `NN-<name>.md`. 用在没有固定产物的东西上, 比如目录布局标准, 工作流规范. 就是一份普通的 markdown, 没有配套 template.

---

## 4. 写一份新 spec 的顺序

1. **先去读真实写过的文件.** 从已发布的 repo 里翻出几份同类的, 尽量覆盖不同题材. 读完就走, 不要往 ref 里拷贝.
2. **再从里面归纳规范.** 找的是重复出现的分寸: 哪一节到什么程度就该收, 哪一类写法每次都翻车.
3. **最后才写 template.**

顺序不能反. 先拍脑袋定规范再回头找例子印证, 出来的规范一定和实际写法对不上, 而且对不上的地方要等到真去写一门课才暴露.

一条经验判据: 一份 spec 里如果风格类的话不到十行, 那它基本上只是在描述骨架, 还没有到能约束人的程度.

---

## 5. 术语

- 全套规范只用三个词: **Lesson** (一个 repo), **Task** (携带一对 README 与 TICKET 的最小单位), **特殊文件**. 定义见 [00-common/01-repo-layout.md](00-common/01-repo-layout.md) 第 1 节.
- **不要再用 tutorial 或 mini task.** 它们指的都是 Task. 改术语的时候连带 spec 的目录名一起改, 别只改正文.

---

## 6. 语种

当前**只写中文**. 工作流里没有翻译, 也没有中译英的重写环节; 产出英文的那部分以后作为独立的多语种模块单独做. 但英文文件本身仍然存在, 只是留空.

维护 ref 时因此有三条:

- **砍的是工作流, 不是规范.** "英文版专属" 那种教你怎么重写的小节可以走, 因为现在没有重写这一步.
- **但按语种分档的预算, 字符集这类硬约束要留着.** 一份英文文件该长什么样, 规范里还得说得清. 删掉的代价是多语种模块接手时要重新推导一遍.
- 存量文件里翻译相关的部分先留着不动, 等统一 archive, 不要一份份手工删.

---

## 7. 当前状态与欠账

**已经落位的**:

- `00-common/01-repo-layout.md`: 已按中文单语种重写, 大段话改成 bullet, frontmatter 那一节从两屏压到一节.
- **spec 目录改成两文件制**: `spec-file-format.md` 已重写, `00-common` 下 `02`, `03`, `04` 三份都已按新格式落地 (spec 加 template), 顶部注释与 `corpus/` 那两套都作废.
- `ref/` 根目录的 flat spec 已清空: `readme-spec.md` 与 `ticket-spec.md` 由 `03` `04` 取代已删, `syllabus-spec.md` 与 `ship-spec.md` 迁成 `07` `09`, `review-spec.md` 重写成 `08-series-converge-spec.md` 已删.
- **lint 的按语种开关**: `constants.py` 的 `LINT_ENABLED_BY_LANG` 决定每个语种参不参与 lint, 英文当前是关的. 关掉的语种被整个跳过, 既不要求存在, 内容也不检查, 所以留空的英文占位文件不再拖垮整仓. 改回来是改一个词.
- `linter.py` 与 `linter_utils.py` 里指向规范位置的 docstring 已改到 `ref/00-common/`.

**还欠的**:

- **`03-task-readme-spec/` 的风格层最薄.** 它是从旧 `readme-spec.md` 忠实迁过来的, 而那一份关于 "怎么写才算写好" 只有零星几句, 骨架也已经和实际写法漂开了. 三份里就数它最需要回去读真实的教学 README 再补一层.
- `ref/01-readup/` 下还留着三个 `corpus/` 目录 (`readme-spec/`, `ticket-spec/`, `examples-readme-spec/`), 语料废弃之后它们该一起删, 但那是特化层的事, 等收敛到那里再动.
- **砍掉 `examples/README` 的连带改动还剩两项.** 规范 (`05` `06`) 与 lint 都已就位, 还欠: 三个特化层的 `<type>-examples-readme-spec.md` 待删 (实测三份只差一段, 那段已吸收进 `05`), 以及三个 authoring workflow 里写 `examples/README` 的地方待改.
- `ref/rewrite-en-spec.md` 属于翻译, 待 archive.
- `01-readup` 等目录里, flat 文件与新式 spec 目录并存, 待收敛.
- 大量入链仍指向旧路径 (`ref/repo-layout.md`, `ref/readup/`, `ref/upskill/`, `ref/showcase/`). 等 ref 重写收敛之后统一扫一遍, 现在改是白改.

**规范与 lint 还对不上的一处**:

- **撇号**: `constants.py` 的 `DESCRIPTION_FORBIDDEN_CHARS` 里目前含 ASCII 单引号 (U+0027). 规范已改成允许 (值本身被双引号包着, 撇号不产生歧义), 需要把它从这个集合里去掉. 注意 `H1_FORBIDDEN_CHARS` 里也有一个, 但 H1 不带包裹的引号, 理由不通用, 那一个要单独决定动不动.
