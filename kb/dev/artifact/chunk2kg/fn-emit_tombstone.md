---
id: https://agentic-knowledge-base.dev/id/chunk/c313808a-9a95-42a4-8ca1-8ffe3e2e8e65
type: artifact
level: executable
title_ko: 함수 emit_tombstone (tools/chunk2kg.py)
title: function emit_tombstone in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/d75bcbfe-969b-45d4-81f9-fc42145f892b]
part_of: https://agentic-knowledge-base.dev/id/composite/7efb5476-c231-4b0e-9e6c-a2389a12409e
---
**함수** — `emit_tombstone(t)` 다. 묘비 하나의 블록 — 클래스·라벨 둘·git 영구 위치뿐이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit_tombstone(t: dict) -> str:
    """묘비 하나의 블록 — 클래스·라벨 둘·git 영구 위치뿐이다. 같은 묘비를 여러 항목이 선언하면 블록이 바이트로 같아야 한다."""
    return (f"<{t['id']}>\n    a {TOMBSTONE_CLASS} ;\n"
            f'    rdfs:label "{esc(t["title"])}"@en ;\n'
            f'    rdfs:label "{esc(t["title_ko"])}"@ko ;\n'
            f'    prov:atLocation "{esc(t["location"])}" .')
```
<!-- 인용 끝 -->
