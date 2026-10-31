---
id: https://agentic-knowledge-base.dev/id/chunk/2dc8dfc7-565d-48c6-9f76-6b81afcd6eea
type: decision
level: logical
title_ko: 믿음 정도는 종류별 사전 분포에 지지와 반박 수를 더한 베타 사후의 평균이다
title: Degree of belief is the mean of a beta posterior adding support and refutation counts to a per-kind prior
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-22T20:51:33+09:00}
layer: methodology
composite: {id: https://agentic-knowledge-base.dev/id/composite/6287d29d-adee-457f-9deb-1a37dab89ca6, title_ko: 극성 계수의 베타-이항 사후, title: Beta-binomial posterior over polarity counts}
part_of: https://agentic-knowledge-base.dev/id/composite/6287d29d-adee-457f-9deb-1a37dab89ca6
---
**결론** — 링크·후보마다 베타 분포의 사전을 증거 종류별로 두고, 지지(+)와 반박(−) 항목 수를 더한 사후의 평균을 믿음 정도로 둔다. 사후 분산을 함께 내어 표본이 적은 링크를 드러낸다.
