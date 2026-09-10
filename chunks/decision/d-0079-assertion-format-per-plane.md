---
id: https://agentic-knowledge-base.dev/id/chunk-d0079
type: decision
level: concrete
title_ko: assertion 본문 형식은 plane마다 다르다
title: Assertion body format differs per plane
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 청크의 assertion 그래프는 공통 형식을 강요하지 않고 plane마다
그 plane의 판정 도구가 읽는 형식을 그대로 쓴다.

| plane | 형식 |
|---|---|
| `decision` | 구조화 산문 — 역할 태그(결론/근거/대안) + 본문 |
| `contract` | 언어 네이티브 선언 |
| `schema` | 스키마 언어 (JSON Schema, protobuf 등) |
| `artifact` | 언어 네이티브 코드 |
| `annotation` | 산문 + 대상 청크 IRI |
| `memory` | 구조화 관측 — 시각, 행동, situation 요약 |

**근거** (노트 4.12절)
- plane은 판정 방식으로 정의되므로, 본문이 그 plane의 판정 도구가 읽는
  형식이어야 검사가 성립한다. 공통 형식으로 감싸면 판정 전에 변환이
  필요해지고 변환이 드리프트의 자리가 된다.
- 42줄의 단위는 `memory`를 뺀 전 plane에서 **줄**이다.

**대안 (미확정)** — 노트가 이 절을 `[안]`으로 둔다. `memory`의 42줄은 줄이
아니라 **항목 수**여야 할 수 있고, 이는 "42줄이 모든 plane에 적정한가"
(4.9절 미해결)와 같은 문제다. 시그니처 청크는 훨씬 짧고 논증 청크는 부족할
수 있으므로, plane별 shape에서 상한을 달리 둘지 하나로 유지하고 분할을
강제할지가 남아 있다.
