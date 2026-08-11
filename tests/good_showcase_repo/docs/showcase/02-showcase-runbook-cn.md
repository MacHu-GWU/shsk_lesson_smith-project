# GitHub 基础协作 跑起来

> 这门课怎么跑起来: 开始之前要做什么 setup, 推进过程中会遇到哪些环境, 命令与操作步骤. 跑不起来先看这里.

## 1. 环境准备

开始 examples 之前的一次性 setup. 这门课不装任何东西, 也不碰命令行, 一切都在浏览器里的 github.com 上完成.

- 前置要求: 一个 GitHub 账号 (在 github.com 免费注册) 和一个现代浏览器. 不用装软件, 不用装 git, 不用命令行. 注意根目录的 [mise.toml](../../mise.toml) 只是给测试用的项目根标记, 这里没有 `mise` task 要跑.
- 首次 setup:
1. 在 github.com 注册或登录一个 GitHub 账号.
2. 就这些, 剩下的每个 Task 会带着你在浏览器里做.

## 2. 推进中的操作

整体节奏: 每个 Task 都是读 README 然后直接在浏览器的 github.com 上照着做. 没有 `cd`, 没有环境变量, 没有本地命令, 也没有服务要起; 只有下面两处要跳出常规.

值得单独说的几步:

- 开始 examples/02 之前: 你得有一个能登录的 GitHub 账号, 这是整门课唯一的前置条件. 先去 github.com 注册, 之后所有操作都在你自己的账号上做.
- 到 [examples/05-merge-branch](../../examples/05-merge-branch/README-cn.md) 时: repo 主页上那个 `Compare & pull request` 横幅不是每次都出现. 没有的话, 从 `Pull requests` 标签页点 `New pull request` 手动开, 并确认方向读起来是 `base: main <- compare: your-branch`.

## 3. 常见卡点

- 在 web editor 里打字不会自动保存, 要点了 `Commit changes` 才算数; 改动只有在 commit 之后才真正进 repo. 见 [03-edit-files 里讲 Commit changes 的那段](../../examples/03-edit-files/README-cn.md).
- merge conflict 不是报错: 它只是说两条 branch 改了同一个文件的同一处, GitHub 要人来选. 见 [05-merge-branch 里讲 merge conflict 的旁注](../../examples/05-merge-branch/README-cn.md).
