---
id: https://agentic-knowledge-base.dev/id/chunk/e961f335-1010-4425-a957-f31f46615ac7
type: decision
level: concrete
title_ko: 검사 게이트는 A-Box를 SHACL로 검사한다
title: The inspection gate validates the A-Box with SHACL
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0086]
part_of: https://agentic-knowledge-base.dev/id/composite/194f050d-929c-4c2c-a42e-887beed7b690
composite: {id: https://agentic-knowledge-base.dev/id/composite/194f050d-929c-4c2c-a42e-887beed7b690, title_ko: 검사 게이트, title: The inspection gate}
---
**결론** — 에이전트가 A-Box와 설계 공간을 채우게 하려면 기계적 검사가 필수다. **SHACL 제약**으로 카디널리티·타입 일관성·필수 필드를 검사한다.

걸러야 할 무효 출력은 셋이다 — **중간 산출물 반환 / 형식 오류 / 형식 이탈(자유형 텍스트).**

모델에 따라 구조화 출력 강제를 위한 별도 전략이 필요하며, **모델 교체 시 통과율을 먼저 측정한다.** 2.5절 온톨로지 위생과 이 게이트는 대상이 다르다 — 위생은 T-Box, 게이트는 A-Box다.
