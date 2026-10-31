---
id: https://agentic-knowledge-base.dev/id/chunk/3591b8e8-245b-4398-94da-2db2b7e3339d
type: artifact
level: executable
title_ko: 함수 space_linkage_edges (tools/kb_lib.py)
title: function space_linkage_edges in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/464fe842-81a3-438f-901c-e9cef6f1dc88]
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `space_linkage_edges(g)` 다. 설계 공간 그래프의 연결 쌍 — (공간, 변수 출발 항목)과 후보마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def space_linkage_edges(g: Graph) -> list:
    """설계 공간 그래프의 연결 쌍 — (공간, 변수 출발 항목)과 후보마다 (공간, 후보 대상)이다 (유저 결정 Q60-a).

    후보의 state(open·eliminated·confirmed)를 가리지 않는다 — 배제된 후보도 공간이 담은 지식이다.
    """
    var_from, has_cand, _ = SPACE_LINKAGE_PREDICATES
    edges = []
    for space, frm in g.subject_objects(var_from):
        edges.append((space, frm))
        for link in g.objects(space, has_cand):  # 후보는 변수 출발 항목이 아닌 쪽 끝이다 (방향은 SPACE_CANDIDATE_DIRECTION)
            cand = space_candidate_of(g, space, link)
            if cand is not None:
                edges.append((space, cand))
    return sorted(edges, key=lambda e: (str(e[0]), str(e[1])))
```
<!-- 인용 끝 -->
