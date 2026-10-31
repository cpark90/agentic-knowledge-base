---
id: https://agentic-knowledge-base.dev/id/chunk/1b200fe1-27e5-419f-8fe5-eaf4d13b6e90
type: norm
level: logical
title_ko: docs/method.md 절 V&V 절차의 이어짐 — 위험 분석 G1~G6의 산출과 나머지 절차
title: docs/method.md V&V procedure section continued — the outputs of risk analysis G1 to G6 and the remaining procedures
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:17:27+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4a1e3076-cfac-4bb5-b327-92c6093a38d1
continues: true
form: table
columns: [절차, 요지, 결정]
link_column: 결정
items: [p8-mismatch-attribution#2, p8-vv-reports#1, p8-agent-vv#1 + p12-cognition-measurement, p12-symbolic-diagnosis#1 + p12-incident-postmortem, p8-proactive-vv#1]
---
위험 분석 G1의 산출은 `defect` 모듈의 요인 개체이고, 피해와 현상, 가정은 질문지의 것을 그대로 채택했다(유저 답, 2026-09-29). 현상을
더할 때는 세 갈래 아래 **잎으로만** 더하고 새 상위 개념을 만들지 않는다. 개체마다 정의와 질문지 표기 `skos:notation`, 관측
수단 `agt:observationMeans`, 출처를 적는다. 관측 수단이 아직 없으면 `미확정`을 적고 그 까닭은 정의문에 적으며, 미확정의 수가
위험 분석의 산출 후보다. 2026-10-01에 미확정은 P17과 P20의 둘이다. G2의 인과는 `agt:hasImpact`로, G3은 `agt:hasTrigger`와
`agt:discoveredAtLevel`로, G4의 지표는 `agt:severityGrade`와 `agt:exposureGrade`, `agt:detectabilityGrade`로, G5의 부류는
`agt:exposesFactor`로 적는다. 판정은 vnv가 `kb/vv/`에서 하고, T-Box 트리플은 developer가 `defect-rules`의
`impact-causation-rules.ttl`로 옮긴다. 등급은 곱하지 않는다. G6의 목표 거동은 술어가 아니라 V&V 요구와 결정의 본문으로 적는다.
