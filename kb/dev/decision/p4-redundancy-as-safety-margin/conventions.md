---
id: https://agentic-knowledge-base.dev/id/chunk/28d27e57-2f6c-4a39-ad95-ab284fec1f80
type: decision
level: concrete
title_ko: 규범 문서 규약 — 본문 중복은 안전율로 용인하되 coUpdatesWith로 묶고 재검증 시점에서 정리한다
title: Normative-document conventions — Body redundancy is tolerated as a safety margin, linked by coUpdatesWith, consolidated at revalidation points
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-label-representativeness-protocol}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6053b67e-afec-4a59-b710-31b6ab85b108
---
**규약** — `p4-redundancy-as-safety-margin`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **중복 대신 재사용한다.** 새 개념·항목을 만들기 전에 기존 것을 찾는다. 찾는 수단은 `grep -r kb/ontology/`와 라벨 목록이다. 같은 뜻의 항목 둘이 이 체계가 막는 드리프트다.
규약: 정합성 보고 | 정확·근사 중복, 묶인 쌍의 응집 저하, 라벨 중복·형식, 용어 옛 표기 — `//kb:consistency`. 판정은 사람이 한다
