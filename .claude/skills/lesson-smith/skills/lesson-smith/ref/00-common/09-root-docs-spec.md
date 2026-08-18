# 写根目录文档规范

统稿之后 `examples/` 是稳定素材. 这一步基于它们写 repo **根目录**那三份文档, 让整门课有总入口, 总验收和对外门面.

**适用范围**: readup, upskill, showcase 三类. evolve 一个 branch 一个 Task, 根目录那几份各归各的 branch, 没有 "回头汇总一次" 这一步, 不适用.

**位置**: 统稿之后 (见 [08-series-converge-spec.md](08-series-converge-spec.md)), 出厂之前. **upskill 与 showcase 还要等 forge 跑完**, 因为这两类的根 README 与根 TICKET 要指名道姓提到 forge 产出的那几个子 skill; 子 skill 还不存在就写, 等于写一句没法验证的话.

**为什么单独一步**: 这三份全都拿 `examples/` 当素材 (根 TICKET 要从各 Task 萃取关键能力, 根 README 要讲清怎么读, README-ORIGINAL 要和成品对齐). 素材还在漂的时候写, 全是白写.

---

## 1. 产出三份

| 文件 | 是什么 | 按哪份 spec |
| :--- | :--- | :--- |
| `README-cn.md` | 仓库总览加操作入口 | readup [readup-readme-spec](../01-readup/readup-readme-spec/readup-readme-cn-spec.md) / upskill [upskill-readme-spec](../02-upskill/upskill-readme-spec/upskill-readme-cn-spec.md) / showcase [showcase-readme-spec](../03-showcase/showcase-readme-spec/showcase-readme-cn-spec.md) |
| `TICKET-cn.md` | 整门课的验收清单 | readup [readup-ticket-spec](../01-readup/readup-ticket-spec/readup-ticket-cn-spec.md) / upskill [upskill-ticket-spec](../02-upskill/upskill-ticket-spec/upskill-ticket-cn-spec.md) / showcase [showcase-ticket-spec](../03-showcase/showcase-ticket-spec/showcase-ticket-cn-spec.md) |
| `README-ORIGINAL-cn.md` | 对外门面, 重写最早那版粗稿 | [02-readme-original-spec](02-readme-original-spec/readme-original-cn-spec.md), 三类通用 |

**这一步不碰 `examples/`.** 索引 Task 和收尾 Task 都属于 examples, 在统稿之前就该写完了.

---

## 2. 先采集素材

三份的内容几乎都能从既有文件推导, 直接读, 不必派 subagent:

- 各 `examples/NN-title/README-cn.md` 的 frontmatter description: 根 README 那行 description 要从中挑几个有代表性的主题串出来.
- 各 `examples/NN-title/TICKET-cn.md` 的 description 与正文: 根 TICKET 第 4 节 "关键能力" 的原料.
- 最早那版 `README-ORIGINAL-cn.md`: 课程定位的起点, **但它是内容没写时的粗稿, 只作参考不作准**.
- `examples/_lm-example-plan.md`: 分组意图的参考.

---

## 3. 写根 README

要点是**多链接少复述**: pitch 一句话带过并链到 `README-ORIGINAL-cn.md`, 内容一句话带过并链到 `examples/`, 绝不重复它们已经讲清的东西. 超出软上限通常就是又抄了一遍 pitch.

**顶部那行 description 和 README-ORIGINAL 那段分工不同**, 别把那段抄过来: 这一行是 Task 级的, 回答 "你将学到什么"; 那一段是 Lesson 级的, 回答 "为什么值得学". 这一行会流进 SYLLABUS.

各类型的红线在各自的 spec 里 (readup 不提任何斜杠命令; upskill 与 showcase 要写死那几个 skill 且不提 runbook), 照那一份写.

---

## 4. 写根 TICKET

三段式加第 4 个 H2 (关键能力). 第 4 节从各个 Task 的 TICKET 萃取, **纯 bullet, 不带 checkbox, 10 条以内且必须取舍**. 预计用时**不许估**: 把 `examples/` 下每个 Task TICKET 的档位下限与上限分别相加, 写法见 [04-task-ticket-spec](04-task-ticket-spec/task-ticket-cn-spec.md) 第 8.1 节. **这一行不能省**: 它属于受控词汇, 三份根 TICKET spec 的自检都要求它在.

**不写指向 repo 内文件或目录的相对路径链接.** TICKET 会进 GitHub Issue, 相对路径点不动; 绝对 URL 可以. 提到别的 Task 一律用文字提及.

---

## 5. 重写 README-ORIGINAL

最早那版是内容还没写时的粗稿, description 太粗, 也和最终的 examples 对不齐. 现在内容齐了, **重写整份** (正文加 description 加 github_about), 让这门 Lesson 的门面和成品对齐.

完整要点见 [02-readme-original-spec](02-readme-original-spec/readme-original-cn-spec.md), 这里只提最容易翻车的两处:

- `description` 写给**学生**, 黄金标准是这段话能原样复制粘贴发给一个学生. **绝不罗列知识点**, 写出 "涵盖 A, B, C, D" 这种句式就是跑偏了, 哪怕前面加了 "学完你能" 也一样.
- `github_about` 写给**老师** (创作者本人与同行), 一句话说清这个 repo 教什么即可, 望文生义, 不写收获.

### 5.1 人类拍板, 不可跳过

`description` 与 `github_about` 是这门课的门面, 一句话决定别人点不点进来, **不许 AI 单方面定稿**.

初稿写完必须停下来, 把这两句单独摆给创作者看 (拿不准时给两三个不同侧重的候选让他挑), 问他 ok 不 ok, 哪里要调, 按他的意见改完再往下走.

正文那三段不需要这道 gate, 只有这两个字段需要.

---

## 6. 收尾自查

进下一步之前核一遍:

- 三份都写了.
- 各份的相对路径链接都指向 `-cn` 版; 指向目录的链接不带语种后缀.
- 根 TICKET 里没有相对路径链接.
- readup: 根 README 与根 TICKET 里没有任何斜杠命令.
- upskill 与 showcase: 该写死的那几个 skill 都提到了.
- README-ORIGINAL 的两个字段都经创作者确认过, H1 等于 repo 名.
- 根 README 的 description 是 "你将学到什么", 不是 README-ORIGINAL 那段的复制.
