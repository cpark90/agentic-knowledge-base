---
id: https://agentic-knowledge-base.dev/id/chunk/244f435c-f0f7-4b3a-9bbc-b66f3d610f27
type: decision
level: concrete
title_ko: 하위 ODD는 좁히기만 하고 이탈 전파는 비대칭이다
title: A child ODD only narrows; exit propagation is asymmetric
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0066]
part_of: https://agentic-knowledge-base.dev/id/composite/7699d0eb-b30b-4015-b02c-d7db24b8eed1
composite: {id: https://agentic-knowledge-base.dev/id/composite/7699d0eb-b30b-4015-b02c-d7db24b8eed1, title_ko: ODD 계층, title: The ODD hierarchy}
---
**결론** — 3.1절 "하위 시스템 ODD는 상위의 부분집합"을 구체화한다.

- 하위 ODD는 상위 ODD를 `import`하고 속성 값 범위를 **좁히기만** 한다. 넓히거나 새 속성을 추가하면 **검사 실패**
- **하위 ODD의 이탈은 하위 범위 안에서만** 무효화를 전파한다
- **상위 ODD의 이탈은 모든 하위로** 전파된다
