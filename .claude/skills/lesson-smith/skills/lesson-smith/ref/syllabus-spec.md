<!--
SYLLABUS 格式规范. 正文是脚本产出的样例; 这段注释只服务于理解规范, 脚本自动生成 SYLLABUS 时本来就不会带上它.

docs/tasks/SYLLABUS.md 是整门课的 Task 清单索引, 由 scripts/lesson_smith.py sync 自动生成, 不手写. 每个语种一份: 英文是 SYLLABUS.md, 其他语种是 SYLLABUS-<lang>.md.

结构: 以 # Syllabus 开头. 之后每个 Task 一段, 二级标题就是这个 branch 的目录名 (全小写, 原样输出, 不做任何大小写转换), 空一行再跟一段描述. Task 按 branch 序号升序排列, 段与段之间空一行.

内容来源: 每段描述直接取自对应 Task 的 README.md (或 README-<lang>.md) 顶部 frontmatter 的 description, 原样输出, 不改写. description 本身的约束见 repo-layout.md 第 4 节.

branch name: 全小写, 连字符分隔 (例如 01-branch-name). 全小写加连字符是为了减少认知负担, 不用记大小写规范, 更容易保持统一.

生成: 由 scripts/lesson_smith.py 用 Python 标准库直接字符串拼接生成, 不引第三方模板引擎.
-->

# Syllabus

## 01-branch-name

从零开始讲清 X 的核心概念与常用操作, 覆盖 DataFrame, lazy evaluation 等关键机制, 通过若干个 self-contained 的小例子边讲边练. 学完你能独立写出基础的数据处理代码, 并说清一段程序为什么慢.

## 02-branch-name

在前一个 Task 的基础上, 引入 join, shuffle, partitioning 等进阶主题, 结合一个贴近真实业务的场景动手实践. 学完你能定位常见的性能瓶颈, 并做出针对性的优化.
