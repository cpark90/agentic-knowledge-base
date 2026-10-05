---
id: https://agentic-knowledge-base.dev/id/chunk/5bafec5b-d650-4bae-9281-48066f03f43a
type: decision
level: concrete
title_ko: 규범 문서 규약 — executable의 구현과 검증은 서로 다른 KB에 산다
title: Normative-document conventions — Implementation and verifier live in different KBs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/8e8697a1-16b9-4c24-a377-340db2b6000b
---
**규약** — `p6-executable-splits-by-kb`의 결론을 규범 문서에 싣는 문장이다.

규약: `artifact` | 구현만. verifier는 V&V KB
규약: `verifies` | KB를 가로지르는 유일한 링크. 방향은 V&V → 개발, 같은 level끼리
