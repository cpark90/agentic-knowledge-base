---
id: https://agentic-knowledge-base.dev/id/chunk/af40ba50-b62d-4608-a38e-e57854451132
type: decision
level: concrete
title_ko: 규범 문서 규약 — 한 청크는 한 파일이고 한 주제이며 본문을 고치면 라벨이 그 주제를 대표하는지 재검토한다
title: Normative-document conventions — A chunk is one file on one topic, and editing its body calls for re-checking that the label still represents it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f56035ce-db13-4b21-a3a2-5f5a173f7e03
---
**규약** — `p4-one-file-one-topic`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] **한 청크는 한 파일, 한 파일은 한 주제다.** 지식·온톨로지·shape 전부가 대상이다. 라벨 하나로 요약되지 않으면 두 주제다. 그때는 분할한다.
규약: [지킴] 본문을 고치면 라벨이 여전히 대표하는지 재검토한다.
규약: 해당 위치에 **파일 하나**를 만든다. 파일은 frontmatter(head)와 본문이고, 토큰 상한(저작 산문 1,092)은 본문(frontmatter 제외)에 건다 ([rules §1](../../../../docs/rules.md#1-chunk--자립적-최소-지식-단위)).
