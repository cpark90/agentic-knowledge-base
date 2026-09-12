---
id: https://agentic-knowledge-base.dev/id/chunk-d0014
type: decision
level: concrete
title_ko: 실패 모드 셋(고아·drift·rot)마다 독립된 기계적 방어선을 둔다
title: Each of the three failure modes, orphans, drift and rot, gets an independent mechanical defense
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 자라는 지식그래프의 실패 모드는 셋이고, 각각 독립된 기계적
방어선을 게이트로 둔다.

| 실패 모드 | 방어선 | 강제 |
|---|---|---|
| orphaned nodes (고아) | 구조 검증: 연결성 shape + 전역 도달성 BFS + capability 충족 | 빌드 실패 |
| context drift (어휘 분화) | 통제 어휘: 스키마가 유일한 어휘, 라벨 유일성 + 동의어는 altLabel, typed edge, 추론 정규화 | 빌드 실패 |
| context rot (컨텍스트 부패) | 유계 뷰: 관련도 순위 + 토큰 예산 상한 | 읽기 경로 |

**근거** (harness-functional 구 docs/DESIGN.md — 이 승격으로 원본은 제거됨)
- 고아는 예외가 아니라 build failure다 — 새 노드는 같은 커밋 안에서
  그래프에 연결한다. 노드 지역 규칙(shape)이 놓치는 섬은 도달성 BFS가
  잡고, "연결됐지만 빌드 불가"는 capability 짝 맞춤이 잡는다.
- drift는 손실만큼 정상 위험으로 다룬다 — 근사 동의어 클래스와 untyped
  edge가 바로 막으려는 것이다. "RAG"와 "Document retrieval"은 한 노드의
  pref/alt이지 두 노드가 아니다.
- 셋은 독립 축이라 방어선도 겹치지 않게 둔다 — 하나의 게이트로 셋을
  다 막으려 하지 않는다.
