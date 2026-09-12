---
id: https://agentic-knowledge-base.dev/id/chunk-d0013
type: decision
level: concrete
title_ko: 형식으로 저장하고 좁게 읽는다
title: Store formally, read narrowly
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 저장과 읽기를 2층으로 분리한다. 저장 층은 형식 그래프(검증되고
연결된 단일 진실 공급원)로 두고 통째로 읽지 않으며, 읽기 층은 요청별로
뷰로 생성된 작고 예산 상한이 있는 컨텍스트 팩만 본다.

**근거** (harness-functional 구 docs/DESIGN.md — 이 승격으로 원본은 제거됨)
- 두 요구가 반대로 당긴다: 형식 온톨로지는 연결성 보장·추론·통제 어휘를
  주어 고아와 drift를 죽이지만, 큰 그래프를 통째로 먹이는 것이 곧
  context rot의 교과서적 원인이다.
- 해소: 형식성은 쓰기·검증 시점에 쓰고, 사용 시점에는 증류된 뷰만
  읽는다. 그래프가 아무리 커져도 에이전트의 컨텍스트는 유계다.
- 뷰는 관련도 순위 + 홉 감쇠 + 노드별 토큰 추정치의 예산 admission으로
  구성된다 — 그래프가 두 배가 되어도 컨텍스트는 두 배가 되지 않는다.

**대안** — 텍스트 RAG·벡터 DB 단독은 기각: 연결성 보장이 없어 고아·중복
지식이 나쁜 답을 낼 때까지 보이지 않는다. 형식 층은 그 결함을 빌드
실패로 만들고, 뷰 층이 RAG 수준의 편의를 제공한다.
