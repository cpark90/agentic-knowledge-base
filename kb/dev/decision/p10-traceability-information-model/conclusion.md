---
id: https://agentic-knowledge-base.dev/id/chunk/2f8d8dd3-155f-41bc-a9d7-fd8deef5ce45
type: decision
level: concrete
title_ko: 추적성 정보 모델이 링크를 고정한다
title: A traceability information model fixes what links may exist
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0010]
part_of: https://agentic-knowledge-base.dev/id/composite/e9f394a2-e59b-41ea-be88-d8ed2c5f9c60
composite: {id: https://agentic-knowledge-base.dev/id/composite/e9f394a2-e59b-41ea-be88-d8ed2c5f9c60, title_ko: 추적성 정보 모델이 링크를 고정한다, title: A traceability information model fixes what links may exist}
---
**결론** — 링크가 무엇을 무엇에 어떻게 이을 수 있는지를 **추적성 정보 모델(traceability information model, TIM)** 로 고정한다. TIM은 셋을 정의한다 — **추적 대상 유형**(plane × 원자 단위), **링크 타입**(9.2절), **제약**(타입별 출발·도착 plane 제한과 카디널리티).

**TIM은 온톨로지의 일부다.** `related/trace` 모듈에 링크 타입을 object property로, plane 제한을 정의역·치역 공리로 둔다. 따라서 2.5절 품질 검사가 TIM에도 적용되고, **검사 게이트가 TIM 위반 링크를 거부한다** — 정의역·치역 밖의 plane, 카디널리티 초과, 단방향 규칙 위반.

**링크의 양 끝은 파일이 아니라 청크 또는 복합체다** (Part IV).
