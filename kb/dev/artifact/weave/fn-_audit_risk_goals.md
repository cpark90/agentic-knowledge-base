---
id: https://agentic-knowledge-base.dev/id/chunk/7cf3545d-a032-4824-826f-aca6c0876d34
type: artifact
level: executable
title_ko: 함수 _audit_risk_goals (tools/weave.py)
title: function _audit_risk_goals in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_risk_goals(m, g, vv, pct)` 다. 검증 목표가 노출하는 결함 요인 — 표지는 선언(`exposes`)과 추출(본문의 현상 IRI) 둘이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_risk_goals(m: Model, g, vv: set, pct) -> list[str]:
    """검증 목표가 노출하는 결함 요인 — 표지는 선언(`exposes`)과 추출(본문의 현상 IRI) 둘이다 (8.21절 G1·G5)."""
    body: list[str] = []
    goals = {c for c in vv if m.plane[c] == "requirement"}  # 검증 목표 — 2절과 같은 정의다
    # 2.5 위험에서 파생된 목표 — 검증 목표가 defect 요인(현상)을 가리키는가 (위험 분석 G1·G5, 노트 8.21·8.22절)
    # 파생의 표지는 둘이다. frontmatter `exposes`(agt:exposesFactor)는 저자가 선언한 것이고 본문의 현상 IRI 인용
    # (agt:usesConcept, extract_refs)은 추출된 것이다. 둘 다 있으면 선언을 적는다 — 선언이 더 검사 가능한 근거다.
    factor_classes = set(g.transitive_subjects(RDFS.subClassOf, AGT.DefectFactor))
    factors = {i for cl in factor_classes for i in g.subjects(RDF.type, cl)}
    exposed: dict = defaultdict(dict)
    for pred, mark in ((AGT.exposesFactor, RISK_MARK_DECLARED), (AGT.usesConcept, RISK_MARK_EXTRACTED)):
        for s, o in g.subject_objects(pred):
            if s in goals and o in factors:
                exposed[s].setdefault(o, mark)
    named = {f for fs in exposed.values() for f in fs}
    body += [f"## 위험에서 파생된 목표 — 검증 목표가 노출하는 결함 요인 (표지 둘 — {RISK_MARK_DECLARED}: `exposes` · {RISK_MARK_EXTRACTED}: 본문의 현상 IRI, 8.21절 G1·G5)", "",
             f"- 위험에서 파생된 검증 목표: **{pct(len(exposed), len(goals))}** — 나머지는 게이트·음성 시험을 사슬로 묶은 것이다",
             f"- 어느 목표에도 가리켜지지 않은 현상: **{pct(len(factors) - len(named), len(factors))}**", ""]
    if not exposed:
        body += [f"위험에서 파생된 검증 목표 {kb_lib.NONE_MARK} — 현상을 가리키는 목표가 없다. `exposes:` 또는 본문의 현상 IRI 인용이 표지다.", ""]
    else:
        body += ["| 검증 목표 | 노출하는 현상 | 표기 | 표지 |", "|---|---|---|---|"]
        for c in sorted(exposed, key=lambda c: m.location[c]):
            for f in sorted(exposed[c], key=lambda f: str(f)):
                note = str(next(g.objects(f, SKOS_NOTATION), "")) or kb_lib.NONE_MARK
                body += [f"| `{Path(m.location[c]).stem}` {m.ko(c)} | {m.ko(f)} (`{kb_lib.compact_iri(str(f))}`) | {note} | {exposed[c][f]} |"]
        body += [""]
    return body
```
<!-- 인용 끝 -->
