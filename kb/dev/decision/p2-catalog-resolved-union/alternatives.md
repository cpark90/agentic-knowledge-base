---
id: https://agentic-knowledge-base.dev/id/chunk/f8ebcca7-2f3b-42b4-b8ff-18009d655d20
type: decision
level: concrete
title_ko: 디렉토리 glob과 submodule로 조립하는 안은 택하지 않는다
title: Assembling by directory glob or submodule is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0156-catalog-resolved-union.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:29:30+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:29:30+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/5beca94e-efeb-4e6c-89a7-12c3fa80103e
---
**대안** — 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 디렉토리 glob이나 submodule로 조립한다 | 위치가 곧 정체성이 되어 파일 이동이 IRI 변경이 된다. 배치를 사람이 읽기 좋게 바꾸는 일이 그래프 파괴가 되면 배치는 굳는다 |
