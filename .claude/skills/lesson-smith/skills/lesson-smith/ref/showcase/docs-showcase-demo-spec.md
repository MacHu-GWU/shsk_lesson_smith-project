<!--
本文件是 docs/showcase/04-showcase-demo.md 的规范加可直接套用的模板. 这段顶部注释只服务于创作; 产出真正的 doc 时, 把整段注释删掉, 只留后面的正文.

本文件独立成篇, 不引用 ref/upskill/ 下任何文件; 需要引用时只引 ref/ 根目录的通用 spec.

定性: 这是 demo 的薄壳, 由 lesson-smith-showcase-forge 生成, 给 showcase-demo skill 消费. 它本身不写故事: 完整的讲故事底稿 (七幕主线, 常见追问, 按听众裁剪) 全在那个 demo mini task 的 README 里 (规范见 showcase-examples-demo-readme-spec.md). 这份 doc 只做三件事: 指出底稿在哪, 记下默认故事主线 (七幕) 好让 skill 不必每次重推, 以及记录人类对排练方式的自定义要求.

适用范围: showcase 类型 repo 的 docs/showcase/04-showcase-demo.md. 这是给 AI/skill 看的元文件, 人类读的是真正的底稿 (examples 下那个 how-i-build-this mini task, 是给人读的双语正文), 不读这份薄壳; 所以它产出内容全英文, 不走 cn-first 铁律. 因此下面的正文模板本身就是英文的. 注意区分: 底稿真身 (examples 下那个 mini task) 是人类看的, 走 cn-first 双语; 这份指针薄壳是 skill 看的, 全英文.

内容分三部分, 正文就是这三部分:

第一部分, 底稿位置: 用 markdown 链接指向那个 demo mini task 的 README (即讲故事底稿真身), 让 showcase-demo skill 知道去哪读故事. forge 扫一遍 examples 找到最后那个 how-i-build-this 就能填.

第二部分, 默认故事主线: 把七幕主线极简记一遍 (每幕一句), 让 skill 手里有默认骨架. 默认主线讲的是 "我如何用 AI 快速把一个技能学会并投入实战" 这套方法论 (既是作品叙事, 又证明 AI 协作能力). 若这个 repo 的底稿偏离了默认主线, 在这里一句话说明偏离在哪; 没偏离就写 uses the default seven beat arc.

第三部分, 排练自定义 (可选): 人类在这里写对 showcase-demo 行为的特殊要求. 例如: 目标听众默认是谁, 面试时长偏好, 哪几幕要重点练, 追问要不要更狠等. 没有特殊要求就写一句 no special requirements, use the skill default.

写作原则:
- 不要把整份底稿复制到这里, 避免和底稿真身两处漂移; 这里只放指针, 默认骨架和自定义说明.
- 指向文件用 markdown 链接, 定位用 header 或关键字, 不用 line no.
-->

# [Course Name] Demo

> The showcase-demo skill uses this doc to find the story script and learn how to rehearse it. The full script (the seven beats, the follow-up questions, the audience tailoring) is not here; it lives in the example this points to.

## 1. Story Script Location

The script is the README of the demo mini task: [examples/NN-how-i-build-this](../../examples/NN-how-i-build-this/README.md). It is the first-person story of how this repo was built and learned.

## 2. Default Story Arc

The story defaults to the seven beat arc (how I used AI to learn a skill fast and put it to work):

1. Found a skill worth investing a week to learn.
2. Had AI research the authoritative material for it.
3. Distilled that into a super expert AI agent skill.
4. Had the expert design a one week syllabus (became examples/README).
5. Turned each syllabus point into a readable, hands-on example (became the examples).
6. Learned the whole course with AI alongside.
7. Put the skill to work on a real problem.

[If this repo's script deviates from the default, note where in one line; otherwise write: uses the default seven beat arc.]

## 3. Demo Customization

[The human's special requirements for how showcase-demo should run. If none, write the line below.]

No special requirements, use the showcase-demo skill default.
