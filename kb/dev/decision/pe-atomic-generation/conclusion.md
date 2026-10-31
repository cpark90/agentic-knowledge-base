---
id: https://agentic-knowledge-base.dev/id/chunk/f8a8acdf-ff53-4bce-9a56-fd043f1bb077
type: decision
level: concrete
title_ko: 생성은 전부 성공했을 때만 원자적으로 교체한다
title: Generation replaces the destination atomically only when everything succeeds
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0179-atomic-generation.md, id: https://agentic-knowledge-base.dev/id/chunk-d0179, title_ko: "생성은 전부 성공했을 때만 원자적으로 교체한다", title: "Generation lands atomically, only on full success"}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0188, title_ko: "대안 — 재현 가능한 빌드 투영", title: "Alternatives — reproducible build projection"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0179, https://agentic-knowledge-base.dev/id/chunk-d0188]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/99254d62-ee67-4d34-aa30-a42211166fd5
composite: {id: https://agentic-knowledge-base.dev/id/composite/99254d62-ee67-4d34-aa30-a42211166fd5, title_ko: 원자적 생성, title: Atomic generation}
---
**결론** — 생성은 임시 위치에 산출물 전체를 만들고 모든 게이트를 그 위에서 통과시킨 뒤, **전부 성공했을 때만** 원자적 교체로 목적지에 놓는다. 어느 단계에서든 실패하면 임시본을 버리고 목적지는 손대지 않는다.
