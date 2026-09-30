---
id: https://agentic-knowledge-base.dev/id/chunk/ac4042d4-658b-4464-af33-c3e2da6754d5
type: artifact
level: executable
title_ko: 함수 axis_proxies (tools/metrics.py)
title: function axis_proxies in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/8fa054a4-1f2a-4d86-b98d-3c68ca9a4619
---
**함수** — `axis_proxies(g, live, plane, level, authored, comp_of, siblings)` 다. 저작된 지식의 연결 성분·수준 건너뜀·매트릭스 채움·수준 허용표 위반을 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def axis_proxies(g, live, plane, level, authored, comp_of, siblings):
    """저작된 지식의 연결 성분·수준 건너뜀·매트릭스 채움·수준 허용표 위반을 돌려준다."""
    # 세 축 대리 (14.1 정정본, p14-stage-pass-conditions): 연결 성분 · 매트릭스 채움률 · level 건너뜀 · 수준 허용표 위반
    parent = {c: c for c in authored}  # 관측·주석 제외 — 저작된 지식의 고립을 잰다
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a_, b_):
        if a_ in parent and b_ in parent: parent[find(a_)] = find(b_)
    for p_ in LINKS + [AGT.hasDirectPart]:
        for s_, o_ in g.subject_objects(p_): union(s_, o_)
    for part_, comp_ in comp_of.items():
        for sib in siblings[comp_]: union(part_, sib)
    components = len({find(c) for c in authored})
    skips = [(s_, o_) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level and level[s_] in LEVELS and level[o_] in LEVELS
             and LEVELS.index(level[s_]) - LEVELS.index(level[o_]) != 1]
    lvl_pairs = {(level[o_], level[s_]) for s_, o_ in g.subject_objects(AGT.refines) if s_ in level and o_ in level}
    adjacent = [(LEVELS[i], LEVELS[i + 1]) for i in range(4)]
    filled = [p_ for p_ in adjacent if p_ in lvl_pairs]
    residency_bad = [c for c in live if plane[c] in RESIDENCY and level[c] not in RESIDENCY[plane[c]]]
    return components, skips, filled, residency_bad
```
<!-- 인용 끝 -->
