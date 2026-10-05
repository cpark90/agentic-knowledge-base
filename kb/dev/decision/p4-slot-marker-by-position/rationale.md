---
id: https://agentic-knowledge-base.dev/id/chunk/bb9956b6-40ec-44e7-916e-b10ac894d016
type: decision
level: logical
title_ko: 표지 셋을 더한 날 본문 중간의 강조 네 곳이 슬롯으로 방출되었다
title: On the day three markers were added, four emphases mid-body were emitted as slots
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e1fb54c7-56d8-4864-b56b-cbd7327217d1
---
**근거** — 2026-09-29 실측이 출발점이다. V&V 시나리오의 표지 셋(`자극`·`요인`·`배제 자극`)을 더하자 본문 중간의 "요인 분류"·"요인별로" 같은 굵은 강조가 슬롯으로 방출되었다. 오탐은 `d-0134`·`p8-scenario-authoring`·`p8-simulation-credibility`·`p8-two-verification-targets`의 넷이다. 슬롯 방출은 본문 shape(`*-body-shapes.ttl`)가 순서와 필수 여부를 판정하는 입력이다.

게이트 `decision-role`은 이미 "본문 첫 산문 줄이 굵은 표지로 시작한다"는 자리 판정을 쓰고 있었다. 방출도 그것과 같게 맞춰 두 판정이 갈리지 않게 했다.

한정어 규칙은 2026-09-13 첫 실행의 실측에서 왔다. 대안 청크 21/187이 한정어 형태였고, 그것은 "대안 없음"을 기록하라는 규칙의 이행이지 표지 누락이 아니었다(`p6-mass-fail-suspects-the-rule`). 길이 상한은 "요인 분류가 환경 배정을 결정한다."처럼 표지 낱말로 시작하는 문장을 한정어로 읽지 않으려고 둔다.

접두 겹침 검사는 같은 날 드러난 공백을 메운다. 표지를 늘리는 사람이 기존 표지와의 겹침을 확인할 수단이 없었다.
