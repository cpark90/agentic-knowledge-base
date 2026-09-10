---
id: https://agentic-knowledge-base.dev/id/chunk/ed543173-7943-418a-880a-818bb6cce52a
type: decision
level: concrete
title_ko: 하네스는 관측 사영과 행동 사영 둘을 담당한다
title: The harness owns two projections, observation and action
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0037, https://agentic-knowledge-base.dev/id/chunk-d0042]
part_of: https://agentic-knowledge-base.dev/id/composite/cca68a89-e572-4104-ba7e-cddd3c67c7bb
composite: {id: https://agentic-knowledge-base.dev/id/composite/cca68a89-e572-4104-ba7e-cddd3c67c7bb, title_ko: 부분관측의 형식화와 두 사영, title: Partial observability and the two projections}
---
**결론** — "에이전트는 부분관측 분산 시스템의 행위자"라는 전제를 형식화해 각
개념의 자리를 고정한다.

| 부분관측 모델의 요소 | 이 체계 |
|---|---|
| 상태 | 지식 베이스 + 환경의 현재 상태 |
| 관측 함수 | 스코프 — 상태에서 작업 집합을 만드는 질의 |
| 관측 | 작업 집합 |
| 행동 | 편집 연산. 링크의 부산물을 남김 (9.3절) |
| 신념 상태 | 에이전트의 `memory` plane |

하네스는 이 대응에서 **두 사영**을 담당한다 — 지식 베이스에서 작업 집합을 만드는
**관측 사영**(스코프)과, 제안된 행동을 실행 가능한 전이로 바꾸거나 근거를 들어
거부하는 **행동 사영**(검사 게이트). 학습 사영을 쓰더라도 **스코프와 게이트의
규칙이 학습 사영의 상한**이다 — 학습이 규칙을 넘으면 스코프가 무의미해진다.
