---
id: https://agentic-knowledge-base.dev/id/chunk/f50c86b2-b06c-45b9-8585-08b4f14565b6
type: decision
level: concrete
title_ko: 에이전트 V&V는 제품 V&V와 같은 사슬이되 실체가 다르고 부류는 하네스에 종속된다
title: Agent V&V shares the product chain with different substance; its classes depend on the harness
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
composite: {id: https://agentic-knowledge-base.dev/id/composite/a47a3cfd-e9df-401a-90d1-d49cfff12452, title_ko: 에이전트 V&V, title: Agent V&V}
part_of: https://agentic-knowledge-base.dev/id/composite/a47a3cfd-e9df-401a-90d1-d49cfff12452
---
**결론** — 8.8절 두 대상 중 에이전트 쪽의 상세. 제품 V&V와 같은 사슬이되 실체가 다르다 (노트 8.25절).

| 요소 | 제품 V&V | 에이전트 V&V |
|---|---|---|
| 검증 목표 | 요구에서 | 카탈로그 역할의 책임에서 |
| 시나리오 actor | 클라이언트·외부 서비스 | 에이전트, 자동 응답 유저, 시뮬레이션 프로젝트 |
| 자극 | 입력 데이터·응답 | 작업 집합 + 요구 + (의도된) ODD 이탈 |
| 기준 | 계약 사후조건 | shape 통과, `refines` 완주, 인지 누락률, 게이트 통과율, 안전 정지 |
| 환경 | 단위 → 실환경 | 시뮬레이션 프로젝트(3단계) 중심 |
| 결함 | 실행 요인 위주 | 인지 요인 위주 |
| 되먹임 | 요구·결정 | 스코프·카탈로그·승격 규칙 (입력) |

에이전트 V&V의 시나리오 부류(G5)는 도메인이 아니라 **하네스에 종속**된다. 프로젝트를 넘어 재사용되되 하네스 버전이 바뀌면 재검토한다.
