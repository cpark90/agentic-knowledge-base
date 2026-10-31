---
id: https://agentic-knowledge-base.dev/id/chunk/a4fbabb3-5a44-4221-bf3c-10e32145d51c
type: decision
level: concrete
title_ko: 뷰는 저장하지 않고 질의로 조립한다
title: Views are never stored; they are assembled by query
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0075-projection-as-query.md, id: https://agentic-knowledge-base.dev/id/chunk-d0075, title_ko: "뷰는 저장하지 않고 질의로 조립한다", title: "Views are assembled by query, never stored"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0075]
part_of: https://agentic-knowledge-base.dev/id/composite/5d561aaa-6fc8-4102-91b9-96db89f984e8
composite: {id: https://agentic-knowledge-base.dev/id/composite/5d561aaa-6fc8-4102-91b9-96db89f984e8, title_ko: 뷰 — 질의로서, title: Projection as query}
---
**결론** — 문학적 프로그래밍의 두 연산(tangle, weave)은 별도 도구가 아니라
**그래프 질의**다. **뷰는 저장하지 않고 질의로 조립한다.**

| 연산 | 질의 | 산출 |
|---|---|---|
| **tangle** | 복합체의 `agt:ArtifactChunk` 부분을 `co:index` 순으로 뽑아 assertion 본문을 이어 붙임 | 코드 파일 |
| **weave** | `agt:ArtifactChunk`와 그것을 `targets`하는 `agt:AnnotationChunk`를 함께 뽑아 순서대로 배치 | 문서 |
| **라벨 목록** | 적용 범위 안 단위 지식의 `rdfs:label`만 | 5.3절 읽기 응답 |
| **작업 집합** | 적용 범위의 지식 종류 클래스와 ODD 조건으로 지식을 거름 | 0.5절 |
