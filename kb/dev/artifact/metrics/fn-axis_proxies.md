---
id: https://agentic-knowledge-base.dev/id/chunk/ac4042d4-658b-4464-af33-c3e2da6754d5
type: artifact
level: executable
title_ko: 함수 axis_proxies (tools/metrics.py)
title: function axis_proxies in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/c15db5ea-e132-44e3-b82c-929369970f50]
part_of: https://agentic-knowledge-base.dev/id/composite/8fa054a4-1f2a-4d86-b98d-3c68ca9a4619
---
**함수** — `axis_proxies(g, live, plane, level, authored, comp_of, siblings, declarer, space_edges)` 다. 저작된 지식의 연결 성분 수·주 성분 밖 성분들·수준 건너뜀·매트릭스 채움·수준 허용표 위반을 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def axis_proxies(g, live, plane, level, authored, comp_of, siblings, declarer, space_edges=()):
    """저작된 지식의 연결 성분 수·주 성분 밖 성분들·수준 건너뜀·매트릭스 채움·수준 허용표 위반을 돌려준다.

    `space_edges` 는 `kb_lib.space_linkage_edges` 의 (공간, 변수 출발 항목 | 후보) 쌍이다 (유저 결정 Q60-a). 공간은 복합체처럼
    경유 노드이고 셈은 청크만 한다 — 공간 그래프는 지표의 그래프 union 밖이므로 공간 청크는 살아 있는 청크 수에 들지 않는다.
    """
    # 세 축 대리 (14.1 정정본, p14-stage-pass-conditions): 연결 성분 · 매트릭스 채움률 · level 건너뜀 · 수준 허용표 위반
    parent = {c: c for c in authored}  # 관측·주석 제외 — 저작된 지식의 고립을 잰다
    # 복합체는 청크가 아니지만 연결의 경유 노드다 — 중첩 복합체(문서 → 묶음)와 복합체를 가리키는 링크
    # (`agt:projectsConvention` 의 치역은 결정 복합체)가 그 노드를 거쳐 부분들에 닿는다. 셈은 청크만 한다
    for comp_ in comp_of.values(): parent.setdefault(comp_, comp_)
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a_, b_):
        if a_ in parent and b_ in parent: parent[find(a_)] = find(b_)
    for p_ in kb_lib.linkage_predicates(g):  # 추적 링크 잎 + 세 족의 하위 속성 + 구성 관계 + prov:specializationOf
        for s_, o_ in g.subject_objects(p_): union(s_, o_)
    for part_, comp_ in comp_of.items():
        for sib in siblings[comp_]: union(part_, sib)
    # 선언 청크 = 복합체 (유저 결정 Q49-a, p7-code-links-on-file-composite) — 파일 청크는 파일 복합체의 부분이 아니므로
    # 이 합침이 없으면 파일 청크의 링크가 복합체를 거쳐 부분(머리·절·정의)에 닿지 않는다
    for comp_, decl_ in declarer.items():
        parent.setdefault(comp_, comp_)
        union(decl_, comp_)
    # 설계 공간의 후보 링크 (유저 결정 Q60-a) — 후보 결론은 head `refines` 가 없으므로 공간을 거쳐 변수 출발 항목에 닿는다
    for space_, end_ in space_edges:
        parent.setdefault(space_, space_)
        union(end_, space_)
    groups = defaultdict(list)
    for c in authored: groups[find(c)].append(c)
    # 성분을 크기 내림차순(동수는 작은 IRI)으로 두고 첫째를 주 성분으로 본다 — 나머지가 진단 대상이다
    ordered = sorted(groups.values(), key=lambda m: (-len(m), str(min(m, key=str))))
    components, outside = len(ordered), ordered[1:]
    skips = [(s_, o_) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level and level[s_] in LEVELS and level[o_] in LEVELS
             and LEVELS.index(level[s_]) - LEVELS.index(level[o_]) != 1]
    lvl_pairs = {(level[o_], level[s_]) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level}
    adjacent = [(LEVELS[i], LEVELS[i + 1]) for i in range(4)]
    filled = [p_ for p_ in adjacent if p_ in lvl_pairs]
    residency_bad = [c for c in live if plane[c] in RESIDENCY and level[c] not in RESIDENCY[plane[c]]]
    return components, outside, skips, filled, residency_bad
```
<!-- 인용 끝 -->
