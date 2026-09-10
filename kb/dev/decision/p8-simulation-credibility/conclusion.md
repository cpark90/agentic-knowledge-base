---
id: https://agentic-knowledge-base.dev/id/chunk/bdb1f8b2-86ba-44fa-8005-1e49d4ccc031
type: decision
level: concrete
title_ko: 시뮬레이션의 신뢰도는 요인별로 관리한다
title: Simulation credibility is managed factor by factor
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0138]
part_of: https://agentic-knowledge-base.dev/id/composite/962ef704-4544-41b5-8b6d-bea52f11c595
composite: {id: https://agentic-knowledge-base.dev/id/composite/962ef704-4544-41b5-8b6d-bea52f11c595, title_ko: 시뮬레이션의 신뢰도, title: Credibility of the simulation}
---
**결론** — 시뮬레이션이 실환경을 대신하려면 **시뮬레이션 자체가 검증되어야 한다.** 신뢰도 근거는 넷이다.

- **상관** — 같은 검증 청크를 시뮬레이션과 실환경에서 실행해 결과 대조. 불일치가 시뮬레이션 결함
- **이탈 관측** — 실환경에서만 발견된 결함(트리거 = 실행 시)의 비율. 높으면 시뮬레이션이 그 요인을 못 잡는 것
- **mock 계약** — mock이 실제 서비스의 `schema` 청크를 준수하는지 shape 검사
- **합성 데이터 분포** — 합성 데이터가 ODD 동적 요소의 값 범위 안인지

신뢰도는 **요인별로** 기록한다 — "시뮬레이션이 믿을 만하다"가 아니라 "순서·동기화 요인에 대해서는 믿을 만하고 실제 사용자 분포에 대해서는 아니다"로 적는다. 이것이 환경 배정표(7.10절)의 근거를 갱신한다.
