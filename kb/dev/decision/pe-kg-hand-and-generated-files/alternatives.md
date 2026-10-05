---
id: https://agentic-knowledge-base.dev/id/chunk/b9f7d20d-e694-4d6a-80de-6355c6222f04
type: decision
level: logical
title_ko: head의 손 작성과 손 TTL의 복합체 저작 유지는 기각된다
title: Hand-writing the head and keeping composites authored in hand-written TTL are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:10:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3b6eaa94-2497-48bd-96c7-2b84963394d7
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 청크 head를 손 TTL에 쓴다 | frontmatter가 이미 head다. 같은 사실을 두 곳에 적게 되고 초판부터 금지였다 |
| 복합체를 `composite-kg.ttl`에 손으로 계속 쓴다 | 2026-09-29 유저 답이 도구를 고치는 쪽을 골랐다. 부분이 하나뿐이던 `comp-project-harness`는 청크이지 복합체가 아니어서 지웠다 |

손 개체를 한 파일에 모으는 안과 개체 라벨을 한 언어로 두는 안은 검토 기록이 없다.
