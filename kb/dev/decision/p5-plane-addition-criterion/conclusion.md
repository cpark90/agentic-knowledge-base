---
id: https://agentic-knowledge-base.dev/id/chunk/97ff6e27-ac14-4d59-bd25-6fc00d166861
type: decision
level: concrete
title_ko: 지식 종류 추가의 유일한 근거는 판정 방식이 다를 때다
former_title_ko: ["plane 추가의 유일한 근거는 판정 방식이 다를 때다"]
title: A new plane is justified only by a different verification mechanism
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0003-plane-by-verification.md, id: https://agentic-knowledge-base.dev/id/chunk-d0003, title_ko: "plane은 판정 방식으로 정의된다", title: "Planes are defined by verification mechanism"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:30:08+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0003]
part_of: https://agentic-knowledge-base.dev/id/composite/ab95f777-16da-41c6-8b1d-5f51f1484840
composite: {id: https://agentic-knowledge-base.dev/id/composite/ab95f777-16da-41c6-8b1d-5f51f1484840, title_ko: 지식 종류 추가 절차, title: Procedure for adding a plane, former_title_ko: ["plane 추가 절차"]}
---
**결론** — 지식 종류를 추가하는 **유일한 근거는 판정 방식이 기존 지식 종류 어디와도 다를
때**다. 판정 방식이 같으면 같은 지식 종류의 **하위 클래스**로 둔다.

후보 검토의 결과 — **`requirement`는 승격되어 코어가 일곱이 되었고, `ui`만
후보로 남는다.** 나머지는 하위 클래스나 다른 장치로 흡수된다.

`requirement` 승격의 귀결로 **functional이 `requirement` 전용이 되고
`decision`은 abstract 이하만 갖는다** (6.4절 수준 허용표).

미확정: 지식 종류 수의 상한(노트 5.3절, Q15-c·Q20-a로 이전).
