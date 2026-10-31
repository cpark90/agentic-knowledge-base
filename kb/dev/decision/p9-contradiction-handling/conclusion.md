---
id: https://agentic-knowledge-base.dev/id/chunk/5fecc471-fe63-4526-9dca-9ba0bf3c2a77
type: decision
level: concrete
title_ko: 모순은 자동으로 풀지 않고 유저에게 넘긴다
title: Contradictions are handed to the user, never auto-resolved
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0103-contradiction-handling.md, id: https://agentic-knowledge-base.dev/id/chunk-d0103, title_ko: "후보 없음(모순)은 자동으로 풀지 않고 유저에게 넘긴다", title: "Contradictions are handed to the user, never auto-resolved"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0103]
part_of: https://agentic-knowledge-base.dev/id/composite/60c37dde-858e-4e6a-b878-b8340bcef798
composite: {id: https://agentic-knowledge-base.dev/id/composite/60c37dde-858e-4e6a-b878-b8340bcef798, title_ko: 모순은 자동으로 풀지 않고 유저에게 넘긴다, title: Contradictions are handed to the user, never auto-resolved}
---
**결론** — 후보가 하나도 남지 않은 상태는 **모순 신호**다. 체계는 이것을 **자동으로 풀지 않는다.** 세 원인 중 무엇인지 판별한 결과와 함께 유저에게 넘긴다.

상위 지식 종류의 단위 지식을 고쳐야 풀리는 모순이라도 단방향 규칙상 자동 전파가 불가능하므로, 상위 재검토는 유저 판단으로만 시작된다.
