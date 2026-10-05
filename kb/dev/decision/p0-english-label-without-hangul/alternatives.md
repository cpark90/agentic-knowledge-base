---
id: https://agentic-knowledge-base.dev/id/chunk/4f5ce2e7-bd7b-4abc-b26e-837fcf00185c
type: decision
level: logical
title_ko: 보고에만 두는 안과 규약 한 줄만 두는 안은 기각된다
title: Leaving it to a report only, or to a single line of convention only, is rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f0b99b6e-b385-4a1a-a879-a46b0b5c8faa
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| `consistency` 보고에만 추가한다 | 판정이 정규식 하나로 끝나는 규칙이다. 판정 가능한 것은 게이트로 만든다는 원칙(`docs/tools.md`)에 어긋나고, 보고는 커밋을 막지 않는다 |
| `STYLEGUIDE.md`에 규약 한 줄만 둔다 | 치환 도구를 쓸 때마다 사람이 확인해야 한다. 2026-09-12의 오염이 그 확인을 놓친 경로다 |
