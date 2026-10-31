---
id: https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4
type: decision
level: concrete
title_ko: 라벨이 단위 지식의 인터페이스다
former_title_ko: ["라벨이 청크의 인터페이스다", "라벨이 지식 항목의 인터페이스다"]
title: The label is the chunk's interface
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0082-read-response-is-label-list.md, id: https://agentic-knowledge-base.dev/id/chunk-d0082, title_ko: "라벨이 인터페이스 — 읽기 응답은 라벨 목록이 기본", title: "The label is the interface - reads return a label list by default"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0082]
part_of: https://agentic-knowledge-base.dev/id/composite/004649e6-0eb9-42fb-b3dc-60c65883d906
composite: {id: https://agentic-knowledge-base.dev/id/composite/004649e6-0eb9-42fb-b3dc-60c65883d906, title_ko: 라벨이 인터페이스다, title: The label is the interface}
---
**결론** — **라벨이 단위 지식의 인터페이스다.** 에이전트는 **라벨 목록을 먼저 받고**
필요한 단위 지식만 assertion 그래프를 연다.

**라벨이 본문을 대표하지 못하면 단위 지식이 잘못 나뉜 것이다.** 라벨 실패는 라벨을
고쳐서 해결할 문제가 아니라 **분할 문제**로 다룬다 — 라벨을 하나로 쓸 수 없다는
것은 그 단위 지식이 두 주제를 담고 있다는 신호다 (4.10절).
