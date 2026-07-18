---
description: 学完你能在 GitHub 上创建和编辑文件, 写出一条合格的 commit message, 并看懂文件的修改历史.
---

# 在 Repository 里创建与编辑文件

> 教你在 GitHub 网页上创建文件, 编辑文件, 并用 commit 记录每次改动.

## 1. 概览

有了 repo, 下一步就是往里放内容. GitHub 网页端就能直接创建和编辑文件, 每次保存都是一次 commit: 一条带说明的, 可追溯的修改记录.

---

## 2. 学习目标

普通网盘也能存文件, 但它答不上 "这个文件上周改了什么, 为什么改". commit 历史让每一次修改都有作者, 时间和理由, 这是版本管理和裸存储的本质区别.

学完这个 Task, 你将能够:

1. 在 GitHub 网页上创建新文件和编辑已有文件.
2. 写出一条清晰说明改动内容的 commit message.
3. 通过 History 查看一个文件的历次修改.

---

## 3. 动手做

1. 打开上一课创建的 repo, 点击 Add file, 选择 Create new file.
2. 文件名填 notes.md, 正文随意写几行, 例如今天学到的东西.
3. 在 commit message 里用一句话说明这次改动, 例如 Add first note, 然后提交.
4. 回到文件列表, 点开 notes.md, 点击铅笔图标进入编辑模式.
5. 追加一行内容, 再写一条说明本次改动的 commit message 并提交.
6. 点击文件页面的 History, 确认能看到两条 commit 记录.

---

## 4. 回顾

- 每次保存就是一次 commit, commit message 要说清 "改了什么, 为什么改".
- 文件的 History 是它的完整履历, 任何一版都能找回来.
- 网页端适合小改动; 大量修改以后会用本地 clone 加 push 的方式.
