---
id: https://agentic-knowledge-base.dev/id/chunk/a40ae293-0c0f-42f5-8dbb-abbb49b49ad3
type: norm
level: logical
title_ko: docs/method.md 절 순서의 이어짐 — 단계를 건너뛰지 않고 정제와 검증은 두 KB에 쌓인다
title: docs/method.md order section continued — steps are not skipped and refinement and verification accrue in two KBs
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/61ca9d74-d16e-46ad-8e75-46954e9f27f0
continues: true
---
**단계를 건너뛰지 않는다.** functional에서 곧바로 executable로 가는 것이 현재 에이전트의
기본 동작이다. 그것이 정제 계층 단절의 원인이다 (노트 6.1절).

**정제의 산출은 개발 KB(`kb/dev/`)에, 검증 지식은 V&V KB(`kb/vv/`)에 쌓인다.** 정제와
나란히 vnv 역할이 검증 목표·시나리오·판정 기준을 저작하고 `verifies`로 개발 KB를
가리킨다. 저작·판정 분리가 KB 수준에서도 성립한다 (노트 Part VII).
