---
id: https://agentic-knowledge-base.dev/id/chunk/cd115985-2a81-4190-92e0-d21052bfb28a
type: decision
level: concrete
title_ko: 규범 문서 규약 — 복합체는 표준 part-of와 순서 컬렉션으로 쓴다
title: Normative-document conventions — Composites use standard part-of and an ordered collection
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/85fcc7f3-446f-46d6-b386-693544fefe6e
---
**규약** — `p4-composite-as-part-of`의 결론을 규범 문서에 싣는 문장이다.

규약: 순서 | 순서가 뜻을 갖는 복합체만 `co:List` + `co:index`. 순서의 원본은 **선언**이다 — 선언 청크의 `composite:`에 선택 키 `ordered: [<부분 IRI>…]`(부분 전부를 빠짐없이 한 번씩)가 있을 때만 생성기가 낸다. 결정 복합체도 예외가 아니다 — 생성기가 결론·근거·대안 순서를 `ordered` 인자로 선언한다(유저 답 2026-09-29). 시나리오 복합체는 `ordered`가 필수다. 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다
