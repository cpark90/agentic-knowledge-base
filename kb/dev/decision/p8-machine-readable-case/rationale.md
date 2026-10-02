---
id: https://agentic-knowledge-base.dev/id/chunk/d625e077-8f31-4358-97ed-d61b3e0ed25c
type: decision
level: logical
title_ko: 자극이 산문에만 있으면 검증기가 음성 절반을 실행하지 못한다
title: A stimulus that lives only in prose leaves the verifier unable to run the negative half
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T10:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e2064625-339c-4cef-8f06-5e775874f177
---
**근거** — 2026-09-22 실측이 비용을 보인다. 케이스 28 중 둘(`chunk-42-lines`·`foreign-vocabulary-rejected`)의 음성 명령이 `임시 파일 자극 — 프로즈에 구조만 있어 자동 생성 불가`로 건너뛰어졌고, 그래서 두 케이스의 판정이 `skip`이다. 판정 주석 `skipped-negative-stimuli`가 그것을 `issue (non-blocking)`으로 적었다.

게이트의 값은 무엇을 통과시키는가가 아니라 무엇을 거부하는가에 있다. 양성 명령만 도는 케이스는 그 절반을 보이지 못한다. 자극이 사람이 읽는 산문에만 있으면 검증기가 그 절반을 영원히 실행할 수 없다.

기대 문구를 대조하는 근거는 판정 주석 `exit-code-only-judgement`가 적은 것과 같다. 종료 코드 1은 "실패했다"만 뜻하고, 기대한 사유로 실패했는지는 말하지 않는다. 다른 이유로 실패한 검증기는 통과한 것처럼 보이지 않지만 **틀린 것을 검증한다.** 이것이 `verification-means-trust`가 재려는 검증 수단 자체의 신뢰다.

펜스를 산문 옆에 두고 산문을 지우지 않는 근거는 두 독자가 다르다는 것이다. 다음 세션의 에이전트는 라벨과 산문으로 케이스를 고르고 검증기는 펜스로 실행한다. 펜스만 남기면 사람이 표본 근거를 읽을 수 없고, 산문만 남기면 지금 상태다.

점진 도입의 근거는 비용이다. 케이스 28을 한 번에 옮기면 그 편집이 전부 `contentHash`를 바꾸고 재판정 대상이 된다. 건너뛰는 케이스는 둘이므로 거기서 값이 가장 크다.
