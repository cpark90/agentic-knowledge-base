---
id: https://agentic-knowledge-base.dev/id/chunk/21d36097-2599-4a14-8057-733c634ae0b6
type: artifact
level: executable
title_ko: 함수 def_kind (tools/extract.py)
title: function def_kind in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `def_kind(node)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def def_kind(node) -> str:
    return "cls" if isinstance(node, ast.ClassDef) else "fn"
```
<!-- 인용 끝 -->
