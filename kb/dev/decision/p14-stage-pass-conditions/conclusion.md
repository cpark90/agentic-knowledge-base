---
id: https://agentic-knowledge-base.dev/id/chunk/1f7d15d7-e85d-42dd-bef3-fb9c9a6d0365
type: decision
level: concrete
title_ko: 도입 단계별 통과 조건은 의미 보존·구체화·유기적 연결 세 축이다
title: Stage pass conditions are three axes: meaning preserved, concretisation, organic linkage
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T21:10:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/7ffcce18-39d0-45b3-90f7-6ac8d1528254]
composite: {id: https://agentic-knowledge-base.dev/id/composite/6878b566-73c2-462f-a524-5203c4c3832e, title_ko: 단계별 통과 조건 — 세 축, title: Stage pass conditions — three axes}
part_of: https://agentic-knowledge-base.dev/id/composite/6878b566-73c2-462f-a524-5203c4c3832e
---
**결론** — 도입 8단계(사례 프로젝트 하나에서 끝까지, 동시 도입 없음)는 유지하되, 각 단계의 통과 조건을 **양**이 아니라 세 축으로 쓴다 (노트 14.1절, 2026-09-10 정정).

| 축 | 묻는 것 | 대리 지표(생성물) | 최종 판정 |
|---|---|---|---|
| **의미 보존** | 원문·상위 수준의 확정 내용이 빠짐없이 아래로 전달됐는가 | 확정 문장 커버리지, 대안·근거 존재, `sources`, 절 인용 결정의 포함 | 라벨 대표성·답 완전성 **실험** |
| **구체화** (가상화 단계 = 수준 계층) | 각 수준이 상위를 정제해 더 구체적인 것을 더했는가 | 수준 허용표 위반 0, `refines` 한 단계씩, 빈 수준 0, 결정 완결률, 수기 케이스 0 | — |
| **유기적 연결** | 지식이 고립되지 않고 질의로 서로 닿는가 | 연결 성분 수, 매트릭스 채움률, ODD 밖 참조 0, 검증 대응물 채움률, 영향 집합 = 실제 의존 | 무효화 실험(정밀도·재현율) |

단계별 조건은 노트 14.1 표(정정본)와 `docs/feedback/stage-pass-conditions.md`의 채택 표가 원본이다. 이 저장소의 1단계: 고아율 0%·예산 이내는 통과, 확정 문장 커버리지와 라벨 대표성 실험이 남았다.
