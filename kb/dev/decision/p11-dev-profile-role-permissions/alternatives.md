---
id: https://agentic-knowledge-base.dev/id/chunk/e738c171-600f-4a35-aa8b-f9e8afc5bf2f
type: decision
level: logical
title_ko: write 스코프 공유의 기각
title: Rejecting shared write scopes across design, build and operate
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T19:40:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4dbb535c-ea05-4b67-accf-29c2ef7f6ee3
---
**대안** — 설계·구현·운영 역할이 같은 write 스코프를 갖는 안. 기각 — 세 영역은 독립 분리한다. 같은 write 스코프를 가지면 만든 쪽이 판정 기준을 고칠 수 있다 (11.2절, 8.5절).
