---
id: https://agentic-knowledge-base.dev/id/chunk/f7f0c5b0-b934-447e-9f43-393c81170b7a
type: decision
level: concrete
title_ko: 규범 문서 규약 — 가정이 깨지면 의존 항목이 자동으로 무효화된다
title: Normative-document conventions — Breaking an assumption invalidates every dependent item automatically
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:27:16+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/db06ba12-f04a-45c7-b5e3-d26d97dc7e51
---
**규약** — `p6-assumption-invalidation`의 결론을 규범 문서에 싣는 문장이다.

규약: 6 | **갱신** | 가정을 판정하고 무효화를 전파한 뒤 재검증한다 | 갱신 단절의 해소가 이 체계의 존재 이유다 | [§7](#7-갱신)
규약: 갱신 | 전수조사 없이 무효 범위가 계산된다
규약: 깨진 가정에 의존하는 항목을 `invalidated`로, 그 항목을 가리키는 링크의 반대편을 `suspect`로 표시한다. 전파는 지식 종류 사이의 단방향 규칙을 따르므로 유계다 (`p6-invalidation-propagation`).
