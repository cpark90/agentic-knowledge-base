---
iri: https://agentic-knowledge-base.dev/id/chunk-d0064
plane: decision
level: concrete
label_ko: 판정 방법을 A~D로 등급화하고 D는 ODD에 넣지 않는다
label_en: Grade measurement methods A-D; grade D stays out of the ODD
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — ODD 속성의 판정 방법을 A~D로 등급화하고, **판정 불가(D) 속성은
ODD에 넣지 않는다.** D는 가정으로만 기록하되 무효화 트리거가 될 수 없음을
안다.

**근거** (노트 3.9절)
- A는 기계가 질의 하나로 즉시 판정한다(언어·의존성 버전, 헬스체크).
  B는 기계가 판정하되 비용이 있어 주기 판정한다(테스트 실행, 벤치마크).
  C는 사람이 판정하므로 주기적 재확인이 필요하다("고객이 이 기능을 원한다").
  D는 판정 불가다("경쟁사가 먼저 출시하지 않는다").
- 등급이 낮은 속성이 많으면 대조가 `unverified`로 남아 ODD 이탈을 놓친다
  (3.5절). 등급은 이 위험을 측정하는 지표다.
- D를 ODD에 넣으면 영원히 `unverified`인 속성이 생겨 ODD 전체의 대조 결과가
  늘 불완전해진다.
