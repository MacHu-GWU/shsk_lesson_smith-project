---
description: "一套面试式自测题, 检验你对整门课是否知其然知其所以然."
---

# GitHub 基础协作 自测题

> 本文档是对整门课学到的东西的一次验证, 看你是否不仅知其然, 更知其所以然. 把每道题当成面试官当面问你, 先自己答, 再对照参考回答与深入解读.

## 1. Repository 是什么

**问题**

> 用一句话说清 repository 是什么, 它和电脑上一个普通文件夹有什么不一样?

**考察点**

> 看你是否把 repo 理解成 "带完整历史的项目容器", 而不只是一堆文件.

**参考回答**

> repository 是一个项目的家, 装着这个项目的所有文件, 以及每个文件从头到尾的每一次改动记录. 普通文件夹只有文件的当前状态, repo 还额外保存了完整的变更历史.

**深入解读**

> 关键区别在 "历史". 普通文件夹里你改了文件, 旧版本就没了; repo 把每次改动都记成一个 commit 存起来, 随时能回看甚至回退. 见 [01-create-repo](../01-create-repo/README-cn.md) 里讲 repository 概念的部分.

---

## 2. Commit 是什么

**问题**

> commit 是什么? 为什么说它像游戏存档?

**考察点**

> 看你是否理解 commit 是 "一次带说明的快照", 而不只是保存文件.

**参考回答**

> 一个 commit 是项目在某一刻的一次快照, 附带一句说明这次改了什么. 像游戏存档一样, 它把当前状态记下来, 以后可以回到这个点.

**深入解读**

> 存档的比喻点出两件事: 一是 commit 是离散的时间点 (不是连续自动保存), 二是你可以回到任意一个存档点. 每个 commit 都有作者, 时间和一句 message. 见 [01-create-repo](../01-create-repo/README-cn.md) 里把 commit 比作存档的部分.

---

## 3. 建 repo 时为什么勾选 Add a README

**问题**

> 在 GitHub 上新建 repository 时, 勾选 Add a README file 有什么用? 不勾会怎样?

**考察点**

> 看你是否理解 README 的作用, 以及空 repo 的初始状态.

**参考回答**

> 勾选后 GitHub 会自动建一个 README.md 并替你做第一个 commit, 于是 repo 一建好就非空, 能直接在网页上编辑. 不勾的话 repo 是空的, GitHub 会给你一屏命令行指引, 对新手不友好.

**深入解读**

> README 是别人打开你 repo 第一眼看到的介绍页, GitHub 会把它渲染在主页正中间. 对这门纯网页的课来说, 勾上 README 还有个实际好处: 让你有个文件可以马上练习编辑. 见 [01-create-repo](../01-create-repo/README-cn.md) 里讲初始化 README 的部分.

---

## 4. public 和 private 的区别

**问题**

> 建 repo 时选 public 还是 private, 影响的是什么?

**考察点**

> 纯知识点, 看你知不知道可见性的含义.

**参考回答**

> public 的 repo 任何人都能看到内容, private 只有你和你邀请的人能看. 代码本身的功能不受影响, 区别只在谁能访问.

**深入解读**

> 这门课建议用 public, 因为后面 Pull Request 的 review 过程在 public repo 里更直观可见, 也方便当作作品展示. 见 [01-create-repo](../01-create-repo/README-cn.md) 里对比 public 与 private 的部分.

---

## 5. 为什么每次改动都要 commit, 而不是攒着一起存

**问题**

> 为什么建议每完成一个小改动就 commit 一次, 而不是改一大堆再一次性提交?

**考察点**

> 看你是否理解小步 commit 对 "可回退, 可追溯" 的价值.

**参考回答**

> 小步 commit 让历史清晰: 每个 commit 只做一件事, 出问题时容易定位到是哪次改动引入的, 也容易只回退那一步. 一次提交一大堆, 历史就成了一团, 难查难退.

**深入解读**

> commit 的粒度直接决定历史的可读性. 一个理想的 commit 是 "一件语义上完整的小事". 见 [02-edit-files](../02-edit-files/README-cn.md) 里讲 commit 记录改动的部分.

---

## 6. Commit message 为什么重要

**问题**

> commit message 写得好不好, 到底影响谁? 举例说明一条好 message 和一条差 message.

**考察点**

> 看你是否明白 message 是写给未来的人 (包括自己) 看的.

**参考回答**

> commit message 是写给未来的读者看的, 让人不打开 diff 也能大致知道这次改了什么. 好 message 如 Add install steps to README; 差 message 如 update 或 asdf, 事后完全看不出改了啥.

**深入解读**

