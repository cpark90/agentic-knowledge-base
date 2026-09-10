---
id: https://agentic-knowledge-base.dev/id/chunk/a4934aca-9aac-4883-88ce-45b81c7dad0b
type: decision
level: concrete
title_ko: ODD 밖 케이스는 odd:outside로 표시해 분리 보관한다
title: Cases outside the ODD are kept, tagged odd:outside
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0067]
part_of: https://agentic-knowledge-base.dev/id/composite/334ec611-70bf-40cd-85df-7ed0431ac556
composite: {id: https://agentic-knowledge-base.dev/id/composite/334ec611-70bf-40cd-85df-7ed0431ac556, title_ko: ODD 밖 케이스의 태그 분리, title: Tagging cases outside the ODD}
---
**결론** — **ODD 밖 케이스는 존재할 수 있되 `odd:outside` 태그로 표시한다.** 설계 범위 밖에서 무엇이 일어나는지 아는 것에도 가치가 있으나, 그것을 설계 범위 안 케이스와 섞으면 커버리지가 왜곡된다.

커버리지의 분모는 ODD이므로(3.3절), 태그된 케이스는 분모에 들어가지 않고 별도로 집계된다.
