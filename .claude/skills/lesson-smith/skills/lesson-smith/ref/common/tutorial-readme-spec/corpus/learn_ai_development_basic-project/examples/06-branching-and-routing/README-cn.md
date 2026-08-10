---
description: "学完你能把一根直线 chain 改造成带分支判断的图: 用 RunnableBranch 把分类与路由声明进同一根 runnable 里, 说得清手写 if elif 会丢掉哪些能力, 并用 with_fallbacks 给主链加一层失败兜底."
---

# 分支路由, 让 chain 长出 if else

> 这一节把流水线从直线升级成一张带判断的图: 输入先过分类器, 再按分类结果走不同的 chain, 主链失败时还能自动切到备用链.

## 1. 概览

04 和 05 教的都是**直线流水线**: 输入进来, 沿着固定步骤跑到底. 但真实应用很少这么单纯.

一个客服 bot 收到问题, 总是先判断 "这是账单问题还是技术问题", 再交给对应的专家 chain 去处理. 这就像 ChatGPT 商店里那些垂直 GPTs, 每个只专注一件事; 一个看起来什么都会的助手, 内部其实是先分流再分发的结构.

这一节用 3 个脚本走完这条路: 手写 if elif 路由看清机制, `RunnableBranch` 把分流也声明进 chain 里, `.with_fallbacks([...])` 给主链加一层失败兜底.

---

## 2. 学习目标

先说清楚为什么值得花时间在这件事上.

只要你的应用要面对真实用户, 输入就一定是杂的. 有人问账单, 有人问报错, 有人问跟产品毫无关系的事. 用一个万能 prompt 硬扛, 结果是每一类都答得平庸: 想让它回答账单问题时严谨, 它对技术问题就啰嗦; 想让它对技术问题给出具体的排查步骤, 它回答闲聊时就一本正经. 分支路由是这个问题唯一干净的解法, 让每条分支各自专业, 再用一个分类器把人送到对的地方.

失败兜底是同一个道理的另一面. 线上 LLM 调用一定会失败, 你不可能给每次调用都手写 try except. 这两件事凑齐, 你的 chain 才第一次像一个能上线的东西, 而不是一个 demo.

学完这个 Task, 你将能够:

1. 说清 "分类" 和 "路由" 是分开的两件事, 并用手写 if elif 把它们跑通.
2. 用 `RunnableBranch` 把分流声明进 chain 里, 让整根 pipeline 仍然是一个 runnable.
3. 指出 `RunnablePassthrough.assign` 在 pipeline 里的位置, 并说清没有它 predicate 为什么读不到 label.
4. 讲出把路由逻辑留在 LCEL 之外的代价, 也就是用不上 batch, stream 与全链路 trace.
5. 用 `.with_fallbacks([...])` 让主链失败时自动切到备用链, 并知道多个 fallback 是怎么顺着试的.

---

## 3. 前置知识

- 完成 04 和 05 两节, 会用 `|` 拼 LCEL chain, 认得 `RunnablePassthrough.assign`.
- 项目根目录的 `.env` 里 `OPENAI_API_KEY` 已经填好, 能用 `uv run python` 跑起前几节的脚本.
- 知道 Python 的异常是怎么抛出和捕获的.

---

## 4. 你将构建或学到什么

你会得到三份可以直接改的参考实现, 它们共同拼出一个能上线的路由骨架: 一个分类器 chain, 三条各自专业的下游 chain, 一个把它们串成单根 runnable 的 `RunnableBranch`, 以及一层在主链崩掉时自动接管的 fallback.

更重要的是一个判断力: 什么时候该用 Python 的控制流, 什么时候该把控制流也交给 LCEL. 这两种写法都能跑通, 但代价完全不同, 而代价是在你写下第一行的时候就选定的.

---

## 5. 手写 if else 版本, 先看清机制

最直白的分支路由是这样的: 一个分类器 chain 把问题打成标签, Python 里写 `if/elif/else` 决定调哪个下游 chain.

```python
classify_chain = classify_prompt | model | parser  # 输出 "billing" / "tech" / "other"

billing_chain = billing_prompt | model | parser
tech_chain    = tech_prompt    | model | parser
default_chain = default_prompt | model | parser

def route(input_dict):
    label = classify_chain.invoke(input_dict).strip().lower()
    if "billing" in label:
        return billing_chain.invoke(input_dict)
    if "tech" in label:
        return tech_chain.invoke(input_dict)
    return default_chain.invoke(input_dict)
```

这里有两个细节值得停一下.

第一, 三条下游 chain 的区别全在 system prompt 里: billing 那条被设定成账单团队的客服, 技术那条被设定成会给出第一步排查建议的工程师, 默认那条只是一个友好的通用助手. 路由的价值就在这儿, 每条分支都可以有自己的人设, 自己的语气, 自己的字数限制.

