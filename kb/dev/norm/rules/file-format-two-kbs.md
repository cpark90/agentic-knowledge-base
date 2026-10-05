---
id: https://agentic-knowledge-base.dev/id/chunk/06219313-af40-4d3e-8e91-0884c0451629
type: norm
level: logical
title_ko: docs/rules.md 절 파일 형식의 이어짐 — 두 KB와 네 그래프의 논리적 구분
title: docs/rules.md file-format section continued — the two KBs and the logical split into four graphs
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
continues: true
---
**지식은 두 KB로 갈려 산다.** 개발 KB `kb/dev/`는 요구·결정·계약·스키마·구현을 담고, V&V KB
`kb/vv/`는 검증 목표·시나리오·판정 기준을 담는다. 두 KB를 잇는 링크는 `verifies` 하나뿐이고 주어는
항상 V&V 쪽이며, `kb/vv/`의 편집 주체는 vnv 역할뿐이다 (노트 Part VII, 유저 결정 저장 분리).
`chunks/`는 v1 유래 결정의 잔류 위치로, 재도출로 대체된 것은 `deprecated`가 된다.

**네 그래프는 현재 논리적 구분이다.** 저장 형식이 Turtle이라 물리적으로는 기본 그래프
하나다. TriG 전환은 `annotation`이 생겨 "어느 그래프에 대한 주석인가"를 말해야 할 때
재검토한다.
