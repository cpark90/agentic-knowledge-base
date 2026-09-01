---
iri: https://agentic-knowledge-base.dev/id/chunk-d0139
plane: decision
level: concrete
label_ko: 테스트베드의 구성과 ODD 부분집합 제약
label_en: Testbed composition and the ODD-subset constraint
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 테스트베드는 **3~4단계 환경의 영속적 구현**이며, 그 환경 정의는
**ODD의 부분집합**이어야 한다.

**근거** (노트 10.1절) — 여섯 구성과 이 체계에서의 대응.
- 시나리오 저장소 = `-kg`의 시나리오 구성체 (재현 가능한 concrete 시나리오)
- 환경 정의 = ODD의 부분집합 (각 단계의 mock·인프라·seed 구성)
- 실행기 = 하네스의 일부 (시나리오를 환경에서 실행하고 관측을 기록)
- 관측 저장소 = `run-kg`
- 판정기 = `defect-rules` (합격 기준 청크를 관측에 적용)
- 비교기 = `prov:wasRevisionOf` 연쇄 위의 질의 (같은 시나리오의 시간에 따른
  결과 변화)

**ODD 부분집합이어야 하는 이유** — 환경이 ODD 밖 조건을 포함하면 그 환경의
통과는 설계 범위 안에서의 통과를 뜻하지 않는다. ODD 이탈
시나리오(`odd:outside`) 실행은 허용하되 커버리지에 넣지 않는다.

**대안**
- 외부 평가자 다수를 고용해 각자의 관점으로 시나리오를 평가하는 것 —
  **미확정**. 5단계의 한 형태다. 평가자의 질의("얼마나 이상한가", "왜 그렇게
  보는가")는 관측 청크로 기록하고 요인 태그를 붙여 상승의 입력으로 삼는다.
