---
id: https://agentic-knowledge-base.dev/id/chunk/f6bfebac-476b-436a-b265-8b5940dbbdff
type: decision
level: logical
title_ko: 단위 지식 속성으로서의 재현성과 억지 테스트 케이스화의 기각
former_title_ko: ["청크 속성으로서의 재현성과 억지 케이스화의 기각", "지식 항목 속성으로서의 재현성과 억지 테스트 케이스화의 기각"]
title: Rejecting reproducibility as a chunk attribute and forced concretisation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c71e12a1-2a31-43f5-af40-c670d767f559
---
**대안** — 재현성을 검증 단위 지식의 속성으로 두는 안. 기각 — 재현성은 환경 할당의 조건이며 재현 안 되는 검증은 5~6단계로 강등된다 (8.12절).

**대안** — 재현 불가한 관측을 억지로 concrete 테스트 케이스로 만드는 안. 기각 — 재현되지 않는 테스트 케이스는 커버리지를 부풀린다. `origin:observed`로 6단계 관측에 남긴다 (8.12절).
