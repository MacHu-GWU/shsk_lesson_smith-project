---
description: "三个脚本都跑通并看懂输出, 能演示同一根 pipeline 按 label 走进不同分支, 也能演示主链抛异常时 with_fallbacks 自动切到备用链."
---

# 让 chain 学会分支路由与失败兜底

## 1. 目标

把 chain 从直线流水线升级成一张带分支判断的图. 你要亲手跑通三种写法: 手写 if elif 路由先看清机制, `RunnableBranch` 把分流也声明进 chain 里, `.with_fallbacks([...])` 给主链加一层失败兜底. 完成后你应该能说清楚, 为什么把路由逻辑留在 LCEL chain 之外会丢掉 batch, stream 与全链路 trace, 以及什么场景下该选哪一种写法.

---

## 2. 要做的事情

1. 完整读完本节 README, 重点弄明白 "分类" 和 "路由" 是两件分开的事.
2. 确认项目根目录的 `.env` 里 `OPENAI_API_KEY` 已经填好, 然后跑 `example_01_classify_then_route.py`, 观察分类器输出的 label 以及最终走的是哪一条 chain.
3. 换不同的输入把 01 多跑几次, 让 billing, tech, other 三条分支各命中一次, 确认路由结果符合预期.
4. 跑 `example_02_runnable_branch.py`, 对照 01 的代码, 找出 `RunnablePassthrough.assign` 是在哪一步把 label 注入 input 字典的.
5. 在 02 的基础上做一个小改动: 自己加一个分类 (例如 shipping), 补上对应的 predicate 与 chain, 确认新分支能被命中, 同时 default chain 依然兜得住没匹配上的输入.
6. 跑 `example_03_fallback_chain.py`, 看清主链是一个标着 `TEACHING HACK` 的必然 raise 的 `RunnableLambda`, 再把它换成一个正常能跑通的 chain, 确认这时 fallback 不会被触发.
7. 给 03 串上两个 fallback, 让第一个 fallback 也失败, 观察它是不是顺着试到第二个才返回.

**预计用时:** 30 到 45 分钟

---

## 3. 检查清单

- [ ] **三个脚本都跑通**: 01, 02, 03 都能在本地正常执行并打印出结果.
- [ ] **三条分支都命中过**: 用不同输入让 billing, tech, other 各走了一次, 并能对上分类器输出的 label.
- [ ] **看懂 label 注入**: 能指出 `RunnablePassthrough.assign` 在 pipeline 里的位置, 并说清没有它 predicate 为什么读不到 label.
- [ ] **亲手扩过分支**: 在 02 里加了一条自己的 predicate 与 chain, 新分支能命中, default chain 仍然兜底.
- [ ] **说得清取舍**: 能讲出手写 if elif 版本失去了什么, 也就是整根管线不再是一个 runnable, 用不上 batch, stream 与全链路 trace.
- [ ] **fallback 真的生效**: 能演示主链抛异常时 `.with_fallbacks([...])` 自动切到备用链, 调用方拿到的是 fallback 的结果, 而且不需要写 try except.
- [ ] **理解多级 fallback**: 知道 fallback 列表是顺着一个个试的, 全都失败才把异常向上抛.
- [ ] **认得出教学 hack**: 能说清 03 里那个必然失败的主链只是为了让演示稳定复现, 真实代码里主链是真 chain, 失败只是偶发.
