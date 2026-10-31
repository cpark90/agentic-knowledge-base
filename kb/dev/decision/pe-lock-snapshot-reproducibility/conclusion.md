---
id: https://agentic-knowledge-base.dev/id/chunk/acd33470-3f79-4c6a-b2a5-4add868a694d
type: decision
level: concrete
title_ko: 선택 스냅샷(lock)이 재현의 계약이다
title: The selection snapshot (lock) is the contract for reproduction
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0178-lock-snapshot-reproducibility.md, id: https://agentic-knowledge-base.dev/id/chunk-d0178, title_ko: "선택 스냅샷(lock)이 재현의 계약이다", title: "The selection snapshot (lock) is the reproducibility contract"}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0188, title_ko: "대안 — 재현 가능한 빌드 투영", title: "Alternatives — reproducible build projection"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0178, https://agentic-knowledge-base.dev/id/chunk-d0188]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/ab3d3668-34d4-43a1-b5d2-220cdbd6ca30
composite: {id: https://agentic-knowledge-base.dev/id/composite/ab3d3668-34d4-43a1-b5d2-220cdbd6ca30, title_ko: 재현의 계약인 선택 스냅샷, title: Selection snapshot as the reproduction contract}
---
**결론** — 생성할 때마다 이번에 실제로 무엇이 선택되었는가를 **lock 스냅샷**으로 산출물과 함께 쓴다. 그 스냅샷을 입력으로 다시 생성하면 결과가 바이트 동일해야 하고, 하나라도 어긋나면 재현을 **거부**한다.
