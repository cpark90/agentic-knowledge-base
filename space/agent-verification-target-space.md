---
id: https://agentic-knowledge-base.dev/id/chunk/5494b7c3-09b0-4566-bd1d-b660fd9ae058
type: agt:Space
level: logical
title_ko: 에이전트 검증의 verifies 도착점이 무엇인가
title: What the verifies link of agent verification points at
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T21:10:00+09:00}
---
요구 `r-025`는 제품과 에이전트 둘 다 검증하라고 정하는데, 에이전트 쪽 사슬이 0이다. 막는 것은 도착점의 불일치다 — 결정 `p8-two-verification-targets`는 에이전트 검증이 하네스·스코프 개체를 검증한다고 적고, `defs/kb.bzl`의 링크 규칙은 `verifies`의 대상을 개발 KB 청크로 한정한다. 둘 중 하나가 바뀌어야 후보가 생긴다.

후보를 아직 열거하지 않는다. 셋 중 어느 쪽도 청크로 존재하지 않고, 근거 없이 하나를 적으면 그것이 `r-011`이 막는 할당이다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193
  kind: refines
status: open
```
