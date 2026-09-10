---
id: https://agentic-knowledge-base.dev/id/chunk/1f407ad0-2e57-4e62-96b4-640c246a6100
type: decision
level: concrete
title_ko: 매트릭스 화면은 plane 격자에 색으로 suspect와 누락을 나눠 보여준다
title: The matrix screen is a plane grid where color separates suspect cells from missing ones
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0155]
part_of: https://agentic-knowledge-base.dev/id/composite/78873300-5f9a-4316-bc7c-9a384d60822b
composite: {id: https://agentic-knowledge-base.dev/id/composite/78873300-5f9a-4316-bc7c-9a384d60822b, title_ko: 추적 매트릭스 화면의 상호작용, title: Interaction of the traceability matrix screen}
---
**결론** — 9.12절 추적 매트릭스 화면의 상호작용을 아래로 정한다.

- 셀 클릭 → 그 셀의 링크 목록 (라벨 + 상태)
- `suspect` 셀은 색으로 구분. 색 값은 suspect 비율
- "TIM 허용 & 0" 칸은 별도 색
- 행·열은 plane. 필터는 level · 상태 · 기간
