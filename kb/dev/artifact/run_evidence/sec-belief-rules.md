---
id: https://agentic-knowledge-base.dev/id/chunk/2a0f118f-b4cc-431e-9c70-e8e3b60041f1
type: artifact
level: executable
title_ko: 절 belief-rules (tools/run_evidence.py)
title: section belief-rules in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a7e4d5c8-a3b3-466a-93eb-1bb3d94b2ed5
composite: {id: https://agentic-knowledge-base.dev/id/composite/a7e4d5c8-a3b3-466a-93eb-1bb3d94b2ed5, title_ko: 절 복합체 belief-rules (tools/run_evidence.py), title: section composite belief-rules in tools/run_evidence.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/2a0f118f-b4cc-431e-9c70-e8e3b60041f1, https://agentic-knowledge-base.dev/id/chunk/1fd3a79a-b431-4470-8d04-5282bbc0eb31, https://agentic-knowledge-base.dev/id/chunk/7d5d8898-16f3-47f6-a6e3-e5e8a50f08c8], part_of: https://agentic-knowledge-base.dev/id/composite/27628b6a-73ec-4466-bb12-a1a1ae970dd7}
---
**절** — `tools/run_evidence.py` 의 절 `belief-rules` 다. 믿음 정도 — 열린 계산 규칙 A·B·C 의 병기 값 (task 0304, 요구 r-032, 설계 공간 degree-of-belief-space)

**정의** — `belief_of` · `belief_lines` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 믿음 정도 — 열린 계산 규칙 A·B·C 의 병기 값 (task 0304, 요구 r-032, 설계 공간 degree-of-belief-space) ────────────────────
# 값은 후보 링크 곁에만 싣고 상태를 바꾸지 않는다(Q90-a). 상태를 정하는 함수(ledger_lines·judgement_lines)는 이 절을 부르지 않는다 —
# 게이트 belief-consistency(validate)가 코드 단위 지식에서 그것을 본다. 세 규칙 모두 열린 후보라 닫지 않는다(Q166-a).
BELIEF_RULES = {   # 계산 규칙 slug → 설계 공간 후보 결정의 결론 IRI
    "kind-rank": ID_BASE + "chunk/8b6a4563-17d3-4c5c-a9a1-ea46f0babdbc",      # A p9-belief-by-evidence-kind-rank
    "beta-binomial": ID_BASE + "chunk/2dc8dfc7-565d-48c6-9f76-6b81afcd6eea",  # B p9-belief-by-beta-binomial
    "judge-mean": ID_BASE + "chunk/88b97e4d-57de-4ec9-8824-5decb2f9184f",     # C p9-belief-by-calibrated-judge (보정 전, 보정은 S3)
}
# A 의 서열 — 구축, 실행, 동시 편집, 공동 커버, 판정, 임베딩, 세션 (p9-evidence-ledger-with-belief, Q118-a). 순위 i(0부터)의 가중은
# (7 − i) / 7 이다 — 가중표의 근거가 아직 없어 서열만 담는 등간격을 고른다. 유저 결정은 서열 밖의 확정 권한이라 가중이 없다
BELIEF_KIND_RANK = ("agt:constructionRecord", "agt:runResult", "agt:coEditHistory", "agt:testCoverage", "agt:judgement",
                    "agt:embeddingSimilarity", "agt:coRead")
BELIEF_KIND_WEIGHT = {k: (len(BELIEF_KIND_RANK) - i) / len(BELIEF_KIND_RANK) for i, k in enumerate(BELIEF_KIND_RANK)}
BELIEF_PRIOR = (1, 1)   # B 의 사전 Beta(α₀, β₀) — 종류마다 같은 균등 사전이다. 종류별로 달리 둘 표본이 아직 없다
```
<!-- 인용 끝 -->
