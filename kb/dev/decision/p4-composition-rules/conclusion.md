---
id: https://agentic-knowledge-base.dev/id/chunk/930258f9-270a-484b-9b01-6841e72a9eae
type: decision
level: concrete
title_ko: 구성 규칙은 비순환·7±2·동질성·참조 재사용이며 shape으로 쓴다
title: Composition rules are acyclicity, 7±2, homogeneity and reference reuse, written as shapes
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
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
| **동질성** | 모든 부분의 plane 클래스와 `agt:hasLevel`이 전체와 같음 (`sh:sparql`) | plane·level을 넘는 관계는 링크 |
| **참조** | 별도 규칙 불필요 | 단일 소스 |

**동질성이 핵심이다.** `part-of`는 같은 plane·level 안에서 청크를 묶는 유일한
수단이고, plane이나 level을 넘는 모든 관계는 링크(Part X)다.

**복합체의 상태는 부분에서 추론된다** — 부분 청크 하나가 `invalidated`이면
복합체는 `suspect`. 이 추론은 `defect-rules`의 규칙 하나다.
