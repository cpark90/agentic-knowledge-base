---
id: https://agentic-knowledge-base.dev/id/chunk/5aed4ec9-28da-4515-9967-a23a1753d366
type: decision
level: concrete
title_ko: 실행 기록은 두 검증 대상의 관측을 함께 담고 사후분석의 요인 분류가 둘을 가른다
title: Run records hold observations of both verification targets and postmortem factor classification separates them
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193, https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e182245c-43fd-46de-819d-cb809a20aa8e
composite: {id: https://agentic-knowledge-base.dev/id/composite/e182245c-43fd-46de-819d-cb809a20aa8e, title_ko: 두 검증 대상의 실행 기록, title: Run records for both verification targets}
---
**결론** — 실행 기록(`agt:Run`)은 제품과 에이전트 두 검증 대상의 관측을 함께 담는다(노트 8.8절 `[확정]`). 기록 단계에서 대상을 나누지 않는다.

결함이 제품의 것인지 에이전트의 것인지는 사후분석(노트 12.12절)에서 **요인 분류**로 갈린다.

| 요인 | 대체로 귀속되는 대상 |
|---|---|
| 실행 요인 | 제품 |
| 인지 요인 | 에이전트 |

요인 세 갈래는 `p8-defect-factor-taxonomy`가 정하고, 사후분석의 단계는 `p12-incident-postmortem`이 정한다. 두 검증 대상의 구분과 `verifies` 도착점은 `p8-agent-verification-target`이 정한다. 이 결정은 그 결정이 옮기지 않은 노트 8.8절의 셋째 `[확정]` 문장을 결정으로 세운다.
