---
id: https://agentic-knowledge-base.dev/id/chunk/03347148-9ef4-4738-b83b-c2e7a65f75e6
type: decision
level: logical
title_ko: 게이트 id를 도구마다 상수로 두는 안과 등록부를 파이썬에 두는 안은 기각된다
title: Keeping gate ids as per-tool constants and keeping the registry in Python are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/d36b748b-cc0d-46c5-9df7-7d05708e3cd1
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 게이트 id를 `kb_lib`의 `*_GATE` 상수와 총람 표에 각각 적는다 | 2026-10-01까지의 방식이다. 같은 목록이 넷으로 갈렸고 어느 것이 원본인지 판정할 수 없었다 |
| 등록부를 `tools/kb_lib.py`에 두고 Starlark가 그것을 따른다 | Starlark는 파이썬 파일을 읽지 못한다. 분석 시점 판정에 쓰이는 표가 파이썬에 있으면 Bazel 쪽에 사본이 생긴다 |
