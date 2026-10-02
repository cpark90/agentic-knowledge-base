---
id: https://agentic-knowledge-base.dev/id/chunk/a30e68f5-b43c-4872-9976-ebcdb40c174e
type: artifact
level: executable
title_ko: 함수 _audit_verification (tools/weave.py)
title: function _audit_verification in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_verification(m, g, dev, vv, pct)` 다. 요구의 검증 대응물과 V&V 사슬 (p8-scenario-ladder-rungs · p8-pass-criteria).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_verification(m: Model, g, dev: set, vv: set, pct) -> list[str]:
    """요구의 검증 대응물과 V&V 사슬 (p8-scenario-ladder-rungs · p8-pass-criteria)."""
    body: list[str] = []
    # 2. 검증 현황
    dev_reqs = {c for c in dev if m.plane[c] == "requirement"}
    goals = {c for c in vv if m.plane[c] == "requirement"}
    covered = {t for s, t in g.subject_objects(AGT.derivesFrom) if s in goals and t in dev_reqs}
    criteria_of = defaultdict(set)
    cases_of = defaultdict(set)
    verifiers_of = defaultdict(set)
    for s, t in g.subject_objects(AGT.refines):
        if s in vv and t in vv:
            if m.plane[s] == "contract" and t in goals:
                criteria_of[t].add(s)
            elif m.plane[s] == "schema" and m.plane[t] == "contract":
                cases_of[t].add(s)
            elif m.plane[s] == "artifact" and m.plane[t] == "schema":
                verifiers_of[t].add(s)
    chains = [gl for gl in goals if any(cases_of[cr] for cr in criteria_of[gl])]
    verifies = [(s, t) for s, t in g.subject_objects(AGT.verifies) if s in vv]
    no_criteria = [s for s, _ in verifies if not any((c_, RDF.type, AGT.ContractChunk) in g for c_ in g.objects(s, AGT.refines))]
    units = {m.decision_unit(c) for c in dev if m.plane[c] == "decision"}
    verified_units = {m.decision_unit(t) for _, t in verifies if t in m.chunks and m.plane.get(t) == "decision"}
    body += ["## 검증 현황 — 요구의 검증 대응물과 V&V 사슬 (p8-scenario-ladder-rungs · p8-pass-criteria)", "",
          f"- 검증 대응물이 있는 요구(검증 목표가 `agt:derivesFrom` 으로 가리킴): **{pct(len(covered), len(dev_reqs))}** (목표 100.0%)",
          f"- `agt:verifies` 대상이 된 결정 단위: **{pct(len(verified_units), len(units))}** · verifies 링크 {len(verifies)}",
          f"- 사슬: 검증 목표 {len(goals)} · 합격 기준이 달린 목표 {sum(1 for gl in goals if criteria_of[gl])} · 케이스까지 이어진 목표 {len(chains)} · "
          f"검증기 {sum(len(v) for v in verifiers_of.values())} (합격 기준 {sum(len(v) for v in criteria_of.values())} · 케이스 {sum(len(v) for v in cases_of.values())})",
          f"- 기준 없는 `verifies`: **{len(no_criteria)}** (목표 0 — verify 질의 `verifies-without-criteria` 와 같은 정의)", ""]
    uncovered = sorted(dev_reqs - covered, key=lambda c: m.location[c])
    if uncovered:
        body += [f"검증 대응물 없는 요구 {len(uncovered)}건:", ""] + [f"- `{Path(m.location[c]).stem}` {m.ko(c)}" for c in uncovered] + [""]
    return body
```
<!-- 인용 끝 -->
