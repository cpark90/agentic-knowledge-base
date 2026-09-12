---
id: https://agentic-knowledge-base.dev/id/chunk/20148952-30c4-4f76-8cbf-4d9b32c68b25
type: requirement
level: functional
title_ko: 청크는 프로젝트를 넘지 않는다
title: Chunks never cross the project boundary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T16:00:00+09:00}
---
**요구** — 체계는 청크를 프로젝트 경계 밖으로 넘기지 않아야 한다 — 청크는 그 프로젝트의 ODD 안에서만 유효하다.

- **이해관계자**: 업체 · **관심사**: 축적과 재사용
- **출처**: 구조도 축적의 단위 / 노트 12.7절

청크의 가정이 ODD 조건 위의 명제이므로, ODD가 다르면 가정의 판정 자체가 성립하지 않는다.
