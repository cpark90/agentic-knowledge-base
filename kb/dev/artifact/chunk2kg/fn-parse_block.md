---
id: https://agentic-knowledge-base.dev/id/chunk/9e16611b-2397-4b7d-a033-267e745a1aeb
type: artifact
level: executable
title_ko: 함수 parse_block (tools/chunk2kg.py)
title: function parse_block in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2c7e96e6-1c7a-4f75-b63b-8c0d0db3e828
---
**함수** — `parse_block(block)` 다. emit_links 가 낸 블록 → (IRI, [(술어, [목적어…])…]).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_block(block: str) -> tuple:
    """emit_links 가 낸 블록 → (IRI, [(술어, [목적어…])…]). 링크·증거 블록 전용 — 목적어에 ` , ` 나 따옴표 속 콤마가 없다."""
    lines = block.split("\n")
    iri = lines[0].strip().strip("<>")
    stmts = []
    for raw in lines[1:]:
        t = raw.strip()
        if t.endswith(" ;") or t.endswith(" ."):
            t = t[:-2]
        pred, _, objs = t.partition(" ")
        stmts.append((pred, [o.strip() for o in objs.split(" , ") if o.strip()]))
    return iri, stmts
```
<!-- 인용 끝 -->
