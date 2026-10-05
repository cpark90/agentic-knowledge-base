---
id: https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8
type: requirement
level: functional
pattern: event-driven
title_ko: 라벨 목록이 본문보다 먼저다
title: Labels come before bodies
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-10-05T00:30:10+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T00:30:20+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-req-agent
composite: {id: https://agentic-knowledge-base.dev/id/comp-req-agent, title_ko: 요구 — 에이전트 관측과 통제, title: requirements — agent observation and control}
---
**요구** — 에이전트가 판단할 때, 체계는 판단에 필요한 지식을 청크 라벨 목록으로 먼저 보여주고 요청된 본문만 펼쳐야 한다.

- **이해관계자**: 에이전트 · **관심사**: 좁은 관측
- **출처**: 노트 1.1절·1.4절·5.3절

5,418토큰 예산에서 라벨 목록이 조망을, 선택된 본문이 깊이를 담당한다.
