---
id: https://agentic-knowledge-base.dev/id/chunk/f1c5a605-771b-4cc4-adbe-1dd237407427
type: decision
level: concrete
title_ko: 설정 어휘는 닫힌 집합이고 미인식 값은 기본값으로 떨어지지 않고 실패한다
title: The configuration vocabulary is a closed set, and unrecognised values fail instead of falling back to defaults
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0177-closed-policy-vocabulary.md, id: https://agentic-knowledge-base.dev/id/chunk-d0177, title_ko: "설정 어휘는 닫힌 집합이고 미인식 값은 기본값으로 떨어지지 않고 실패한다", title: "Configuration vocabulary is a closed set; unknown values fail instead of defaulting"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0177]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/89fef3f3-3d51-4599-8978-a4308453ba39
composite: {id: https://agentic-knowledge-base.dev/id/composite/89fef3f3-3d51-4599-8978-a4308453ba39, title_ko: 닫힌 정책 어휘, title: Closed policy vocabulary}
---
**결론** — 선택 정책처럼 거동을 바꾸는 설정 어휘는 **닫힌 집합**으로 정의하고, 집합 밖의 값은 조용히 기본값으로 떨어뜨리지 않고 **즉시 실패**시킨다. 실패 메시지는 대상과 잘못된 값, 허용 집합을 함께 말한다. 조건에 맞는 후보가 하나도 없는 고정(pin)도 같은 실패다.
