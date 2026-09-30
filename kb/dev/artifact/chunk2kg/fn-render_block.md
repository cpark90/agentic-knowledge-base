---
id: https://agentic-knowledge-base.dev/id/chunk/38150f41-1adc-4ea1-9c7f-f722f721fe9a
type: artifact
level: executable
title_ko: 함수 render_block (tools/chunk2kg.py)
title: function render_block in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2c7e96e6-1c7a-4f75-b63b-8c0d0db3e828
---
**함수** — `render_block(iri, stmts)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_block(iri: str, stmts: list) -> str:
    lines = [f"<{iri}>"]
    for i, (pred, objs) in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {pred} {' , '.join(objs)}{sep}")
    return "\n".join(lines)
```
<!-- 인용 끝 -->
