---
id: https://agentic-knowledge-base.dev/id/chunk/2c7d59a4-3581-4f91-9eaa-9175bc0cee55
type: decision
level: logical
title_ko: 분리의 이유는 독립성이고 연동의 이유는 완주다
title: Separation buys independence; coupling buys completion of the descent
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/ff2266a5-716f-41ad-a738-292aca41f27b
---
**근거** (노트 8.1절) — **분리의 이유는 독립성이다.** 만든 쪽이 판정 기준을 고치면 검증은 형식이 된다. V&V KB를 개발 역할이 쓸 수 없게 하는 것이 판정의 독립을 구조로 보장하는 유일한 방법이다.

- **연동의 이유는 완주다.** 개발 계층의 각 높이에 V&V 계층의 같은 높이가 대응하고, 둘 사이의 검증 대응물(`verifies`)가 없으면 개발 계층가 다음 높이로 내려갈 수 없다 (7.3절). 검증이 개발 뒤의 단계가 아니라 같은 시점의 산출물이 된다.
- 코어을 새로 만들지 않는 이유는 두 벌의 규칙이 생기면 어느 쪽 규칙으로 판정하는지가 매번 문제가 되기 때문이다. 같은 청크·plane·level·링크를 쓰고 실체만 바꾼다 (7.2절).
- 되먹임은 링크가 아니라 일반화으로 간다 — 실행 기록과 결함이 요구·ODD를 고치는 경로다 (7.4절·7.5절).
