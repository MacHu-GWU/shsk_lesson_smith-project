# Readup 写全局中文规范

统稿之后, examples 是稳定素材. 这一步基于它们写四份全局文档的**中文版**, 让整门课有总入口, 总索引和总验收.

适用范围: readup 类型. 位置在统稿之后, 英文重写之前.

产出四份, 全部只写 cn:

| 文件 | 是什么 | 按哪份 spec |
| :--- | :--- | :--- |
| `examples/README-cn.md` | 系列索引, 内容地图 | [ref/readup/readup-examples-readme-spec.md](readup-examples-readme-spec.md) |
| `README-cn.md` | 仓库总览加 "怎么读" 的入口 | [ref/readup/readup-readme-spec.md](readup-readme-spec.md) |
| `TICKET-cn.md` | 整门课的验收清单 | [ref/readup/readup-ticket-spec.md](readup-ticket-spec.md) |
| `README-ORIGINAL-cn.md` | 对外门面, 重写第 1 步那版粗稿 | [ref/readme-original-spec.md](../readme-original-spec.md) |

**一份英文都不写.** 英文是下一步整门课统一重写出来的, 在这里另起一条产英文的路径, 术语和标题就会和 examples 那批对不上.

---

## 1. 采集素材

四份的内容几乎都能从既有文件推导, 直接读, 不必派 subagent:

- 各 `examples/NN-title/README-cn.md` 的 frontmatter description 与小节标题: 系列索引要按主题分组梳理它们.
- 各 `examples/NN-title/TICKET-cn.md` 的 description 与正文: 根 TICKET 第 4 节 "关键能力" 的原料.
- 第 1 步那版 `README-ORIGINAL-cn.md`: 课程定位的起点, 但它是内容没写时的粗稿, 只作参考不作准.
- `examples/_lm-example-plan.md`: 分组意图的参考.

---

## 2. 写 examples/README-cn.md

重点是**避免陈列**: 不是把 mini task 无脑罗列一遍 (那是 SYLLABUS 的活, 而且它是脚本生成的), 而是按主题分组梳理, 让读者拿到一张地图.

人类通常要在开头和结尾插入个性化的内容和观点, 所以初稿写完摆给创作者看, 问他要不要加.

---

## 3. 写根目录 README-cn.md

要点: 阅读总入口, **多链接少复述**. pitch 一句话带过并链到 `README-ORIGINAL-cn.md`, 内容一句话带过并链到 `examples/README-cn.md`, 绝不重复它们已经讲清的东西. 篇幅软上限约 50 到 70 行, 超了通常是又抄了一遍 pitch 或内容地图.

**readup 的红线: 不提任何斜杠命令.** 不引导环境 setup, 不提任何给 AI 看的元文档. 学生要做什么, 怎么自查, 全靠一篇篇 mini task 自己的 README 与 TICKET.

顶部 frontmatter 的 `description` 是 Task (这个 branch) 级的介绍, 回答 "你将学到什么", 这里罗列知识点是对的. 它和 README-ORIGINAL 那段的分工不同, 别把那段抄过来. 它会流进 SYLLABUS.

---

## 4. 写根目录 TICKET-cn.md

三段式 (目标, 要做的事情, 检查清单) 加第 4 个 H2 (关键能力). 第 4 节从各 mini task 的 TICKET 萃取, 纯 bullet, 不带 checkbox, 10 条以内且必须取舍. 预计用时创作者给了就用, 没给就保守估计或省略.

**不写指向 repo 内文件或目录的相对路径链接.** TICKET 会进 GitHub Issue, 相对路径点不动; 绝对 URL 可以. 提到 mini task 或系列索引一律用文字提及.

同样守 readup 的红线: 不出现任何斜杠命令或自测工具, 自查判据一律落在 "读完, 做完, 能独立复现, 能讲清概念" 上.

---

## 5. 重写 README-ORIGINAL-cn.md

第 1 步那版是内容还没写时的粗稿, description 太粗, 也和最终的 examples 对不齐. 现在内容齐了, 重写整份 (正文加 description 加 github_about), 让这门 Lesson 的门面和成品对齐.

要点见 [ref/readme-original-spec.md](../readme-original-spec.md), 这里只强调最容易翻车的三处:

- `description` 写给**学生**, 黄金标准是这段话能原样复制粘贴发给一个学生. 两段式: 先一句人话说清这门课学的是什么, 再说清为什么值得学以及学完有什么收获. cn 版用足预算写到接近 400 字符. **绝不罗列知识点**, 写出 "涵盖 A, B, C, D" 这种句式就是跑偏了, 哪怕前面加了 "学完你能" 也一样.
- `github_about` 写给**老师** (创作者本人与同行), 一句话说清这个 repo 教什么即可, 望文生义, 不写收获, cn 版 200 字符以内.
- H1 保持与 repo 名一模一样, 不改.

两个字段都用双引号包起来; 写 cn 版时术语, 产品名, 技术名词一律保留英文原文, 不要强行译成中文.

### 5.1 人类拍板 (不可跳过)

`description` 与 `github_about` 是这门课的门面, 一句话决定别人点不点进来, 不许 AI 单方面定稿.

初稿写完必须停下来, 把这两句单独摆给创作者看 (拿不准时给两三个不同侧重的候选让他挑), 问他 ok 不 ok, 哪里要调, 按他的意见改完再往下走. 正文那 3 段不需要这道 gate.

**这道 gate 只在中文版上过一次.** 英文版是已批准中文版的重写, 不需要第二次拍板.

---

## 6. 收尾自查

进下一步之前核一遍:

- 四份 cn 都写了, 一份英文都没写.
- 各份的相对路径链接都指向 `-cn` 版; 指向目录的链接不带语种后缀.
- 根 TICKET 里没有相对路径链接.
- 根 README 与根 TICKET 里没有任何斜杠命令 (readup 红线).
- README-ORIGINAL 的两个字段都经创作者确认过, H1 等于 repo 名.
- 根 README 的 description 是 "你将学到什么", 不是 README-ORIGINAL 那段的复制.
