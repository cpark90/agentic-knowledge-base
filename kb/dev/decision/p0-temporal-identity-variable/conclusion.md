---
id: https://agentic-knowledge-base.dev/id/chunk/a7b7d807-9b90-4682-a116-a585da5c9c6e
type: decision
level: abstract
title_ko: 리팩터링에서 개체가 새로 생기는 것을 무엇이 막는가는 결정 변수다
title: What prevents a refactoring from minting a new entity is a decision variable
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
composite: {id: https://agentic-knowledge-base.dev/id/composite/4d329cea-48b1-454e-861a-a3f1a0831831, title_ko: 개체 신생을 막는 장치라는 변수, title: The variable of what prevents minting new entities}
part_of: https://agentic-knowledge-base.dev/id/composite/4d329cea-48b1-454e-861a-a3f1a0831831
---
**결론** — 리팩터링에서 개체가 새로 생기는 것을 무엇이 막는가와 버전 IRI를 쓰는가를 결정 변수로 선언한다. 막을 대상은 본문만 고쳤는데 새 항목으로 취급되는 과잉 신생과, 같은 지식을 새 파일로 만드는 중복 신생이다. 값은 이 변수를 출발로 둔 설계 공간이 고르고, 고른 결정은 이 결론을 `refines`한다. 이 결론은 값을 정하지 않는다.
