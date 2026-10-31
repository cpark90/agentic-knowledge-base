---
id: https://agentic-knowledge-base.dev/id/chunk/53ab4452-1b2f-494f-afb8-8706debe19f0
type: decision
level: concrete
title_ko: 각 지식 종류는 정해진 level 구간에만 거주한다 — 격자는 성기다
former_title_ko: ["각 plane은 정해진 level 구간에만 거주한다 — 격자는 성기다"]
title: Each plane occupies only its own level band - the grid is sparse
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0084-plane-level-grid.md, id: https://agentic-knowledge-base.dev/id/chunk-d0084, title_ko: "모든 plane이 다섯 level을 갖는다 — plane × level 격자", title: "Every plane has all five levels - the plane x level grid"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-15T15:50:42+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0084]
part_of: https://agentic-knowledge-base.dev/id/composite/8387ed4f-09c5-48b5-b682-704a045a79a1
composite: {id: https://agentic-knowledge-base.dev/id/composite/8387ed4f-09c5-48b5-b682-704a045a79a1, title_ko: 지식 종류 × level 수준 허용표, title: The plane x level occupancy table, former_title_ko: ["plane × level 수준 허용표"]}
---
**결론** — level이 정제 수준이므로 **모든 지식 종류가 모든 level을 갖지 않는다.** 각 지식 종류는 정해진 구간에만 거주한다.

- `requirement` — functional **전용**
- `decision` — abstract(결정 변수 선언) · logical(후보·제약·배제 근거·기준) · concrete(확정된 값)
- `contract` — abstract(시그니처 변수) · logical(타입 범위·계약 조건·판정 술어)
- `schema` — logical(필드 범위·호환 제약) · concrete(확정 스키마)
- `artifact` — concrete(고정 입력·설정) · executable **전용**(구현/검증)
- `memory` — concrete(관측)만
- `annotation` — 임의 level의 단위 지식을 `targets` 하고 **자기 level은 대상의 level**

**거주 밖의 조합은 shape 위반이다.** 요구에 `level: logical`을 붙이면 검사 게이트가 거부한다.

`contract`·`schema`의 logical 칸이 실체인가 뷰인가는 계약 logical 공간 `https://agentic-knowledge-base.dev/id/chunk/6a2c53a6-5833-4a8c-a773-f1d0bee785cc`이 답했다. 독립 내용이고 후보를 logical 단위 지식으로 둔다(`p6-contract-logical-is-content`, Q79-a).

**게이트** (노트 6.4절) — 거주 밖의 조합은 shape `residency-shapes`가 거부하고 게이트 id는 `shacl`이다. 해소는 저작자가 수준이나 지식 종류를 고치는 것이다. 허용표의 단일 정의 위치는 `defs/kb.bzl`의 `RESIDENCY`다. Starlark는 파일을 읽지 못하므로 분석 시점 판정을 지키려면 표가 거기 있어야 한다. `kb_lib.load_residency`가 그 리터럴을 읽어 파생하고 `metrics`의 사본은 없앴다. shape의 구간이 리터럴과 갈리면 `validate`의 `check_residency`가 verify 실행 계층의 게이트 `residency`로 거부하고(2026-09-26), developer가 shape를 원본에 맞춘다.
