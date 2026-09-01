---
iri: https://agentic-knowledge-base.dev/id/chunk-d0061
plane: decision
level: concrete
label_ko: ODD 이탈은 결함이 아니라 신호다
label_en: ODD exit is a signal, not a defect
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 실행 시점의 실제 조건을 `run-kg`에 관측으로 기록하고 ODD와
대조한다. 속성 하나 이상이 ODD 밖이면 **ODD 이탈**이며, 이탈은 결함이 아니라
설계 범위 밖 상황에 들어섰다는 신호다. 대응은 둘 — 기본값은 작업 중단과
유저 에스컬레이션, 이탈이 반복되면 ODD 확장 후보로 올린다(3.6절).

**근거** (노트 3.5절)
- ODD는 설계 시점의 조건이므로 실행 조건과 어긋날 수 있다. 대조 결과는 셋
  이다 — 전부 ODD 안(정상), 하나 이상 밖(이탈), 판정 불가 속성 존재(대조
  불완전, `unverified`로 두고 판정 방법 보완 대상).
- 이탈의 파급은 항목별 가정 위반보다 넓다. 가정 위반은 항목 하나를
  무효화하지만, ODD 이탈은 그 속성에 의존하는 **전부**를 6.5절 무효화
  대상으로 만든다.
- 이탈 감지는 판정 방법이 있는 속성에서만 가능하다. 판정 방법이 없는 속성은
  이탈해도 알 수 없다 — 판정 방법이 필수인 두 번째 이유다.
