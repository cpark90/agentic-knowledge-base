---
id: https://agentic-knowledge-base.dev/id/chunk/9c1f0e81-8372-48a1-8b8a-ce9753e86988
type: decision
level: logical
title_ko: 배정 조건으로 두어야 강등이 자동으로 따라온다
title: Only as an assignment condition does demotion follow automatically
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c71e12a1-2a31-43f5-af40-c670d767f559
---
**근거** (노트 8.12절) — 재현성을 배정의 조건으로 두면 강등이 자동으로 따라온다. 청크의 속성으로 두면 "재현 불가"라고 적힌 채 1단계에 남아 커버리지에 계산되고, 통제된 시험이 아닌 것이 시험으로 세어진다 (7.10절 합산 규칙).

- 다섯 기록 중 하나만 빠져도 같은 결과가 나오지 않는다. 특히 KB 리비전과 ODD 버전이 빠지면 자극이 같아도 판정 기준이 달라진다 — 검증 대상 자체가 바뀌기 때문이다.
- 억지로 케이스화하지 않는 이유는 재현되지 않는 관측을 concrete로 올리면 커버리지가 부풀고 상승의 입력 품질이 떨어지기 때문이다. 6단계 관측으로 남겨 두는 것이 정직한 기록이다 (r-026).
