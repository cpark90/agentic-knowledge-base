---
id: https://agentic-knowledge-base.dev/id/chunk/04194c8d-79e2-4a55-b424-6a121c26d7b6
type: decision
level: concrete
title_ko: 열린 어휘와 미인식 값 무시는 택하지 않는다
title: An open vocabulary that ignores unrecognised values is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0177-closed-policy-vocabulary.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:54:08+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:54:08+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/89fef3f3-3d51-4599-8978-a4308453ba39
---
**대안** — 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 열린 어휘를 두고 미인식 값을 무시한다 | 확장성을 얻는 대신 오설정과 미지원 전략을 구별할 수 없게 되고, 둘 다 기본값으로 수렴한다 |
