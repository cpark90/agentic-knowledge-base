---
id: https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c
type: requirement
level: functional
pattern: state-driven
title_ko: 근거 없는 할당은 불가능해야 한다
title: Groundless assignment must be impossible
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-22T20:51:41+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:11:22+09:00}]
part_of: https://agentic-knowledge-base.dev/id/comp-req-project
---
**요구** — 후보가 여럿 남아 있는 동안, 체계는 근거 없이 하나를 할당하는 것을 자료구조 수준에서 불가능하게 하여야 한다. 할당의 근거는 증거 기록이다. 증거에서 계산한 믿음 정도는 후보 곁에 병기할 수 있으나 그것만으로 할당의 근거가 되지 않는다.

- **이해관계자**: 프로젝트 · **관심사**: 미확정의 보존
- **출처**: 노트 1.2절·Part IX. 2026-10-22 개정 — 믿음 정도 병기(유저 답 Q87-b · Q90-a)

'추측하지 마라'는 지시는 성립하지 않는다 — 후보가 여럿인 상태를 정상으로 두는 구조만이 막는다.
