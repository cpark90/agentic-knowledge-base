---
id: https://agentic-knowledge-base.dev/id/chunk/539016c1-28bb-47b2-b587-948dbf710bc6
type: norm
level: logical
title_ko: docs/method.md 절 ODD 작성의 이어짐 — 게이트와 산출
title: docs/method.md ODD section continued — the gate and the output
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/bdc0f6e2-e2e2-4438-a6bd-917dec16b120
continues: true
---
게이트는 `bazel test //kb/odd:gate_test`다. 산출은 `kb/odd/*-odd.yml`(OpenODD, 부록 E.4)이고,
그것에서 `*-odd.ttl`이 생성되며 그 위에서 스코프가 파생된다. 속성 범주는 `related/condition`에서
생성된 택소노미 안이어야 한다.
