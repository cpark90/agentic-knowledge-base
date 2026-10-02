---
id: https://agentic-knowledge-base.dev/id/chunk/d9954f7c-ecea-4fab-bd8a-b3ca49bd90b5
type: decision
level: abstract
title_ko: 위험 지표의 값 어휘는 S0~S3 · E1~E4 · D1~D3이고 등급을 곱하지 않는다
title: The risk grade vocabulary is S0–S3, E1–E4 and D1–D3, and the grades are never multiplied
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-missing-vocabulary-is-signal, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-10-01T01:35:32+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/1467d7fe-f090-46b6-974d-e8d33bbcfd78, https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a, https://agentic-knowledge-base.dev/id/chunk/d5257525-c3ef-4680-a611-ed964eff79c0]
---
**결론** — 위험 지표의 값 어휘를 순서 척도 셋으로 정한다. 심각도는 S0~S3, 노출은 E1~E4, 탐지가능성은 D1~D3이다. 등급은 현상의 정렬에만 쓰고 곱하지 않는다. 합격 기준은 케이스가 정한다.

심각도(`agt:severityGrade`)의 단계는 정도가 아니라 상황이다.

- S0: 피해가 생성 보고서의 수치에만 남고 산출물·추적성·가정은 달라지지 않는다.
- S1: 산출물 하나가 틀리되 링크 하나를 고치거나 다시 생성해 회복된다.
- S2: 여러 항목이 틀린 전제 위에 서고 회복에 사람의 재판정이 필요하다.
- S3: 틀린 것이 검증된 것으로 기록되어 하류가 그 기록을 근거로 쓴다.

노출(`agt:exposureGrade`)의 단계는 체계가 그 상황에 놓이는 자리다.

- E1: 아직 한 번도 관측되지 않았고 일어나려면 규약을 의도적으로 어겨야 한다.
- E2: 특정 작업에서만 일어나고 관측 건수가 한 자리다.
- E3: 통상 세션에서 일어나고 관측 건수가 두 자리다.
- E4: 매 세션이 그 상황에 놓이거나 관측 건수가 세 자리다.

탐지가능성(`agt:detectabilityGrade`)의 단계는 무엇이 현상을 드러내는가다. 소프트웨어 FMEA가 제어가능성 대신 쓰는 D 자리이고, 세 값은 현상 개체의 `agt:observationMeans`가 실제로 갈리는 세 꼴이다 — 게이트 이름 포함 7 · 그 밖 15 · `미확정` 2다(2026-10-01 실측, 미확정 둘은 P17·P20).

- D1: 게이트가 FAIL로 잡고 메시지가 수정 방향을 낸다.
- D2: 생성 보고서가 수치로 내되 진행을 막지 않는다.
- D3: 관측 수단이 `미확정`이라 사람이 알아차릴 때만 드러난다.

기각한 안은 셋을 1~5로 매겨 곱한 종합 지표다. 순서 척도의 곱이 순위를 왜곡한다는 비판이 공개돼 있고, 곱셈값을 합격 기준에 넣으면 케이스가 정할 자리를 지표가 빼앗는다.

세 척도의 값은 `kb/ontology/shapes/risk-grade-shapes.ttl`의 `sh:in`으로 닫는다. 그 편집은 developer의 몫이다.

미확정: 관측 건수의 자리 수로 노출을 가르는 규칙은 실행 기록이 두 건뿐인 지금의 대리다. 기록이 쌓이면 빈도로 바꾼다.
