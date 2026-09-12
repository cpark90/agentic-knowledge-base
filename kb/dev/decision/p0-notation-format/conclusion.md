---
id: https://agentic-knowledge-base.dev/id/chunk/0b18332b-1a03-4019-a50f-9c419b230184
type: decision
level: concrete
title_ko: 온톨로지 자체가 용어집이다
title: The ontology is the glossary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7, https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0031]
part_of: https://agentic-knowledge-base.dev/id/composite/fc68c83c-8feb-47ce-8dea-30f24d2ee645
composite: {id: https://agentic-knowledge-base.dev/id/composite/fc68c83c-8feb-47ce-8dea-30f24d2ee645, title_ko: 표기 형식과 용어집의 위치, title: Notation format and where the glossary lives}
---
**결론** — 표기를 다음으로 고정한다.

- **식별자** — 영어 단수 소문자 케밥 (`design-space`)
- **개념** — PascalCase (`agt:Assumption`)
- **산문·설명** — 한글
- **용어집** — 한글↔영어 1:1 대응 고정. 확정 후 동의어 사용 금지
- **용어집의 위치** — 온톨로지의 `rdfs:label`. **온톨로지 자체가 용어집이다**

출처 보강(2026-09-11, 확정 문장 커버리지 감사): 노트 13.3절(언어 정책 — 한글·영어 강제, 0.6절 참조)도 이 결정의 원문이다.
