---
id: https://agentic-knowledge-base.dev/id/chunk-d0133
type: decision
level: concrete
title_ko: 시뮬레이션 프로젝트가 에이전트 검증의 중심
title: The simulation project is the core of agent verification
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 에이전트 검증의 중심을 사다리 3단계의 **시뮬레이션 프로젝트**에
둔다. 실제 서비스의 서브셋을 게임처럼 격리 구축하고, 미리 정의한 문제
(시나리오)를 에이전트가 해결하게 한다. 유저 피드백은 자동 응답으로 대체하고
seed를 고정한다.

**근거** (노트 10.1절)
- 에이전트의 인식과 행동 범위가 **스코프로 정해져 있으므로** 시뮬레이션
  안에서의 관측이 실환경과 같은 형태다 — 관측을 그대로 상승(6.3절)의
  입력으로 쓸 수 있다.
- 시뮬레이션에서 생긴 문제는 **실환경 유저 개입 없이** 검토할 수 있다.
  에이전트 결함을 실제 유저에게 노출시키지 않고 반복 관측할 수 있는
  단계는 여기가 마지막이다.
- 인지 요인 결함은 3단계 아래에서 잡히지 않는다 (10.1절 환경 배정) —
  situation을 조립해 에이전트가 실제로 행동해야 드러나기 때문이다.
- 평가(10.3절)의 인지능력 측정도 여기서 기록된 situation을 재생해 한다.
