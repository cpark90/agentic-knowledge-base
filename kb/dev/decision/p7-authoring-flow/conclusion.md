---
id: https://agentic-knowledge-base.dev/id/chunk/5d09956e-4811-4c26-b1e4-1367209763a9
type: decision
level: concrete
title_ko: 요구 하나는 여덟 단계로 산출물이 되고 요구마다 독립적으로 정제한다
title: One requirement becomes an artifact in eight steps, and each requirement descends independently
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/71d2b786-e873-4705-b160-a443603ae0d2]
composite: {id: https://agentic-knowledge-base.dev/id/composite/8d167ee6-64e5-48ee-b34d-ed2d994669d1, title_ko: 개발 저작 흐름, title: The development authoring flow}
part_of: https://agentic-knowledge-base.dev/id/composite/8d167ee6-64e5-48ee-b34d-ed2d994669d1
---
**결론** — 요구 하나가 산출물이 되기까지의 순서. 6.2절 전이와 6.8절 게이트를 개발 역할의 작업 순서로 편 것이다 (노트 7.3절).

| 단계 | 역할 | 만드는 것 | 게이트 | V&V 대응물 (8.3절) |
|---|---|---|---|---|
| 1. 요구 작성 | 유저 + design | `requirement` — EARS, 이해관계자·관심사 | 형식 검사 + 승인 | 검증 목표 파생 |
| 2. 형식화 | design | `decision` abstract — 변수 선언, `serves` | 기여 없는 설계 거부 | — |
| 3. 계약 선언 | design | `contract` abstract — 시그니처 | 타입 검사 | — |
| 4. 전개 | design | `decision` logical(`-space`) / `contract` logical / `schema` logical | 판정식 없는 기준 강등 | 합격 기준 존재 |
| 5. 확정 | design + 유저 | `decision` concrete — 값, `-space` resolved | 표본·배제 근거 | 케이스 |
| 6. 스키마 확정 | design | `schema` concrete | 스키마 검사 | — |
| 7. 구현 | developer | `artifact` executable — 함수 | 컴파일·린터 + `satisfies`·`refines` | 검증기 존재 + 바인딩 |
| 8. 리뷰 | V&V 또는 다른 developer | `annotation` | 해소 | 판정 주석 |

순서는 요구 하나에 대한 것이지 프로젝트 전체가 폭포식이라는 뜻이 아니다. 요구마다 독립적으로 정제하고, 요구 간 순서는 `depends-on` 링크와 ODD 동적 갈래의 시간 제약이 정한다.
