---
id: https://agentic-knowledge-base.dev/id/chunk/2f8d8dd3-155f-41bc-a9d7-fd8deef5ce45
type: decision
level: concrete
title_ko: 추적성 정보 모델이 링크를 고정한다
title: A traceability information model fixes what links may exist
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0010-link-types.md, id: https://agentic-knowledge-base.dev/id/chunk-d0010, title_ko: "추적성 정보 모델과 링크 타입", title: "Traceability information model and link types"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0010]
part_of: https://agentic-knowledge-base.dev/id/composite/e9f394a2-e59b-41ea-be88-d8ed2c5f9c60
composite: {id: https://agentic-knowledge-base.dev/id/composite/e9f394a2-e59b-41ea-be88-d8ed2c5f9c60, title_ko: 추적성 정보 모델이 링크를 고정한다, title: A traceability information model fixes what links may exist}
---
**결론** — 링크가 무엇을 무엇에 어떻게 이을 수 있는지를 **추적성 정보 모델(traceability information model, TIM)** 로 고정한다. TIM은 셋을 정의한다 — **추적 대상 유형**(지식 종류 × 원자 단위), **링크 타입**(9.2절), **제약**(타입별 출발·도착 지식 종류 제한과 카디널리티).

**TIM은 온톨로지의 일부다.** `related/trace` 모듈에 링크 타입을 object property로, 지식 종류 제한을 정의역·치역 공리로 둔다. 따라서 2.5절 품질 검사가 TIM에도 적용되고, **검사 게이트가 TIM 위반 링크를 거부한다** — 정의역·치역 밖의 지식 종류, 카디널리티 초과, 단방향 규칙 위반.

**링크의 양 끝은 파일이 아니라 단위 지식 또는 복합체다** (Part IV).

**게이트** (노트 10.1절, analysis) — `defs/kb.bzl`의 규칙이 분석 시점 `fail()`로 판정하고 게이트 id는 `tim`이다(2026-09-11). `refines`는 상위 수준·지식 종류 단방향, `serves`는 요구만, `supersedes`는 같은 지식 종류, `verifies`는 V&V 주어와 같은 수준을 받는다. 끊긴 링크는 로드 에러이고 방향은 `package_group` 가시성이 막는다. 기계화는 부분이다. 해소는 저작자가 링크의 방향과 수준을 고치는 것이고, 규칙 변경은 유저 승인 사항이다.
