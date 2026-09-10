---
id: https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869
type: decision
level: concrete
title_ko: 개발 프로파일에서 일곱 plane의 실체·거주 수준·단위·판정 도구
title: Substance, residency, unit and verification tool of the seven planes in the development profile
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
composite: {id: https://agentic-knowledge-base.dev/id/composite/ec197591-b1c7-494e-bc07-2f27b96cd057, title_ko: 개발 프로파일의 plane 실체, title: Plane substance in the development profile}
part_of: https://agentic-knowledge-base.dev/id/composite/ec197591-b1c7-494e-bc07-2f27b96cd057
---
**결론** — 개발 프로파일(부록 D)에서 일곱 plane의 실체. 6.4절 수준 허용표를 개발 관점에서 다시 읽은 것이다 (노트 7.2절).

| plane | 실체 | 거주 수준 | 청크의 단위 | 판정 도구 |
|---|---|---|---|---|
| `requirement` | 요구 문장, EARS 다섯 패턴 중 하나 | functional | 요구 하나 | 이해관계자 승인 |
| `decision` | 설계 결정, ADR 형식 | abstract → concrete | 결론 / 근거 / 대안 각각 | 논증 구조 검사 + 유저 승인 |
| `contract` | 인터페이스 시그니처, 사전·사후조건 | abstract → logical | 시그니처 하나 | 타입 체커 |
| `schema` | 메시지·필드 정의 | logical → concrete | 메시지 하나 | 스키마 검사기 |
| `artifact` | 함수. 구현 역할만 (verifier는 V&V KB) | executable | 함수 하나 (≤42줄) | 컴파일·린터·V&V 검증기 |
| `annotation` | 코드 리뷰 코멘트, 설계 리뷰 | 대상의 수준 | 코멘트 하나 | 해소 |
| `memory` | 세션 관측 | concrete | 관측 하나 | — |
