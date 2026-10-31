---
id: https://agentic-knowledge-base.dev/id/chunk/405d77a3-d480-42cd-a81c-5bb548b673db
type: decision
level: concrete
title_ko: 원천이 없는 것은 지어내지 않는다
title: What the source lacks is not invented
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0020-source-gated-axes.md, id: https://agentic-knowledge-base.dev/id/chunk-d0020, title_ko: "원천이 없는 것은 지어내지 않는다", title: "Source-gated axes - never fabricate fixtures"}, {resource: git:aeb0a58:chunks/decision/d-0186-recipe-standard-alternatives.md, id: https://agentic-knowledge-base.dev/id/chunk-d0186, title_ko: "대안 — 레시피 표준", title: "Alternatives — recipe standard"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0020, https://agentic-knowledge-base.dev/id/chunk-d0186]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/de0d3031-0a4f-4bcf-bc8f-fedfbb99b3aa
composite: {id: https://agentic-knowledge-base.dev/id/composite/de0d3031-0a4f-4bcf-bc8f-fedfbb99b3aa, title_ko: 원천이 뒷받침하는 축만 필수, title: Axes required only when the source supports them}
---
**결론** — 실행 거동 축은 **원천이 뒷받침할 때만 필수**다(source-gated). 그 축은 실행 모드와 테스트 시나리오, 실패 정책이다. 원천이 정말로 그 축을 갖지 않으면 픽스처를 발명하지 않고 **명시적 수용 사유**를 기록한 뒤 그 축을 생략한다. 이것은 결손이 아니라 정당한 감사 결과다.
