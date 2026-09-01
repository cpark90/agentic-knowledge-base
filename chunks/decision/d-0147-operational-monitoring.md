---
iri: https://agentic-knowledge-base.dev/id/chunk-d0147
plane: decision
level: concrete
label_ko: 운영 모니터링이 체계에서 받는 것
label_en: What operational monitoring draws from the system
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 전체 시스템을 모니터링하는 에이전트가 이상 신호를 보내면 문제
지점에 orchestrator를 하네스와 함께 생성해 해결하게 한다. 그 구조의 **지식
측면**을 체계가 공급한다.

**근거** (노트 10.5절)
- 이상 신호의 분류 = `defect` 어휘(인지 / 상호작용 / 실행 요인).
- 이상이 설계 범위 안인가 = ODD 대조(3.5절). 밖이면 ODD 이탈, 안이면 결함.
- 대응 절차 = `agt:Runbook`. 시나리오에 `대응` 링크로 붙는다.
- 새로 생성할 orchestrator의 스코프 = 이상 지점의 청크가 속한 plane과
  그 상위.
- 사후 기록 = 관측 청크 → 상승 (6.3절).
- **사전 시나리오가 모든 이상을 커버한다는 전제는 성립하지 않는다**
  (10.1절 커버리지). 커버되지 않은 이상은 ODD 이탈로 처리하고 유저에게
  넘긴다 — 자동 대응을 시도하지 않는다.
