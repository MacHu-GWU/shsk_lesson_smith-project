---
name: cn-to-en
description: 把中文 Markdown 文档改写 (而不是翻译) 成地道英文. 先出英文草稿, 再用 cn-to-en-reviewer 与 cn-to-en-polisher 两个 subagent 多轮对照打磨, 最后统稿输出 final. Use when turning a Chinese .md doc into natural English, or when an existing English version still reads like translationese.
argument-hint: "<source-cn.md> [output.md]"
allowed-tools: Read Write Edit Glob Grep Agent Task Bash(mkdir *) Bash(python3 *) Bash(git rev-parse *) Bash(ls *) Bash(wc *)
---

参数: $ARGUMENTS

把一份中文 Markdown 改写成英文. 注意是**改写**不是翻译: 目标读者是英语母语的技术读者,
成品要读起来像英语母语作者自己写的, 而不是像一份译稿.

整个流程是: 出草稿 (主线程) → 审阅 (subagent) → 打磨 (subagent) → 审阅 → 打磨 → ... → 统稿 (主线程).
审阅和打磨反复交替直到收敛.

---

## 术语与路径

| 名字 | 含义 |
| --- | --- |
| source | 中文原稿, `$0` |
| final | 最终英文成品, `$1` |
| draft | 英文草稿, 全程在 tmp 里反复被改 |
| workspace | 这次任务的 tmp 工作目录 |
| rules | `${CLAUDE_SKILL_DIR}/references/english-rewrite-rules.md` |
| script | `${CLAUDE_SKILL_DIR}/scripts/check_invariants.py` |

传给 subagent 的路径**一律用绝对路径**, 不要让它自己找文件.

---

## 第 0 步: 定场

1. `$0` 是 source. 没给就问用户要, 不要自己猜.
2. `$1` 是 final. 没给就按规则推:
   - 文件名以 `-cn.md` 结尾 → 去掉 `-cn`, 例如 `guide-cn.md` → `guide.md`
   - 否则 → `<stem>-en.md`
   推完把结论告诉用户一句, 然后继续, 不用等确认.
3. 用 `git rev-parse --show-toplevel` 找仓库根, workspace 定为
   `<repo-root>/tmp/cn-to-en/<source-stem>/`, `mkdir -p` 建出来.
   (本仓库的 `tmp/` 已在 `.gitignore` 里, 中间产物不会污染仓库.)
4. workspace 里的文件名固定:
   - `draft.md` 英文草稿
   - `review-r1.md`, `review-r2.md`, ... 每轮的修改意见
5. Read rules 文件. 这是全流程的裁判标准, 主线程自己也要遵守.
6. Read source 全文, 顺便 `wc -l` 看看规模.

---

## 第 1 步: 出英文草稿 (主线程做)

把 source 改写成英文, 写进 `draft.md`.

- **按顶层 header 分批写.** 文档长的时候一次写不完, 第一批用 Write 建文件,
  后面每批用 Edit 追加. 不要试图一口气吐完整篇.
- 每一节的做法是: 先把这一节读懂, 想清楚它到底在说什么, 然后用英文表达这件事.
  不要打开中文句子逐句找对应的英文.
- 严格守住 rules 的 A 节不变量, 尤其是 header 结构, 代码块, 表格, 引用块, 以及不许有破折号.
- 这一步产出的东西**必然还有翻译腔**, 这是预期之内的, 不要在这一步反复纠结.
  后面的 2, 3 步就是专门来治它的.

写完跑一次机械检查, 把 FAIL 全修掉再进入循环:

```
python3 <script> --source <source> --draft <workspace>/draft.md
```

---

## 第 2 步: 审阅 (subagent `cn-to-en-reviewer`)

用 Agent 工具起一个 `cn-to-en-reviewer`, 任务描述里给全这些:

