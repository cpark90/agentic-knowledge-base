---
id: https://agentic-knowledge-base.dev/id/chunk/2a213451-6832-4f8a-9f9b-44ce5de04fa8
type: decision
level: concrete
title_ko: assertion의 물리적 위치는 plane마다 다르고 메타데이터는 -kg에 있다
title: Assertion storage differs per plane; metadata lives in -kg
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0079]
part_of: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3
composite: {id: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3, title_ko: 청크의 저장, title: Chunk storage}
---
**결론** — 네 그래프 중 **head·provenance·pubinfo는 `-kg`에 있다.** assertion
그래프의 물리적 위치는 plane마다 다르다.

| plane | assertion 본문 | 해석 |
|---|---|---|
| 산문 계열 | 파일 하나 = 청크 하나 | IRI → 파일 경로 |
| 코드 계열 | 심볼 | IRI → 심볼 ID → 파일 내 범위 |
| `memory` | `-kg` 안의 리터럴 | 직접 |

**청크 메타데이터 질의에 본문을 열 필요가 없다.** 라벨·plane·level·출처·버전은
전부 `-kg`에 있다.
