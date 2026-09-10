---
id: https://agentic-knowledge-base.dev/id/chunk/2c2b0d83-f624-4d8a-bc06-a3953a64a455
type: decision
level: logical
title_ko: 시나리오가 decision이고 합격 기준이 contract인 이유
title: Why a scenario is a decision and a pass criterion is a contract
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8348f42d-da82-4b6f-b1a0-d31a93ff3d65
---
**근거** (노트 8.2절) — plane은 판정 방식으로 정의되므로(5.1절) 판정 방식이 같으면 같은 plane이다. 배정은 이름의 유사성이 아니라 판정 방식에서 따라 나온다.

- **시나리오가 `decision`인 이유** — 시나리오는 "무엇을 자극할 것인가"에 대한 결정이며 결론(자극)·근거(요인)·배제된 대안의 구성체 형태가 그대로 맞는다. 근거는 결함 요인이고, 배제된 대안은 ODD 밖이거나 다른 시나리오가 이미 덮는 자극이다.
- **합격 기준이 `contract`인 이유** — 기준은 verifier와 검증 대상 사이의 계약이다. "이 입력에 이 출력이면 통과"는 시그니처와 같은 성격이고, 판정식이 실행 가능한가라는 형식 검사로 판정된다.
- 새 plane을 만들면 판정 도구·shape·권한을 새로 정의해야 하고, 개발 KB와의 대응이 끊겨 가로대를 level로 맞출 수 없다 (7.3절).
