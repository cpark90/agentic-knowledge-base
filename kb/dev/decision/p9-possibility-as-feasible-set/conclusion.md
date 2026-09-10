---
id: https://agentic-knowledge-base.dev/id/chunk/204c3abf-f882-4a82-92d0-a375d4e859e2
type: decision
level: concrete
title_ko: 링크의 가능성은 확률이 아니라 가능 집합이다
title: Link possibility is a feasible set, not a probability
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0097]
part_of: https://agentic-knowledge-base.dev/id/composite/3d6c3728-c1d8-4bc4-8d9e-f6963425410c
composite: {id: https://agentic-knowledge-base.dev/id/composite/3d6c3728-c1d8-4bc4-8d9e-f6963425410c, title_ko: 링크의 가능성은 확률이 아니라 가능 집합이다, title: Link possibility is a feasible set, not a probability}
---
**결론** — 연결의 가능성은 **가능 집합**으로 표현한다. 링크에 붙는 값은 `가능` / `불가능` 둘뿐이고, 판정은 제약 검사로 이루어지며 **결정론적**이다.

- 표준 명칭은 **제약 만족(constraint satisfaction)**. 기계 검사로 충분하다.
- 선호(연성 제약)는 후보 사이의 **부분순서**로만, 필요할 때 얹는다 (8.9절). 수치는 붙이지 않는다.
- 등급(가능성 측도·확률 [0,1])은 **미채택**이다.

가능 집합 수준에서 시작한다.
