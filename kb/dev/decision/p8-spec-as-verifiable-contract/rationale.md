---
id: https://agentic-knowledge-base.dev/id/chunk/dcbd854a-5c12-4131-8693-f7631ad0f8cb
type: decision
level: concrete
title_ko: 구조 검증의 통과는 산출물에 대해 아무것도 말하지 않는다
title: Passing structural validation says nothing about the outputs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0182-spec-as-verifiable-contract.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:08:10+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:08:10+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/bff15384-be48-4304-95be-bcc0f46ef542
---
**근거** — 출처는 harness-concrete `docs/odr-contract-verify.md`다.

- 구조 검증의 통과는 산출물에 대해 **아무것도 말하지 않는다.** 잘 형성된 그래프가 아무것도 만들지 못하거나 틀린 것을 만들 수 있다. 그래서 세 번째 방향이 없으면 명세는 끝까지 검증되지 않은 주장으로 남는다.
- 명세를 계약으로 쓰면 판정 근거가 산출물이 아니라 명세에 있다. 그래서 산출물을 다시 만들 때마다 기준을 다시 쓰지 않아도 되고, 기준의 변경 이력이 산출물의 변경 이력과 섞이지 않는다.
- 생성의 입력과 검증의 기준을 **하나의 문서**로 두는 것이 핵심이다. 둘을 따로 쓰면 그 둘 사이가 새로운 드리프트 면이 되기 때문이다.