> 半年后你或队友翻历史找 "哪次引入了这个改动", 靠的就是 message. 一句清楚的 message 是最省事的沟通. 见 [02-edit-files](../02-edit-files/README-cn.md) 里讲 commit message 的部分.

---

## 7. 怎么在网页上新建一个文件

**问题**

> 不用命令行, 完全在 GitHub 网页上, 怎么给 repo 新加一个文件?

**考察点**

> 纯操作题, 看你是否真的动手做过.

**参考回答**

> 在 repo 主页点 Add file 下拉, 选 Create new file, 输入文件名和内容, 再往下点 Commit changes 就建好了.

**深入解读**

> 网页端的 web editor 让你完全不碰 git 也能增删改文件, 每次 Commit changes 就等于做了一个 commit. 见 [02-edit-files](../02-edit-files/README-cn.md) 里讲用 web editor 新建文件的部分.

---

## 8. Commit history 是什么, 怎么看

**问题**

> 在哪里能看到一个 repo 的所有 commit? 这个列表能告诉你什么?

**考察点**

> 看你是否知道历史在哪, 以及它的用途.

**参考回答**

> 在 repo 里点 commits (通常在文件列表上方, 显示 commit 数量的地方) 就能看到从最早到最新的每一次 commit, 包括作者, 时间和 message. 它告诉你这个项目一路是怎么演变过来的.

**深入解读**

> commit history 是项目的时间线, 点开任意一个 commit 还能看到那次具体改了哪些行. 这就是版本控制的核心价值: 一切改动有据可查. 见 [02-edit-files](../02-edit-files/README-cn.md) 里讲 commit history 的部分.

---

## 9. Branch 是什么

**问题**

> 用一个类比说清 branch 是什么.

**考察点**

> 看你是否理解 branch 是 "隔离的平行工作线".

**参考回答**

> branch 像是把整个项目另存了一个副本, 你在副本上随便改, 原来的主线一点不受影响. 改好了再合回去, 改砸了直接丢掉副本.

**深入解读**

> 重点是 "隔离": branch 让未完成或有风险的改动待在自己的线上, 不污染大家共享的稳定版本. 见 [03-git-branch](../03-git-branch/README-cn.md) 里用另存副本类比 branch 的部分.

---

## 10. 默认分支 main 是什么

**问题**

> main 这个 branch 有什么特殊? 为什么不建议直接在 main 上改?

**考察点**

> 看你是否理解 main 是团队共享的稳定主干.

**参考回答**

> main 是 repo 的默认分支, 代表项目当前的正式, 稳定版本, 是所有人共享的基准. 直接在 main 上改, 相当于把没验证过的东西塞进大家都在用的版本, 风险高.

**深入解读**

> 正因为 main 是共享基准, 现代协作的规矩才是 "不直接动 main, 改动先在 branch 上做". 见 [03-git-branch](../03-git-branch/README-cn.md) 里讲默认分支的部分.

---

## 11. 为什么协作离不开 branch

**问题**

> 如果一个五人团队都直接往 main 上提交, 会出什么问题? branch 怎么解决?

**考察点**

> 看你能否把 branch 的价值连接到真实协作场景.

**参考回答**

> 都往 main 上提交, 别人没写完的, 有 bug 的代码会互相干扰, main 随时可能是坏的. branch 让每个人在自己的线上干活, 完成并验证后再合并, main 始终保持可用.

**深入解读**

> branch 把 "正在进行的工作" 和 "稳定的成品" 在物理上分开, 这是多人协作能并行推进的前提. 见 [03-git-branch](../03-git-branch/README-cn.md) 里讲为什么协作需要分支的部分.

---

## 12. 怎么在网页上建一个 branch

**问题**

> 完全在 GitHub 网页上, 怎么新建一个 branch 并切换过去?

**考察点**

> 纯操作题.

**参考回答**

> 在 repo 主页左上角的 branch 下拉框里输入一个新名字, 点 Create branch, 就基于当前分支建出并切到了新 branch.

**深入解读**

> 新 branch 一开始是当前分支的完整副本, 之后你在它上面的 commit 都只留在这条线上. 见 [03-git-branch](../03-git-branch/README-cn.md) 里讲在 web 上建 branch 的部分.

---

## 13. 在 branch 上改动会影响 main 吗

**问题**

> 你切到一个新 branch 改了文件并 commit, 此时去看 main, main 上的文件变了吗? 为什么?

**考察点**

> 看你是否真正理解 branch 的隔离性.

**参考回答**

> 不会变. 你的 commit 只落在当前 branch 这条线上, main 还停在你分出去之前的状态, 直到你显式把改动合并回 main.

**深入解读**

