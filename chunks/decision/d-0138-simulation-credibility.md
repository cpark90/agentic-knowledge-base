---
iri: https://agentic-knowledge-base.dev/id/chunk-d0138
plane: decision
level: concrete
label_ko: 시뮬레이션의 신뢰도는 요인별로 관리한다
label_en: Simulation credibility is managed per defect factor
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 시뮬레이션이 실환경을 대신하려면 **시뮬레이션 자체가 검증되어야
한다.** 신뢰도는 통째로가 아니라 **결함 요인별로** 기록한다.

**근거** (노트 10.1절)
- 3~4단계 통과가 실환경 통과를 예측한다는 근거가 없으면 사다리가
  무의미하다.
- 신뢰도 근거 넷 — **상관**(같은 시나리오를 시뮬레이션과 실환경에서 실행해
  대조. 불일치가 시뮬레이션 결함), **이탈 관측**(실환경에서만 발견된
  결함, 즉 트리거가 '실행 시'인 결함의 비율. 높으면 시뮬레이션이 그 요인을
  못 잡는 것), **mock 계약**(mock이 실제 서비스의 `schema` 청크를 준수하는지
  shape 검사), **합성 데이터 분포**(ODD 동적 요소의 값 범위 안인지).
- "시뮬레이션이 믿을 만하다"가 아니라 "순서·동기화 요인에 대해서는 믿을
  만하고 실제 사용자 분포에 대해서는 아니다"로 기록한다. 이것이 환경
  배정표(10.1절)의 근거를 갱신한다.

**대안**
- 실환경 관측으로 시뮬레이션을 보정하는 것(역강화학습 등으로 외부 행위자를
  모사) — **미확정**. 4~6단계 관측이 충분히 쌓인 뒤의 과제다. 그 전에는
  mock을 `schema` 청크에서 직접 생성한다.
