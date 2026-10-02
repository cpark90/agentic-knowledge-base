---
id: https://agentic-knowledge-base.dev/id/chunk/100129c2-a2cd-484c-b610-46e6ba849016
type: artifact
level: executable
title_ko: 함수 signature (tools/extract.py)
title: function signature in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `signature(node)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def signature(node) -> str:
    if isinstance(node, ast.ClassDef):
        return f"class {node.name}"
    a = node.args
    names = [x.arg for x in a.posonlyargs + a.args] + ([f"*{a.vararg.arg}"] if a.vararg else [])
    names += [x.arg for x in a.kwonlyargs] + ([f"**{a.kwarg.arg}"] if a.kwarg else [])
    return f"{node.name}({', '.join(names)})"
```
<!-- 인용 끝 -->
