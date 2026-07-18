---
description: 学完你能通过 Pull Request 把 branch 合并回 main, 并说清 PR 在团队协作里的审查作用.
---

# 通过 Pull Request 合并 Branch

> 教你用 Pull Request 把 branch 上的改动审查并合并回 main, 走完协作闭环的最后一步.

## 1. 概览

Branch 上的工作做完了, 最后一步是把它合并回 main. GitHub 上标准的做法不是直接合并, 而是发起一个 Pull Request (PR): 先展示改动, 请人审查, 通过后再 merge.

---

## 2. 学习目标

直接把改动塞进 main, 队友只能事后发现问题. PR 把 "合并" 变成一次公开的审查: 改了什么一目了然, 讨论有记录, 问题在进 main 之前就被拦住. 这是现代团队协作的核心仪式.

学完这个 Task, 你将能够:

1. 为一个 branch 发起 Pull Request.
2. 看懂 PR 页面上的改动对比 (diff).
3. 完成 merge, 并在合并后删除已完成使命的 branch.

---

## 3. 动手做

1. 打开你的 repo, 切到上一课创建的 update-notes branch.
2. 点击 Contribute, 选择 Open pull request.
3. 确认方向是从 update-notes 合入 main, 填写标题和一句话说明, 点击 Create pull request.
4. 在 PR 页面的 Files changed 标签下检查 diff, 确认改动符合预期.
5. 点击 Merge pull request 完成合并, 然后点击 Delete branch.
6. 切回 main, 确认 notes.md 上已经能看到 branch 里的那行新内容.

---

## 4. 回顾

- PR 是 "请求把我的 branch 合并进 main" 的正式流程, 自带审查和讨论.
- Merge 之后 branch 的使命就结束了, 及时删掉保持 repo 干净.
- 至此你走完了协作闭环: 建 repo, 改文件, 开 branch, 合并回 main.
