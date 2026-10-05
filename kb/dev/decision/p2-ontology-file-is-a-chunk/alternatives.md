---
id: https://agentic-knowledge-base.dev/id/chunk/7576c90f-add4-4bde-9541-ca2f9d3c2214
type: decision
level: logical
title_ko: 단일 온톨로지 파일과 모듈당 파일 하나는 기각된다
title: A single ontology file and one file per module are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2c53f95f-200a-4ae9-8dbe-b28de0df7378
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 온톨로지 전체를 파일 하나로 둔다 | 노트 2.3절이 기각했다. 온톨로지는 모듈로 나누고 최상위가 import해 합친다(`p2-ontology-module-structure`) |
| 모듈마다 파일 하나를 둔다 | 모듈 14 가운데 7이 토큰 상한 1,092를 넘는다(2026-10-03 실측). 파일이 청크라는 원칙과 함께 성립하지 않는다 |

둘째 대안은 규약 제정 때 비교한 기록이 없다. 기각 이유는 2026-10-03 실측이다.
