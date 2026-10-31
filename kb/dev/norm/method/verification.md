---
id: https://agentic-knowledge-base.dev/id/chunk/49d90c85-6c85-4d78-91aa-056a1bfa04f3
type: norm
level: logical
title_ko: docs/method.md 절 — 검증은 두 번째 지식 베이스인 V&V KB다
title: docs/method.md section — verification is the second knowledge base in the V&V layer
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:27:16+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6a4bb0-67a3-435c-bdab-850ae50240c4
composite: {id: https://agentic-knowledge-base.dev/id/composite/ec6a4bb0-67a3-435c-bdab-850ae50240c4, title_ko: docs/method.md의 검증·영향 분석 절 묶음, title: docs/method.md verification and impact analysis section group, part_of: https://agentic-knowledge-base.dev/id/composite/c040ba95-dc6c-4c10-af69-8d0d4c0cf6ec, ordered: [https://agentic-knowledge-base.dev/id/chunk/49d90c85-6c85-4d78-91aa-056a1bfa04f3, https://agentic-knowledge-base.dev/id/chunk/5bf9e568-5eb8-4c6e-b0fb-b59020cea362, https://agentic-knowledge-base.dev/id/chunk/3d45e545-3e32-424e-8f36-0b6c9eda7354, https://agentic-knowledge-base.dev/id/chunk/6b073d14-5780-416a-af16-5b54897193ab, https://agentic-knowledge-base.dev/id/chunk/544c73da-ad3f-4d03-a0ac-8561fc696df1]}
heading: 검증 — V&V KB로
depth: 2
---
v1의 "검증은 응용"은 v3부터 대체되었다(`p8-two-knowledge-bases`). 검증·확인은 **두 번째 지식 베이스**이고, 절차는
§14 V&V에 있다 ([`p12-dev-vv-kb-exchange`](../../decision/p12-dev-vv-kb-exchange/conclusion.md)).
코어가 제공하는 단위는 시험 대상과 경계를 정하는 ODD, 결과를 축적하는 실행 기록, 실패를 분류하는 defect다.

2026-09-19의 첫 형태에서 사슬은 세 고리로 이루어진다. 검증 목표(`kb/vv/goal/`, requirement·functional)는 개발 요구에서
`derivesFrom`으로 파생된다. 합격 기준(`kb/vv/criteria/`, contract·logical)은 `refines`로 검증 목표를 가리키고, 그 판정
술어가 게이트다. 테스트 케이스(`kb/vv/case/`, schema·concrete)는 자극과 기대, 실행 명령을 담아 `refines`로 합격 기준을
가리키고, `verifies`로 개발 결정의 결론(concrete)을 가리킨다. 테스트 케이스가 `schema` 지식 종류인 이유는 `refines`가
contract와 schema가 decision 뒤에 오는 지식 종류의 순서를 거스르지 못하기 때문이다. 검증기(`kb/vv/verifier/`, artifact·executable)와
판정 주석(`kb/vv/verdict/`, annotation)도 2026-09-22에 실물을 얻었다. 실행기 `vv_run`이 테스트 케이스의 실행 명령 가운데
읽기 전용 검증기를 돌려 실행 기록(`kb/vv/run/`, memory·concrete, append-only, `process:vv_run`)을 남기고, 감사 보고서
`//kg:audit`가 그래프와 그 기록만으로 검증 현황을 낸다. 이로써 V&V 순환이 처음으로 닫혔다.
