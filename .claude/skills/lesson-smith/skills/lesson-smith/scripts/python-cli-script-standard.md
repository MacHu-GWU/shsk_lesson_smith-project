# 纯标准库 Python CLI 脚本规范

> 本目录下所有只依赖 Python 标准库的可执行 CLI 脚本, 都遵循这份规范. 目的是让脚本既能被 agent 或人从命令行直接调用, 又能被 import 后单元测试, 结构一眼看清.

---

## 1. 适用范围

只依赖 Python stdlib, 不引任何第三方包的命令行脚本. 这类脚本承担确定性的机械操作 (建目录, 校验, 汇总等), 由上层 skill 或 agent 通过命令行调用.

---

## 2. 两层函数结构

每个脚本至少有两个固定的函数. 底层 `_main` 承载核心逻辑, 顶层 `main` 负责命令行解析. 两者之间职责清晰: `_main` 不关心命令行长什么样, `main` 不关心业务逻辑怎么做. 更细的逻辑可以再拆成模块级辅助函数, 但这两层是固定骨架.

---

## 3. 底层核心函数 `_main`

`_main` 的签名接收已经解析好, 带类型标注的参数, 例如 `def _main(target: Path, quiet: bool = False) -> int`.

脚本的主 docstring 写在这里, 说明它到底做什么. 核心逻辑, 以及读写文件, 打印结果这类副作用, 都在这里. 函数返回一个 int 作为 exit code.

因为它的入参是干净的类型化值, 不掺命令行细节, 所以测试可以直接 `import` 后调用 `_main(...)`, 不必走命令行.

---

## 4. 顶层解析函数 `main`

`main` 的签名是 `def main(argv: list[str] | None = None) -> int`. 它用 argparse 从 `sys.argv` 解析参数, 把命令行解析成正确的 key value, 再以关键字参数调用 `_main`, 并原样返回 `_main` 的结果.

`argv` 默认 `None`, 这样 argparse 会去读 `sys.argv`; 显式传入一个列表则方便在测试里模拟命令行. `main` 本身不写业务逻辑, 只做参数解析和转交.

---

## 5. 一律用 `--arg_name` 关键字风格

所有参数都用明显的 `--arg_name` 关键字风格, 不用 positional 参数. flag 名与 `_main` 的参数名保持一致, 都用下划线, 这样从命令行到函数入参的映射一目了然.

必填输入用 `required=True`. 布尔开关用 `action="store_true"`. 可选值给一个 `default`. 每个参数都写 `help`.

---

## 6. 入口与 exit code

文件末尾固定这一行.

```python
if __name__ == "__main__":
    sys.exit(main())
```

exit code 语义统一为: `0` 成功, `1` 运行失败 (业务层面的错误), `2` 用法错误 (argparse 在参数不合法时自动返回).

---

## 7. 其它约定

文件顶部加 `from __future__ import annotations`, 所有函数补全 type hint.

只用标准库, 不引第三方依赖.

docstring 和错误信息用英文, 因为脚本面向机器和跨环境运行. 错误信息打到 stderr, 正常输出打到 stdout.

---

## 8. 骨架示例

```python
#!/usr/bin/env python3
"""One line module summary."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _main(target: Path, quiet: bool = False) -> int:
    """Do the real work. The main docstring and core logic live here.

    Returns an exit code: 0 on success, 1 on failure.
    """
    if not target.exists():
        print(f"ERROR: {target} not found", file=sys.stderr)
        return 1
    if not quiet:
        print(f"Processing {target}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="example_tool",
        description="One line description of the tool.",
    )
    parser.add_argument("--target", type=Path, required=True, help="path to process")
    parser.add_argument("--quiet", action="store_true", help="suppress normal output")
    args = parser.parse_args(argv)
    return _main(target=args.target, quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
```
