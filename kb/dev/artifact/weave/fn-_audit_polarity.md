---
id: https://agentic-knowledge-base.dev/id/chunk/54a6b278-cb6f-4c88-8935-01b236a2b7ba
type: artifact
level: executable
title_ko: 함수 _audit_polarity (tools/weave.py)
title: function _audit_polarity in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55]
part_of: https://agentic-knowledge-base.dev/id/composite/ebcf6e73-cc0b-447d-ac23-00290abee9ca
---
**함수** — `_audit_polarity(g, gs)` 다. 증거 기록(`agt:Evidence`)의 종류별·극성별 건수 — 출처는 union 그래프와 설계 공간 파일이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_polarity(g, gs) -> list[str]:
    """증거 기록(`agt:Evidence`)의 종류별·극성별 건수 — 출처는 union 그래프와 설계 공간 파일이다 (유저 답 Q117-a).

    union 그래프의 증거는 링크 개체의 구축·복원 기록과 실행 증거(run_evidence)다. 설계 공간 그래프는 union 밖이고 후보의 `evidence`
    (지지, +)와 `eliminated_by`(배제, −)를 낸다. 극성이 한쪽에 쏠렸는지를 보이는 표이고 판정은 하지 않는다.
    """
    counts: Counter = Counter()
    for graph, union in ((g, True), (gs, False)):
        for ev in graph.subjects(RDF.type, AGT.Evidence):
            pol = str(next(graph.objects(ev, AGT.polarity), "")) or kb_lib.NONE_MARK
            kind = kb_lib.compact_iri(str(next(graph.objects(ev, AGT.evidenceKind), ""))) or kb_lib.NONE_MARK
            src = "union 그래프" if union else SPACE_EVIDENCE_SOURCE.get(pol, "설계 공간 (극성 밖)")
            counts[(src, kind, pol)] += 1
    keys = sorted({(src, kind) for src, kind, _ in counts})
    body = ["## 증거 극성 — 증거 기록의 종류별·극성별 건수 (출처별)", "",
            f"- 증거 기록 {sum(counts.values())} — 지지(+) {sum(v for k, v in counts.items() if k[2] == '+')} · "
            f"반박(−) {sum(v for k, v in counts.items() if k[2] == '-')}. 설계 공간 그래프는 union 밖이라 출처를 따로 적는다", "",
            "| 출처 | 증거 종류 | 지지(+) | 반박(−) | 계 |", "|---|---|---|---|---|"]
    for src, kind in keys:
        plus, minus = counts[(src, kind, "+")], counts[(src, kind, "-")]
        other = sum(v for k, v in counts.items() if k[:2] == (src, kind) and k[2] not in ("+", "-"))
        body.append(f"| {src} | `{kind}` | {plus} | {minus} | {plus + minus + other} |")
    if not keys:
        body.append("| " + " | ".join([kb_lib.NONE_MARK] * 5) + " |")
    return body + [""]
```
<!-- 인용 끝 -->
