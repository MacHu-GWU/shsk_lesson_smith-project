---
description: 在你的 repository 里新建并编辑若干文件, 留下几条语义清晰的 commit.
---

# 用 Web Editor 提交你的前几条 Commit

## 1. 目标

在完全不装 git 的前提下, 用 GitHub 的 web editor 给你已有的 repository 新建和修改文件, 并且每一次改动都配上一条说清意图的 commit message. 做完之后, 你的 Commits 页面上应该排着一串读得懂的历史.

---

## 2. 要做的事情

1. 打开 Task 01 建好的 repository (例如 recipe-box).
2. 用 Add file, Create new file 新建一个文件, 文件名带一层文件夹, 例如 recipes/pancakes.md, 写几行 Markdown 内容.
3. 提交时把 commit message 写成动词开头的一句话, 例如 Add pancake recipe.
4. 点开 README.md, 用铅笔图标编辑它, 补一句项目介绍, 再提交一次, message 例如 Update README with project intro.
5. 进入 Commits 页面, 找到你刚才这几条 commit, 点开其中一条看它的 diff (绿色新增, 红色删除).

**预计用时:** 10 到 15 分钟

---

## 3. 检查清单

- [ ] **新建文件成功**: repository 里出现了一个新文件, 且文件名里的斜杠自动建出了对应文件夹.
- [ ] **编辑文件成功**: 已有文件 (如 README.md) 的内容被改动并提交.
- [ ] **commit message 清晰**: 每条 message 都是动词开头, 一句话说清这次改了什么, 没有 update, fix 这类含糊词.
- [ ] **读懂 history**: 能在 Commits 页面找到自己的 commit, 并点开看懂它的 diff.
