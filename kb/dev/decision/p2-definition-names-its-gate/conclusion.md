---
id: https://agentic-knowledge-base.dev/id/chunk/0ea16a47-6e97-451e-bc6a-93c9154824d6
type: decision
level: concrete
title_ko: 정의문의 규칙 문장은 실행 자리를 이름 짓거나 절차 규범임을 표시한다
title: A rule sentence in a definition names its executing gate or is marked as a procedural norm
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-26T15:10:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/fc9c449c-45c7-4951-929d-b201dd7c2d45
composite: {id: https://agentic-knowledge-base.dev/id/composite/fc9c449c-45c7-4951-929d-b201dd7c2d45, title_ko: 정의문의 규칙과 그 실행 자리, title: Rules in definitions and where they execute}
---
**결론** — 온톨로지 `skos:definition`이 데이터에 대해 참·거짓이 갈리는 문장을 품으면, 그 문장은 셋 중 하나여야 한다.

| 갈래 | 조건 | 정의문에 적는 것 |
|---|---|---|
| 실행된다 | shape·질의·분석 시점·도구 검사 중 어느 하나가 판정한다 | 그 자리의 이름(`게이트: residency-shapes` 같이) |
| 옮긴다 | 기계 판정이 가능한데 자리가 없다 | 자리를 세운 뒤 위와 같이 적는다 |
| 절차 규범이다 | 의미 판정·시점 비교·서열 같은 것이라 기계가 판정하지 못한다 | "리뷰 규범이다" 또는 "게이트가 아니다"를 문장 끝에 붙인다 |

넷째 갈래는 없다. 실행되지도 않고 옮길 수도 없으며 절차 규범도 아닌 문장은 규칙이 아니라 희망이므로 정의문에서 뺀다.

2026-09-26 전수 판정 — 정의문 154개 중 52개가 규칙 문장을 품었다. 실행되는 것 29, 옮길 것 14(그중 상태 전이 5는 링크 상태 유도가 켜진 2026-09-26 이후 `assume_check`가 자리다), 절차 규범 9다. 표본이었던 `refines`의 "후보 상한 1"은 청크당도 전이당도 아니라 **설계 공간에서 변수 하나가 확정하는 링크가 하나**라는 뜻이고 게이트 `space`가 이미 실행한다.

두 가지로 읽히는 문장은 **시행된 읽기**로 고친다. 복합체의 "부분 수준 동일"은 결정 복합체를 제외한 형태로 2026-09-13에 이미 좁혀졌으나 정의문이 남아 있었다.
