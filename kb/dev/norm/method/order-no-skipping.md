---
id: https://agentic-knowledge-base.dev/id/chunk/a40ae293-0c0f-42f5-8dbb-abbb49b49ad3
type: norm
level: logical
title_ko: docs/method.md 절 순서의 이어짐 — 단계를 건너뛰지 않고 정제와 검증은 두 KB에 쌓인다
title: docs/method.md order section continued — steps are not skipped and refinement and verification accrue in two KBs
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:08+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/61ca9d74-d16e-46ad-8e75-46954e9f27f0
continues: true
---
**단계를 건너뛰지 않는다.** 현재 에이전트는 기본 동작으로 기능 수준(functional)에서 곧바로
실행 수준(executable)으로 가고, 그 건너뜀이 정제 계층 단절의 원인이다 (노트 6.1절).

**정제의 산출은 `kb/dev/`의 개발 KB에, 검증 지식은 `kb/vv/`의 V&V KB에 쌓인다.** vnv 역할은 정제와
나란히 검증 목표와 시나리오, 판정 기준을 저작하고 `verifies`로 개발 KB를 가리킨다. 따라서 저작과 판정의
분리가 KB 차원에서도 성립한다 (노트 Part VII).
