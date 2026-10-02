---
id: https://agentic-knowledge-base.dev/id/chunk/02294b6e-a9eb-4ee5-8972-ff224087e9a4
type: decision
level: logical
title_ko: 저작된 링크와 추출 참조는 증거의 질이 다른데 표기가 같았다
title: Authored links and extracted references differ in evidence quality but shared one notation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T17:20:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/91fabd55-5c34-4d7e-a663-4dc72e486767
---
**근거** (노트 10.4절·9.11절; hci 조사 2026-09-18 선택지 A, 유저 승인 2026-09-19) — 저작된 청크 간 링크 504건은 전부 링크
개체와 증거를 갖는데, 본문에서 추출한 참조(`cites` 30·`usesConcept` 156)는 상태 없이 단언돼 있었다. 어휘의 `agt:CandidateLink`는 실물이 0이라
후보 → 확정 절차가 데이터를 갖지 못했다. 추출 참조가 바로 그 자리다.

조사는 "증거 종류를 구축 기록이 아닌 것으로"를 권했으나 유저 결정 2026-09-12 (b)가 본문 식별자 추출을 구축 기록을 읽는
것으로 정했으므로, 증거 종류는 유지하고 **상태**로 가른다 — 저자가 적은 식별자는 기록이지 추정이 아니며, 확정되지 않은 이유는
근거가 약해서가 아니라 아무도 링크 키에 적지 않았기 때문이다. 상태와 증거를 분리하면 두 결정이 충돌하지 않는다.

`usesConcept`의 대상은 온톨로지 용어라 `agt:linkTo`의 치역(`KnowledgeItem`) 밖이다 — 그래서 `cites`만 후보 개체가 되고
`usesConcept`는 직접 술어로만 남는다.
