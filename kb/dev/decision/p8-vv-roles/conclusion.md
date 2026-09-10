---
id: https://agentic-knowledge-base.dev/id/chunk/cf8fcbbf-d356-4c6d-af23-d4b26ce3ba75
type: decision
level: concrete
title_ko: V&V KB에는 다섯 역할이 쓰고 기준 저자와 검증기 저자는 다른 세션이다
title: Five roles write to the V&V KB; criteria author and 검증기 저자 work in different sessions
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7, https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/ba638521-e9b0-4c38-b073-44230ac22785]
composite: {id: https://agentic-knowledge-base.dev/id/composite/666bd423-dc26-4857-9841-c1e3aa131223, title_ko: V&V 역할, title: V&V roles}
part_of: https://agentic-knowledge-base.dev/id/composite/666bd423-dc26-4857-9841-c1e3aa131223
---
**결론** — V&V KB에 쓰기 권한을 갖는 역할 (노트 8.20절).

| 역할 | 쓰기 | 읽기 | 책임 |
|---|---|---|---|
| V&V engineer | `requirement`·`decision`·`contract`·`schema`(vv) | 개발 KB 전부 | 검증 목표·시나리오·기준 저작 |
| 검증기 저자 | `artifact`(vv) | 개발 KB `contract`·`schema`, V&V 기준 | 검증기 구현 |
| executor (하네스) | `memory`(vv) | 케이스, 검증기 | 실행·관측 기록 |
| judge | `annotation`(vv) | 실행 기록, 기준 | 결함 분류, 통과/실패 확정 |
| audit | 없음 | 두 KB 전부 | 독립성·커버리지 감사 |

작은 팀에서는 한 에이전트가 engineer와 author를 맡되 **다른 세션**에서 한다. judge는 학습된 판정자일 수 있고(8.14절), 그 경우 판정 결과가 청크 head `verified` 목록에 남으며 사람 승인이 `stable` 전이의 조건이다.
