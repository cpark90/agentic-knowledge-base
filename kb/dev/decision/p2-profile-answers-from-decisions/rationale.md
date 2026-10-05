---
id: https://agentic-knowledge-base.dev/id/chunk/2c636f49-f6ce-4121-9b95-e4ce6e1ceaf7
type: decision
level: logical
title_ko: 노트는 프로파일을 결정의 모음으로 정의하고 첫 프로파일의 절차가 그 순서를 적었다
title: The notes define a profile as a collection of decisions, and the first profile's procedure recorded the order
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:22:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2b47645a-4247-4eb8-a741-7a7a41d206cf
---
**근거** — 노트 2.11절(`[확정]`)은 "부록 D에 개발 프로파일의 결정을 모아 둔다. 다른 프로파일을 만들 때 부록 D가 템플릿이다"라고 적는다. 부록 D의 표는 코어 항목마다 "개발 프로파일의 결정"과 그 결정의 노트 위치를 짝짓는다. 프로파일의 내용은 확장점마다 내린 결정이고, 모듈은 그 결정을 어휘로 옮긴 것이다. 그러므로 확장점의 답을 읽는 자리가 결정이다.

이 순서는 첫 프로파일(`development`, 2026-09-18)을 만들면서 뽑은 절차로 `docs/method.md` §1에 손으로 쓰였다. 절차의 둘째 항목이 "확장점마다 답을 결정에서 읽는다. 결정이 없으면 먼저 결정을 만든다(유저 승인)"였고, 개발 프로파일의 원천으로 `p7-dev-plane-substance`와 `pe-anchor-is-bazel-label`을 들었다. `docs/method.md`가 생성 문서가 되면서 이 문장의 원본 결정이 없어 이 결정이 그 자리를 잇는다.

유저 승인은 `decision` plane의 판정 방식에서 온다. `p7-dev-plane-substance`의 표는 `decision`의 판정을 "논증 구조 검사 + 유저 승인"으로 적는다. 확장점의 답을 새로 정하는 것은 결정을 새로 내는 것이므로 같은 판정을 받는다.

미확정: 결정을 모듈 작성보다 **먼저** 두는 이유를 손 문서와 노트는 따로 적지 않았다. 위 근거는 프로파일이 결정의 모음이라는 노트의 정의에서 순서를 읽은 것이다.
