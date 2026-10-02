---
id: https://agentic-knowledge-base.dev/id/chunk/ed759600-6622-448e-be33-8fab9ae6b4eb
type: artifact
level: executable
title_ko: 함수 module_head_end (tools/extract.py)
title: function module_head_end in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `module_head_end(tree)` 다. 모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def module_head_end(tree: ast.Module) -> int:
    """모듈 머리의 마지막 줄 — docstring 과 앞머리 import 까지. 그 뒤가 첫 구역이다."""
    end = 0
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str) and end == 0:
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
