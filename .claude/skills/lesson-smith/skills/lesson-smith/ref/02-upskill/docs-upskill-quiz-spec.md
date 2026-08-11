<!--
本文件是 docs/upskill/03-upskill-quiz.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

定性: 这是 quiz 的薄壳, 由 lesson-smith-upskill-forge 生成, 给 upskill-quiz skill 消费. 它本身不出题: 题目, 参考回答, 深入解读全在那个 quiz mini task 的 README 里 (规范见 [upskill-examples-quiz-readme-spec.md](upskill-examples-quiz-readme-spec.md)). 这份 doc 只做两件事: 指出题库在哪, 以及记录人类对考法的自定义要求.

适用范围: upskill 类型 repo 的 docs/upskill/03-upskill-quiz.md. 这是给 AI/skill 看的元文件, 人类读的是真正的教程正文 (examples 下的 quiz 题库真身也是给人读的), 不读这份薄壳; 所以它产出内容全英文, 不走 cn-first 铁律. 因此下面的正文模板本身就是英文的. 注意区分: 题库真身 (examples 下那个 mini task) 是人类看的, 走 cn-first 双语; 这份指针薄壳是 skill 看的, 全英文.

内容分两部分, 正文就是这两部分:

第一部分, 题库位置: 用 markdown 链接指向那个 quiz mini task 的 README (即题库真身), 让 upskill-quiz skill 知道去哪读题. 这部分容易, forge 扫一遍 examples 找到那个 quiz 环节就能填. 一句话说清是哪个 example.

第二部分, 考法自定义 (可选): 人类在这里写对 upskill-quiz 行为的特殊要求和说明. 例如: 默认抽几道, 是否按主题分组考, 哪些题偏重, 用什么口吻, 有没有时间限制, 及格线怎么算等. 没有特殊要求就写一句 no special requirements, use the skill default.

写作原则:
- 不要把题目本身复制到这里, 避免和题库真身两处漂移; 这里只放指针和自定义说明.
- 指向文件用 markdown 链接, 定位用 header 或关键字, 不用 line no.
-->

# [Course Name] Quiz

> The upskill-quiz skill uses this doc to find the question bank and learn how to run the quiz. The questions themselves are not here; they live in the example this points to.

## 1. Question Bank Location

The bank is the README of the quiz mini task: [examples/NN-prove-i-get-it](../../examples/NN-prove-i-get-it/README.md). It holds [N] questions covering the key points of the whole course.

## 2. Quiz Customization

[The human's special requirements for how upskill-quiz should run. If none, write the line below.]

No special requirements, use the upskill-quiz skill default.
