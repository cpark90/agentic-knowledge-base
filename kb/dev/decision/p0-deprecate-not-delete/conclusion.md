---
id: https://agentic-knowledge-base.dev/id/chunk/2e558417-83e2-4f30-8da2-6fca18f21865
type: decision
level: concrete
title_ko: 개념·청크·링크 타입은 폐기 표시로만 물러난다
title: Concepts, chunks and link types retire by deprecation only
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0035]
part_of: https://agentic-knowledge-base.dev/id/composite/8453e658-a276-4f75-83a4-9926df17826b
composite: {id: https://agentic-knowledge-base.dev/id/composite/8453e658-a276-4f75-83a4-9926df17826b, title_ko: 삭제하지 않고 폐기한다, title: Deprecate, never delete}
---
**결론** — 개념·청크·링크 타입은 삭제하지 않고 **폐기(deprecate)** 한다.

- `owl:deprecated true` + 대체 개념을 `agt:replacedBy`로 지정
- 폐기된 개념을 참조하는 청크는 검사 게이트가 **경고**한다 (거부는 아님)
