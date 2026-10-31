---
id: https://agentic-knowledge-base.dev/id/chunk/930258f9-270a-484b-9b01-6841e72a9eae
type: decision
level: concrete
title_ko: 구성 규칙은 비순환·7±2·동질성·참조 재사용이며 shape으로 쓴다
title: Composition rules are acyclicity, 7±2, homogeneity and reference reuse, written as shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0074-composition-rules-homogeneity.md, id: https://agentic-knowledge-base.dev/id/chunk-d0074, title_ko: "구성 규칙 — 비순환·7±2·동질성·참조 재사용", title: "Composition rules - acyclic, 7+-2, homogeneity, reference reuse"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4, https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0074]
part_of: https://agentic-knowledge-base.dev/id/composite/27157a50-048e-4b31-835f-ce91abcb93a8
composite: {id: https://agentic-knowledge-base.dev/id/composite/27157a50-048e-4b31-835f-ce91abcb93a8, title_ko: 구성 규칙, title: Composition rules}
---
**결론** — 구성 규칙을 shape으로 쓴다.

| 규칙 | shape | 근거 |
|---|---|---|
| **비순환** | `part-of` 반대칭 공리로 추론 | 상위 온톨로지 |
| **7±2** | `agt:hasDirectPart` `sh:maxCount 9` | 인지 한계 |
| **동질성** | 모든 부분의 지식 종류 클래스와 `agt:hasLevel`이 전체와 같음 (`sh:sparql`) | 지식 종류·level을 넘는 관계는 링크 |
| **참조** | 별도 규칙 불필요 | 단일 소스 |

**동질성이 핵심이다.** `part-of`는 같은 지식 종류·level 안에서 단위 지식을 묶는 유일한
수단이고, 지식 종류나 level을 넘는 모든 관계는 링크(Part X)다.

**복합체의 상태는 부분에서 추론된다** — 부분 단위 지식 하나가 `invalidated`이면
복합체는 `suspect`. 이 추론은 `defect-rules`의 규칙 하나다.

**게이트** (노트 4.5절, analysis와 verify) — 규칙마다 판정 자리가 다르다. shape `composite-shapes`가 직접 부분 9 이하를 보고, `composite-order-shapes`가 순서 있는 복합체의 색인 1..n 연속과 중복 없음, 부분 집합과의 일치를 본다(2026-09-29, 게이트 id `shacl`). 분석 시점에는 `kb_decision`이 결정의 세 부분·수준·`ordered`와 부분 집합의 일치를 보고, `kb_composite`가 부분 2~9와 지식 종류·수준 한 쌍을 본다(2026-09-29). 생성 시점에는 `gen_build._check_bundle`이 묶음(패키지 × `composite.id`)의 패키지 밖 부분, 중복 선언, 이질, 상한, `ordered`와 부분 집합의 불일치를 거부한다(게이트 id `gen-build`). 전체 복합체는 verify 질의 `composite-heterogeneous`·`composite-cycle`이 본다(2026-09-13, 게이트 id `verify`). 해소는 저작자가 복합체 선언과 부분 단위 지식을 고치는 것이다.
