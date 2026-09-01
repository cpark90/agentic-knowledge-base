---
iri: https://agentic-knowledge-base.dev/id/chunk-d0096
plane: decision
level: concrete
label_ko: 모든 미확정은 연결의 미확정이다
label_en: All uncertainty is link uncertainty
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 이 체계에서 미확정은 항상 "두 지식 항목이 연결되는가"의
미확정이다. 값이 미확정인 것처럼 보이는 경우도 연결로 환원한다.
결정한다는 것은 값을 고르는 것이 아니라 **링크 하나를 확정하고 나머지를
기각하는 것**이다.

**근거** (노트 7.1절)
- "인증 방식이 미정이다"는 값의 문제로 보이지만, 이 체계에서는 functional
  항목 `인증 필요`에서 concrete 후보 `OAuth2`·`mTLS`·`APIKey`로 가는
  `refines` 링크 셋 중 어느 것이 성립하는가의 문제다.
- 환원이 성립하는 이유 — 지식 항목은 온톨로지 개체이므로 값이 아니라
  **개체 간 관계**만 존재한다. "값을 갖는다"는 항상 "어떤 개체와
  연결된다"의 줄임말이다.
- **어느 단계든 같다.** 수직 링크(`refines`)의 후보는 주로 logical에
  열거되지만, 수평 링크(`satisfies`·`constrains`·`verifies`)의 후보는
  concrete 항목 사이에도 생긴다 — 확정된 시그니처가 어느 확정된 결정을
  충족하는지 아직 모를 수 있다.
- 미확정은 사다리의 특정 단계에 갇히지 않는다. **연결이 있는 곳이면
  어디든 가능성이 표현되어야 한다.**