第二, 分类器的输出是自由文本, 不是枚举值. 你在 prompt 里要求它只回一个小写单词, 它绝大多数时候会照做, 但偶尔会回 `Billing.` 或者 `tech support`. 所以代码里先 `.strip().lower()`, 再用 `in` 做包含匹配, 而不是 `==` 精确比较. 这是所有 "让 LLM 输出标签" 的场景都要面对的问题, 03 节的 structured output 是更硬的解法, 这里先用最省事的方式扛住.

这种写法逻辑一目了然, 想调试直接 print 就行. 代价是整个分流逻辑写在了 LCEL chain 之外: 你失去了 "整根管线就是一个 runnable" 那种对称性, 也就用不上 batch, stream 和全链路 trace.

教学上这一节就是为了留下一个对照. 看完手写版, 你才能体会下一节的 `RunnableBranch` 到底解决了什么.

详细演示见 [example_01_classify_then_route.py](./example_01_classify_then_route.py).

---

## 6. RunnableBranch, 把 if else 也变成一根 runnable

`RunnableBranch` 是 LangChain 提供的 chain 里的 if else. 语法是一串 `(predicate, chain)` 元组, 加一个 default chain 收尾:

```python
from langchain_core.runnables import RunnableBranch, RunnablePassthrough

branch = RunnableBranch(
    (lambda d: "billing" in d["label"].lower(), billing_chain),
    (lambda d: "tech" in d["label"].lower(),    tech_chain),
    default_chain,  # 默认分支, 写在最后, 它不是元组
)
```

跑法是: 把当前 input 依次喂给每个 predicate, **第一个返回真的赢**, 它对应的 chain 来跑, 后面的 predicate 根本不会被调用. 最后那个不带 predicate 的 chain 是默认分支, 谁也没匹配上时由它兜住, 所以它必须写, 而且必须写在最后.

但 predicate 要看 `d["label"]`, 而 label 是分类器算出来的, 所以路由之前得先把 label 塞进 input 字典. 这正是 05 节 `RunnablePassthrough.assign` 的用武之地:

```python
pipeline = (
    RunnablePassthrough.assign(label=classify_chain)  # 把 label 塞进 input dict
    | branch                                          # 然后按 label 路由
)
```

跟着数据走一遍就清楚了:

| 阶段 | 此刻的数据 |
| :--- | :--- |
| 输入 | `{"question": "Why was I charged twice this month?"}` |
| assign 之后 | `{"question": "...", "label": "billing"}` |
| predicate 逐个试 | 第一条 `"billing" in label` 返回真, 后面不再试 |
| 选中的 chain 跑 | 拿到的仍是完整的 dict, 它的 prompt 只用 `{question}`, 多出来的 `label` 不碍事 |
| 输出 | billing chain 给出的那句回答 |

注意倒数第二行: 下游 chain 拿到的是整个字典, 而不是被裁剪过的输入. 这是 LCEL 一个很省心的性质, 你在管线中途 assign 进去的任何东西, 后面都还拿得到, prompt 用不上的键被安静忽略就是了.

两种写法放在一起, 取舍就摆在明面上:

| 维度 | 手写 if elif | RunnableBranch |
| :--- | :--- | :--- |
| 分流逻辑在哪 | 在 LCEL 之外的 Python 函数里 | 在 chain 内部, 是管线的一部分 |
| 整根管线是什么 | 一个普通函数, 里面藏着几个 runnable | 一个 runnable |
| batch 与 stream | 只能对单条下游 chain 用, 整体用不了 | 整根管线直接 `.batch()`, `.stream()` |
| trace | 只看得到一次次孤立的调用 | 一条完整的链路, 看得出走了哪个分支 |
| 能不能再嵌进更大的 chain | 要先包一层 `RunnableLambda` | 直接用 `|` 接上去 |
| 上手难度 | 最低, 想 print 就 print | 要习惯 predicate 拿到的是整个 dict |

整根 `pipeline` 还是一个 runnable, 你可以 `.invoke()`, `.batch()`, `.stream()`, 也可以把它整个嵌进更大的 chain 里. 这是 LangChain 一贯的设计: **每个抽象都是 runnable, 都能用 `|` 接着拼**.

详细演示见 [example_02_runnable_branch.py](./example_02_runnable_branch.py).

---

## 7. fallback chain, 主链坏了自动走备份

线上的 LLM 调用是会失败的: API 限流, 服务抖动, 你选的模型暂时下线, structured output 解析挂了. 每一处失败都手写 try except 并不现实, 因为失败可能发生在管线的任何一层. LCEL 的 `.with_fallbacks([...])` 让你把这件事声明出来:

