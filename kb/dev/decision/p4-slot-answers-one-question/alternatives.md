---
id: https://agentic-knowledge-base.dev/id/chunk/75a36c9b-9230-4545-8b3b-cc469ad883aa
type: decision
level: logical
title_ko: 틀 28종 도입·즉시 게이트화·리뷰 의존 안은 기각된다
title: Adopting 28 templates, gating immediately, and relying on review are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T19:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f7ac1b83-2f07-479d-a1ac-dfa68858e15f
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 제안의 블록 틀 28종을 그대로 들인다 | 유저 지시가 "정해진 것을 최대한 손대지 않고 비어 있는 부분만 채운다"이다. 실물이 있는 plane은 일곱이고 나머지 틀은 대상 산출물이 없다. 채워도 쓸 데가 없다 |
| 슬롯 규칙을 만들면서 바로 게이트로 올린다 | 기존 청크 695개가 한꺼번에 FAIL이다. 보고로 수치를 먼저 내고 0이 된 뒤 올린다 |
| 규칙만 문서에 적고 기계 검사를 두지 않는다 | 빈 값 표기와 목록 규칙은 이미 산문으로 있던 것에 가깝고 지켜지지 않았다. 검사 가능해야 규칙이다 |
| "한 주장은 한 블록"까지 함께 받는다 | 중복을 안전율로 용인한 유저 결정(`p4-redundancy-as-safety-margin`, 2026-09-11)을 뒤집는다. 기정은 손대지 않는다 |
