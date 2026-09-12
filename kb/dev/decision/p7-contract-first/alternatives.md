---
id: https://agentic-knowledge-base.dev/id/chunk/e2482f22-3c16-4d3d-8e87-77f6dd17849a
type: decision
level: logical
title_ko: 구현 후 시그니처 추출의 기각
title: Rejecting post-hoc signature extraction
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/5957a996-1394-4279-8e3c-31b55c586f62
---
**대안** — 먼저 구현하고 시그니처와 사후조건을 코드에서 추출하는 안. 기각 — 정제 단절이며, 추출된 사후조건으로 만든 기준은 구현의 동어반복이라 결함을 거르지 못한다 (노트 7.5절, 8.6절).
