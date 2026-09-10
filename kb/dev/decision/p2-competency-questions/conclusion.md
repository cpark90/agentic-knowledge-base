---
id: https://agentic-knowledge-base.dev/id/chunk/0c829785-f155-4ab8-bf9a-1f69b0d3e85d
type: decision
level: concrete
title_ko: 온톨로지의 충분성은 답해야 할 질문 목록으로 검사한다
title: Ontology sufficiency is checked against the question list
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0052]
part_of: https://agentic-knowledge-base.dev/id/composite/5f6eadd5-ef4f-47cb-8128-f72cca5e8575
composite: {id: https://agentic-knowledge-base.dev/id/composite/5f6eadd5-ef4f-47cb-8128-f72cca5e8575, title_ko: 역량 질문이 온톨로지의 요구사항이다, title: Competency questions are the ontology's requirements}
---
**결론** — 온톨로지는 **답해야 할 질문 목록(competency questions)**으로 요구사항을 정의한다. 각 질문은 **그래프 질의 하나**로 답할 수 있어야 하고, 온톨로지가 충분한지를 이 목록으로 검사한다.

목록은 링크가 답하는 것(`satisfies`·`assumes`·`verifies`·`refines`·`allocates`·`conflicts-with`), 스코프가 답하는 것(지금 볼 수 있는 것, 스코프 밖 의존), provenance가 답하는 것(누가 언제 무엇을 근거로), `defect-rules`가 답하는 것(이 실행 기록의 결함 요인), 그리고 온톨로지 자신에 대한 것(쓰이지 않는 개념, 42줄을 가장 자주 넘는 plane)을 포괄한다.

두 질문이 추적성의 양방향 완주를 검사한다 — **CQ19 executable까지 닿지 않은 요구**(`refines` 하향 질의)와 **CQ20 요구로 거슬러 오르지 못하는 산출물**(`refines+` 상향 질의).

**역량 질문에 답할 수 없는 온톨로지 변경은 검토 대상이다.** 새 개념을 추가할 때는 어느 역량 질문에 기여하는지 적는다.
