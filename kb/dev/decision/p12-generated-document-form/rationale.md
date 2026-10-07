---
id: https://agentic-knowledge-base.dev/id/chunk/0341ff56-096f-494a-abca-f0b76153438d
type: decision
level: logical
title_ko: 서식이 생성기마다 갈리면 문서마다 읽는 법을 다시 익힌다
title: When form diverges per generator, each document must be learned anew
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-10-06T10:57:19+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T10:57:27+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6364f6e3-f553-4178-946c-36246fed08a9
---
**근거** — 2026-09-19 실측이 갈래를 셌다. 빈 값의 표기가 네 갈래, 시각 형식이 세 갈래, 머리 문구가 세 갈래, 절 제목 명명이 세 갈래였다. 같은 뜻을 네 가지로 적으면 읽는 쪽이 넷을 다 알아야 한다. 이것은 이 체계가 어휘에서 막는 드리프트와 같은 것이 문서 쪽에서 일어난 것이다.

규칙의 출처를 밖에서 가져오는 이유는 `STYLEGUIDE.md` §0의 "표준어가 우선이다"와 같다. markdownlint의 규칙 번호는 구현이 이미 있고 판정이 확정적이다. 지어낸 규칙은 근거를 스스로 대야 하고, 개정될 때 무엇을 다시 볼지 알 수 없다.

빈 값을 `없음`으로 통일하는 근거는 Microsoft Writing Style Guide다. 빈 셀과 대시는 "값이 없다"와 "해당하지 않는다"와 "아직 재지 않았다"를 구분하지 못한다. 생성 문서에서 그 셋의 구분은 판정의 일부다.

목차를 120줄에서 요구하는 근거는 ISO/IEC/IEEE 26514:2022가 온라인 정보에 목차·색인·검색 중 하나를 요구한다는 것이다. 2026-09-19 실측에서 목차를 가진 것은 7112줄인 `adr` 하나였고 999줄인 `index`, 639줄인 `workset`에는 없었다. 임계를 정하지 않으면 길이와 목차 유무가 무관해진다.
