---
id: https://agentic-knowledge-base.dev/id/chunk/55c0dffc-fb43-485f-abee-4db384f48469
type: artifact
level: executable
title_ko: 함수 louvain (tools/community.py)
title: function louvain in tools/community.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-community}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/29733e84-623f-4e11-b466-6c084c8510a5
---
**함수** — `louvain(nodes, adj)` 다. 결정론적 Louvain — 노드는 IRI 정렬 순으로, 이웃 군집도 정렬 순으로 보고 이득이 양수일 때만 옮긴다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def louvain(nodes: list, adj: dict) -> dict:
    """결정론적 Louvain — 노드는 IRI 정렬 순으로, 이웃 군집도 정렬 순으로 보고 이득이 양수일 때만 옮긴다.

    adj[u][v] 는 대칭 가중치, adj[u][u] 는 자기 고리(집약 단계에서 생긴다). 반환은 원래 노드 → 군집 id (군집 id 는 그 안의 최소 IRI 문자열).
    """
    member_of = {u: u for u in nodes}   # 원래 노드 → 현재 층의 노드
    cur_nodes, cur_adj = list(nodes), {u: dict(vs) for u, vs in adj.items()}
    for _ in range(50):
        comm, moved = _one_level(cur_nodes, cur_adj)
        member_of = {u: comm[c] for u, c in member_of.items()}
        if not moved:
            break
        cur_nodes, cur_adj = _aggregate(cur_nodes, cur_adj, comm)
    return member_of
```
<!-- 인용 끝 -->
