---
id: https://agentic-knowledge-base.dev/id/chunk/4edeeed1-0c25-4965-a4f6-5ed608c2b07c
type: decision
level: concrete
title_ko: 산출물의 주소는 구현이 아니라 명세의 슬롯에서 얻는다
title: An output takes its address from the specification slot, not from the implementation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0180-output-address-from-spec-slot.md, id: https://agentic-knowledge-base.dev/id/chunk-d0180, title_ko: "산출물의 주소는 구현이 아니라 명세의 슬롯에서 얻는다", title: "An artifact's address comes from the spec slot, not the implementation"}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0188, title_ko: "대안 — 재현 가능한 빌드 투영", title: "Alternatives — reproducible build projection"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0180, https://agentic-knowledge-base.dev/id/chunk-d0188]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/e69281eb-93ed-4314-8a54-0c18ff5cf4f1
composite: {id: https://agentic-knowledge-base.dev/id/composite/e69281eb-93ed-4314-8a54-0c18ff5cf4f1, title_ko: 명세 슬롯에서 얻는 산출물 주소, title: Output address from the specification slot}
---
**결론** — 생성된 산출물의 이름과 위치는 **명세 쪽 슬롯**에서 파생하고, 그 슬롯을 실현한 구현에서 파생하지 않는다. 구현을 다른 후보로 바꿔도 산출물의 주소는 그대로이므로 그것을 참조하던 쪽이 깨지지 않는다.
