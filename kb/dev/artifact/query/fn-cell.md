---
id: https://agentic-knowledge-base.dev/id/chunk/577e30ee-635f-4a97-a192-b3780a178be7
type: artifact
level: executable
title_ko: 함수 cell (tools/query.py)
title: function cell in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/4358cd56-6be2-4ce1-9f2f-9fb0ed47b5d3
---
**함수** — `cell(g, term, labels, width)` 다. 표 셀 하나.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def cell(g: Graph, term, labels: bool, width: int = 0) -> str:
    """표 셀 하나. 빈 값의 표기는 `없음` 하나다 (G14 — 셀을 비우거나 대시를 쓰지 않는다)."""
    if term is None:
        s = kb_lib.NONE_MARK
    elif isinstance(term, URIRef):
        s = kb_lib.label_of(g, term) if labels else kb_lib.compact_iri(str(term))
    elif isinstance(term, Literal):
        s = str(term)
    else:
        s = f"_:{term}"
    s = " ".join(s.split()).replace("|", "\\|") or kb_lib.NONE_MARK
    if width and len(s) > width:
        s = s[: width - 1] + "…"
    return s
```
<!-- 인용 끝 -->