```python
chain_with_fallback = primary.with_fallbacks([fallback])
```

一旦 `primary` 抛异常, LangChain 自动接住, 转去跑 `fallback`, 整个 `.invoke()` 透明返回 fallback 的结果, 调用方根本不知道刚才出过事. 你还可以串多个: `.with_fallbacks([fallback_a, fallback_b])` 会顺着一个个试, 全都失败了才把异常向上抛.

真实项目里, fallback 通常是一次有意的降级, 常见的有三种形态: 换一个更小更便宜, 但更不容易被限流的模型; 换一个更简单的 prompt, 少要一点结构, 换取更高的成功率; 或者干脆返回一句兜底话术, 至少让用户看到一个像样的回答, 而不是一个 500.

这一节的 03 脚本为了让 fallback 每次都稳定地跑起来, **主链是一个不管输入是什么都直接 raise 的 `RunnableLambda`**, 显眼地标着 `TEACHING HACK`. 真实代码里这个位置当然是一个会调 LLM 的真 chain, 失败是偶发的, fallback 也只在偶发时启动. 你把那个 lambda 换成真 chain, 剩下的接线一个字都不用改, 这正是这个脚本想让你看到的.

最后一条边界要记住: fallback 只认异常. 主链抛异常, 它接管; 主链跑通了但给出一个糟糕的答案, 它不会有任何反应. 质量兜底是另一个话题, 得靠校验和重试, 别指望 `.with_fallbacks([...])` 替你做.

详细演示见 [example_03_fallback_chain.py](./example_03_fallback_chain.py).

---

## 8. 怎么跑

设置和前几节一致, 确认 `.env` 里 `OPENAI_API_KEY` 已经填好. 在项目根目录:

```bash
uv run python examples/06-branching-and-routing/example_01_classify_then_route.py
uv run python examples/06-branching-and-routing/example_02_runnable_branch.py
uv run python examples/06-branching-and-routing/example_03_fallback_chain.py
```

01 和 02 会先打印问题, 再打印回答; 01 还会额外打出一行 `[classified as: ...]`, 让你看见分类器到底判成了什么.

---

## 9. 练习

### 练习 1: 让三条分支都命中一次

**目标:** 亲眼确认分类和路由是两件分开的事, 而且路由结果跟着 label 走.

**怎么做:**

1. 跑 `example_01_classify_then_route.py`, 对着三个内置问题看 `[classified as: ...]` 那一行, 确认它和后面那段回答的语气对得上.
2. 把 `questions` 列表换成你自己写的三个问题, 一个明显是账单的, 一个明显是技术的, 一个跟产品毫无关系的.
3. 再加一个故意写得模棱两可的问题, 比如既提到付款又提到报错的那种, 看分类器把它判成了什么.

**你会观察到:**

前三个问题稳稳地各走一条分支. 那个模棱两可的问题则不一定, 多跑几次甚至可能得到不同的 label, 而回答的风格会跟着 label 一起变.

> **关键洞见:** 路由的准确率就是分类器的准确率. 下游 chain 写得再好, 分错了也白搭, 所以真正该投精力的地方是分类那一步的 prompt.

### 练习 2: 给 RunnableBranch 加一条自己的分支

**目标:** 把 `RunnableBranch` 从 "读得懂" 变成 "改得动".

**怎么做:**

1. 打开 `example_02_runnable_branch.py`, 先找出 `RunnablePassthrough.assign` 那一行, 确认 label 是在这里被塞进 input 字典的.
2. 在分类器的 system prompt 里加一个新类别, 比如 `shipping`.
3. 写一条 `shipping_chain`, 给它一个物流客服的人设.
4. 在 `RunnableBranch` 里补上对应的 `(predicate, chain)` 元组, 注意它要排在 `default_chain` 前面.
5. 用一个物流问题验证新分支能命中, 再用一个八竿子打不着的问题验证 `default_chain` 依然兜得住.

**你会观察到:**

新分支一次就能跑通, 而且你没有动 pipeline 的任何其他部分. 如果你不小心把新元组写到了 `default_chain` 后面, LangChain 会直接报错, 因为默认分支必须是最后一个.

> **关键洞见:** 加一条分支只需要动两个地方, 分类器的 prompt 和 branch 的元组列表. 这种改动成本正是把控制流放进 chain 里换来的.

### 练习 3: 拆掉教学 hack, 再串两级 fallback

**目标:** 看清 fallback 的触发条件, 以及多个 fallback 的试探顺序.

**怎么做:**

