---
id: https://agentic-knowledge-base.dev/id/chunk/b5c00d1b-3969-4f02-8a7c-138a8a0b56b9
type: decision
level: concrete
title_ko: 규범 문서 규약 — 복합체의 순서는 선언하는 단위 지식의 목록이 원본이고 선언된 것만 co:List로 방출한다
title: Normative-document conventions — A composite's order is declared in the declaring chunk, and only declared order is emitted as co:List
former_title_ko: ["규범 문서 규약 — 복합체의 순서는 선언하는 지식 항목의 목록이 원본이고 선언된 것만 co:List로 방출한다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c15bc5d0-4f85-4d7b-bdd2-85cca14af3ba
---
**규약** — `p4-composite-order-is-declared`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 순서가 뜻을 갖는 복합체만 선언하는 단위 지식의 `composite:`에 선택 키 `ordered: [<부분 IRI>…]`를 더하고, 이 목록은 부분 전부를 빠짐없이 한 번씩 담는다(2026-09-29). 키가 없으면 순서가 없고 **예외는 없다**(유저 승인 2026-09-29). 따라서 결정 기록의 선언은 `kb_decision`의 `ordered` 인자로 `gen_build`가 넣으며, 205개 `conclusion.md`를 손으로 고치지 않는다. 도구는 역할 이름으로 순서를 추측하지 않는다.
