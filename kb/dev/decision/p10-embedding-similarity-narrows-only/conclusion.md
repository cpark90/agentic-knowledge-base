---
id: https://agentic-knowledge-base.dev/id/chunk/31e8b1ba-7ec7-4147-94d8-f56e682874cb
type: decision
level: concrete
title_ko: 임베딩 유사도는 후보를 추리는 데만 쓰고 판정은 온톨로지 개념과 역할 정보로 한다
title: Embedding similarity only narrows candidates; ontology concepts and role information decide
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/41924645-e7b3-4971-9d53-34676190d8fd
composite: {id: https://agentic-knowledge-base.dev/id/composite/41924645-e7b3-4971-9d53-34676190d8fd, title_ko: 임베딩 유사도의 자리, title: The place of embedding similarity}
---
**결론** — 임베딩 유사도는 후보를 추리는 데만 쓴다. 확정 근거로 쓰지 않는다(노트 10.4절 `[확정]`).

판정 순서는 둘이다.

1. 유사도로 후보를 좁힌다.
1. 남은 후보를 온톨로지 개념과 역할 정보로 판정한다.

`p10-link-judgement-evidence`의 근거 서열은 임베딩 유사도를 검사 가능성 중간에 두고 "후보 추림에만"이라 적는다. 이 결정은 그 제한의 이유와 판정 순서를 적는다. 판정 단계의 근거는 그 서열의 높은 근거와 `p10-candidate-and-confirmed-link`의 제약 검사다.
