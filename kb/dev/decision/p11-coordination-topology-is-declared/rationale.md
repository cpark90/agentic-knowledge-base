---
id: https://agentic-knowledge-base.dev/id/chunk/5895ac5f-7189-416c-a753-fad653349483
type: decision
level: concrete
title_ko: 선언되는 차원이어야 방식이 공존하고 확장이 가산적이다
title: Only as a declared dimension do topologies coexist and extensions stay additive
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0185-topology-as-declared-dimension.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:16:35+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:16:35+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/2c1f938b-829d-4a41-b29b-b82d166d0ab5
---
**근거** — 출처는 harness-concrete `docs/composition-methodology.md`다.

- 조율 방식을 전역 상수로 두면 다른 방식이 필요한 구성물이 체계 자체를 고치도록 요구한다. 반면 선언되는 차원으로 두면 서로 다른 방식이 **공존**하고 어느 쪽도 다른 쪽을 밀어내지 않으며, 기본 방침도 대안 가운데 하나일 뿐이다.
- 한 방식은 **방침 개체와 통로 개체의 짝**으로 표현한다. 방침만으로는 참여자와 매체가 정해지지 않고, 통로만으로는 누가 무엇을 결정하는지가 없다. 그래서 짝으로 두어야 선언 하나가 조율 방식 전체를 특정한다.
- 따라서 **확장이 가산적**이다. 새 방식은 방침과 통로의 한 쌍과 그것을 물고 있는 구성물 하나를 추가하면 끝이고, 어휘도 기존 방식도 바뀌지 않는다. 어휘 변경을 요구하는 확장은 이 차원을 잘못 모델링했다는 신호다.
- 다만 기본값은 여전히 필요하다. 대부분의 구성물이 같은 방식을 쓰므로 기본 개체를 라이브러리에 두어 재사용하게 하고, 재정의는 예외로 남긴다. 재정의를 허용한다는 것과 매번 새로 정의하는 것은 다르다.

이 결정은 코어를 고치지 않고 하위 클래스와 shape의 추가만 허용하는 프로파일 규칙(`p2-skeleton-and-domain-profile`)의 개체(A-Box) 축 대응이다.
