---
id: https://agentic-knowledge-base.dev/id/chunk/53ab4452-1b2f-494f-afb8-8706debe19f0
type: decision
level: concrete
title_ko: 각 plane은 정해진 level 구간에만 거주한다 — 격자는 성기다
title: Each plane occupies only its own level band - the grid is sparse
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0084]
part_of: https://agentic-knowledge-base.dev/id/composite/8387ed4f-09c5-48b5-b682-704a045a79a1
composite: {id: https://agentic-knowledge-base.dev/id/composite/8387ed4f-09c5-48b5-b682-704a045a79a1, title_ko: plane × level 수준 허용표, title: The plane x level occupancy table}
---
**결론** — level이 정제 수준이므로 **모든 plane이 모든 level을 갖지 않는다.** 각 plane은 정해진 구간에만 거주한다.

- `requirement` — functional **전용**
- `decision` — abstract(결정 변수 선언) · logical(후보·제약·배제 근거·기준) · concrete(확정된 값)
- `contract` — abstract(시그니처 변수) · logical(타입 범위·계약 조건·판정식)
- `schema` — logical(필드 범위·호환 제약) · concrete(확정 스키마)
- `artifact` — concrete(고정 입력·설정) · executable **전용**(구현/검증)
- `memory` — concrete(관측)만
- `annotation` — 임의 level의 청크를 `targets` 하고 **자기 level은 대상의 level**

**거주 밖의 조합은 shape 위반이다.** `requirement` 청크에 `level: logical`을 붙이면 검사 게이트가 거부한다.
