---
id: https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee
type: contract
level: abstract
title_ko: 결정 결론의 내용 해시가 바뀌면 그것을 충족하는 링크가 재판정 대상이 된다
title: When the content hash of a decision conclusion changes, the links that satisfy it become re-judgement targets
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/9e1150bc-5668-4f5d-aa95-684f45b7bf4a]
---
**합격 기준** — 기준 종류는 불변식이다. 결정 결론 `d`의 `agt:contentHash`가 리비전 사이에 바뀌었으면 `d`를 대상으로 하는 확정 링크 전부가 `suspect`로 유도되거나 재판정 기록을 갖는 것이 합격이다.

**확인 절차**

- 두 리비전의 `bazel build //kg:chunks_kg` 산출에서 같은 IRI의 `agt:contentHash`를 비교해 바뀐 결론을 고른다.
- 그 결론을 대상으로 하는 링크를 `agt:linkTo` 로 찾아 `suspect` 유도 또는 재판정 주석의 존재를 본다. 둘 다 없으면 불합격이다.
- 라벨이 여전히 본문을 대표하는지의 재검토 기록이 있는지 함께 본다. 기록이 없으면 `agt:labelRot`(P14)의 자리다.

**등급** — C다. 재판정 기록의 존재 판정이 사람 판단이고 `suspect` 상태의 자동 전파 규칙이 아직 없다.

미확정: `suspect` 전파의 트리거가 `supersedes` 하나뿐이라 내용 해시 변경은 트리거에 들어 있지 않다.
