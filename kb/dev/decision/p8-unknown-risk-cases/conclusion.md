---
id: https://agentic-knowledge-base.dev/id/chunk/467199b6-287f-4e76-8832-6f13e753d943
type: decision
level: concrete
title_ko: 알려지지 않은 위험 케이스는 어휘 문제와 커버리지 문제로 갈린다
title: Unknown risk cases split into a vocabulary problem and a coverage problem
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0143]
part_of: https://agentic-knowledge-base.dev/id/composite/afadcad8-6d9b-4e7d-aac5-cdc0c6ffe89c
composite: {id: https://agentic-knowledge-base.dev/id/composite/afadcad8-6d9b-4e7d-aac5-cdc0c6ffe89c, title_ko: 알려지지 않은 위험 케이스, title: Unknown risk cases}
---
**결론** — 알려지지 않은 위험 케이스는 둘 중 하나에서 온다.

- **알려지지 않은 요인** — `defect` 어휘에 없는 요인. 대응은 6.3절 **일반화** — 실행 기록에서 새 요인을 추출해 어휘에 추가한다
- **알려진 요인의 알려지지 않은 조합** — 조합이 concrete 케이스에 없음. 대응은 **조합 테스팅** — logical 공간을 체계적으로 표본 추출한다

첫째는 **어휘 문제**이고 둘째는 **커버리지 문제**다.
