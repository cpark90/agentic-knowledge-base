---
id: https://agentic-knowledge-base.dev/id/chunk/70d56a11-ab22-475f-8ca6-7af9c727eb1d
type: decision
level: logical
title_ko: 코드를 청크로 투영하는 범위는 등록 목록이 정한다
title: The range of code projected into chunks is set by registered lists
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-09T18:04:39+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7c00131b-7fdb-42db-947e-49d184967047
composite: {id: https://agentic-knowledge-base.dev/id/composite/7c00131b-7fdb-42db-947e-49d184967047, title_ko: 목록으로 정하는 추출 범위, title: Extraction range set by lists}
---
**결론** — 코드를 청크로 투영하는 범위는 지금처럼 `defs/kb.bzl`의 목록 셋(`EXTRACTED_SOURCES`·`EXTRACTED_QUERY_DIRS`·`EXTRACTED_STARLARK`)이 정한다. 목록에 없는 코드는 추출하지 않는다.
