---
id: https://agentic-knowledge-base.dev/id/chunk/94f03899-180a-4035-a936-da9c7940a55f
type: decision
level: logical
title_ko: 시점 의존 표현은 사본이 낡으면 거짓이 되지만 2026-09-29 실측에서 후보 일곱이 전부 오탐이었다
title: Time-dependent words turn false once a copy ages, but all seven candidates were false positives in the 2026-09-29 measurement
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5f72b379-57f1-49df-b178-9b9de7afac11
---
**근거** — 규약의 원천은 Google developer documentation style guide의 Timeless documentation이다. 시점 의존 표현 대신 버전·날짜로 고정한다(`docs/references.md` §생성 문서 작성). 생성 문서는 사본으로 돈다. "현재"는 읽는 시점에 따라 다른 값을 가리키고 사본이 낡으면 거짓이 된다.

게이트화를 보류한 근거는 2026-09-29 오탐률 실측이다. 인용·제목·표 헤더를 뺀 후보 7건이 전부 오탐이었다. 오탐의 종류는 셋이다 — CQ 정식 문구, 인용 표시 없이 옮긴 주석 청크 본문, 이미 값이 적힌 문장의 부연(생성 뷰 `//kg:cq`·`//kg:metrics`·`//kg:open`)이다. 값 대신 쓰였는가는 문맥 판단이라 낱말 정규식으로 가르지 못한다.

같은 날 같은 방식으로 잰 목표 표기 G16은 위반 1·오탐 0이어서 게이트로 올렸다. 두 규약의 등급 차이는 오탐률 실측에서 나왔다.
