---
id: https://agentic-knowledge-base.dev/id/chunk/d03431bf-2330-4c3c-9fdc-99221b37916e
type: artifact
level: executable
title_ko: 함수 classify_chunks (tools/metrics.py)
title: function classify_chunks in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/87e62ada-8184-4c95-b1be-e30d2b876be2
---
**함수** — `classify_chunks(g)` 다. 청크 집합과 plane·level·status·줄 수·살아 있는 것을 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def classify_chunks(g):
    """청크 집합과 plane·level·status·줄 수·살아 있는 것을 돌려준다."""
    chunks = {s for s in g.subjects(AGT.lineCount, None)}
    plane = {c: str(next(g.objects(c, RDF.type))).split("/")[-1].replace("Chunk", "").lower() for c in chunks}
    level = {c: str(next(g.objects(c, AGT.hasLevel), "")).split("/")[-1] for c in chunks}
    status = {c: str(next(g.objects(c, AGT.status), "")) for c in chunks}
    lines = {c: int(next(g.objects(c, AGT.lineCount))) for c in chunks}
    live = {c for c in chunks if status[c] != "deprecated"}
    return chunks, plane, level, status, lines, live
```
<!-- 인용 끝 -->
