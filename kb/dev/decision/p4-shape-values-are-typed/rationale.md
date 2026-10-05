---
id: https://agentic-knowledge-base.dev/id/chunk/bc30aa28-585f-4771-8093-40ebcd903606
type: decision
level: logical
title_ko: 2026-09-23 실측에서 shape의 sh:datatype이 1이라 슬롯 값이 대부분 문자열이었다
title: The 2026-09-23 survey found a single sh:datatype across shapes, leaving most slot values as strings
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c1a7b38a-801d-4968-9c9f-d8db75756183
---
**근거** — 2026-09-23 실측이 출발점이다. shape 전체에서 `sh:datatype`이 1, `sh:in`이 17, `sh:class`가 10이었고 범위·단위 표기는 없었다. 슬롯 값의 형이 대부분 문자열이라 "이상·이하·약"이 산문에 남았다. 이 공백이 자연어 모호성 항목 M5(값의 형과 단위)다.

유저는 2026-09-23에 링크 견고성 항목을 먼저 수행하고 M1(관계의 성질 공리)과 M5를 함께 옮기라고 답했다. 반영(2026-09-26)에서 `sh:datatype`은 1에서 27이 됐다. 2026-10-03 shape 파일 안의 출현 수는 `sh:datatype` 47, `sh:in` 28, `sh:class` 17이다.

`sh:in`의 원천을 정의의 서술에 맞추는 것은 저장소 구축(2026-09-01) 때부터의 권장이다. 그 원문은 값을 추가하면 해당 개념의 `skos:definition`도 갱신하라고 적었다.

미확정: M5의 "단위"는 shape에 자리가 없다. 2026-10-03 실측에서 단위를 값으로 다루는 shape는 0이다.
