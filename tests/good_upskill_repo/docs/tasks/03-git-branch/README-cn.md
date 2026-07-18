---
description: 学完你能解释 branch 解决什么问题, 并独立创建一个 branch 在上面提交改动而不影响 main.
---

# 使用 Git Branch 隔离改动

> 教你创建 branch, 在上面安全地做修改, 而不动 main 上的稳定版本.

## 1. 概览

Branch 是 repo 里的平行工作线. main branch 存放稳定版本, 新想法和半成品都放在自己的 branch 上, 做完再合并回去. 这是团队协作里 "互不踩脚" 的关键机制.

---

## 2. 学习目标

如果所有人都直接改 main, 半成品和稳定版会混在一起, 任何人的一次失误都会影响全队. branch 让每个人先在自己的平行世界里把事情做完.

学完这个 Task, 你将能够:

1. 解释 branch 解决什么问题, main branch 的角色是什么.
2. 从 main 创建一个新 branch.
3. 在 branch 上提交改动, 并确认 main 不受影响.

---

## 3. 动手做

1. 打开你的 repo, 点击左上角显示 main 的 branch 下拉框.
2. 输入新 branch 的名字, 例如 update-notes, 点击 Create branch.
3. 确认页面左上角显示的当前 branch 已经切换成 update-notes.
4. 在这个 branch 上编辑 notes.md, 追加一行内容并提交.
5. 用 branch 下拉框切回 main, 确认 notes.md 上没有这行新内容.

---

## 4. 回顾

- main 存稳定版本, 改动先发生在自己的 branch 上.
- 在哪个 branch 上提交, 改动就只属于哪个 branch.
- branch 名和 repo 名一样用小写加连字符, 说清这个 branch 在干什么.
