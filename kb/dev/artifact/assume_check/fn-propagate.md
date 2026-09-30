---
id: https://agentic-knowledge-base.dev/id/chunk/fc00bd15-31c6-4e4b-b28e-773cbf0b1e48
type: artifact
level: executable
title_ko: 함수 propagate (tools/assume_check.py)
title: function propagate in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `propagate(g, direct, live)` 다. 직접 영향 집합에서 하류로 전이 폐포 + 복합체 형제 → (1홉 suspect 후보, 전이 suspect 후보).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def propagate(g: Graph, direct: set, live: set) -> tuple[set, set]:
    """직접 영향 집합에서 하류로 전이 폐포 + 복합체 형제 → (1홉 suspect 후보, 전이 suspect 후보). 둘 다 직접 집합을 뺀 살아 있는 청크."""
    rdep = dependents(g)
    comp_of = {part: comp for comp, part in g.subject_objects(AGT.hasDirectPart)}
    siblings = defaultdict(set)
    for part, comp in comp_of.items():
        siblings[comp].add(part)

    def step(x):
        out = set(rdep.get(x, ()))
        if x in comp_of:
            out |= siblings[comp_of[x]]
        return out

    hop1 = set().union(*(step(x) for x in direct)) if direct else set()
    seen, stack = set(direct), list(direct)
    while stack:
        x = stack.pop()
        for y in step(x):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return (hop1 - direct) & live, (seen - direct) & live
```
<!-- 인용 끝 -->