1. 跑 `example_03_fallback_chain.py`, 确认输出来自 fallback 那条链, 再回到代码里找到 `TEACHING HACK` 那段.
2. 把必然 raise 的 `RunnableLambda` 换成一条正常能跑通的 chain, 再跑一次, 确认这次 fallback 完全没有被触发.
3. 把主链换回会 raise 的版本, 然后写第二条 fallback, 改成 `.with_fallbacks([fallback_a, fallback_b])`, 并让 `fallback_a` 也直接 raise.
4. 在三条链里各加一行 print, 跑起来看它们的先后顺序.

**你会观察到:**

第 2 步里 fallback 一次都没跑, 因为主链没抛异常. 第 3 步的 print 会按主链, `fallback_a`, `fallback_b` 的顺序依次出现, 最终返回的是 `fallback_b` 的结果.

> **关键洞见:** fallback 列表是一条按顺序试探的降级路径, 不是并行的备份. 所以越靠后的 fallback 应该越简单, 越不容易失败, 最后一条最好是完全不依赖外部服务的那种.

---

## 10. 回顾: 我们学到了什么

- 分类和路由是两件事: 前者把输入打成 label, 后者根据 label 选 chain.
- 手写 if elif 最直观, 代价是分流逻辑跑到了 LCEL 之外, 整根管线不再是一个 runnable.
- `RunnableBranch` 用 `(predicate, chain)` 元组加一个默认分支表达 if else, 第一个为真的 predicate 获胜, 默认分支必须写在最后.
- `RunnablePassthrough.assign` 负责在路由之前把 label 算好塞进 input 字典, 没有它 predicate 就无从判断.
- 下游 chain 拿到的是完整的 input 字典, prompt 用不上的键会被安静忽略.
- `.with_fallbacks([...])` 在主链抛异常时自动切到备用链, 多个 fallback 顺着试, 全失败才向上抛.
- fallback 只认异常, 救不了 "跑通了但答得不好" 这种情况.

---

## 11. 导师寄语

**为什么这个练习重要:**

从这一节开始, 你写的东西才第一次有了 "系统" 的样子. 前面几节里, 一个 chain 就是一条从输入到输出的直线, 而真实系统的形状是一张图: 有判断, 有分支, 有失败时的退路.

我特别希望你记住第 5 节和第 6 节的那个对照. 两种写法都能跑通, 面试时你也都答得上来, 但只有一种写法能让你在半年后从容地给管线加上 batch, 接上 tracing, 或者把它整个塞进一个更大的 agent 里. 框架的价值往往不体现在第一天, 而体现在第一次需求变更的那一天.

**关键洞见:**

- 把控制流交给框架, 换来的是可组合性, 这是 LCEL 全部设计的出发点.
- 分类器是整条路由的上限, 它错了后面全错, 所以它值得你写最认真的 prompt.
- 兜底不是补丁, 而是设计的一部分. 在动手之前就想好 "这一步挂了怎么办", 比出事之后再回来补要便宜得多.
- 教学代码里那种必然失败的主链, 在真实项目里对应的是一次真实的故障. 你要练的是接线, 不是那个 lambda.

**下一步:**

回到你自己手上的项目, 找一个正在用 "一个万能 prompt 应付所有情况" 的地方, 试着把它拆成一个分类器加两三条专业分支. 你多半会发现, 拆完之后每条分支的 prompt 都变短了, 效果反而更好.

---

## 12. 速查

**跑这一节:** `uv run python examples/06-branching-and-routing/example_01_classify_then_route.py`, 把 `01` 换成 `02` 或 `03` 跑另外两个.

**三个 API:**

- `RunnableBranch((pred, chain), ..., default_chain)`: chain 里的 if else, 第一个为真的 predicate 获胜, 默认分支写在最后.
- `RunnablePassthrough.assign(label=classify_chain)`: 把新键算好塞进 input 字典, 原有的键原样保留.
- `primary.with_fallbacks([fallback_a, fallback_b])`: 主链抛异常时顺着试备用链, 全失败才向上抛.

**关键文件:**

- `example_01_classify_then_route.py`: 手写 if elif 路由, 看清分类与路由是分开的两件事.
- `example_02_runnable_branch.py`: `RunnableBranch` 加 `RunnablePassthrough.assign`, 整根管线仍是一个 runnable.
- `example_03_fallback_chain.py`: `.with_fallbacks([...])` 失败兜底, 主链是标着 `TEACHING HACK` 的必然失败版本.

到这一节, 你的 chain 已经能在多个候选里自己选路了. 下一节 (07) 换一个方向: 让 chain 同时做多件事 (`RunnableParallel`), 把长输入拆成小块并行处理再合回去 (map-reduce), 把任务从串行多步扩展到并行加聚合.
