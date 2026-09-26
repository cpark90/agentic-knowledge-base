---
id: https://agentic-knowledge-base.dev/id/chunk/889cd3dc-d652-4e79-b911-9a052216801b
type: decision
level: concrete
title_ko: 검증 대상은 둘이되 verifies의 도착점은 개발 KB 청크 하나다
title: There are two verification targets, but verifies points only at development KB chunks
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/1346522d-0e9b-4a3d-9390-082cf9aa47f3]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-24T10:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/70615ceb-7f52-4c6f-ae72-3d83ab59dbe0
composite: {id: https://agentic-knowledge-base.dev/id/composite/70615ceb-7f52-4c6f-ae72-3d83ab59dbe0, title_ko: 에이전트 검증의 도착점, title: Where agent verification points}
---
**결론** — 검증 대상은 제품과 에이전트 둘이다. 그러나 **`verifies`의 도착점은 둘 다 개발 KB 청크**다. 나뉘는 것은 도착점의 종류가 아니라 **겨누는 결정의 종류**다.

| 대상 | 자극 | `verifies` 도착점 |
|---|---|---|
| 제품 | concrete 케이스 — 입력 데이터·외부 서비스 응답·사용자 행동 | 산출물을 정한 `decision`·`contract`의 기준 |
| 에이전트 | 작업 집합과 유저 피드백 | **역할·스코프·작업 집합을 정한 결정과 요구** |

에이전트 검증의 검증 목표는 카탈로그 역할(`id:role-*`)의 책임에서 파생하고, 합격 기준은 이미 도는 게이트다 — shape 통과·`refines` 완주·게이트 통과율이다.

이 결정은 `p8-two-verification-targets`를 대체한다. 옛 결론은 에이전트 검증이 하네스·스코프 개체를 도착점으로 삼는다고 적었으나 그 개체는 청크가 아니라 A-Box 개체라 `verifies`의 대상이 될 수 없다. **검증 대상 둘이라는 구분은 그대로 남는다.** 없어지는 것은 도착점의 종류가 둘이라는 부분뿐이다.

`defs/kb.bzl`의 링크 규칙과 게이트는 바뀌지 않는다. 검사 약화가 없다.
