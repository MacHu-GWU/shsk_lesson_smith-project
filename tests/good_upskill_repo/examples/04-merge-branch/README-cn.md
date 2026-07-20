---
description: 学会用 Pull Request 把 branch 的改动 review 后合并回主干, 走完一次协作闭环.
---

# 用 Pull Request 合并 Branch

> 教你把上一课 branch 上的改动, 通过 Pull Request 让人看过之后, 干净地合并回 main.

## 1. 概览

上一课你在 branch 上安全地做了改动, main 保持不变. 但改动待在 branch 上是没有价值的: 它必须回到 main, 才能成为项目的正式版本. Pull Request (简称 PR) 就是这个 "请把我的改动合并进来" 的正式请求. 它不是简单地一键覆盖, 而是给了团队一个先看一眼, 讨论, 然后再合并的机会. 这一课, 我们走完从 branch 到 main 的最后一段路, 也就走完了整门课的协作闭环.

---

## 2. 学习目标

想象你在一家咖啡馆点单. 你不会自己冲进后厨去操作咖啡机, 而是把订单交给店员, 由店员确认, 再交给厨房制作. Pull Request 就是这张订单: 你不直接改 main, 而是提出一个请求, 让改动经过一道确认再进入主干. 为什么要多这一道手续? 因为 main 是所有人共享的稳定版本. 一旦有人把没写完或有 bug 的代码直接推上 main, 全队都会被牵连. PR 把 "改动" 和 "正式采纳改动" 拆成两步, 中间留出检查和讨论的空间. 这就是现代团队协作的核心节奏.

学完这个 Task, 你将能够:

1. 解释 Pull Request 是什么, 以及它和直接改 main 有什么本质区别.
2. 说清 code review 在团队里解决什么问题.
3. 独立开一个 PR, 走完 review 和 merge, 并在合并后删掉用完的 branch.
4. 认出什么是 merge conflict, 知道它大致什么时候会出现.

---

## 3. 前置知识

- 完成过第 03 课, 手上有一个带 branch (例如 update-notes) 且 branch 上有改动的 repo.
- 理解 branch 是平行工作线, main 是稳定主干 (第 03 课讲过).
- 会用 GitHub 网页端的文件编辑和 commit (第 02 课讲过).

---

## 4. 你将学到什么

学完你会亲手把一个 branch 的改动, 通过 PR 合并回 main, 并看到 main 上真的出现了这些改动. 你会知道 PR 页面上每个区域是干什么的, 也会第一次理解为什么全世界的工程团队都围着 PR 转.

---

## 5. Pull Request 是什么

Pull Request 是一个请求: "请把我这个 branch 上的改动, 拉 (pull) 进目标 branch (通常是 main)." 名字里的 request 是关键 - 它是请求, 不是命令. 提出请求和真正合并是两件事, 中间隔着一次审阅.

一个 PR 页面把三样东西集中在一起:

- **对比 (diff)**: 你的 branch 相对 main 到底改了哪些行, 红色是删掉的, 绿色是新增的, 一目了然.
- **对话 (conversation)**: 一个讨论区, 你和队友可以在这里留言, 提问, 逐行评论.
- **合并按钮 (merge)**: 讨论清楚, 大家满意了, 点一下就把改动并入 main.

可以把 PR 理解成给一份改动开的 "线上评审会": 改了什么摊在桌上, 相关的人围着看, 达成一致后拍板采纳. 它把原本口头, 私下, 容易漏掉的 "你看看我这个改动行不行", 变成一个有记录, 可追溯的正式流程.

---

## 6. Code review: 为什么合并前要先看一眼

Code review (代码审阅) 是指: 改动在合并进 main 之前, 由作者之外的人先读一遍. 这是 PR 存在的最大理由.

假设 Maria Garcia 在 branch 上改好了 notes.md, 开了一个 PR. 队友 John Smith 打开 PR, 看到那份 diff, 他可以:

- **留 comment**: 在某一行旁边提问或提建议, 例如 "这里是不是漏了一个标题?".
- **approve**: 觉得没问题, 点 Approve, 表示 "我看过了, 支持合并".
- **request changes**: 觉得还得改, 打回去让作者再改改.

