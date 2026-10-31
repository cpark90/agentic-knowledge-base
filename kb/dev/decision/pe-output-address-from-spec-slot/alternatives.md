---
id: https://agentic-knowledge-base.dev/id/chunk/2e821855-c9fe-4b77-aac6-302ca8735fc0
type: decision
level: concrete
title_ko: 선택된 후보 파일의 이름을 물려받는 안은 택하지 않는다
title: Inheriting the selected candidate file name is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0188-reproducible-build-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:02:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:02:35+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/e69281eb-93ed-4314-8a54-0c18ff5cf4f1
---
**대안** — 원천(harness-functional `docs/materialize-design.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 산출 파일 이름을 선택된 후보 파일의 basename에서 얻는다 | 후보를 바꾸면 파일 이름이 바뀌어 호출자가 깨진다. 후보가 없는 직접 참조 도구만 참조의 basename을 쓴다(materialize-design "Stable emitted filenames") |
