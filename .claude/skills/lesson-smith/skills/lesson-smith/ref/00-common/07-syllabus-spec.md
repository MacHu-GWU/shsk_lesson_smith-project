# SYLLABUS 格式规范

`docs/tasks/SYLLABUS-cn.md` 是整门课的 Task 清单索引. 每个语种一份, 英文那份是 `SYLLABUS.md` (当前是个空壳, 见第 5 节).

**它不手写.** 由 `lesson-smith sync` 自动生成, 所以这一份没有配套 template: 没人需要复制一个骨架去填. 这里写清它长什么样, 只是为了让人和 lint 都能判断生成出来的东西对不对.

适用范围: 四类 repo 都有.

---

## 1. 结构

- 以 `# Syllabus` 开头. **这个 H1 逐字节写死**, 不随语种变.
- 之后每个 Task 一段: 一个 H2 加一段描述, 中间空一行.
- H2 就是那个 branch 的目录名, **全小写, 原样输出, 不做任何大小写转换**.
- Task 按 branch 序号升序排列, 序号必须从 01 连续, 不许有缺口.
- 段与段之间空一行.

---

## 2. 内容来源

每段描述**直接取自**对应 Task `README-cn.md` 顶部 frontmatter 的 `description`, 原样输出, 不改写.

所以 SYLLABUS 里出现的任何内容问题, 根都在那份 README 的 description 上, 改那边然后重跑 sync, 不要改这里. description 本身的约束见 [01-repo-layout.md](01-repo-layout.md) 第 6 节.

---

## 3. lint 查什么

- H1 逐字节等于 `Syllabus`.
- H2 那组 branch 名与 `docs/tasks/` 下的目录**同集合且同顺序**.
- 序号连续.
- 每段描述是一行, 非空, 且**逐字等于**对应 README 的 description.

最后一条是最常报的: 改过某份 README 的 description 却没重跑 sync.

---

## 4. 生成

由 `shsk_lesson_smith` package 的 `lesson-smith sync` 直接字符串拼接生成, 不引第三方模板引擎. 怎么跑见 [09-ship-spec.md](09-ship-spec.md).

---

## 5. 英文版

**sync 不认那个按语种开关**, 那是 lint 的东西. sync 对每个支持的语种都生成一份, 所以 `SYLLABUS.md` (英文) 现在也会被生成出来.

但英文 Task README 目前是留空的占位文件, 取不到 `description`, 所以生成出来的英文 SYLLABUS 是**一个只有骨架没有内容的壳**: `# Syllabus` 在, 各个 `## branch-name` 也在, 每段描述是空的.

三件事要知道:

- **这不是 bug, 也不用手动清理.** 它是 "英文文件存在但留空" 这条约定的自然结果.
- **lint 不检查它.** 英文那一档是关的, 所以空描述不会报错; 换成开着就会当场报 "has no description line".
- **它会自愈.** 哪天英文 README 被填上, 重跑一次 sync 那份 SYLLABUS 就自动有内容了, 不需要另外做什么, 也不需要改这份规范.

---

## 6. 生成出来长这样

```markdown
# Syllabus

## 01-branch-name

从零开始讲清 X 的核心概念与常用操作, 覆盖 DataFrame, lazy evaluation 等关键机制, 通过若干个 self-contained 的小例子边讲边练. 学完你能独立写出基础的数据处理代码, 并说清一段程序为什么慢.

## 02-branch-name

在前一个 Task 的基础上, 引入 join, shuffle, partitioning 等进阶主题, 结合一个贴近真实业务的场景动手实践. 学完你能定位常见的性能瓶颈, 并做出针对性的优化.
```
