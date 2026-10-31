---
id: https://agentic-knowledge-base.dev/id/chunk/d3c90085-77cc-454d-8e8b-c5010b9e86ba
type: decision
level: concrete
title_ko: 형식 그래프의 보장과 컨텍스트 부패는 쓰기 시점과 읽기 시점을 나누어야 함께 풀린다
title: Formal guarantees and context rot are reconciled only by separating write time from read time
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0013-store-formal-read-narrow.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:02:46+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:02:46+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/72187560-4939-4225-8319-7c8e0345b251
---
**근거** — 출처는 harness-functional의 옛 `docs/DESIGN.md`이고, 그 원본은 이 승격으로 제거됐다.

- 두 요구가 반대로 당긴다. 형식 온톨로지는 연결성 보장과 추론, 통제 어휘를 주어 고아와 drift를 없앤다. 그러나 큰 그래프를 통째로 먹이는 것이 바로 context rot의 전형적인 원인이다.
- 그래서 형식성은 쓰기와 검증 시점에 쓰고, 사용 시점에는 증류된 뷰만 읽는다. 따라서 그래프가 아무리 커져도 에이전트의 컨텍스트는 유계다.
- 뷰는 관련도 순위와 홉 감쇠, 노드별 토큰 추정치에 따른 예산 승인(admission)으로 구성된다. 그래서 그래프가 두 배가 되어도 컨텍스트는 두 배가 되지 않는다.
