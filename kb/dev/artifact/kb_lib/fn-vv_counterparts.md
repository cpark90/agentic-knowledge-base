---
id: https://agentic-knowledge-base.dev/id/chunk/6553eed2-c1d9-41a4-b5c8-549f5d93193e
type: artifact
level: executable
title_ko: 함수 vv_counterparts (tools/kb_lib.py)
title: function vv_counterparts in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/92ac1970-f252-48a0-b11a-fbaa774b2f4a, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
part_of: https://agentic-knowledge-base.dev/id/composite/45dfc4dd-c694-47a7-9a8c-6398612879db
---
**함수** — `vv_counterparts(g, plane, live)` 다. V&V 정제 계층의 대응물 — 개발 요구·검증 목표·목표가 덮는 요구·기준이 달린 목표·기준과 그 바인딩.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def vv_counterparts(g: Graph, plane: dict, live: set) -> dict:
    """V&V 정제 계층의 대응물 — 개발 요구·검증 목표·목표가 덮는 요구·기준이 달린 목표·기준과 그 바인딩.

    KB 는 청크 위치로 가른다(`kb_of`). 키: `dev_reqs`·`goals`·`covered_reqs`(목표가 derivesFrom 하는 개발 요구)·
    `goals_with_criteria`·`goals_of`(요구 → 목표들)·`criteria_of`(목표 → 기준들)·`bound`(검증기가 바인딩한 기준)·`human`.
    """
    loc = {c: str(next(g.objects(c, AGT.assertionLocation), "")) for c in live}
    vv = {c for c in live if kb_of(loc[c]) == KB_VV}
    dev_reqs = {c for c in live - vv if plane.get(c) == "requirement"}
    goals = {c for c in vv if plane.get(c) == "requirement"}
    goals_of, criteria_of = {}, {}
    for s, o in g.subject_objects(AGT.derivesFrom):
        if s in goals and o in dev_reqs:
            goals_of.setdefault(o, set()).add(s)
    for s, o in g.subject_objects(AGT.refines):
        if o in goals and plane.get(s) == "contract":
            criteria_of.setdefault(o, set()).add(s)
    verifiers = {c for c in vv if plane.get(c) == "artifact"}
    cases = {c for c in vv if plane.get(c) == "schema"}
    case_criteria = {}
    for s, o in g.subject_objects(AGT.refines):
        if s in cases and plane.get(o) == "contract":
            case_criteria.setdefault(s, set()).add(o)
    bound = set()
    for s, o in g.subject_objects(AGT.refines):
        if s in verifiers:
            bound |= {o} if plane.get(o) == "contract" else case_criteria.get(o, set())
    return {"dev_reqs": dev_reqs, "goals": goals, "covered_reqs": set(goals_of), "goals_with_criteria": set(criteria_of),
            "goals_of": goals_of, "criteria_of": criteria_of, "bound": bound, "human": human_check_criteria(g, plane)}
```
<!-- 인용 끝 -->
