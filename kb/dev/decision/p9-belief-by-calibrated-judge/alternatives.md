---
id: https://agentic-knowledge-base.dev/id/chunk/0643cbf2-e3aa-4933-8b74-bb24c85d0703
type: decision
level: logical
title_ko: 판정자 보정 후보 곁의 두 후보
title: The two candidates beside the calibrated-judge candidate
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T02:22:01+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f383d72c-472a-4807-984a-76b137bc5e1d
---
**대안** — 같은 공간의 다른 후보는 둘이다. 후보 `p9-belief-by-evidence-kind-rank`의 증거 종류 서열 가중 점수와 후보 `p9-belief-by-beta-binomial`의 베타-이항 사후는 증거 기록에서 값을 낸다. 이 후보만 증거 기록 밖의 판정자 출력을 원천으로 쓴다.

**충돌** — 이 후보는 확정된 결정 하나와 어긋난다. `p8-judge-session-agreement`의 규칙 ②는 확신도가 자기 보고라 캘리브레이션을 재지 않는다고 정했으나, 이 후보는 그 확신도를 사람 정답 라벨로 보정한다. 그래서 이 후보가 확정되면 ②는 "확신도는 사람 정답 라벨 표본이 구간마다 하한을 채운 뒤에만 보정해 믿음 정도로 쓰고, 그 전에는 판정 불가로 적는다"로 바뀌어야 한다.
