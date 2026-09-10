---
id: https://agentic-knowledge-base.dev/id/chunk/462530a9-e459-4c7e-9f55-5ee5de29c9fe
type: decision
level: concrete
title_ko: plane 순서는 변화 속도이고 requirement가 최상위다
title: Plane order follows rate of change, with requirement at the top
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0004]
part_of: https://agentic-knowledge-base.dev/id/composite/f49e799a-b677-42d6-bc5c-84cefbc27122
composite: {id: https://agentic-knowledge-base.dev/id/composite/f49e799a-b677-42d6-bc5c-84cefbc27122, title_ko: plane 순서 — 단방향 영향 규칙, title: Plane order and one-way influence}
---
**결론** — **상위 plane만 하위 plane에 영향을 줄 수 있다.** 순서 기준은 **변화
속도**이며, `requirement`가 최상위다.

```
requirement           (가장 느림, 상위)
  ↓
decision
  ↓
contract / schema
  ↓
artifact
  ↓
annotation
  ↓
memory                (가장 빠름, 하위)
```
