---
id: https://agentic-knowledge-base.dev/id/chunk/15d8c8e5-5bd9-44ba-ae32-7580a70fc20c
type: decision
level: abstract
title_ko: 시나리오 배제 자극 — 생성물의 수치가 바뀌고 문서의 표가 그대로인 편집에서 다루지 않는 것
title: Scenario excluded stimuli — what an edit that changes the generated numbers and leaves the document table does not cover
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-29T15:40:00+09:00}
verified: [{by: vnv/claude-sonnet-5, at: 2026-10-01T18:00:07+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/d71fb313-ed12-47c0-87f8-3c79d7531adf
specializationOf: https://agentic-knowledge-base.dev/id/chunk/31b9d3b9-577d-486a-8792-1146783508ae
---
**배제 자극** — 다루지 않는 자극은 셋이다.

- 문서가 수치를 적지 않고 생성 명령만 인용하는 경우는 이 부류가 다루지 않는다. 어긋날 값이 없으므로 자극이 아니다.
- 생성 트리 파일의 바이트 비교는 다른 부류가 덮는다. 그쪽은 `agt:generatedArtefactDrift`(P8)이고 드리프트 시험 둘이 이미 센다.
- 소통 채널의 낡은 수치는 제외한다. 채널은 소통 기록이고 그래프 밖이라 게이트 검사 대상이 아니다.
