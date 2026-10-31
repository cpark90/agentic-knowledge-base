---
id: https://agentic-knowledge-base.dev/id/chunk/d6abc9e6-c3ab-4417-b387-fcaa33c5a76f
type: decision
level: concrete
title_ko: 조용한 대체는 고정했다고 믿는 명세를 만들고 산출 전에 거부해야 반쪽 산출이 없다
title: Silent fallback creates a specification believed to be pinned, and rejecting before output leaves no partial output
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0177-closed-policy-vocabulary.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:54:08+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:54:08+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/89fef3f3-3d51-4599-8978-a4308453ba39
---
**근거** — 출처는 harness-concrete `docs/odr-bind-lock.md`의 "The policy set is CLOSED" 절이다.

- 조용한 대체는 **고정했다고 믿는 명세**를 만든다. 오타 하나가 지정한 전략 대신 기본 전략을 실행시키고 산출물은 정상으로 보인다. 그래서 명세와 실제 거동의 차이가 어느 게이트에도 걸리지 않고 자란다.
- 실패 시점은 **산출 이전**이다. 설정 해석 단계에서 거부하면 파일이 하나도 쓰이지 않으므로 잘못된 설정이 반쪽 산출을 남기지 않는다.
- 체계가 답을 모르는 상황에서 그럴듯한 답을 지어내지 않는다는 점에서, 이 규칙은 모순을 자동으로 풀지 않고 사람에게 넘기는 규칙(`p9-contradiction-handling`)과 같은 결이다.
