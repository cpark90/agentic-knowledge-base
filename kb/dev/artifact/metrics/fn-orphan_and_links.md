---
id: https://agentic-knowledge-base.dev/id/chunk/45edd053-bd47-4049-8f15-85cc5fb30edf
type: artifact
level: executable
title_ko: 함수 orphan_and_links (tools/metrics.py)
title: function orphan_and_links in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/643e2ab5-0c10-48af-9127-e4240447b639
---
**함수** — `orphan_and_links(g, chunks)` 다. 고아 집합(복합체 부분도 링크도 없는 청크, 4.13절)과 링크 타입별 수를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def orphan_and_links(g, chunks):
    """고아 집합(복합체 부분도 링크도 없는 청크, 4.13절)과 링크 타입별 수를 돌려준다."""
    linked = set()
    for p in LINKS:
        for s, o in g.subject_objects(p):
            linked.add(s); linked.add(o)
    parts = {o for o in g.objects(None, AGT.hasDirectPart)}
    orphans = {c for c in chunks if c not in linked and c not in parts}
    link_count = Counter(g.qname(p) for p in LINKS for _ in g.subject_objects(p))
    return linked, parts, orphans, link_count
```
<!-- 인용 끝 -->
