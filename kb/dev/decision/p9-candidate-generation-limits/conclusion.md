---
id: https://agentic-knowledge-base.dev/id/chunk/0f68d642-0020-443f-9876-072e8832b270
type: decision
level: concrete
title_ko: 후보 링크에는 출처와 상한이 있다
title: Candidate links have a source and an upper bound
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0102-candidate-generation-limits.md, id: https://agentic-knowledge-base.dev/id/chunk-d0102, title_ko: "후보 링크의 출처와 상한", title: "Candidate link sources and their upper bounds"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-26T22:31:39+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-26T22:31:39+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0102]
part_of: https://agentic-knowledge-base.dev/id/composite/24a2256b-3151-4896-a1f5-712d76f8b4fc
composite: {id: https://agentic-knowledge-base.dev/id/composite/24a2256b-3151-4896-a1f5-712d76f8b4fc, title_ko: 후보 링크에는 출처와 상한이 있다, title: Candidate links have a source and an upper bound}
---
**결론** — 후보 링크 집합에는 **상한이 있어야 한다.** 상한이 있어야 후보 집합이 단위 지식 라벨 목록 안에 들어가고, 에이전트가 한 화면에서 조망할 수 있다.

복원으로 만드는 후보의 상위 `k`도 **7±2 원칙을 따른다 — `k ≤ 7`.**

상한 안에 드는 후보는 근거 순위, 공유 개념 수, 대상 IRI 순서로 정한다. 라벨은 표시 순서에만 쓰고 어느 후보가 상한 안에 드는지에는 쓰지 않는다. 라벨 순서로 자르면 라벨만 고쳐도 뷰와 사람 확인 큐의 구성이 바뀐다. 실제로 task 0301이 두 단위 지식의 라벨을 바꾸자 앵커 일곱에서 후보 11쌍이 들어오고 11쌍이 밀려났다(result 0319). 이 순서는 2026-10-26 유저 결정이다(Q-0073 Q169-a).

상한을 넘는 후보 집합은 후보를 더 만들 문제가 아니라 변수를 잘못 잡았다는 신호로 읽는다.
