---
id: https://agentic-knowledge-base.dev/id/chunk/a595f2cf-63e4-4f64-9c59-7d6765f0eb1e
type: decision
level: logical
title_ko: 전 게이트 즉시 실행과 실패 전파의 기각
title: Rejecting all-gates-immediately and propagating failures
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/33c8a1a1-fc90-4ce7-83a9-20c607a7c163
---
**대안** — 모든 게이트를 편집 즉시 돌리는 안. 기각 — verify·test는 그래프·실행이 필요해 편집을 막는다 (노트 6.7절).

**대안** — 게이트 실패를 하류 링크로 전파하는 안. 기각 — 실패한 청크는 `draft`라 애초에 링크의 끝이 될 수 없다. 전파할 것이 없다 (노트 6.7절, 4.11절).
