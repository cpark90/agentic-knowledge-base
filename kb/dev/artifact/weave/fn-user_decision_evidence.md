---
id: https://agentic-knowledge-base.dev/id/chunk/ef9472b8-59c4-47b6-91eb-b0532f4403de
type: artifact
level: executable
title_ko: 함수 user_decision_evidence (tools/weave.py)
title: function user_decision_evidence in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55]
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `user_decision_evidence(g)` 다. 그래프의 유저 결정 증거 → [(참조, 자리)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def user_decision_evidence(g: Graph) -> list[tuple[str, str]]:
    """그래프의 유저 결정 증거 → [(참조, 자리)]. 참조는 `Q-NNNN#Qn` 또는 `legacy/<파일>.md`(kb_lib.USER_DECISION_REF)이고, 자리는 증거를 가진
    링크가 후보로 든 설계 공간의 stem 과 링크 상태다(space2kg — 설계 공간 → agt:hasCandidate → 링크 → agt:hasEvidence → 증거)."""
    out = []
    for ev in g.subjects(AGT.evidenceKind, AGT[kb_lib.USER_DECISION_KIND]):
        ref = str(next(g.objects(ev, AGT.evidenceRef), ""))
        for link in sorted(g.subjects(AGT.hasEvidence, ev), key=str) or [None]:
            space = next(g.subjects(AGT.hasCandidate, link), None) if link is not None else None
            loc = str(next(g.objects(space, AGT.assertionLocation), "")) if space is not None else ""
            state = str(next(g.objects(link, AGT.linkState), "")) if link is not None else ""
            where = Path(loc).stem if loc else (kb_lib.compact_iri(str(link)) if link is not None else kb_lib.NONE_MARK)
            out.append((ref, f"`{where}` ({state or kb_lib.NONE_MARK})"))
    return sorted(out)
```
<!-- 인용 끝 -->
