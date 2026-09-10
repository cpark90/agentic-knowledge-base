---
id: https://agentic-knowledge-base.dev/id/chunk-d0108
type: decision
level: concrete
title_ko: 링크 모델이 답해야 할 표준 질의 네 가지
title: Four standard queries the link model must answer
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 링크 모델은 네 표준 질의에 답할 수 있어야 한다.

- **영향 분석** — X가 바뀌면 무엇이 영향받는가.
  `satisfies`·`refines`·`assumes`를 거슬러.
- **커버리지** — `satisfies`가 없는 결정, `verifies`가 없는 인터페이스.
  고아 탐지.
- **근거 추적** — 이 코드는 왜 이렇게 됐는가. `refines`를 거슬러
  functional까지.
- **상태 집계** — `suspect`·`invalid` 링크 목록. 8.6절 재판정 큐.

**근거** (노트 8.7·8.13절) — 네 질의가 링크 모델의 요구사항이고, 전부
그래프 질의로 표현된다.

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
