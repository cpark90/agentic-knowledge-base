---
iri: https://agentic-knowledge-base.dev/id/chunk-d0140
plane: decision
level: concrete
label_ko: 결함 요인 3갈래와 위험 시나리오의 구성
label_en: Three defect factors and how risk scenarios are composed
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 실패 요인을 **인지 / 상호작용 / 실행** 세 갈래로 분류한다.
에이전트 작업의 세 단계에 대응한다. **위험 시나리오는 요인을 하나 이상
포함하는 시나리오**이며, 세 갈래의 요인을 조합해 위에서 아래로 체계적으로
구성한다.

**근거** (노트 10.1절)
- **인지 요인** — 입력을 잘못 읽음. 예: 잘못된 테스트 결과를 근거로 삼음,
  오래된 문서 기반 추측.
- **상호작용 요인** — 다른 행위자와의 조율 실패. 예: 통신 로직 충돌,
  동시 편집 충돌.
- **실행 요인** — 판단은 옳았으나 수행 실패. 예: 잘못된 명령어, 환경 불일치.
- `defect` 어휘가 요인을, `defect-rules`가 조합 규칙을 담는다.
- 세 갈래가 뒤의 두 판단의 1차 기준이 된다 — 환경 배정(10.1절)과 결함
  귀속(제품이냐 에이전트냐, 10.12절).
- 시나리오를 요인 조합에서 내려 만들면 "무엇을 아직 시험하지 않았는가"가
  조합 공간의 빈칸으로 보인다.
