---
id: https://agentic-knowledge-base.dev/id/chunk/8382b3eb-033b-4299-a06a-a544995b0ea1
type: artifact
level: executable
title_ko: 함수 top_name (tools/extract.py)
title: function top_name in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/52eb4f03-55ea-4dfb-be6d-9164da7da5ef
---
**함수** — `top_name(node)` 다. 최상위 문의 이름 — 정의면 그 이름, 이름 하나에 대입하면 그 이름, 그 밖은 빈 문자열이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def top_name(node) -> str:
    """최상위 문의 이름 — 정의면 그 이름, 이름 하나에 대입하면 그 이름, 그 밖은 빈 문자열이다 (배선 목록의 키)."""
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return node.name
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    return ""
```
<!-- 인용 끝 -->
