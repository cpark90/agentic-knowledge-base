---
id: https://agentic-knowledge-base.dev/id/chunk/5494b7c3-09b0-4566-bd1d-b660fd9ae058
type: agt:Space
level: logical
title_ko: 에이전트 검증의 verifies 도착점이 무엇인가
title: What the verifies link of agent verification points at
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-10-04T14:34:02+09:00}
---
요구 `r-025`는 제품과 에이전트 둘 다 검증하라고 정한다. 옛 결정 `p8-two-verification-targets`의 도착점(하네스·스코프 개체)과 `defs/kb.bzl`의 링크 규칙(개발 KB 청크)이 어긋난 것이 변수였고 유저 답(2026-09-24)으로 해소됐다. 확정은 결정 `p8-agent-verification-target`의 결론이다. `verifies`의 도착점은 둘 다 개발 KB 청크다.

옛 결정은 새 결정의 대안 청크가 기각한 안(옛 결정을 두고 사슬을 포기한다)이라 배제한다. 청크로 존재하지 않는 기각안은 후보로 세우지 않는다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193
  kind: refines
status: resolved
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/889cd3dc-d652-4e79-b911-9a052216801b
    state: confirmed
    evidence: [{kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/889cd3dc-d652-4e79-b911-9a052216801b}]
  - to: https://agentic-knowledge-base.dev/id/chunk/1346522d-0e9b-4a3d-9390-082cf9aa47f3
    state: eliminated
    eliminated_by: {kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/3cbd4ee9-bf86-4244-9922-2d8ba28c8678}
```
