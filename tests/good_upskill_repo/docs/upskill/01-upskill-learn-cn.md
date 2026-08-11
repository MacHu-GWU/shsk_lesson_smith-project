# GitHub 基础协作 学习索引

> 这门课要学的东西有哪些, 分别在哪, 按什么顺序过. upskill-learn-cn skill 就是按这份索引带着你往前走的.

## 1. 学习素材

这是一门边读边做的课, 教程本身就是要学的东西, 全部在 `examples/` 那条渐进序列里. 没有另外的源代码, 配置或旁支文档要学.

- 引导路径之外没有额外素材, 全在 [examples/](../../examples/) 下那几个 Task 里. 你唯一要从外面带进来的是自己的 GitHub 账号, 直接在浏览器里练.
- 有个坑: 根目录的 [mise.toml](../../mise.toml) 只是给测试用的项目根标记, 不是真的工具链. 这门课没有 `mise` task 要跑, 别去那里找 build 或 setup 命令.

## 2. 引导路径

`examples/01, 02 ...` 这条渐进序列就是要走的路. 整条线分成三段:

- **打地基**: examples/02 到 examples/03, 从零建一个 repository, 再让每次改动落成一个干净的 commit. 覆盖 repository, commit, README, public 与 private, web editor, commit message, commit history.
- **协作主线**: examples/04 到 examples/05, 这是整门课的核心. 先用 branch 把没写完的工作隔离出去, 再通过一次经过 review 的 Pull Request 合并回 main. 覆盖 branch, 默认分支 main, Pull Request, code review, merge, 删掉合并完的 branch, 以及 merge conflict.
- **收尾**: examples/07 回望整条闭环, 确认达标, 并给出继续进阶的方向与搜索关键字.

examples/06 那个自测 Task 不在带学路径里, 它归 `upskill-quiz-cn` 管.

另见 [索引 Task](../../examples/01-overview/README-cn.md) 与 [SYLLABUS](../tasks/SYLLABUS-cn.md).
