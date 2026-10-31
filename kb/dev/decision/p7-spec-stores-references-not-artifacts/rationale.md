---
id: https://agentic-knowledge-base.dev/id/chunk/b7ab2486-78bc-4e4b-9aa0-38fc0d319782
type: decision
level: concrete
title_ko: 산출물을 복사해 넣으면 진실 공급원이 둘이 되고 명세와 구현의 경계가 무너진다
title: Copying artifacts in creates two sources of truth and collapses the boundary between specification and implementation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0183-spec-stores-references-not-artifacts.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:10:57+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:10:57+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/959d935b-e16d-4955-acf0-12c81c12e8aa
---
**근거** — 출처는 harness-concrete `docs/recipes-design.md`의 "What a recipe stores" 절이다.

- 산출물을 복사해 넣는 것은 vendoring이고, 원천과 사본이라는 **두 진실 공급원**을 만든다. 사본은 조용히 드리프트하고, 그 드리프트는 명세가 검증될 때 걸리지 않는다.
- 명세와 구현의 경계도 흐려진다. 구현은 **참조되고 빌드에서 재생성되는 것**이지 명세 안에 사는 것이 아니며, 이 경계가 무너지면 구현 교체가 명세 편집이 된다.
- 판정 기준은 이렇다. 그것이 **조립을 결정하는 정보**이면 명세에 담고, **그 결정의 결과물**이면 참조만 남긴다. 그래서 라벨과 정의, 바인딩, 근거는 담고 본문과 코드, 바이너리는 참조한다.
- 설명을 함께 두는 이유는 식별자의 나열만으로는 왜 이 조합인가가 복원되지 않기 때문이다. 어떤 방법론으로 어떻게 조립해 무엇이 나왔는지를 산문으로 남겨야 명세가 읽히는 문서가 된다.

이 저장소에서 중립 부품을 복사가 아니라 IRI로 참조한다는 규칙(`p4-recipe-as-assembly-spec`)이 부품 축을 다룬다면, 이 결정은 명세와 산출물 축을 다룬다.
