<!--
本文件是 docs/upskill/03-upskill-quiz.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

定性: 这是 quiz 的薄壳, 由 lesson-smith-upskill-forge 生成, 给 upskill-quiz skill 消费. 它本身不出题: 题目, 参考回答, 深入解读全在那个 quiz mini task 的 README 里 (规范见 [examples-quiz-spec.md](examples-quiz-spec.md)). 这份 doc 只做两件事: 指出题库在哪, 以及记录人类对考法的自定义要求.

适用范围: upskill 类型 repo 的 docs/upskill/03-upskill-quiz.md. 语言遵循创作铁律 (先写 cn, 定稿后 translate-to-en), 或按 repo 的语言约定.

内容分两部分, 正文就是这两部分:

第一部分, 题库位置: 用 markdown 链接指向那个 quiz mini task 的 README (即题库真身), 让 upskill-quiz skill 知道去哪读题. 这部分容易, forge 扫一遍 examples 找到那个 quiz 环节就能填. 一句话说清是哪个 example.

第二部分, 考法自定义 (可选): 人类在这里写对 upskill-quiz 行为的特殊要求和说明. 例如: 默认抽几道, 是否按主题分组考, 哪些题偏重, 用什么口吻, 有没有时间限制, 及格线怎么算等. 没有特殊要求就写一句 "无特殊要求, 按 skill 默认行为考" .

写作原则:
- 遵循 markdown-style 和 chinese-english-punctuation 两个 Agent Skill.
- 不要把题目本身复制到这里, 避免和题库真身两处漂移; 这里只放指针和自定义说明.
- 指向文件用 markdown 链接, 定位用 header 或关键字, 不用 line no.
-->

# [课程名] Quiz

> upskill-quiz skill 靠这份 doc 找到题库并了解考法. 题目本身不在这里, 在下面指向的那个 example 里.

## 1. 题库位置

题库是那个 quiz 环节 mini task 的 README: [examples/0X-quiz-title](../../examples/0X-quiz-title/README.md). 一共 [N] 道题, 覆盖整门课的关键知识点.

## 2. 考法自定义

[人类对 upskill-quiz 考法的特殊要求. 没有就写下面这句.]

无特殊要求, 按 upskill-quiz skill 的默认行为考.
