---
id: https://agentic-knowledge-base.dev/id/chunk/9b7251c8-6991-5c90-916f-b6faec9cdb72
type: decision
level: logical
title_ko: 논리 시나리오 배제 자극 — 결론 본문 한 문장만 바꾼 결정 스냅숏 쌍의 재판정에서 다루지 않는 것
title: Logical scenario excluded stimuli — what revalidating a decision snapshot pair that differs in one sentence of the conclusion body does not cover
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:16:12+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/92837b35-799b-52bf-993e-07d95d83e4ae
---
**배제 자극** — 다루지 않는 자극은 둘이다.

- 저장소 리비전 사이의 실제 편집은 다루지 않는다. 기본 꼴은 git·`bazel query` 를 불러 `vv_run` 이 실행하지 않는다.
- 라벨만 바뀐 결론은 다루지 않는다. 라벨 부패는 세션 판정자 질문 `agt:labelRepresentsBody` 의 자리다.
