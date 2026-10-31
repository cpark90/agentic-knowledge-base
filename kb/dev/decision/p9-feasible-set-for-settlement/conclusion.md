---
id: https://agentic-knowledge-base.dev/id/chunk/d8fdd8fc-692f-430e-8d89-6542564f6626
type: decision
level: concrete
title_ko: 확정의 표현에서 링크의 가능성은 가능 집합이고 믿음 정도는 그 위에 병기한다
title: In the settled representation link possibility is a feasible set, with a degree of belief alongside
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-22T20:50:46+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:11:22+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/204c3abf-f882-4a82-92d0-a375d4e859e2]
composite: {id: https://agentic-knowledge-base.dev/id/composite/b735df63-3e97-47c1-946e-2f9d10e0aa04, title_ko: 확정의 표현으로서의 가능 집합, title: The feasible set as the settled representation}
part_of: https://agentic-knowledge-base.dev/id/composite/b735df63-3e97-47c1-946e-2f9d10e0aa04
---
**결론** — 확정의 표현에서 연결의 가능성은 **가능 집합**이다. 링크에 붙는 판정 값은 `가능` / `불가능` 둘이고, 판정은 제약 검사로 이루어지며 결정론적이다.

- 표준 명칭은 **제약 만족(constraint satisfaction)**이다. 기계 검사로 충분하다.
- 선호(연성 제약)는 후보 사이의 **부분순서**로 얹는다 (8.9절).
- 증거에서 계산한 **믿음 정도**([0,1])는 가능한 후보 곁에 병기할 수 있다. 가능 집합을 넓히거나 줄이지 않고, 확정·배제의 판정에 들지 않는다(r-011 개정, Q90-a). 그 계산과 보정은 설계 공간 '믿음 정도의 계산과 보정'이 정한다.
