---
id: https://agentic-knowledge-base.dev/id/chunk/90637802-c79a-43f1-8665-8c50f3b6fd9f
type: decision
level: concrete
title_ko: 실패 요인은 인지·상호작용·실행 셋이고 그 조합이 위험 케이스다
title: Three failure factors - cognition, interaction, execution - and their combinations
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0140]
part_of: https://agentic-knowledge-base.dev/id/composite/941cae39-2d59-468c-bd54-9d71cf8982ba
composite: {id: https://agentic-knowledge-base.dev/id/composite/941cae39-2d59-468c-bd54-9d71cf8982ba, title_ko: 결함의 구성, title: How defects are composed}
---
**결론** — 실패 요인을 세 갈래로 분류한다. 에이전트 작업의 세 단계에 대응한다.

- **인지 요인** — 입력을 잘못 읽음 (잘못된 테스트 결과를 근거로 삼음, 오래된 문서 기반 추측)
- **상호작용 요인** — 다른 행위자와의 조율 실패 (통신 로직 충돌, 동시 편집 충돌)
- **실행 요인** — 판단은 옳았으나 수행 실패 (잘못된 명령어, 환경 불일치)

**위험 케이스 = 요인을 하나 이상 포함하는 케이스.** 세 갈래의 요인을 **조합하여 위에서 아래로** 체계적으로 구성하며, 그 조합이 logical 공간의 표본 추출 근거가 된다. `defect` 어휘가 요인을, `defect-rules`가 조합 규칙을 담는다.
