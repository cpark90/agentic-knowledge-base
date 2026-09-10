---
id: https://agentic-knowledge-base.dev/id/chunk/7689649d-91bd-4238-9873-39caa8461cf0
type: decision
level: logical
title_ko: 지표는 이 파트의 규칙이 실제로 지켜지는지를 잰다
title: Each metric measures whether one rule of this part still holds
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/759aa68a-d77b-425c-b819-42ead2a9b0e9
---
**근거** (노트 10.14절) — 다섯 지표는 각각 이 파트의 결정 하나가 무너지는 것을 감지한다 — 링크 밀도와 복원 비율은 "구축이 기본"(9.3절)이 지켜지는지를, `suspect` 비율과 평균 재판정 지연은 경계 일괄 재판정(9.6절)이 밀리지 않는지를, 확정 정밀도는 판정 근거 서열(9.8절)이 적절한지를 잰다.

지표는 링크 속성(9.10절)의 시각과 상태에서 계산되므로 별도 계측을 두지 않는다.
