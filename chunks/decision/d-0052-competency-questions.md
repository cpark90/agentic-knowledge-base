---
iri: https://agentic-knowledge-base.dev/id/chunk-d0052
plane: decision
level: concrete
label_ko: 경쟁 질문이 온톨로지의 요구사항이다
label_en: Competency questions are the ontology's requirements
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 온톨로지의 요구사항을 "답해야 할 질문 목록"(competency question,
CQ)으로 정의한다. 각 질문은 그래프 질의 하나로 답할 수 있어야 하고,
온톨로지가 충분한지를 이 목록으로 검사한다. 새 개념을 추가할 때는 어느
경쟁 질문에 기여하는지 적으며, 답할 수 없게 만드는 변경은 검토 대상이다.

**근거** (노트 2.7절)
- 온톨로지 공학의 표준 관행이다 (0.0절 표준어 원칙).
- 질문이 질의 하나로 답되지 않으면 필요한 링크·상태·속성이 온톨로지에 없다는
  뜻이다. 요구사항 누락이 개념을 늘리기 전에 드러난다.
- CQ 18개가 덮는 범위: 추적성(코드↔결정, `satisfies`·`verifies` 빈 칸,
  `allocates`), 가정과 무효화(가정 상태, 역방향 전파, 같은 가정에 의존하는
  집합, 재검토되지 않은 무효 항목), 스코프와 가시성(에이전트가 지금 볼 수
  있는 것, 스코프 밖 의존), ODD 대조(시나리오가 범위 안인가), 근거 보존
  (배제된 대안, 상승으로 올라간 제약), provenance, 결함 추론, 그리고
  온톨로지 자기 점검(고립 개념)과 운영 통계(42줄 초과 분포).
