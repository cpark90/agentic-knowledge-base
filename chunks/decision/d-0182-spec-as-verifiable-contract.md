---
iri: https://agentic-knowledge-base.dev/id/chunk-d0182
plane: decision
level: concrete
label_ko: 명세는 주장이 아니라 검증 가능한 계약이다 — 게이트는 세 방향
label_en: A spec is a verifiable contract, not an assertion - three gate directions
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-harness-recipes]
generated_at: 2026-09-02T00:00:00+09:00
---
**결론** — 명세는 "이렇게 되어 있다"는 주장이 아니라 **기계가 판정할 수
있는 계약**으로 쓴다. 같은 명세가 생성의 입력이자 검증의 기준이 된다.
그리고 검사 게이트는 서로 다른 **세 방향**이며, 하나의 초록이 나머지를
말해 주지 않는다.

| 방향 | 묻는 것 |
|---|---|
| 구조 | 저장된 그래프가 연결·타입·충족을 만족하는가 |
| 원천 → 명세 | 원천의 구조 요소가 모두 표현되었는가 (coverage audit, d-0015) |
| 명세 → 산출 | 만들어진 것이 명세의 계약을 만족하는가 |

**근거** (harness-concrete docs/odr-contract-verify.md)
- 구조 검증의 통과는 산출물에 대해 **아무것도 말하지 않는다.** 잘 형성된
  그래프가 아무것도 만들지 못하거나 틀린 것을 만들 수 있다. 세 번째
  방향이 없으면 명세는 끝까지 검증되지 않은 주장으로 남는다.
- 명세를 계약으로 쓰면 판정 근거가 산출물이 아니라 명세에 있다. 산출물을
  다시 만들 때마다 기준을 다시 쓰지 않아도 되고, 기준의 변경 이력이
  산출물의 변경 이력과 섞이지 않는다.
- 생성의 입력과 검증의 기준을 **하나의 문서**로 두는 것이 핵심이다. 둘을
  따로 쓰면 그 둘 사이가 새로운 드리프트 면이 된다.
