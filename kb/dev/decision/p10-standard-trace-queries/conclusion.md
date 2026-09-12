---
id: https://agentic-knowledge-base.dev/id/chunk/9245ee8e-581f-44df-a08b-3a386eecbded
type: decision
level: concrete
title_ko: 링크 모델은 영향 분석·커버리지·근거 추적·상태 집계 네 질의에 답해야 한다
title: The link model must answer four queries: impact, coverage, rationale trace and state aggregation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
verified: [{by: orchestrator/claude-fable-5-1, at: 2026-09-12T00:50:00+09:00}, {by: process:label-judge-20260912, at: 2026-09-12T12:40:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0108]
part_of: https://agentic-knowledge-base.dev/id/composite/03b399d7-2688-4588-bfed-7942e0e30aab
composite: {id: https://agentic-knowledge-base.dev/id/composite/03b399d7-2688-4588-bfed-7942e0e30aab, title_ko: 링크 모델이 답해야 할 표준 질의 네 가지, title: Four standard queries the link model must answer}
---
**결론** — 링크 모델은 네 질의에 답해야 한다.

| 질의 | 용도 |
|---|---|
| **영향 분석** — X가 바뀌면 무엇이 영향받는가 | `satisfies`·`refines`·`assumes`를 거슬러 |
| **커버리지** — `satisfies` 없는 결정, `verifies` 없는 인터페이스 | 고아 탐지 |
| **근거 추적** — 이 코드는 왜 이렇게 됐는가 | `refines`를 거슬러 functional까지 |
| **상태 집계** — `suspect`·`invalid` 링크 목록 | 9.6절 재판정 큐 |

그래프 질의로 그대로 표현된다.

```
# CQ4: 가정 A가 깨지면 무엇이 무효가 되는가 (단방향 규칙 적용 전)
SELECT ?item WHERE { ?item agt:assumes :A }

# CQ7: satisfies가 없는 concrete 결정
SELECT ?d WHERE {
  ?d a agt:DecisionChunk ; agt:hasLevel agt:concrete .
  FILTER NOT EXISTS { ?x agt:satisfies ?d }
}

# 근거 추적: 이 소스 청크의 functional까지
SELECT ?anc WHERE { :s-203 agt:refines+ ?anc }
```
