---
id: https://agentic-knowledge-base.dev/id/chunk/c9389c95-3596-453d-9915-6d4a28898afb
type: decision
level: concrete
title_ko: 학습된 판정자는 정확도·판별력·캘리브레이션을 모두 통과해야 한다
title: A learned judge must pass accuracy, discrimination, and calibration
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/0b5e9efb-5c56-4cc8-92bf-bc0ba2f4f531
composite: {id: https://agentic-knowledge-base.dev/id/composite/0b5e9efb-5c56-4cc8-92bf-bc0ba2f4f531, title_ko: 학습된 환경과 학습된 판정자, title: Learned environments and learned judges}
---
**결론** — 시뮬레이션의 두 구성요소는 규칙 기반과 학습 기반의 두 구현 경로를 갖는다. 실환경 관측(`run-kg`)으로 **전이 모델**(행동→환경 반응)과 **판정 모델**(궤적→합격 여부)을 학습해 물리 환경 없이 3단계를 구성하는 것이 실증되어 있다.

- **환경 반응(전이)** — 규칙 기반은 mock을 `schema` 청크에서 생성, 학습 기반은 실환경 관측으로 학습. 조건은 **관측 데이터가 충분하고 상관 검증을 통과**할 것
- **합격 판정** — 규칙 기반은 합격 기준 청크 + 판정 도구, 학습 기반은 학습된 판정자

**학습된 판정자는 세 지표를 모두 통과해야 한다** — 최선 선택의 **정확도**, 성립·불성립의 **판별력**, 확신도의 **캘리브레이션**. 판정자 자체가 검증 대상이며, 판정자를 검증하는 별도 벤치마크가 대상 검증을 예측하는지(상관)를 확인한다.

**커버리지 합산 규칙은 그대로다** — 학습 기반 3단계의 통과는 상관 검증이 유지되는 요인에 대해서만 "시험되었다"로 센다.
