---
id: https://agentic-knowledge-base.dev/id/chunk-d0135
type: decision
level: concrete
title_ko: 커버리지의 분모와 단계별 합산
title: Coverage denominator and cross-rung accumulation
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 커버리지는 **측정 지표**이며 분모는 ODD다. 단계별로 합산하되
6단계(실환경) 관측은 넣지 않는다. **완전성을 전제한 무인 운영은 성립하지
않는다.**

**근거** (노트 10.1절)
- 분모가 ODD(3.3절)이므로 ODD 밖 조건은 커버리지의 대상이 아니고, ODD가
  커지면 같은 시나리오 집합의 커버리지가 떨어진다.
- ODD의 한 속성 조합이 **어느 단계에서든 한 번** 검증되면 커버된 것이다 —
  같은 조합을 단계마다 반복 검증할 필요가 없다.
- 6단계 관측을 빼는 이유 — 통제되지 않은 관측은 "그 조합이 시험되었다"는
  주장이 되지 못한다. 같은 이유로 시뮬레이션이 ODD 이탈
  시나리오(`odd:outside`)를 실행하는 것은 허용하되 커버리지에 넣지 않는다.
- 커버리지가 100이 될 수 없으므로 사전 시나리오가 모든 이상을 커버한다는
  전제 위에 무인 운영을 세울 수 없다 (10.5절과 같은 결론).
- 자율 진행을 허용할 커버리지 하한(커버리지 임계)은 입력이다 (9.1절).
