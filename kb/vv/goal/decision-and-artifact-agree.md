---
id: https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a
type: requirement
level: functional
pattern: event-driven
title_ko: 결정 본문이 바뀌면 그것을 충족한다고 적힌 산출물이 재판정 대상이 되어야 한다
title: When a decision body changes, the artefact claimed to satisfy it must become a re-judgement target
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
exposes: [https://agentic-knowledge-base.dev/agt/reasoningActionMismatch, https://agentic-knowledge-base.dev/agt/labelRot]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:20:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
---
**검증 목표** — 결정의 결론 본문과 그 결론을 충족한다고 적힌 산출물이 어긋난 상태가 기록으로 드러난다는 것이 보여져야 한다. 이 목표가 다루는 위험은 현상 `agt:reasoningActionMismatch`(P16)이고 같은 자리의 항목 안 어긋남은 `agt:labelRot`(P14)이다.

- **이해관계자**: 검증자 · **관심사**: 결정과 산출물의 일치

**무엇을 관측하면 성립하는가**

- 결정 결론의 `agt:contentHash`가 바뀌면 그 결론을 가리키는 `satisfies` 링크가 `suspect`로 유도되고, 유도되지 않으면 그 자리가 공백이다.
- 산출물이 결정과 다른 것을 하는 경우가 `satisfies` 증거 기록의 극성 (−) 항목으로 남는다.
- 본문을 고친 뒤 라벨이 여전히 대표하는지의 재검토가 수행됐다는 기록이 판정 주석으로 남는다.
- 이 목표는 기존 검증 목표 35건과 달리 위험 분석 G1의 현상에서 파생됐다. 35건은 분석 시점·그래프 게이트의 성립을 재고 이 목표는 게이트가 재지 않는 어긋남을 겨눈다.

미확정: 결정 본문과 산출물의 어긋남을 재는 관측 수단이 없다 — 개발 KB의 `artifact`가 3건이라 표면이 아직 작다.
