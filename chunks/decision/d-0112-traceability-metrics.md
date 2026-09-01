---
iri: https://agentic-knowledge-base.dev/id/chunk-d0112
plane: decision
level: concrete
label_ko: 추적성 지표 다섯과 그 경고 신호
label_en: Five traceability metrics and their warning signals
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 링크 모델의 건강을 다섯 지표로 관측하고, 각 지표의 움직임을
특정 고장의 경고로 읽는다.

- **링크 밀도** = 링크 수 / 청크 수. 급락하면 **구축 누락**
- **`suspect` 비율** = suspect / 전체. 상승하면 **재판정 지연**
- **평균 재판정 지연** = suspect 진입 → 해소 시간. 상승하면 **재판정
  경계**(8.6절)를 조정한다
- **복원 비율** = 복원 링크 / 전체. 상승하면 **구축이 안 되고 있다**
  (구축이 기본, 복원은 예외)
- **확정 정밀도** = 확정 후 `invalid`가 된 비율. 나쁘면 **판정 근거**
  (8.8절)를 재검토한다

**근거** (노트 8.14절) — 지표 각각이 8.3·8.6·8.8절 메커니즘 하나에
대응한다. 어느 지표가 나빠졌는지가 곧 어느 메커니즘을 손볼지를 가리킨다.
