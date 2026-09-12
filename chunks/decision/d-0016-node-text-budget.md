---
id: https://agentic-knowledge-base.dev/id/chunk-d0016
type: decision
level: concrete
title_ko: 노드 서술 텍스트는 130–260 token 대역에 두고 상한만 기계적으로 강제한다
title: Node description text stays in a 130-260 token band, with only the upper bound enforced
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
generated: {by: claude/fable-5, at: 2026-09-12T00:50:00+09:00}
---
**결론** — 검색 단위로 뷰에 실리는 노드의 서술 텍스트 합은 260 token을
넘지 않는다 (측정: 문자수 ÷ 4 — 외부 tokenizer에 의존하지 않아
결정론적). 목표 대역은 130–260 token이며 하한은 권고, 상한만 기계적으로
강제한다.

**근거** (harness-functional ONTOLOGYSTYLE §1c)
- 검색 정밀도 최적대가 100–200 word(≈130–260 BPE token)라는 실증에서
  온 값이다.
- 초과는 그 노드가 두 가지 이상을 말하고 있다는 단일 책임 위반
  신호다 — 분해하거나, 같은 대상의 대안 서술이면 별도 노드로 분리한다.
- 텍스트를 지닌 노드에는 토큰 추정치를 반드시 붙인다 — 빠지면 뷰
  예산이 부정확해져 context rot 방어가 샌다. 뷰 비용(추정치)과 런타임
  관측량은 별개 축이므로 섞지 않는다 — 섞으면 팩이 조용히 잘린다
  (실제 발생한 결함).

**이 저장소와의 관계** — 42줄 청크 규칙(d-0002)과 같은 뿌리의 예산
규칙이다. 42줄은 조망 단위, 130–260 token은 검색 정밀도 단위로, 둘 다
"한 단위 = 한 주제"를 크기로 강제한다.
