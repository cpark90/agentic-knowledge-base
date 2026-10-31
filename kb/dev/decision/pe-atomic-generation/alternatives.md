---
id: https://agentic-knowledge-base.dev/id/chunk/112755c0-2004-4bec-998c-7f8d1e4b52b6
type: decision
level: concrete
title_ko: 목적지에 바로 쓰는 단순 빌드는 택하지 않는다
title: A simple build writing straight to the destination is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:59:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:59:44+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/99254d62-ee67-4d34-aa30-a42211166fd5
---
**대안** — 원천(harness-functional `docs/materialize-design.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 목적지 `--out`에 바로 쓰는 단순 빌드 | 해시값 대조가 쓰기 도중에 돌므로 불일치가 나면 반쪽 트리가 남는다(materialize-design "Atomic emit") |
