---
id: https://agentic-knowledge-base.dev/id/chunk/a50d8354-feca-4ed8-9ea2-e230b680cbcb
type: norm
level: logical
title_ko: docs/rules.md 절 — 가정과 기본 가정 후 좁힘
title: docs/rules.md section — Assumptions and narrowing after the default assumption
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/954d3726-b41f-4726-ad15-f08f92b66d6c
heading: 가정
depth: 3
---
모든 chunk는 ODD 조건 위의 가정 위에 선다. **ODD에 없는 조건을 참조하는 파생물은 게이트가
거부한다.** 대응은 ODD 확장 또는 파생물 기각뿐이다. 가정이 깨지면 그 가정에 의존하는
항목이 자동으로 무효화 표시되므로 전수조사가 필요 없다 ([p6-assumption-invalidation](../../decision/p6-assumption-invalidation/conclusion.md) · [p0-odd-scope-assumption](../../decision/p0-odd-scope-assumption/conclusion.md) · [p6-assumption-verification-methods](../../decision/p6-assumption-verification-methods/conclusion.md)).

**기본 가정 후 좁힘**(2026-09-12)이 규칙이다. 항목 고유의 전제를 아직 적지 않은 청크는 기본 가정
`id:asm-chunk-conventions`를 `assumes`한다. 이 기본 가정은 저장소 구조 + 언어 정책 조건이다. 이것은
자리표시이며, 항목의 실제 전제가 드러나면 그 고유 가정을 **앞에 더한다**. 예를 들어 Bazel 하네스에 기대는
결정의 고유 전제는 `asm-bazel-toolchain`이다. 기본 가정은 항목이 청크 규약에도 기대는 한 남는다. 좁힘의 진행은
고유 가정을 가진 청크 수로 잰다 — `metrics`의 가정 절(2026-09-14 정정).
