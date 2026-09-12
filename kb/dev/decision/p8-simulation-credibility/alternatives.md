---
id: https://agentic-knowledge-base.dev/id/chunk/424cb1a6-90fe-4285-823f-5f8e699bc538
type: decision
level: logical
title_ko: 실환경 관측으로 시뮬레이션을 보정하는 것은 뒤로 미룬다
title: Calibrating the simulation from field observation is deferred
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/962ef704-4544-41b5-8b6d-bea52f11c595
---
**대안** `[안]` — 실환경 관측으로부터 시뮬레이션을 보정하는 것(노트 8.13절)은 **4~6단계 관측이 충분히 쌓인 뒤의 과제**다. 관측이 적은 동안 보정하면 편향된 표본을 시뮬레이션이 그대로 학습한다.

그 전에는 **mock을 `schema` 청크에서 직접 생성한다** — 계약에서 생성된 mock은 적어도 계약 위반은 하지 않으므로 신뢰도의 하한이 보장된다.
