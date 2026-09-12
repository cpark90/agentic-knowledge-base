---
id: https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4
type: decision
level: concrete
title_ko: 라벨이 청크의 인터페이스다
title: The label is the chunk's interface
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0082]
part_of: https://agentic-knowledge-base.dev/id/composite/004649e6-0eb9-42fb-b3dc-60c65883d906
composite: {id: https://agentic-knowledge-base.dev/id/composite/004649e6-0eb9-42fb-b3dc-60c65883d906, title_ko: 라벨이 인터페이스다, title: The label is the interface}
---
**결론** — **라벨이 청크의 인터페이스다.** 에이전트는 **라벨 목록을 먼저 받고**
필요한 청크만 assertion 그래프를 연다.

**라벨이 본문을 대표하지 못하면 청크가 잘못 나뉜 것이다.** 라벨 실패는 라벨을
고쳐서 해결할 문제가 아니라 **분할 문제**로 다룬다 — 라벨을 하나로 쓸 수 없다는
것은 그 청크가 두 주제를 담고 있다는 신호다 (4.10절).
