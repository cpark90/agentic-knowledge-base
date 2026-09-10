---
id: https://agentic-knowledge-base.dev/id/chunk/80c55e7a-50b7-4428-95f3-bd7f814c2411
type: decision
level: logical
title_ko: 표준 분류의 빈 범주만 채운다
title: Fill only the empty categories of the standard classification
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/42c1ecbe-34fd-4c59-9038-51db6144ad29
---
**근거** (노트 10.2절) — 추적성 연구의 표준 분류(의존 / 일반화·정련 / 진화 / 충족 / 근거)로 기존 타입을 정리하면 빈 범주가 드러난다. 채택 4종은 모두 빈 범주를 채우는 것이다 — 충족의 역할 할당(`allocates`), 의존(`depends-on`·`generates`), 그리고 아예 비어 있던 **양립 불가**(`conflicts-with`).

`conflicts-with`가 특별하다. Part VIII의 제약("A→X가 성립하면 B→Y는 불가")을 링크로 저장하면 **제약 자체가 추적 대상이 된다** — 누가 언제 왜 이 양립 불가를 정했는지가 PROV-O로 남는다.

타입 추가는 빈 범주를 채우는 방향으로만 한다. 이미 채워진 범주에 유사 타입을 더하면 9.1절 "TIM은 바꾸기 어렵다"의 비용만 든다.
