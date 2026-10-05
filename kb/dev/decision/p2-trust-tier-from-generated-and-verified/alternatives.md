---
id: https://agentic-knowledge-base.dev/id/chunk/8b4a54e1-18cc-494d-8e1c-a60e2aabdff0
type: decision
level: logical
title_ko: 신뢰 등급을 별도 필드로 저장하는 안은 기각된다
title: Storing the trust tier in a separate field is rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:30:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f
---
**대안** — 하나를 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 등급을 frontmatter의 `trust` 필드로 저장한다 | 노트가 `trust` 필드라 부른 것은 OKF `verified` 목록과 같은 것이다. 필드를 새로 만들지 않는다(`p2-judgement-history-in-verified`) |

검증 뒤 수정을 FAIL 대신 경고로 다루는 안은 검토 기록이 없다.
