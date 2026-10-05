---
id: https://agentic-knowledge-base.dev/id/chunk/cae9f316-30b4-4aec-8a06-4a4df1f8e3f9
type: artifact
level: executable
title_ko: 함수 render_refinement_section (tools/metrics.py)
title: function render_refinement_section in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
part_of: https://agentic-knowledge-base.dev/id/composite/fa0aa6c4-7e2a-449b-9f07-9dd03faa3122
---
**함수** — `render_refinement_section(g, pct, decisions, missing, missing_loc, functional, human, base, reached, candidate_decisions)` 다. 5단계 대리 — 결정 완결률과 전방 추적 (유저 결정 2026-10-04).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_refinement_section(g, pct, decisions, missing, missing_loc, functional, human, base, reached, candidate_decisions=()):
    """5단계 대리 — 결정 완결률과 전방 추적 (유저 결정 2026-10-04)."""
    loc = lambda c: str(next(g.objects(c, AGT.assertionLocation), "")) or kb_lib.NONE_MARK
    kb_split = " · ".join(f"`{k_}` {pct(sum(1 for r in reached if kb_lib.kb_of(loc(r)) == k_), sum(1 for r in base if kb_lib.kb_of(loc(r)) == k_))}"
                          for k_ in sorted({kb_lib.kb_of(loc(r)) for r in base}))
    o = ["", "## 5단계 대리 — 정제 (결정 완결률 · 전방 추적)", "",
         f"- 구체화: 결정 완결률 — 살아 있는 결정 중 대안 청크를 가진 것 **{pct(len(decisions) - len(missing), len(decisions))}** (목표 100.0%). "
         "결정은 **결론** 슬롯 청크를 부분으로 가진 복합체이고(복합체 밖의 결론 청크는 그 하나), 결론이 하나라도 deprecated 가 아니면 살아 있다. "
         "대안 없는 결정: " + (" · ".join(f"{kb_lib.label_of(g, u)} (`{loc(missing_loc[u])}`)" for u in missing) or "없음"),
         f"- 구체화: 열린 공간의 후보 결정 **{len(candidate_decisions)}**개(따로 셈) — 결론이 status open 인 설계 공간의 state open 후보인 결정이다. "
         "아직 고르지 않은 선택지라 위 결정 완결률의 분모·분자에 들지 않는다 (유저 결정 Q60-a). resolved 공간의 confirmed 후보는 확정 결정으로 센다",
         f"- 구체화: 전방 추적 — functional 요구 중 executable까지 내려간 것 **{pct(len(reached), len(base))}** (목표 100.0%; KB별 {kb_split}). "
         f"functional 요구 {len(functional)}건에서 사람 확인 요구 {len(human)}건을 분모에서 뺐다 — 검증 목표를 `refines` 하는 합격 기준의 가운데 슬롯이 "
         f"**{HUMAN_CHECK_SLOT}** 인 목표와 그 목표가 `derivesFrom` 하는 개발 요구다. 아래 「정제 완주」 절은 사람 확인 요구를 포함한 같은 집계다"]
    return o
```
<!-- 인용 끝 -->
