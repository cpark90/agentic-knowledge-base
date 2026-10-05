---
id: https://agentic-knowledge-base.dev/id/chunk/ed759600-6622-448e-be33-8fab9ae6b4eb
type: artifact
level: executable
title_ko: 함수 module_head_end (tools/extract.py)
title: function module_head_end in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `module_head_end(tree, starlark)` 다. 모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def module_head_end(tree: ast.Module, starlark: bool = False) -> int:
    """모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지. 그 뒤가 첫 구역이다.

    Starlark 는 `load(...)` 가 import 자리이고 docstring 이 `load` 뒤에 올 수 있다(`defs/kb.bzl`) — 머리 안의 첫 문자열
    식을 docstring 으로 받는다.
    """
    def is_load(node) -> bool:  # Starlark 의 `load(...)` 문 — 모듈 머리에서 import 의 자리다
        return (isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name)
                and node.value.func.id == "load")

    end, doc_seen = 0, False
    for node in tree.body:
        is_doc = isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str)
        if is_doc and (end == 0 or (starlark and not doc_seen)):
            doc_seen = True
        elif starlark and is_load(node):
            pass
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            pass
        elif isinstance(node, ast.Try) and all(isinstance(n, (ast.Import, ast.ImportFrom)) for n in node.body):
            pass
        else:
            break
        end = node.end_lineno
    return end
```
<!-- 인용 끝 -->
