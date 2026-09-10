---
id: https://agentic-knowledge-base.dev/id/chunk/a02a4db5-cf50-4b19-9a5e-1b101c4e0600
type: decision
level: concrete
title_ko: 입력은 온톨로지 어휘로 쓰고 버전 관리한다
title: Inputs are written in ontology vocabulary and versioned
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0123]
part_of: https://agentic-knowledge-base.dev/id/composite/81f5ea27-b01f-427d-bad5-4d35e593b94d
composite: {id: https://agentic-knowledge-base.dev/id/composite/81f5ea27-b01f-427d-bad5-4d35e593b94d, title_ko: 입력의 표기와 버전 관리, title: Notation and versioning of inputs}
---
**결론** — 10.1절의 모든 입력을 **온톨로지 어휘로 쓰고**, ODD와 같은 방식으로
**버전 관리한다.** 에이전트 카탈로그의 역할은 `related/harness`의 개념이고
실행 모드는 그 속성이다. 카탈로그의 한 항목은 이렇게 쓴다.

```
:developer a agt:Role ;
  rdfs:label "developer"@en , "개발자"@ko ;
  agt:writes agt:ArtifactChunk ;
  agt:reads  agt:ContractChunk , agt:SchemaChunk ;
  agt:executionMode agt:dispatch ;
  agt:maxConcurrent 2 .
```
