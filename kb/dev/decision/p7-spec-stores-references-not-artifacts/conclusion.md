---
id: https://agentic-knowledge-base.dev/id/chunk/da4d5601-74be-485c-aee2-2de09d4e510d
type: decision
level: concrete
title_ko: 조립 명세는 산출물을 저장하지 않고 참조만 담는다
title: An assembly specification stores references, not the artifacts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0183-spec-stores-references-not-artifacts.md, id: https://agentic-knowledge-base.dev/id/chunk-d0183, title_ko: "조립 명세는 산출물을 저장하지 않고 참조만 담는다", title: "An assembly spec stores references, never the artifacts themselves"}, {resource: git:aeb0a58:chunks/decision/d-0189-spec-content-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0189, title_ko: "대안 — 명세가 담는 것", title: "Alternatives — what a specification carries"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/d48f87c5-7224-4e99-b3e1-efa4f8f114ef]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0183, https://agentic-knowledge-base.dev/id/chunk-d0189]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/959d935b-e16d-4955-acf0-12c81c12e8aa
composite: {id: https://agentic-knowledge-base.dev/id/composite/959d935b-e16d-4955-acf0-12c81c12e8aa, title_ko: 참조만 담는 조립 명세, title: Assembly specification holding references only}
---
**결론** — 조립 명세 단위가 담는 것은 셋이다. **명세**는 부품 식별자와 그 조립이고, **설명**은 어떤 부품과 방법론으로 무엇을 만들었는가이며, **참조**는 구체 산출물의 위치다. 실제 코드나 문서 본문, 지시문 본문 같은 구체 산출물 자체는 담지 않는다.