为什么这一步值得花时间? 三个实实在在的好处:

1. **早点抓 bug**: 别人的眼睛常常能看出你自己盯了半天都没发现的错.
2. **知识不再只装在一个人脑子里**: review 过的人也就了解了这块改动, 项目不会因为某个人休假就卡住.
3. **留下记录**: 半年后有人问 "这行为什么这么写", PR 里的对话就是答案.

在个人练习里你既是作者也是 review 的人, 可能觉得多此一举. 但在团队里, code review 几乎是所有严肃项目的默认关卡. 现在就把它当回事, 是在为将来进团队打底子.

---

## 7. 动手: 开一个 Pull Request

1. 打开你在第 03 课改动过的 repo, 确认 update-notes 这个 branch 上已经有至少一次 commit.
2. GitHub 通常会在 repo 主页顶部弹出一条黄色提示, 写着 update-notes had recent pushes, 右边有一个 Compare & pull request 按钮, 点它. (如果没弹出来, 点顶部的 Pull requests 标签, 再点 New pull request, 手动选 base 是 main, compare 是 update-notes.)
3. 确认页面上方的方向是 base: main <- compare: update-notes, 也就是 "把 update-notes 合进 main".
4. 给 PR 填一个清楚的标题, 例如 Add study notes for week one, 下面的描述框里用一两句话说清你改了什么, 为什么改.
5. 往下滚, 看一眼 Files changed 里的 diff, 确认改动就是你预期的那些行.
6. 点击 Create pull request. 恭喜, 你的第一个 PR 开出来了.

---

## 8. Merge: 把改动合并回 main

PR 开好, review 通过之后, 就到了合并这一步.

1. 在 PR 页面往下滚, 找到绿色的 Merge pull request 按钮, 点它.
2. GitHub 会让你确认一条 merge commit 的说明, 保持默认即可, 点 Confirm merge.
3. 页面会变成一句紫色的 Pull request successfully merged and closed. 这说明 update-notes 上的改动此刻已经进入 main.
4. 切回 repo 主页, 把 branch 下拉框切到 main, 打开 notes.md, 你会看到刚才那些改动真的出现在 main 上了.

到这一刻, 一个改动完成了它的完整旅程: 从 branch 上诞生, 经过 PR 被看过, 最后被 merge 进主干, 成为项目的正式一部分.

---

## 9. 合并后删掉 branch

merge 成功后, GitHub 会在原地给出一个 Delete branch 按钮. 放心点它.

为什么要删? 因为 update-notes 的使命已经完成 - 它的改动都进 main 了, 这个 branch 再留着只会让 branch 列表越堆越乱. 删掉的是这条 "工作线" 的标签, 不是那些改动本身, 改动已经安全地存在 main 的历史里了. 需要的话, 这个 branch 之后还能恢复.

一句话记住: 一个 branch 对应一件事, 事做完 (merge 完) 就把 branch 收掉.

---

## 10. 顺带一提: 什么是 merge conflict

大多数 merge 都是干净利落的, 点一下就合并成功. 但偶尔你会撞上 merge conflict (合并冲突), 有必要先认个脸.

merge conflict 发生在: **两个 branch 改了同一个文件的同一处, 而且改得不一样**. 比如 main 上有人把某一行改成了 A, 你在 branch 上把同一行改成了 B. GitHub 合并时发现这里有两个互相打架的版本, 它不敢替你瞎猜哪个对, 于是停下来, 请人来定夺.

不用怕它. 现阶段你只要知道两件事:

- 它不是错误, 只是 GitHub 在说 "这里我拿不准, 你来决定留哪个".
- 解决它就是人工挑一下: 留 A, 留 B, 还是把两者揉在一起, 然后确认.

只要每个人各改各的文件, 或者及时把 main 的新改动同步到自己 branch, conflict 就很少出现. 深入解决冲突是以后的话题, 这门课点到为止.

---

## 11. 全景: 一次完整的协作闭环

把整门课串起来, 你已经走完了一个完整的循环:

