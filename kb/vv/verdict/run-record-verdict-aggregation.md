---
id: https://agentic-knowledge-base.dev/id/chunk/9ec56309-7174-4310-bbba-c0e84cdcc496
type: annotation
level: concrete
title_ko: 커밋된 실행 기록 둘의 pass 수치는 지금의 집계 규칙으로는 skip 을 품는다
title: The pass counts in the two committed run records would hold skips under the current aggregation rule
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/3fa64879-9f43-4c16-bf97-3fcfe5e605a9, https://agentic-knowledge-base.dev/id/chunk/1f14a8b8-9b54-4f28-bdc4-30374c78f784]
generated: {by: vnv/claude-opus-5, at: 2026-09-22T23:52:00+09:00}
---
nitpick (if-minor): 두 실행 기록의 pass 수치를 지금의 집계 규칙으로 읽으면 두 케이스가 skip 으로 내려간다.

대상: https://agentic-knowledge-base.dev/id/chunk/3fa64879-9f43-4c16-bf97-3fcfe5e605a9 · https://agentic-knowledge-base.dev/id/chunk/1f14a8b8-9b54-4f28-bdc4-30374c78f784

본문: 두 기록은 `chunk-42-lines` 와 `foreign-vocabulary-rejected` 를 `1 실행 · 1 건너뜀` 으로 적고도 `pass` 로 판정했다. 2026-09-22 실행에서 같은 두 케이스는 `skip` 이다. 명령별 실행 수와 건너뜀 수가 기록에 남아 있어 새 규칙으로 다시 읽을 값은 갖춰져 있다.

해소: 기각 — 실행 기록은 append-only 관측이라 지난 판정을 고쳐 쓰지 않는다.
