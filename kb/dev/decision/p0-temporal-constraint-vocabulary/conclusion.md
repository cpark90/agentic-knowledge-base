---
id: https://agentic-knowledge-base.dev/id/chunk/b8b2e18e-ae67-4590-a830-e4cf4d54e81b
type: decision
level: concrete
title_ko: 시간적 상호작용은 functional의 EARS 시간 절과 logical의 시간 제약 어휘 두 자리에서 표현된다
title: Temporal interaction is expressed in two places: EARS time clauses at functional and the temporal constraint vocabulary at logical
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
part_of: https://agentic-knowledge-base.dev/id/composite/a65b4cb7-b236-46d5-ba86-c9c9c85ac000
composite: {id: https://agentic-knowledge-base.dev/id/composite/a65b4cb7-b236-46d5-ba86-c9c9c85ac000, title_ko: 시간 요구는 functional 산문과 logical 시간 제약 어휘로 표현한다, title: Temporal requirements are expressed in functional prose and logical constraint vocabulary}
---
**결론** — 시간열 개체가 없으므로(0.5절) "A 뒤에 B", "A와 B는 동시에 불가",
"A는 T 안에" 같은 요구는 두 수준에서 표현된다.

- **functional** — requirement 산문. EARS 형식의 시간 절로 쓴다
- **logical** — ODD 동적 갈래의 **시간 제약 어휘**. 선행·배타·시한 (0.4절)

동시성 요구는 logical에서 이 어휘로 형식화되고, **판정식은 실행 기록의 시각
순서로 검사한다.**
