---
id: https://agentic-knowledge-base.dev/id/chunk/181f6c99-94f8-4b1c-8461-f34fc0d42c58
type: artifact
level: executable
title_ko: 함수 render (tools/space2kg.py)
title: function render in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/2716ece9-44f6-48ff-b2ab-1ad0ea6fa6c0
---
**함수** — `render(iri, stmts)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(iri: str, stmts: list) -> str:
    lines = [f"<{iri}>"]
    for i, s in enumerate(stmts):
        lines.append(f"    {s}{' .' if i == len(stmts) - 1 else ' ;'}")
    return "\n".join(lines)
```
<!-- 인용 끝 -->
