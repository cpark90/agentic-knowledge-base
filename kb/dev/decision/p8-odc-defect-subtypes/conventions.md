---
id: https://agentic-knowledge-base.dev/id/chunk/420be28e-3208-4a07-a2b5-83f8083d54ed
type: decision
level: concrete
title_ko: 규범 문서 규약 — 세 갈래 아래에 ODC 유형과 에이전트 고유 유형을 배치한다
title: Normative-document conventions — ODC types plus agent-specific types sit under the three factors
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:40+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/49d21395-f143-4467-b1e8-55c07e9341dc
---
**규약** — `p8-odc-defect-subtypes`의 결론을 규범 문서에 싣는 문장이다.

규약: 위험 분석의 어휘 | 현상은 `kb/ontology/related/defect/`에 있는 `defect` 모듈의 요인 개체다. 하위 유형 14는 인지와 상호작용, 실행의 세 갈래 아래 ODC 유형이고, 피해는 ODC 영향 차원 다섯인 `agt:DefectImpact`이며, "지식 유실·재생산"은 H1 하위다. 현상 개체는 정의와 P번호 표기, 관측 수단, 출처를 갖는다(게이트 `shacl`, `defect-factor-shapes`). 위험 지표 S와 노출, 탐지가능성은 순서 척도이므로 **곱하지 않으며**, 등급은 정렬용이고 합격 기준은 테스트 케이스가 정한다. 탐지가능성 D는 현상 개체의 `agt:observationMeans`가 갈리는 세 꼴에서 도출되어, 게이트 이름이면 D1, 생성 보고서가 수치로 내되 진행을 막지 않으면 D2, `미확정`이면 D3다. 값의 원본은 `defect-rules/risk-grade-rules.ttl`이므로 수를 여기 적지 않는다. 관측 수단 다섯이 서서 D3가 둘로 줄었다(2026-10-01). `미확정`을 유지하는 현상은 그 까닭을 정의문에 적는데, 관측 수단 자리에 산문을 덧붙이지 않는 것이 세 빈 값 규칙이기 때문이다. 규칙성 가정 A1~A3은 `id:asm-links-only-interaction`, `asm-finite-factor-types`, `asm-missing-vocabulary-is-signal`이고, 프로파일에서 파생되는 항목이 이 가정을 `assumes`로 참조한다(2026-09-29). 현상에서 피해로 가는 인과는 `defect-rules` 모듈의 `agt:hasImpact` 트리플이고, 첫 형태 28건이 질문지의 피해 열이다. 어휘인 `defect`와 형식화인 `defect-rules`를 나눈 이유는 어휘가 안정적이고 규칙이 자주 바뀌므로 어휘 사용자가 규칙 변경에 영향받지 않아야 한다는 데 있다(노트 2.3절 (b)).
규약: 결함 하위 유형 | 코어 `defect` 모듈의 하위 유형 14를 그대로 쓴다 | 채움(2026-09-29, `kb/ontology/related/defect/`, 현상 22·피해 6)
