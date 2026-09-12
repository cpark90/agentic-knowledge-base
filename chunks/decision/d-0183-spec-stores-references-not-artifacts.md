---
id: https://agentic-knowledge-base.dev/id/chunk-d0183
type: decision
level: concrete
title_ko: 조립 명세는 산출물을 저장하지 않고 참조만 담는다
title: An assembly spec stores references, never the artifacts themselves
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 조립 명세 단위가 담는 것은 셋이다: **명세**(부품 식별자와 그
조립), **설명**(어떤 부품과 방법론으로 무엇을 만들었는가), **참조**(구체
산출물의 위치). 구체 산출물 자체 — 실제 코드, 문서 본문, 지시문 본문 —
는 담지 않는다.

**근거** (harness-concrete docs/recipes-design.md §"What a recipe stores")
- 산출물을 복사해 넣는 것은 vendoring이고, 원천과 사본이라는 **두 진실
  공급원**을 만든다. 사본은 조용히 드리프트하고, 그 드리프트는 명세가
  검증될 때 걸리지 않는다.
- 명세와 구현의 경계가 흐려진다. 구현은 **참조되고 빌드에서 재생성되는
  것**이지 명세 안에 사는 것이 아니다 — 이 경계가 무너지면 구현 교체가
  명세 편집이 된다.
- 판정 기준: 그것이 **조립을 결정하는 정보**이면 명세에 담고, **그 결정의
  결과물**이면 참조만 남긴다. 라벨·정의·바인딩·근거는 담고, 본문·코드·
  바이너리는 참조한다.
- 설명을 함께 두는 이유 — 식별자의 나열만으로는 "왜 이 조합인가"가
  복원되지 않는다. 어떤 방법론으로 어떻게 조립해 무엇이 나왔는지를 산문
  으로 남겨야 명세가 읽히는 문서가 된다.

**이 저장소와의 관계** — 중립 부품을 복사가 아니라 IRI로 참조한다는
규칙(d-0018)이 부품 축을 다룬다면, 이 청크는 명세와 산출물 축을 다룬다.
