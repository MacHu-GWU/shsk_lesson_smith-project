# 索引 Task 的 README 规范, 中文版

**适用范围**: `examples/01-overview/README-cn.md`, 也就是 examples 下**固定排在最前面那个索引 Task** 的教学正文. readup, upskill, showcase 三类都有这个 Task; evolve 没有 examples 这一层, 不适用.

**配套骨架**: [overview-readme-cn-template.md](overview-readme-cn-template.md).

**只管中文版**: 英文版另有一套, 属于多语种模块, 现在还没做.

---

## 1. 它是什么, 以及为什么它是一个 Task

它给刚进来的人一张地图: 这门课有哪些 Task, 它们是怎么分组的, 该按什么顺序读.

**它不是教学文档**, 教程在各个 Task 自己的 README 里.

早先这份东西放在 `examples/README-cn.md`, 不是 Task, 没有 TICKET, 也没有 frontmatter. 那个位置制造了两个麻烦: 它和根目录那份 README 界线不清 (两个都像 "总览"), 而且它是整个 examples 下唯一一个不成对的孤儿文件. 所以现在把它降格成 examples 里的第一个普通 Task, **一切都走 Task 的规矩**, 没有例外可记.

**什么时候写**: 不是第一个写的. 主干内容 (02 往后) 全部写完并统稿之后, 回头补开头结尾时才写它. 地图只能在路修完之后画.

---

## 2. 它和 SYLLABUS 的区别

这是这份 spec 的核心, 也是它存在的唯一理由.

| | SYLLABUS | 索引 Task |
| :--- | :--- | :--- |
| 谁产出 | 脚本生成 | 人手写 |
| 形态 | 平铺罗列, 一个 Task 一段, 谁都不挨着谁 | 按主题聚成几个 group, 有分类和递进 |
| 读起来是 | "这里有 8 个东西" | "这门课分成这么几块, 每块解决什么" |

两者海拔和目的都不同, 所以并存不冲突. **写的时候别把它写成 SYLLABUS 的翻版**, 一条条平铺列下来就等于白写.

---

## 3. 结构

三段, 不复杂:

- **开头一段**: 这门课是什么, 下面大致分成哪几块. 给读者一张地图.
- **中间若干个 group**: 每个 group 一个编号 H2, 标题是这一组的主题. H2 下先一句话点出这组在讲什么, 再用 bullet 列出该组的 Task, 每条给出链接和一句话说明.
- **结尾一段小结**: 把这几块串起来, 说清读完整条线能得到什么.

**group 的数量与主题都随课程而定**, template 里的分组和用词只是示例.

---

## 4. 链接怎么写

它现在住在 `examples/01-overview/` 里面, 所以指向兄弟 Task **要往上一级**:

```text
[02-title](../02-title/README-cn.md)
```

这是从旧的 `examples/README-cn.md` 搬过来时最容易漏的一处: 旧位置写的是 `02-title/README-cn.md`, 少了 `../` 就全是死链.

---

## 5. 其余照 Task README 的通用规矩

H1 字符集, frontmatter `description` 的形态与长度, 编号与分隔线, 术语保留英文, 都照 [03-task-readme-spec](../03-task-readme-spec/task-readme-cn-spec.md), 这里不重复.

只有一处要特别说: 它的 `description` 是**这个索引 Task 的承诺**, 写 "读完你知道这门课怎么走", 不是把整门课的介绍搬过来 (那是 README-ORIGINAL 的活).

---

## 6. 交付前自检

- 各 group 的 Task 加起来, 覆盖了 `examples/` 下除它自己以外的全部 Task, 一个不漏
- 指向兄弟 Task 的链接都带 `../`
- 读起来是分组和递进, 不是平铺罗列
- description 写的是 "读完你知道这门课怎么走", 没有和 README-ORIGINAL 撞车
