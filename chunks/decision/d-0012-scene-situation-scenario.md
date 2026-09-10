---
id: https://agentic-knowledge-base.dev/id/chunk-d0012
type: decision
level: concrete
title_ko: scene·situation·scenario 3분리
title: Scene, situation, scenario separation
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T19:48:09+09:00}
---
**결론** — 인접한 세 개념을 관측자 관점의 유무로 분리한다.
scene은 특정 시점의 시스템 상태 스냅샷(관측자 없음), situation은 scene
중 특정 에이전트의 스코프와 목표로 걸러진 부분(관측자 있음), scenario는
scene의 시간열 + 행위자의 행동 + 트리거(관측자 없음).

**근거** (노트 0.5절)
- situation이 인지능력 측정의 단위다 — 입력 정보량은 scene 전체가 아니라
  그 에이전트의 situation으로 잰다. scene 대비 누락은 스코프 설계 문제,
  situation 대비 누락은 에이전트의 문제로 갈라진다.
- 트리거가 있어야 시나리오가 시간열이 된다. 트리거 없는 행동 목록은
  시나리오가 아니라 절차(Runbook)다.
- 시나리오(처방적 명세)와 실행 기록 agt:Run(관측, concrete 전용,
  append-only)을 같은 이름으로 부르면 관측을 명세로 올리는 일반화
  단계가 사라진다.

**분류는 태그로** — 시나리오·실행 기록의 범주화는 계층이 아니라 태그
집합으로 한다. 최선의 계층은 존재하지 않고, 계층을 강제하면 첫 분기
기준이 나머지를 지배한다. 태그 값은 온톨로지 개념이어야 한다.
