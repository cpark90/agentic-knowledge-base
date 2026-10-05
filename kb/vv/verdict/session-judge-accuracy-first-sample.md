---
id: https://agentic-knowledge-base.dev/id/chunk/27232738-729e-4860-ac93-ee0db71f4c58
type: annotation
level: concrete
title_ko: 라벨 대표성 판정자의 정확도는 유저 재판정 10건 기준 판정자 a 4/10 · b 3/10 이고 둘 다 유저보다 높게 판정한다
title: Against 10 human re-judgements the label representativeness judges score 4/10 and 3/10 in accuracy and both grade higher than the user
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-03T09:07:56Z}
---
thought (non-blocking): 2026-09-30 세션 판정자의 정확도가 처음 측정되었다 — 판별력·판정자 간 일치는 높고 정확도는 낮다.

대상: https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0

본문: 판별력은 미끼 10건 중 값 2 를 받은 것이 0건이고, 판정자 간 일치는 67/70(2026-09-30)과 69/70(2026-09-11, 결정 근거 `https://agentic-knowledge-base.dev/id/chunk/487f2dda-e832-44f5-abbd-3b904b678c6f`)이다. 2026-09-30 세션 판정자의 정확도는 유저 재판정 10건 기준 판정자 a 4/10 · b 3/10 이고 편향은 a +0.6 · b +0.9 로 둘 다 유저보다 높게 판정하며, 수치의 원본은 관측 `https://agentic-knowledge-base.dev/id/chunk/3815425a-7408-421e-b749-344215f01f28` 이다. 같은 측정 방식의 선례는 2026-09-11 실험의 유저 재판정 10건이고, 그 프로토콜 기준(일치 ≥ 9/10)에 이번 두 판정자는 미달한다. 판정자 간 일치가 높아도 정확도가 낮다는 것은 일치율만으로 자동 적용을 여는 근거가 되지 못한다는 뜻이다.

해소: 열림 — 임계 수치는 표본이 더 쌓인 뒤의 항목이다.
