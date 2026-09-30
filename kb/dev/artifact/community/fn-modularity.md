---
id: https://agentic-knowledge-base.dev/id/chunk/d055d81b-2c2f-4f5d-87f5-b4425c8c4311
type: artifact
level: executable
title_ko: 함수 modularity (tools/community.py)
title: function modularity in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/09eb4947-176f-41ad-92ee-7632b5240022
---
**함수** — `modularity(nodes, adj, part)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def modularity(nodes: list, adj: dict, part: dict) -> float:
    deg = {u: sum(w for v, w in adj.get(u, {}).items() if v != u) + 2 * adj.get(u, {}).get(u, 0) for u in nodes}
    m = sum(deg.values()) / 2
    if m == 0:
        return 0.0
    q = 0.0
    for u in nodes:
        for v, w in adj.get(u, {}).items():
            if part[u] == part[v]:
                q += w - deg[u] * deg[v] / (2 * m)
    return q / (2 * m)
```
<!-- 인용 끝 -->
