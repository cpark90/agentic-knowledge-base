---
id: https://agentic-knowledge-base.dev/id/chunk-d0185
type: decision
level: concrete
title_ko: 조율 방식은 전역 고정이 아니라 구성물이 선언하는 차원
title: Coordination topology is a declared dimension, not a global constant
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 구성물의 참여자들이 **어떻게 조율하는가**(topology)는 체계
전역에 하나로 고정하지 않는다. 재사용 가능한 기본 개체로 제공하되, 구성물
마다 어느 것을 쓰는지 **선언**하고 필요하면 자기 것을 정의해 덮어쓴다.

**근거** (harness-concrete docs/composition-methodology.md)
- 조율 방식을 전역 상수로 두면 다른 방식이 필요한 구성물이 체계 자체를
  고치도록 요구한다. 선언되는 차원으로 두면 서로 다른 방식이 **공존**하고
  어느 쪽도 다른 쪽을 밀어내지 않는다 — 기본 방침도 대안 중 하나일 뿐이다.
- 한 방식은 **방침 개체 + 통로 개체의 짝**으로 표현한다. 방침만으로는
  참여자와 매체가 정해지지 않고, 통로만으로는 누가 무엇을 결정하는지가
  없다. 짝으로 두어야 선언 하나가 조율 방식 전체를 특정한다.
- 그래서 **확장이 가산적**이다: 새 방식은 (방침, 통로) 한 쌍과 그것을 물고
  있는 구성물 하나를 추가하면 끝이고, 어휘도 기존 방식도 바뀌지 않는다.
  어휘 변경을 요구하는 확장은 이 차원을 잘못 모델링했다는 신호다.
- 기본값은 여전히 필요하다. 대부분의 구성물이 같은 방식을 쓰므로 기본
  개체를 라이브러리에 두어 재사용하게 하고, 재정의는 예외로 남긴다 —
  재정의를 허용한다는 것과 매번 새로 정의하는 것은 다르다.

**이 저장소와의 관계** — 골격을 고치지 않고 하위 클래스·shape 추가만
허용하는 프로파일 규칙(d-0057)의 개체(A-Box) 축 대응이다.
