---
id: https://agentic-knowledge-base.dev/id/chunk/3591b8e8-245b-4398-94da-2db2b7e3339d
type: artifact
level: executable
title_ko: 함수 space_linkage_edges (tools/kb_lib.py)
title: function space_linkage_edges in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `space_linkage_edges(g)` 다. 설계 공간 그래프의 연결 쌍 — (공간, 변수 출발 항목)과 후보마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def space_linkage_edges(g: Graph) -> list:
    """설계 공간 그래프의 연결 쌍 — (공간, 변수 출발 항목)과 후보마다 (공간, 후보 대상)이다 (유저 결정 Q60-a).

    후보의 state(open·eliminated·confirmed)를 가리지 않는다 — 배제된 후보도 공간이 담은 지식이다.
    """
    var_from, has_cand, link_to = SPACE_LINKAGE_PREDICATES
    edges = []
    for space, frm in g.subject_objects(var_from):
        edges.append((space, frm))
        for link in g.objects(space, has_cand):
            edges.extend((space, to) for to in g.objects(link, link_to))
    return sorted(edges, key=lambda e: (str(e[0]), str(e[1])))
```
<!-- 인용 끝 -->
