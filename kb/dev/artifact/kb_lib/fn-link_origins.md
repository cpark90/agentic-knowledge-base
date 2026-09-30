---
id: https://agentic-knowledge-base.dev/id/chunk/ff5236c7-129e-43c7-9466-8cf55445d254
type: artifact
level: executable
title_ko: 함수 link_origins (tools/kb_lib.py)
title: function link_origins in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/5c3f6ad5-769e-4850-970b-a137fa5ebc55]
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `link_origins(g)` 다. 링크 개체(agt:Link)의 후보·구축·복원 구분 — metrics 3단계 대리와 weave audit 링크 근거 절이 이 하나의 정의를 쓴다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_origins(g: Graph) -> dict:
    """링크 개체(agt:Link)의 후보·구축·복원 구분 — metrics 3단계 대리와 weave audit 링크 근거 절이 이 하나의 정의를 쓴다.

    후보 링크 = linkState 가 candidate 인 agt:Link (본문 추출 참조 — extract_refs). 종류별 수를 candidate_kinds 로 낸다.
    확정 링크(나머지) 중 복원 링크 = 구축 기록이 아닌 증거 종류를 하나라도 가진 것 (restored: 표시 → proposal 이 확정 기록과 함께 붙는다),
    구축 링크 = 그 밖(구축 기록 증거뿐 또는 증거 없음). 복원 비율 = 복원 / (확정 구축 + 복원), 분모 0 이면 None —
    후보는 분모에 들어가지 않는다 (p10-extracted-references-are-candidates). extracted 는 본문 식별자 추출의 직접 트리플 수(참고).
    반환 키: links · confirmed · candidates · candidate_kinds{축약 술어: 수} · built · restored · restored_links · no_evidence ·
             extracted{축약 술어: 수} · ratio
    """
    links = sorted(g.subjects(RDF.type, AGT.Link), key=str)
    candidates = [l for l in links if any(str(s) == LINK_STATE_CANDIDATE for s in g.objects(l, AGT.linkState))]
    confirmed = [l for l in links if l not in set(candidates)]
    restored, no_ev = [], 0
    for link in confirmed:
        kinds = [k for e in g.objects(link, AGT.hasEvidence) for k in g.objects(e, AGT.evidenceKind)]
        if not kinds:
            no_ev += 1
        elif any(k != CONSTRUCTION_EVIDENCE for k in kinds):
            restored.append(link)
    candidate_kinds: dict = {}
    for l in candidates:
        k = compact_iri(str(next(g.objects(l, AGT.linkKind), "")))
        candidate_kinds[k] = candidate_kinds.get(k, 0) + 1
    extracted = {compact_iri(str(p)): sum(1 for _ in g.subject_objects(p)) for p in LINK_EXTRACTED}
    built = len(confirmed) - len(restored)
    total = built + len(restored)
    return {"links": len(links), "confirmed": len(confirmed), "candidates": len(candidates), "candidate_kinds": candidate_kinds,
            "built": built, "restored": len(restored), "restored_links": restored, "no_evidence": no_ev,
            "extracted": extracted, "ratio": (len(restored) / total) if total else None}
```
<!-- 인용 끝 -->
