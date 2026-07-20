---
description: "建出一个 branch 并在其上提交改动, 主干 (默认分支) 保持不受影响."
---

# 开一个 Branch 并在上面提交改动

## 1. 目标

在自己的 repo 里开出一条新的 branch, 在这条 branch 上编辑文件并提交, 同时确认默认分支 (main) 没有被这次改动碰到. 这一步让你亲手体会 branch 的隔离作用: 进行中的工作待在自己的分支里, 主干始终保持干净.

---

## 2. 要做的事情

1. 打开你的 repo, 用左上角的 branch switcher (显示 main 的那个下拉按钮) 新建一条 branch, 名字用小写加短横线, 例如 add-tagline.
2. 确认你现在站在新 branch 上 (下拉按钮显示的是新分支名), 编辑 README.md, 加一行内容并提交, 提交时确认选的是 Commit directly to the 新分支 branch.
3. 用 branch switcher 切回 main, 打开同一个 README.md, 确认你刚加的那行不在 main 上.

**预计用时:** 10 到 15 分钟

---

## 3. 检查清单

- [ ] **新 branch 已创建**: branch switcher 里能看到一条 main 之外的分支, 名字是描述性的小写短横线格式.
- [ ] **改动提交在 branch 上**: 新 branch 上的 README.md 有你新加的那行, 且有对应的 commit.
- [ ] **main 未受影响**: 切回 main 看同一个文件, 新加的那行不存在, main 保持原样.
- [ ] **能说清原理**: 你能用一句话解释为什么在 branch 上提交不会改到 main.