> 这正是 branch 的意义所在: 隔离. 只有 merge 这个动作才会把 branch 的改动带回 main. 见 [03-git-branch](../03-git-branch/README-cn.md) 里讲改动不影响主干的部分.

---

## 14. Pull Request 是什么

**问题**

> Pull Request 是什么? 名字里的 request 有什么讲究?

**考察点**

> 看你是否理解 PR 是 "请求合并", 把改动和采纳分成两步.

**参考回答**

> Pull Request 是一个 "请把我这个 branch 的改动合并进目标分支" 的请求. request 表示它是请求不是命令: 提出请求和真正合并是两件事, 中间隔着一次审阅.

**深入解读**

> 把 "改动" 和 "正式采纳改动" 拆开, 正是 PR 的核心设计: 中间那道缝隙留给 review 和讨论. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里讲 Pull Request 是什么的部分.

---

## 15. 一个 PR 页面上有哪三样东西

**问题**

> 打开一个 PR 页面, 主要能看到哪三个部分, 各是干什么的?

**考察点**

> 看你是否熟悉 PR 的构成.

**参考回答**

> diff (你的 branch 相对目标改了哪些行, 红删绿增), conversation (讨论区, 可逐行评论), 以及 merge 按钮 (讨论通过后一键合并).

**深入解读**

> 这三样把一次改动的 "内容, 讨论, 决定" 集中在一个可追溯的页面上, 这也是为什么 PR 成了团队沟通的载体. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里列 PR 三个区域的部分.

---

## 16. Code review 解决什么问题

**问题**

> 合并前让别人 review 一遍, 到底带来哪些好处?

**考察点**

> 看你能不能说出 review 的实际价值, 而不是当成走过场.

**参考回答**

> 三个好处: 早点抓出作者自己没发现的 bug; 让知识不只装在一个人脑子里; 给改动留下可追溯的讨论记录. 它是几乎所有严肃项目的默认关卡.

**深入解读**

> review 的价值在个人练习里不明显, 但在团队里是质量和知识传递的保障. 半年后 "这行为什么这么写" 的答案就在 PR 对话里. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里讲 code review 的部分.

---

## 17. 怎么开一个 Pull Request

**问题**

> branch 上有了改动之后, 在网页上怎么开一个 PR?

**考察点**

> 纯操作题.

**参考回答**

> repo 主页通常会弹出 Compare & pull request 按钮, 点它; 或走 Pull requests 标签点 New pull request. 确认方向是 base main <- compare 你的 branch, 填好标题和描述, 点 Create pull request.

**深入解读**

> 方向 (base <- compare) 是关键: base 是要被合并进去的目标 (通常 main), compare 是你带改动的 branch. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里讲动手开 PR 的部分.

---

## 18. Merge 之后 main 上会发生什么

**问题**

> 点了 Merge pull request 并确认之后, 你怎么验证改动真的进了 main?

**考察点**

> 看你是否理解 merge 的结果, 以及怎么确认.

**参考回答**

> 合并后页面会显示 successfully merged. 切回 repo 主页, 把 branch 下拉框切到 main, 打开对应文件, 就能看到 branch 上的改动真的出现在 main 上了.

**深入解读**

> merge 是把 branch 的 commit 正式并入 main 的动作, 之后这些改动成为项目正式版本的一部分. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里讲 merge 的部分.

---

## 19. 合并后为什么要删掉 branch

**问题**

> PR 合并成功后 GitHub 会提示 Delete branch. 删掉它安全吗? 为什么要删?

**考察点**

> 看你是否理解删 branch 删的是什么.

**参考回答**

> 安全. branch 的改动已经进了 main, 删掉的只是这条 "工作线" 的标签, 改动本身安全地留在 main 的历史里. 删掉是为了让 branch 列表保持整洁, 一个 branch 对应一件事, 事做完就收掉.

**深入解读**

> 需要的话删掉的 branch 之后还能恢复, 所以不用担心丢东西. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里讲合并后删 branch 的部分.

---

## 20. Merge conflict 是什么

**问题**

> 什么情况下会出现 merge conflict? 遇到了该怎么理解它?

**考察点**

> 看你是否认得 conflict, 并且不怕它.

**参考回答**

> 当两个 branch 改了同一个文件的同一处, 且改得不一样时, 就会出现 merge conflict. 它不是错误, 只是 GitHub 说 "这里有两个打架的版本, 我不敢替你猜, 你来决定留哪个".

**深入解读**

> 解决它就是人工挑一下留哪个再确认; 只要各改各的文件或及时同步 main, conflict 就很少见. 深入解决是以后的话题. 见 [04-merge-branch](../04-merge-branch/README-cn.md) 里讲 merge conflict 的部分.
