---
id: https://agentic-knowledge-base.dev/id/chunk/90552b15-2600-4517-a0e8-87ac5f3e196a
type: decision
level: logical
title_ko: 그대로 두거나 종료 코드를 버리거나 자극을 공유하는 안은 기각된다
title: Leaving it as is, dropping the exit code, and sharing one stimulus are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T13:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6eea0a91-2e8d-400c-a830-ea653fa104f0
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 그대로 두고 `contains` 문구에 맡긴다 | 문구는 게이트 메시지라 개선되며 바뀐다. 바뀔 때 자극이 무엇을 어기는지 종료 코드가 받쳐 주지 않으면 고치는 사람이 새 문구를 무엇에 맞출지 모른다 |
| 종료 코드를 판정에서 뺀다 | 문구만 보면 출력 어딘가에 그 문구가 있기만 하면 통과다. 검증기가 죽어도 로그에 문구가 남으면 통과가 된다 |
| 자극 하나로 여러 규칙을 함께 검사한다 | 표본 근거가 둘을 말해야 하고 그것은 케이스가 둘이라는 뜻이다. 어느 규칙이 깨졌는지도 구분되지 않는다 |
| 최소성을 게이트로 강제한다 | 자극을 하나씩 빼 보는 실험이라 기계가 할 수 없다. 표본 근거의 주장으로 남기고 사람이 재검사한다 |
