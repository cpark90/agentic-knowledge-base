---
id: https://agentic-knowledge-base.dev/id/chunk/abdec406-8c7d-4178-9fd6-73bc42cea633
type: artifact
level: executable
title_ko: 함수 _audit_links (tools/weave.py)
title: function _audit_links in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1, https://agentic-knowledge-base.dev/id/chunk/ff5236c7-129e-43c7-9466-8cf55445d254]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_links(m, g, pct)` 다. 링크 개체의 증거 종류 분포와 복원 비율 (kb_lib.link_origins — 증거 종류가 구축·복원의 기준이다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_links(m: Model, g, pct) -> list[str]:
    """링크 개체의 증거 종류 분포와 복원 비율 (kb_lib.link_origins — 증거 종류가 구축·복원의 기준이다)."""
    body: list[str] = []
    # 8. 링크 근거 — 증거 종류 분포와 복원 비율 (metrics 와 같은 구축·복원 정의: kb_lib.link_origins — 증거 종류 기준)
    links = list(g.subjects(RDF.type, AGT.Link))
    ev_kinds = Counter()
    for l in links:
        for ev in g.objects(l, AGT.hasEvidence):
            ev_kinds[str(next(g.objects(ev, AGT.evidenceKind), "")).split("/")[-1] or "없음"] += 1
    origins = kb_lib.link_origins(g)
    built, restored, no_ev = origins["built"], origins["restored"], origins["no_evidence"]
    states = Counter(str(next(g.objects(l, AGT.linkState), "")) or "없음" for l in links)
    restored_rows = [f"  - {m.ko(next(g.objects(l, AGT.linkFrom), l))} —`{str(next(g.objects(l, AGT.linkKind), '')).split('/')[-1]}`→ "
                     f"{m.ko(next(g.objects(l, AGT.linkTo), l))}" for l in origins["restored_links"]]
    body += ["## 링크 근거 — 링크 개체의 증거 종류와 복원 비율", "",
          f"- 링크 개체 `agt:Link` **{len(links)}** · 증거 없는 링크 {no_ev} (목표 0) · 상태 " + (" · ".join(f"`{k}` {v}" for k, v in sorted(states.items())) or "없음"),
          "- 증거 종류: " + (" · ".join(f"`{k}` {v}" for k, v in ev_kinds.most_common()) or "없음"),
          f"- 확정 {origins['confirmed']} = 구축 {built}(구축 기록 증거뿐) + 복원 {restored}(구축 기록 아닌 증거 `proposal` 을 가진 링크 개체 — frontmatter `restored:` 표시, "
          f"p10-restored-link-marking) → 복원 비율 **{pct(restored, built + restored)}** (목표 20% 미만; 후보는 `//kg:link_candidates`)",
          f"- 후보 {origins['candidates']} (`agt:CandidateLink` — 본문 추출, 증거는 구축 기록; p10-extracted-references-are-candidates): "
          + (" · ".join(f"`{k}` {v}" for k, v in sorted(origins["candidate_kinds"].items())) or "없음")
          + " · 본문 식별자 추출 직접 트리플 " + " · ".join(f"`{k}` {v}" for k, v in origins["extracted"].items())] + restored_rows + [""]
    return body
```
<!-- 인용 끝 -->
