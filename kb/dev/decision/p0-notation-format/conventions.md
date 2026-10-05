---
id: https://agentic-knowledge-base.dev/id/chunk/a487cc2a-29e4-4d0e-8474-234038ddbca5
type: decision
level: concrete
title_ko: 규범 문서 규약 — 온톨로지 자체가 용어집이다
title: Normative-document conventions — The ontology is the glossary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:37:29+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/fc68c83c-8feb-47ce-8dea-30f24d2ee645
---
**규약** — `p0-notation-format`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 언어: 산문·정의·주석은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase다. 라벨은 한/영 각 1이다. TTL의 들여쓰기는 스페이스 4칸이다. 탭은 쓰지 않는다.
규약: [지킴] 모든 `agt:` 클래스·속성·개체에 `rdfs:label` 한/영 각 1과 한글 `skos:definition`을 단다.
규약: 산문은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase(`agt:Assumption`), 라벨은 한/영 1:1이다.
