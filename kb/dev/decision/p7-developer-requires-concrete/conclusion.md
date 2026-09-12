---
id: https://agentic-knowledge-base.dev/id/chunk/a3be2d7b-c106-4026-9278-3b1d8e59f822
type: decision
level: concrete
title_ko: developer는 concrete 결정과 확정 스키마 없이 구현을 시작할 수 없다
title: A developer cannot start implementing without a concrete decision and a fixed schema
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af]
composite: {id: https://agentic-knowledge-base.dev/id/composite/fb8de557-6f61-436f-ae39-57f6c7019555, title_ko: 구현 착수 조건, title: Precondition for implementation}
part_of: https://agentic-knowledge-base.dev/id/composite/fb8de557-6f61-436f-ae39-57f6c7019555
---
**결론** — 저작 흐름의 2~6은 design 역할, 7은 developer 역할이다. **developer는 concrete 결정과 확정 스키마 없이 구현을 시작할 수 없다** — 스코프 conditional("결정이 concrete일 때만 `artifact` 쓰기")이 이것을 강제한다 (노트 7.3절, 3.4절). developer의 작업 집합에 `-space`는 들어오지 않는다 — 후보가 여럿인 상태는 developer에게 존재하지 않는다 (7.7절).
