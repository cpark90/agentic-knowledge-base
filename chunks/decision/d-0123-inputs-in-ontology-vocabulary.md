---
id: https://agentic-knowledge-base.dev/id/chunk-d0123
type: decision
level: concrete
title_ko: 입력은 온톨로지 어휘로 쓰고 버전 관리한다
title: Inputs are written in ontology vocabulary and versioned
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 9.1절의 모든 입력을 온톨로지 어휘로 쓰고, ODD와 같은 방식으로
버전 관리한다.

**근거** (노트 9.1, 9.5절)
- **입력이 어휘 밖에 있으면 체계가 읽을 수 없다.** 에이전트 카탈로그의
  역할은 `related/harness`의 개념이고, 실행 모드는 그 속성이다.
- 입력이 바뀌면 그 위의 파생물이 바뀐다. 언제 무엇이 바뀌었는지 남아야
  파생물의 재검토 범위가 계산된다 — ODD를 버전 관리하는 이유와 같다.
- 어휘로 쓰면 입력 검증(9.6절)이 청크와 같은 shape 수단을 그대로 쓴다.

**형식 예시** (9.5절, 카탈로그의 한 항목) — 권한과 실행 특성이 전부 속성으로
표현된다.

```
:developer a agt:Role ;
  rdfs:label "developer"@en , "개발자"@ko ;
  agt:writes agt:ArtifactChunk ;
  agt:reads  agt:ContractChunk , agt:SchemaChunk ;
  agt:executionMode agt:dispatch ;
  agt:maxConcurrent 2 .
```