1. **建 repo** (第 01 课): 给项目一个唯一的家.
2. **改文件** (第 02 课): 用 commit 记录每一次修改.
3. **开 branch** (第 03 课): 把没写完的改动和 main 隔开.
4. **开 PR** (本课): 把 branch 的改动摊出来, 让人 review.
5. **merge** (本课): 讨论通过后合并回 main, 再删掉 branch.

这五步不是一次性的, 而是一个不断转的轮子. 真实项目里, 每加一个功能, 每修一个 bug, 团队都在重复这个 branch -> PR -> review -> merge 的循环. 你今天走通的这一圈, 就是每天在无数团队里发生的那件事.

---

## 12. 练习

### 练习 1: 完整走一遍 PR 闭环

**目标:** 亲手把 update-notes 的改动, 通过 PR 合并回 main.

**怎么做:**

1. 打开第 03 课那个 repo, 确认 update-notes 上有改动.
2. 按第 7 节开一个 PR, 标题和描述都写清楚.
3. 在 PR 的 diff 里留一条自己的 comment, 假装你是 reviewer.
4. 按第 8 节 merge 这个 PR, 再按第 9 节删掉 branch.
5. 切到 main 打开 notes.md, 确认改动到位了.

**你会观察到:**

merge 之后, 原本只在 update-notes 上的那几行, 现在出现在 main 上了; branch 列表里 update-notes 也不见了.

> **关键洞见:** 改动的价值不在于它被写出来, 而在于它被 review 过之后合并进了主干.

### 练习 2: 制造一个小 conflict 看看

**目标:** 亲眼见一次 merge conflict, 消除对它的恐惧.

**怎么做:**

1. 新建一个 branch, 例如 edit-title, 把 notes.md 第一行改成一句话并 commit.
2. 回到 main, 直接把 notes.md 同样的第一行改成另一句话并 commit.
3. 为 edit-title 开一个 PR, 观察 GitHub 的提示.

**你会观察到:**

GitHub 会提示这个 PR 有 conflict, 不能直接自动合并, 需要先解决冲突.

> **关键洞见:** conflict 不是灾难, 只是系统在诚实地说 "同一处有两个版本, 请你来拍板".

---

## 13. 回顾: 我们学到了什么

- **Pull Request** 是一个 "请把我的改动合并进来" 的请求, 把改动和采纳改动拆成了两步.
- **Code review** 让改动在进 main 前先被人看一遍, 早抓 bug, 摊平知识, 留下记录.
- **Merge** 把 branch 的改动正式并入 main; 合并后 **删掉 branch** 保持整洁.
- **Merge conflict** 出现在两处改动打架时, 它不是错误, 只是需要人来定夺.
- 建 repo -> 改文件 -> 开 branch -> 开 PR -> merge, 是一个不断重复的协作闭环.

---

## 14. 导师寄语

**为什么这个练习重要:**

我带过很多刚上手的人, 他们最容易低估的就是 PR 这一步. 会用 git 的人很多, 但真正让团队跑得顺的, 是那些认真对待 review 的人. 一个好 PR 不只是代码正确, 它还讲清楚了 "我改了什么, 为什么这么改", 让别人五分钟就能看懂并放心合并. 你在这门课里开的第一个 PR, 内容再简单, 也是在练这个习惯.

**关键洞见:**

- PR 是团队沟通的载体, 不只是合并代码的按钮. 你写的标题和描述, 是写给未来的队友看的.
- review 别人的代码和被 review, 都是成长最快的场合之一, 别把它当成挑刺.

**下一步:**

回到真实项目里, 试着给每一个改动都开 PR, 哪怕只有你一个人. 强迫自己在描述里说清 why, 你会发现自己想得更清楚了. 等你进了团队, 这套动作已经是肌肉记忆.

---

## 15. 速查

**开 PR:** 在 repo 主页点 Compare & pull request, 或走 Pull requests 标签 -> New pull request, 确认方向是 base main <- compare 你的 branch.

**合并:** PR 页面 Merge pull request -> Confirm merge -> 出现 successfully merged 即成功.

**善后:** 点 Delete branch 删掉用完的 branch.

**关键概念:**

- `Pull Request`: 把 branch 改动合并进目标 branch 的请求.
- `code review`: 合并前由他人审阅改动的过程.
- `merge conflict`: 两处改动冲突, 需人工决定保留哪个.
