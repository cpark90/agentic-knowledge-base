---
id: https://agentic-knowledge-base.dev/id/chunk/dedc8e99-5853-4e24-9d64-adb22f0c0da4
type: decision
level: concrete
title_ko: 평가는 체계가 이미 산출하는 세 값으로 측정한다
title: Evaluation measures three values the system already produces
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0145]
part_of: https://agentic-knowledge-base.dev/id/composite/a4a5acea-aaed-4439-ac17-164495f5927c
composite: {id: https://agentic-knowledge-base.dev/id/composite/a4a5acea-aaed-4439-ac17-164495f5927c, title_ko: 평가의 세 측정 단위, title: Three units of evaluation measurement}
---
**결론** — 평가의 측정을 셋으로 둔다. 셋 다 체계가 이미 가진 구조에서
읽어내며 별도 계측을 붙이지 않는다.

- **인지능력** — 입력 정보 누락률. 입력은 `agt:Workset`이다
- **추적 커버리지** — 링크 없는 항목 비율. 9.7절 추적 매트릭스의 빈 칸
- **가정 건전성** — `invalidated`·`unverified` 비율. 6.5절 상태 집계
