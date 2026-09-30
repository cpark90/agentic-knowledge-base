---
id: https://agentic-knowledge-base.dev/id/chunk/ce633768-fb36-4abc-b837-106bf5a18571
type: artifact
level: executable
title_ko: 함수 _one_level (tools/community.py)
title: function _one_level in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/29733e84-623f-4e11-b466-6c084c8510a5
---
**함수** — `_one_level(nodes, adj)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _one_level(nodes: list, adj: dict) -> tuple:
    deg = {u: sum(w for v, w in adj.get(u, {}).items() if v != u) + 2 * adj.get(u, {}).get(u, 0) for u in nodes}
    m = sum(deg.values()) / 2
    comm = {u: u for u in nodes}
    tot = dict(deg)
    moved_any = False
    if m == 0:
        return comm, False
    for _ in range(100):
        moved = False
        for u in nodes:
            nbr = defaultdict(float)
            for v, w in adj.get(u, {}).items():
                if v != u:
                    nbr[comm[v]] += w
            cu = comm[u]
            tot[cu] -= deg[u]
            remove_cost = -nbr.get(cu, 0) / m + tot[cu] * deg[u] / (2 * m * m)
            best, best_gain = cu, 0.0
            for c in sorted(nbr, key=str):
                gain = remove_cost + nbr[c] / m - tot[c] * deg[u] / (2 * m * m)
                if gain > best_gain + 1e-12:
                    best, best_gain = c, gain
            tot[best] += deg[u]
            if best != cu:
                comm[u] = best
                moved = moved_any = True
        if not moved:
            break
    # 군집 id 를 그 안의 최소 노드로 정규화 — 층을 거듭해도 이름이 결정적이다
    rep = {}
    for u in nodes:
        c = comm[u]
        rep[c] = min(rep.get(c, u), u, key=str)
    return {u: rep[comm[u]] for u in nodes}, moved_any
```
<!-- 인용 끝 -->
