---
id: https://agentic-knowledge-base.dev/id/chunk/6fc1c9d5-1328-4b8e-8d4b-b2145b8d5602
type: decision
level: concrete
title_ko: 개념 정의와 개체는 파일이 다르고 편집 주체도 다르다
title: Concept definitions and individuals live in different files with different editors
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0049-tbox-abox-separation.md, id: https://agentic-knowledge-base.dev/id/chunk-d0049, title_ko: "T-Box와 A-Box를 다른 파일에 둔다", title: "T-Box and A-Box live in separate files"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/20148952-30c4-4f76-8cbf-4d9b32c68b25]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0049]
part_of: https://agentic-knowledge-base.dev/id/composite/066baab4-8fef-4903-ac08-2d2c9d37f233
composite: {id: https://agentic-knowledge-base.dev/id/composite/066baab4-8fef-4903-ac08-2d2c9d37f233, title_ko: T-Box와 A-Box를 다른 파일에 둔다, title: Keep T-Box and A-Box in separate files}
---
**결론** — 온톨로지(개념 정의)와 지식그래프(개체)를 **다른 파일에 둔다.** 0.2절 접미사가 이를 강제한다.

- **T-Box** — `*-ontology`, `*-rules`. 변경률 낮음. 편집 주체는 설계 에이전트와 유저
- **A-Box** — `*-kg`, `*-space`. 변경률 높음. 적용 범위 안의 모든 에이전트가 편집

요구·기준·테스트 케이스·실행 기록·결정 인스턴스·링크는 전부 A-Box다. **온톨로지 파일을 열지 않고도 생성·편집할 수 있어야 한다.**
