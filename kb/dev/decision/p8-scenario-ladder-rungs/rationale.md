---
id: https://agentic-knowledge-base.dev/id/chunk/68ac1095-a83b-4b37-b61c-2053c833aa68
type: decision
level: logical
title_ko: 검증 대응물를 게이트 조건으로 두면 검증을 나중으로 미룰 수 없다
title: Making the rung a gate condition makes deferred verification impossible
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0ef3233e-c6aa-434b-a0ef-350c857e690e
---
**근거** (노트 8.3절) — 검증 대응물를 게이트의 통과 조건으로 두면 "검증은 나중에"가 구조적으로 불가능해진다. 개발 계층가 혼자 내려가면 산출물이 나온 뒤에야 무엇으로 판정할지 정하게 되고, 그때 기준은 산출물에 맞춰진다.

- 세 높이만 필수인 이유 — abstract는 형식화의 중간 표현이라 대응물이 없어도 다음 높이에서 기준이 요구된다. 나머지 셋은 각각 목표·기준·실행이 빠지면 검증이 성립하지 않는 지점이다.
- 변수를 ODD 속성으로 제한하는 이유 — ODD에 없는 속성을 자극하면 그 통과가 설계 범위 안의 통과를 뜻하지 않는다. ODD 밖 자극은 `odd:outside` 태그로 존재할 수 있되 커버리지에 들지 않는다 (7.15절).
- `refines` 연쇄가 끊기면 V&V KB의 전방 추적 커버리지에 잡힌다 — 두 KB에 각각 완주율이 있다 (7.7절).
