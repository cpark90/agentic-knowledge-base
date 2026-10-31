---
id: https://agentic-knowledge-base.dev/id/chunk/7e598dbd-7b2f-4f30-9640-87c3be26d62f
type: decision
level: concrete
title_ko: 불변식은 union 위에서만 성립하므로 union을 검증한다
title: Invariants hold only over the union, so the union is validated
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0157-validate-the-union.md, id: https://agentic-knowledge-base.dev/id/chunk-d0157, title_ko: "불변식은 union 위에서만 성립하므로 union을 검증한다", title: "Invariants hold only over the union, so validate the union"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0157]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/6e580ff9-3d4a-423c-987d-4724894725a5
composite: {id: https://agentic-knowledge-base.dev/id/composite/6e580ff9-3d4a-423c-987d-4724894725a5, title_ko: union 검증, title: Validating the union}
---
**결론** — 고아 방지와 drift 방지, 조립 가능성 같은 보장은 **합쳐 추론한 그래프**에서만 판정된다. 그래서 검증은 언제나 조립된 union을 대상으로 하고, 파일 하나를 홀로 검증하지 않는다. 게이트는 기여자 로컬과 데이터 저장소 CI의 두 단이며, 둘 다 같은 union을 본다.
