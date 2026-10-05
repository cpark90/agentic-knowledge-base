---
id: https://agentic-knowledge-base.dev/id/chunk/69ed3440-e06b-48e2-968f-ad4461332258
type: norm
level: logical
title_ko: docs/method.md 절 — 정제 전이는 새 청크와 refines다
title: docs/method.md section — a refinement transition is a new chunk plus refines
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/005b8875-a251-4864-a47e-7f261fffe156
heading: 정제 전이
depth: 2
---
level은 `functional → abstract → logical → concrete → executable` 순이다. 각 정제는 **근거와
`refines` 링크를 남기고** 전이 게이트를 통과해야 한다. 전이 게이트는 어휘 검사, 후보가 비어
있지 않음, 배제 근거 존재, 판정 도구 통과다. 게이트 없이 만든 하위 청크는 고아율에 잡힌다
([`id:chunk-d0005`](../../../../chunks/decision/d-0005-abstraction-ladder.md)).

level을 바꾸지 않는다. 전이는 기존 청크의 level 갱신이 아니라 **새 청크 + `refines`**다
(d-0071). 단계를 건너뛰면 의도와 결과만 남고 그 사이가 빈다.
