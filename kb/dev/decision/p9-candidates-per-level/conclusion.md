---
id: https://agentic-knowledge-base.dev/id/chunk/886dfa34-dfe9-4b91-9c7d-80865dce8ed0
type: decision
level: concrete
title_ko: logical → concrete만 표준 표기가 있고 나머지 전이와 수평 링크는 -space이며 ODD 범위가 바깥 경계다
title: Only logical→concrete has a standard notation; other transitions and lateral links use -space, with ODD ranges as the outer bound
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/aa01f873-7345-4c18-a227-e8cc6e4dc958, title_ko: 수준별 후보의 자리, title: Candidate placement per level}
part_of: https://agentic-knowledge-base.dev/id/composite/aa01f873-7345-4c18-a227-e8cc6e4dc958
---
**결론** — 수준별 후보의 자리. **logical → concrete 전이만 표준 표기가 있다** — V&V 시나리오의 `keep(범위)`가 곧 후보 집합이고 `cover()`가 표본 근거다 (부록 E). 나머지 전이(functional → abstract, abstract → logical)와 모든 수평 링크는 `-space`다. OpenODD 모듈의 Range·bound는 후보 집합의 **바깥 경계**이며, 후보가 이를 벗어나면 게이트가 거부한다 (노트 9.10절, 게이트 총람 "ODD 경계").
