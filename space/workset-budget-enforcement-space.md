---
id: https://agentic-knowledge-base.dev/id/chunk/dde74c1a-c45c-4080-99f3-32f49cf8a2b9
type: agt:Space
level: logical
title_ko: 작업 집합의 예산 초과를 무엇이 막는가
title: What enforces the workset budget
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-10-04T14:34:02+09:00}
---
요구 `context-budget`은 작업 집합이 예산 안에 든다고 정한다. 강제 수단이 변수였고 유저 답(2026-09-22)으로 해소됐다. 확정은 결정 `p1-workset-budget-fails-only-with-anchor`의 결론이다. 앵커가 있을 때만 예산 초과가 빌드를 실패시킨다.

항상 실패시키는 안과 V&V 문구 대조에 맡기는 안은 같은 결정의 대안 청크 하나에 함께 기각되어 있어 배제 후보 하나로 적는다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a
  kind: refines
status: resolved
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/3cbdac9a-dbb5-4378-bb0f-89231dd05cd4
    state: confirmed
    evidence: [{kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/3cbdac9a-dbb5-4378-bb0f-89231dd05cd4}]
  - to: https://agentic-knowledge-base.dev/id/chunk/3fab0678-5d4b-46d0-9d0d-f585a3530f25
    state: eliminated
    eliminated_by: {kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/chunk/3fab0678-5d4b-46d0-9d0d-f585a3530f25}
```
