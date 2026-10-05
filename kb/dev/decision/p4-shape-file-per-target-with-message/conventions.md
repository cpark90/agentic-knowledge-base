---
id: https://agentic-knowledge-base.dev/id/chunk/096f9031-0697-435b-b534-83dbcdd15812
type: decision
level: concrete
title_ko: 규범 문서 규약 — shape 파일은 검사 대상 하나를 담고 모든 property shape는 강제하는 규칙을 적은 sh:message를 단다
title: Normative-document conventions — A shape file holds one inspection target, and every property shape carries an sh:message stating the rule it enforces
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/715a53ec-b1a3-4a8a-92ff-31bb1806ef9b
---
**규약** — `p4-shape-file-per-target-with-message`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 파일 하나가 검사 대상 하나 또는 밀접한 쌍을 담는다. 파일명은 `<대상>-shapes.ttl`이다.
규약: [지킴] 모든 property shape에 `sh:message`를 달고, 메시지에 강제하는 규칙을 적는다. 그래야 FAIL이 곧 수정 방향 안내가 된다.
