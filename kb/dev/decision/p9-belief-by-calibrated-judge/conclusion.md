---
id: https://agentic-knowledge-base.dev/id/chunk/88b97e4d-57de-4ec9-8824-5decb2f9184f
type: decision
level: logical
title_ko: 믿음 정도는 판정자의 확신도를 사람 정답 라벨로 보정한 값이다
title: Degree of belief is the judge's confidence calibrated on human ground-truth labels
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-22T20:51:33+09:00}
layer: methodology
composite: {id: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d, title_ko: 사람 라벨로 보정한 판정자 확신도, title: Judge confidence calibrated on human labels}
part_of: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d
---
**결론** — 세션 판정자가 링크·후보마다 성립 여부와 확신도를 내고, 사람 정답 라벨 표본으로 확신도를 보정한 값을 믿음 정도로 둔다. 보정은 확신도 구간마다 표본 하한 20을 채운 뒤에 적용한다.
