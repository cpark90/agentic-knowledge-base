---
iri: https://agentic-knowledge-base.dev/id/chunk-d0101
plane: decision
level: concrete
label_ko: 제약 전파는 게이트와 재판정 경계에서만 실행
label_en: Run constraint propagation only at gates and re-judgement boundaries
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 제약 전파는 **검사 게이트 통과 시점과 재판정 경계**(9.1절
입력)에서 실행한다. 편집마다 실행하지 않는다. 전파 알고리즘은 자체
구현하지 않고 기성 방식을 쓴다.

**근거** (노트 7.6절)
- 후보 링크의 도메인 축소는 **호 일관성(arc consistency)** 검사이고, 새
  제약 도입 시 영향받는 변수만 다시 검사하는 증분 방식이 이미 성숙해 있다.
- 편집이 연속되는 동안 매번 전파하면 낭비다 — 링크 재판정(8.6절)이
  경계에서 일괄로 도는 것과 같은 이유다.

**대안**
- 어느 전파 알고리즘·구현을 쓸지는 **미확정**(노트 `[안]`). 자체 구현하지
  않는다는 것만 정해져 있다.
