---
id: https://agentic-knowledge-base.dev/id/chunk/98142727-d920-46fc-a3e2-22e7d9a57b65
type: decision
level: concrete
title_ko: 경계는 ODD·적용 범위·가정 셋이며 ODD가 상위이고 나머지는 ODD에서 파생된다
former_title_ko: ["경계는 ODD·스코프·가정 셋이며 ODD가 상위이고 나머지는 ODD에서 파생된다"]
title: The three boundaries are ODD, scope and assumption; ODD is primary and the others derive from it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0008-odd-foundation.md, id: https://agentic-knowledge-base.dev/id/chunk-d0008, title_ko: "ODD가 경계의 기반이다", title: "ODD is the foundation of boundaries"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0008]
part_of: https://agentic-knowledge-base.dev/id/composite/d892c74e-912c-45df-a36b-cccefabeed74
composite: {id: https://agentic-knowledge-base.dev/id/composite/d892c74e-912c-45df-a36b-cccefabeed74, title_ko: ODD가 상위이고 적용 범위와 가정은 거기서 파생된다, title: ODD is primary, scope and assumption derive from it, former_title_ko: ["ODD가 상위이고 스코프와 가정은 거기서 파생된다"]}
---
**결론** — 경계는 셋이고 전부 온톨로지 어휘로 쓴 문장이며, **ODD가 상위이고
나머지 둘은 ODD에서 파생된다.**

- **`agt:ODD`** — 프로젝트에 붙는다. 전체가 설계된 운영 조건의 명세이며
  실제로 작성·유지되는 **문서**다 (Part III)
- **`agt:Scope`** — 에이전트에 붙는다. read scope / write scope. ODD 속성의
  부분집합 + 지식 종류 권한
- **`agt:Assumption`** — 지식에 붙는다. 그 항목이 유효하려면 참이어야
  하는 전제. ODD 속성 위의 명제

관계는 `Harness --grants--> Scope`, `Scope --subsetOf--> ODD`,
`지식 항목 --assumes--> Assumption`, `Assumption --refersTo--> ODD 속성`.

**ODD에 없는 속성을 참조하는 적용 범위나 가정은 존재할 수 없다** — 검사 게이트가
거부하고, 필요하면 ODD를 먼저 확장한다 (3.6절).

가정은 **설계 시점에 전제한 조건**이고 실행 시점의 실제 조건은 별개다.
관측 가능한 가정은 실제 조건과 대조되어 `valid` / `invalidated`로, 관측
불가능한 가정은 `unverified`로 남는다.
