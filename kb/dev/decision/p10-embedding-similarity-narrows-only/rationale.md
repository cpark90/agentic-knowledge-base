---
id: https://agentic-knowledge-base.dev/id/chunk/19264973-0a67-4859-9c5d-672e9f4f5eb7
type: decision
level: logical
title_ko: 유사도는 뜻이 같고 표현이 다른 항목에서 실패한다
title: Similarity fails on items with the same meaning and different expressions
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/41924645-e7b3-4971-9d53-34676190d8fd
---
**근거** (노트 10.4절 `[확정]`, 10.8절) — 유사도는 의미가 같고 표현이 다른 항목에서 실패한다. 노트가 드는 경우는 둘이다 — 반복 구조와 다른 용어다. 그런 항목 쌍은 유사도가 낮게 나오거나 무관한 쌍과 구별되지 않는다.

- 노트는 유사도로 좁힌 뒤 온톨로지 개념과 역할 정보로 판정하는 것을 확립된 순서라 적는다.
- "같은 지식"의 정의는 판단이지 사실이 아니며 그 완화가 온톨로지 개념과 역할 정보다(노트 10.8절, `p10-link-judgement-evidence` 근거 청크). 유사도는 그 판단을 대신하지 못한다.
- 임베딩 검색은 항상 순위를 내놓는다(`p9-candidate-generation-limits`). 순위가 있다는 것이 관계가 성립한다는 뜻이 아니다.
