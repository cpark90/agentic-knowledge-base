---
id: https://agentic-knowledge-base.dev/id/chunk/dde74c1a-c45c-4080-99f3-32f49cf8a2b9
type: agt:Space
level: logical
title_ko: 작업 집합의 예산 초과를 무엇이 막는가
title: What enforces the workset budget
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T21:10:00+09:00}
---
요구 `context-budget`은 작업 집합이 예산 안에 든다고 정하는데, 그것을 강제하는 것이 없다. `tools/workset.py`는 예산을 넘겨도 빌드가 성공하고 머리에 판정 한 줄만 적는다. 도입 2단계의 통과 조건이 이 판정에 걸려 있으므로 강제 수단이 변수다.

앵커 없는 전체 뷰는 구조적으로 예산을 넘는다. 그래서 "항상 실패"와 "앵커가 있을 때만 실패"가 갈리고, 셋째로 게이트 대신 V&V 케이스가 뷰의 문구를 대조하는 길이 있다. 셋 다 청크로 존재하지 않아 후보를 열거하지 않는다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/45f9ad28-7bf6-4267-87f0-271ca83fae5a
  kind: refines
status: open
```
