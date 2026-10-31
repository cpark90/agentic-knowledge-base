---
id: https://agentic-knowledge-base.dev/id/chunk/622b0490-06d9-4db1-a2b5-b8e67d0a818f
type: decision
level: concrete
title_ko: 규범 문서 규약 — 뷰는 저장하지 않고 질의로 조립한다
title: Normative-document conventions — Views are never stored; they are assembled by query
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5d561aaa-6fc8-4102-91b9-96db89f984e8
---
**규약** — `p4-projection-as-query`의 결론을 규범 문서에 싣는 문장이다.

규약: 7 | **뷰** | tangle과 weave, 문서, 추적 매트릭스는 저장하지 않고 질의로 만든다 | 축적된 지식이 쓰이는 형태 | [§9](#9-뷰)
규약: 뷰 | 저장된 뷰는 없고 전부 질의 결과다
규약: tangle, 곧 코드 파일 | 복합체의 `artifact` 부분을 `co:index` 순으로 이어 붙인다
규약: weave, 곧 문서 | 산출물과 그 항목을 `targets`로 가리키는 주석을 함께 뽑는다
규약: 라벨 목록 | 적용 범위 안 단위 지식의 `rdfs:label`만 뽑는다
규약: 작업 집합 | 적용 범위의 지식 종류와 ODD 조건으로 거른 지식이다
