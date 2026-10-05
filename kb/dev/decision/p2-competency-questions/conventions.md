---
id: https://agentic-knowledge-base.dev/id/chunk/70971152-2574-4cb3-953d-f1e99daab068
type: decision
level: concrete
title_ko: 규범 문서 규약 — 온톨로지의 충분성은 답해야 할 질문 목록으로 검사한다
title: Normative-document conventions — Ontology sufficiency is checked against the question list
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5f6eadd5-ef4f-47cb-8128-f72cca5e8575
---
**규약** — `p2-competency-questions`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 정의에는 그 개념이 딛고 선 근거를 적는다. 근거 없는 개념은 온톨로지 과설계의 시작이다. 역량 질문에 기여하지 않으면 만들지 않는다.
규약: 프로파일 구축 | 역량 질문이 전부 질의로 답해진다 (d-0052) · `bazel test //kb/ontology:gate_test` PASS
규약: **역량 질문을 더한다.** 프로파일이 답해야 할 질문을 [`competency-questions.md`](../../../../docs/competency-questions.md)에 등재하고 `tools/cq-queries/`에 질의를 만든다(CQ-36 — 각 plane의 청크는 무엇이고 무엇이 판정하는가).
규약: 역량 질문 | CQ 질의 28개의 답을 라벨 목록으로 — `//kg:cq`. 개별 질의는 `bazel run //tools:query -- <CQ>`
