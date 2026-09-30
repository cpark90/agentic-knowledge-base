---
id: https://agentic-knowledge-base.dev/id/chunk/d145900b-81a0-423b-971f-48b3e69188ef
type: artifact
level: executable
title_ko: 함수 _aggregate (tools/community.py)
title: function _aggregate in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/29733e84-623f-4e11-b466-6c084c8510a5
---
**함수** — `_aggregate(nodes, adj, comm)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _aggregate(nodes: list, adj: dict, comm: dict) -> tuple:
    new_adj = defaultdict(lambda: defaultdict(float))
    for u in nodes:
        cu = comm[u]
        for v, w in adj.get(u, {}).items():
            cv = comm[v]
            if u == v:
                new_adj[cu][cu] += w
            elif str(u) < str(v):
                if cu == cv:
                    new_adj[cu][cu] += w
                else:
                    new_adj[cu][cv] += w
                    new_adj[cv][cu] += w
    new_nodes = sorted({comm[u] for u in nodes}, key=str)
    return new_nodes, {u: dict(new_adj[u]) for u in new_nodes}
```
<!-- 인용 끝 -->