```
第 <N> 轮审阅.
中文原稿: <source 绝对路径>
英文草稿: <workspace>/draft.md
规则文件: <rules 绝对路径>
本轮意见写到: <workspace>/review-r<N>.md
机械检查脚本: <script 绝对路径>

按你的系统提示逐节对照, 把 finding 写进意见文件, 只回极短摘要.
不要修改英文草稿.
```

它会返回 `P1=<n> P2=<n> P3=<n> F=<n>` 和意见文件路径. 把这几个数记下来, 收敛判断要用.

---

## 第 3 步: 打磨 (subagent `cn-to-en-polisher`)

用 Agent 工具起一个 `cn-to-en-polisher`, 任务描述里给这些:

```
第 <N> 轮打磨.
英文草稿: <workspace>/draft.md   (直接原地改这个文件)
本轮意见: <workspace>/review-r<N>.md
规则文件: <rules 绝对路径>
机械检查脚本: <script 绝对路径>

按你的系统提示以节为单位重写. 不要读中文原稿.
```

**任务描述里不要出现 source 的路径.** 打磨环节故意不看中文, 给了路径就等于给了它偷看的机会.

---

## 第 4 步: 循环

重复第 2 步和第 3 步, N = 1, 2, 3, ...

每一轮的两个 subagent 都**重新起一个新的**, 不要用 SendMessage 续用上一轮那个.
新起的 reviewer 没有上一轮的记忆, 才会用同样的标准重新审, 续用会让它对自己刚提过的地方放水.

每轮 polisher 跑完后, 主线程跑一次机械检查:

```
python3 <script> --source <source> --draft <workspace>/draft.md
```

有 FAIL 就直接在下一轮的 reviewer 任务描述里点名, 或者主线程自己顺手修掉结构性问题.

**停止条件**, 满足任意一条就停:

- `P1 == 0` 且 `P2 <= 3`. 这是正常收敛.
- 本轮 P1 相比上一轮没有下降. 说明在震荡, 再转也没用.
- 已经跑到第 4 轮. 硬上限.

每轮之间给用户报一行进度: `round <N>: P1=<n> P2=<n> P3=<n> F=<n>`.

---

## 第 5 步: 统稿 (主线程做)

从这里开始 **`draft.md` 不再改动**, 它就留在 tmp 里当存档.

Read source 和 `draft.md`, 把两边对照着过一遍, 只管三件事:

1. **保真.** 中文有的要点英文里在不在, 英文里有没有冒出中文没有的断言, 数字, 例子.
   前面的 polisher 一直没看中文, 这一步是唯一的兜底.
2. **全局一致.** 术语在全篇是不是同一个英文词, 人称 (`we` / `you` / 无人称) 有没有摇摆,
   时态是否合理, header 的大小写风格是否统一, 列表项的并列结构是否整齐.
3. **不变量.** rules 的 A 节再核一遍.

把修正后的结果写到 final 路径. 然后跑最后一次检查:

```
python3 <script> --source <source> --draft <final>
```

必须 0 failure. 有 FAIL 就修到没有为止.

---

## 收尾汇报

给用户这几样, 不要长篇大论:

- final 路径, 以及 draft 和历轮意见留在哪个 workspace
- 一共跑了几轮, 每轮的 P1/P2/P3/F
- 最后一次机械检查的结果
- 统稿阶段自己动手改的地方 (尤其是保真类的修正)
- 还有什么明知不理想但没动的, 以及为什么

---

## 常见坑

- **不要把整篇中文塞进 subagent 的任务描述里.** 给路径, 让它自己 Read.
- **subagent 不能再起 subagent.** 所有 Agent 调用都由主线程发起.
- **不要跳过第 1 步直接让 subagent 写草稿.** 主线程手里有草稿的完整上下文,
  第 5 步统稿要靠它.
- **不要因为第 1 步草稿 "看着还行" 就跳过循环.** 第 1 步的输出必然有翻译腔,
  自己看不出来才是常态, 这就是要一个独立 reviewer 的原因.
- **不要让 reviewer 顺手改草稿.** 审和改分开是这个流程的核心, 合在一起就退化成
  逐条打补丁了.
