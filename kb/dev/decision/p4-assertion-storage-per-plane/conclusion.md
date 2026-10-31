---
id: https://agentic-knowledge-base.dev/id/chunk/2a213451-6832-4f8a-9f9b-44ce5de04fa8
type: decision
level: concrete
title_ko: assertion의 물리적 위치는 지식 종류마다 다르고 메타데이터는 -kg에 있다
former_title_ko: ["assertion의 물리적 위치는 plane마다 다르고 메타데이터는 -kg에 있다"]
title: Assertion storage differs per plane; metadata lives in -kg
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0079-assertion-format-per-plane.md, id: https://agentic-knowledge-base.dev/id/chunk-d0079, title_ko: "assertion 본문 형식은 plane마다 다르다", title: "Assertion body format differs per plane"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0079]
part_of: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3
composite: {id: https://agentic-knowledge-base.dev/id/composite/8d3c07da-293b-47cd-861a-44cfd81449b3, title_ko: 단위 지식의 저장, title: Chunk storage, former_title_ko: ["청크의 저장", "지식 항목의 저장"]}
---
**결론** — 네 그래프 중 **head·provenance·pubinfo는 `-kg`에 있다.** assertion
그래프의 물리적 위치는 지식 종류마다 다르다.

| 지식 종류 | assertion 본문 | 해석 |
|---|---|---|
| 산문 계열 | 파일 하나 = 단위 지식 하나 | IRI → 파일 경로 |
| 코드 계열 | 심볼 | IRI → 심볼 ID → 파일 내 범위 |
| `memory` | `-kg` 안의 리터럴 | 직접 |

**단위 지식 메타데이터 질의에 본문을 열 필요가 없다.** 라벨·지식 종류·level·출처·버전은
전부 `-kg`에 있다.
