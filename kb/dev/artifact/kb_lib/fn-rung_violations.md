---
id: https://agentic-knowledge-base.dev/id/chunk/b743d72c-4fe1-4898-bd6f-aeed9063b344
type: artifact
level: executable
title_ko: 함수 rung_violations (tools/kb_lib.py)
title: function rung_violations in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/6553eed2-c1d9-41a4-b5c8-549f5d93193e, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
part_of: https://agentic-knowledge-base.dev/id/composite/45dfc4dd-c694-47a7-9a8c-6398612879db
---
**함수** — `rung_violations(g, plane, level, live)` 다. 정제 계층 사슬의 위반 — `(정제 수준, 정제의 주어, 정제의 대상, 요구)` 의 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def rung_violations(g: Graph, plane: dict, level: dict, live: set) -> list[tuple]:
    """정제 계층 사슬의 위반 — `(정제 수준, 정제의 주어, 정제의 대상, 요구)` 의 목록. 정제 수준은 `RUNG_DESCENTS` 의 값이다.

    결정 복합체는 한 단위다(p7-decision-spans-three-levels) — 복합체가 닿는 요구는 그 부분들에서 `refines`·`serves` 를 따라
    올라가 처음 만나는 개발 요구이고, 올라간 끝이 결정 청크나 복합체면 그 복합체의 부분들에서 다시 오른다.
    """
    vc = vv_counterparts(g, plane, live)
    dev = {c for c in live if kb_of(str(next(g.objects(c, AGT.assertionLocation), ""))) == KB_DEV}
    comp_of, parts = {}, {}
    for comp, part in g.subject_objects(AGT.hasDirectPart):
        comp_of[part] = comp
        parts.setdefault(comp, set()).add(part)
    up = {}
    for pred in (AGT.refines, AGT.serves):
        for s, o in g.subject_objects(pred):
            up.setdefault(s, set()).add(o)

    def unit(x):
        if x in parts:
            return parts[x] | {x}
        if plane.get(x) == "decision" and x in comp_of:
            return parts[comp_of[x]] | {comp_of[x]}
        return {x}

    def reached(x):
        seen, stack, out = set(), list(unit(x)), set()
        while stack:
            y = stack.pop()
            if y in seen:
                continue
            seen.add(y)
            if y in vc["dev_reqs"]:
                out.add(y)
                continue
            for z in up.get(y, ()):
                stack.extend(unit(z))
        return out

    def concrete(x):
        return any(p in dev and level.get(p) == "concrete" for p in ({x} | parts.get(x, set())))

    out = []
    for pred in (AGT.refines, AGT.serves):
        for s, o in g.subject_objects(pred):
            if (s in dev and plane.get(s) == "decision" and level.get(s) == "concrete"
                    and o in vc["dev_reqs"] and level.get(o) == "functional" and o not in vc["covered_reqs"]):
                out.append((RUNG_DESCENTS[0], s, o, o))
    for d in parts:
        dparts = {p for p in parts[d] if p in live and plane.get(p) == "decision"}
        if {"logical", "concrete"} <= {level.get(p) for p in dparts}:
            head = min((p for p in dparts if level.get(p) == "concrete"), key=str)  # 보고의 자리 — 복합체는 위치가 없다
            for r in reached(d):
                if not vc["goals_of"].get(r, set()) & vc["goals_with_criteria"]:
                    out.append((RUNG_DESCENTS[1], head, r, r))
    for y, x in g.subject_objects(AGT.refines):
        if y not in dev or level.get(y) != "executable" or not concrete(x):
            continue
        for r in reached(x):
            crit = set().union(*(vc["criteria_of"].get(t, set()) for t in vc["goals_of"].get(r, set())))
            machine = crit - vc["human"]
            if (machine or not crit) and not machine & vc["bound"]:
                out.append((RUNG_DESCENTS[2], y, x, r))
    return sorted(set(out), key=lambda v: tuple(map(str, v)))
```
<!-- 인용 끝 -->
