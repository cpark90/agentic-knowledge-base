---
id: https://agentic-knowledge-base.dev/id/chunk/4b805063-e8c4-4ab0-927b-bcd98660bf22
type: decision
level: logical
title_ko: 게이트 없는 전이의 기각
title: Rejecting ungated transitions
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T19:40:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/7daf868e-e331-4e89-bbcc-447c0ce05f29
---
**대안** — 전이 게이트 없이 하위 청크를 만들도록 허용하는 안. 기각 — 게이트를 통과하지 않은 전이는 `refines`를 만들 수 없고, 링크 없는 하위 청크는 고아율에 잡힌다. v3는 게이트의 존재만 명시했고 v4가 네 게이트의 내용을 확정했다 (6.8절).
