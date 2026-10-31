---
id: https://agentic-knowledge-base.dev/id/chunk/f756f425-70ed-4158-9675-e2240ffdf3c0
type: decision
level: concrete
title_ko: 명세는 검증 가능한 계약이고 검사 게이트는 세 방향이다
title: A specification is a verifiable contract, and the check gates run in three directions
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0182-spec-as-verifiable-contract.md, id: https://agentic-knowledge-base.dev/id/chunk-d0182, title_ko: "명세는 검증 가능한 계약이고 검사 게이트는 세 방향이다", title: "A spec is a verifiable contract and gate checks run in three directions"}, {resource: git:aeb0a58:chunks/decision/d-0190-verifiable-spec-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0190, title_ko: "대안 — 검증 가능한 명세", title: "Alternatives — specification as verifiable contract"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0182, https://agentic-knowledge-base.dev/id/chunk-d0190]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/bff15384-be48-4304-95be-bcc0f46ef542
composite: {id: https://agentic-knowledge-base.dev/id/composite/bff15384-be48-4304-95be-bcc0f46ef542, title_ko: 검증 가능한 계약인 명세, title: Specification as a verifiable contract}
---
**결론** — 명세는 이렇게 되어 있다는 주장이 아니라 **기계가 판정할 수 있는 계약**으로 쓰며, 같은 명세가 생성의 입력이자 검증의 기준이 된다. 그리고 검사 게이트는 서로 다른 **세 방향**이어서, 하나의 초록이 나머지를 말해 주지 않는다.

| 방향 | 묻는 것 |
|---|---|
| 구조 | 저장된 그래프가 연결과 타입, 충족을 만족하는가 |
| 원천에서 명세로 | 원천의 구조 요소가 모두 표현되었는가(coverage audit, `p12-composition-workflow`) |
| 명세에서 산출로 | 만들어진 것이 명세의 계약을 만족하는가 |
