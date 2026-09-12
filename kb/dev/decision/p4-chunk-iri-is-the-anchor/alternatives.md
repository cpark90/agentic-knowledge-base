---
id: https://agentic-knowledge-base.dev/id/chunk/aa48f15c-ef15-4c18-af7c-81ee56f094ab
type: decision
level: logical
title_ko: 경로·줄 번호 앵커의 기각
title: Rejecting path-and-line anchors
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T19:40:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/5e2184c3-67a9-4745-b0c3-65e8c3f69fd6
---
**대안** — 경로 + 줄 번호를 앵커로 쓰는 안. 기각 — 편집마다 깨진다. 청크 IRI를 앵커로 두면 본문 편집은 링크에 영향을 주지 않고, 분할·병합으로 IRI가 생기거나 사라질 때만 링크가 `suspect`가 된다 (4.8절).
