---
iri: https://agentic-knowledge-base.dev/id/chunk-d0103
plane: decision
level: concrete
label_ko: 후보 없음(모순)은 자동으로 풀지 않고 유저에게 넘긴다
label_en: Contradictions are handed to the user, never auto-resolved
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 후보 링크가 하나도 남지 않은 상태(모순 신호)는 **자동으로 풀지
않는다.** 세 원인 중 무엇인지 판별한 결과와 함께 유저에게 넘긴다.

**세 원인과 처리** (노트 7.8절)
- **제약이 과도** — 제약 하나를 빼면 후보가 생긴다. 그 제약의 **가정**을
  재검토한다.
- **후보가 부족** — 온톨로지에 후보가 될 개념이 없다. 어휘를 확장한다
  (6.3절 상승 경로).
- **상위 결정이 틀림** — 상위 plane의 청크를 바꾸면 해소된다. 상위를
  재검토한다. 단방향 규칙상 **자동 전파가 불가**하므로 유저 판단이 필요하다.

**대안**
- 판별 절차의 세부는 **미확정**(노트 `[안]`). 자동 해결을 하지 않는다는
  것과 세 원인의 분류는 확정이다.
