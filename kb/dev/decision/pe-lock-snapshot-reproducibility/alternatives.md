---
id: https://agentic-knowledge-base.dev/id/chunk/e555ebbc-3c77-4220-b757-b638d85522f9
type: decision
level: concrete
title_ko: 재현한 빌드가 lock의 정책 값을 고쳐 쓰는 안은 택하지 않는다
title: A reproduced build rewriting the policy value in the lock is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:56:58+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:56:58+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/ab3d3668-34d4-43a1-b5d2-220cdbd6ca30
---
**대안** — 원천(harness-concrete `docs/odr-bind-lock.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 재현한 빌드가 lock의 `policyApplied`를 "lock"으로 고쳐 쓴다 | 고쳐 쓰면 재현된 트리가 원본과 바이트 동일하지 않다. 그래서 값은 그대로 옮기고, lock으로 재현했다는 사실은 빌드 보고에 둔다(odr-bind-lock "The lock") |
