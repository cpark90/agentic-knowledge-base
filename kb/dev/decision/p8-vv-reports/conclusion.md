---
id: https://agentic-knowledge-base.dev/id/chunk/25cf6714-8a00-45b7-8efa-426dda90e785
type: decision
level: concrete
title_ko: 보고서는 저장하지 않고 투영하며 표준 보고 다섯과 지표 일곱을 읽는다
title: Reports are projected, not stored; five standard reports over seven metrics
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
composite: {id: https://agentic-knowledge-base.dev/id/composite/12dac333-3480-43ae-9b38-2884efe35bd0, title_ko: 검증 보고, title: Verification reporting}
part_of: https://agentic-knowledge-base.dev/id/composite/12dac333-3480-43ae-9b38-2884efe35bd0
---
**결론** — 보고서는 저장하지 않고 투영한다 (4.6절). 표준 보고 다섯 (노트 8.24절): **검증 상태**(요구별 목표·기준·verifier 수, 마지막 실행 결과, `verifies` 상태 — level×level 매트릭스 + 실행 기록) · **커버리지**(하강 완주율·상향 귀속률·logical 공간 커버·경계값 커버) · **결함**(요인·트리거·발견 단계 분포 — `defect-rules`) · **가정 건전성**(`invalidated`·`unverified` 가정과 의존 청크 수) · **독립성**(개발 역할이 V&V KB에 쓴 흔적, 0이어야 함).

보고서에 생성 시각·리비전·질의를 적는다. 유저 에스컬레이션(11.1절 커버리지 임계)의 근거가 이 보고서다. V&V KB의 지표 일곱(8.26절): 목표 파생률 · 기준 바인딩률 · V&V 하강 완주율 · 실행 통과율 · 변이 검출률 · 재현 실패율 · 가로대 지연.
