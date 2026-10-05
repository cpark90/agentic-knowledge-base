---
id: https://agentic-knowledge-base.dev/id/chunk/1b9c7db7-1d30-4672-b7c4-192c713bd868
type: norm
level: logical
title_ko: docs/rules.md 절 — development 규칙과 코드의 추출
title: docs/rules.md section — development rules and code extraction
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/9740d5da-ea8e-4ebd-8e50-1e287cdba400
composite: {id: https://agentic-knowledge-base.dev/id/composite/9740d5da-ea8e-4ebd-8e50-1e287cdba400, title_ko: docs/rules.md의 development 절 묶음, title: docs/rules.md development section group, part_of: https://agentic-knowledge-base.dev/id/composite/4ae2bbc4-2198-4191-b626-091c3aecdb23, ordered: [https://agentic-knowledge-base.dev/id/chunk/1b9c7db7-1d30-4672-b7c4-192c713bd868, https://agentic-knowledge-base.dev/id/chunk/602ace1f-da3e-411a-84a5-e86d54a3320a, https://agentic-knowledge-base.dev/id/chunk/f6dc3c29-4cd1-4da5-9216-ab5840b50e90]}
heading: development 규칙 — 개발 KB (노트 7.2~7.7)
depth: 2
---
개발 KB는 요구 명세에서 실산출물을 생산하기 위한 지식이다
([`p7-dev-kb-purpose`](../../decision/p7-dev-kb-purpose/conclusion.md)). 코어 규칙 위에 다음이 더해진다.

**코드는 청크로 올라오고 방향은 추출이다**(유저 승인 2026-09-30, [`p7-code-extraction-direction`](../../decision/p7-code-extraction-direction/conclusion.md)).
소스 파일 하나가 패키지 하나(`kb/dev/artifact/<모듈>/`)이고 청크 전부가 `bazel run //tools:extract -- <소스>`의 생성물이다 —
손으로 고치면 `//:extract_drift_test`가 거부한다. 정체성의 원본은 소스 옆 사이드카 등록부 `<소스>.chunks.yml`의 `한정 이름 →
uuid`이고 신설만 자동이다 — 개명·삭제는 등록부 편집이다([`p10-function-identity-registry`](../../decision/p10-function-identity-registry/conclusion.md)).
링크는 파일 복합체가 갖는다([`p7-code-links-on-file-composite`](../../decision/p7-code-links-on-file-composite/conclusion.md)) — 등록부의
`refines`를 추출기가 파일 청크와 절 청크로 옮기고 정의 청크는 `part_of`만 갖는다. `serves`는 정의역이 `agt:DecisionChunk`이므로
`artifact` 청크가 요구를 직접 `serves`하지 않는다 — 결정을 `refines`하고 그 결정이 요구에 닿는다. `artifact`의 `verified`는
테스트 통과 도장이다(`STYLEGUIDE.md` §4).
