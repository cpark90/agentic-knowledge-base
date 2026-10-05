---
id: https://agentic-knowledge-base.dev/id/chunk/35760d6b-0085-40d3-8399-9ec40573acc2
type: norm
level: logical
title_ko: docs/rules.md 절 traceability의 이어짐 — 링크 개체·증거 기록과 조회·복원 경로
title: docs/rules.md traceability section continued — link objects, evidence ledgers, retrieval and recovery
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:29:17+09:00}
overlapsWith: [https://agentic-knowledge-base.dev/id/chunk/9f6433f5-842d-42ab-8c1f-8a98344d143d]
restored: [https://agentic-knowledge-base.dev/id/chunk/9f6433f5-842d-42ab-8c1f-8a98344d143d]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/608085a2-2251-4b82-8ccc-a5c7e6e71766
continues: true
---
`allocates`는 요구→구성요소 할당이고 `generates`는 산출 의존이며, 둘은 v3 9장에서 추가됐다 (유저 결정
C7). `serves ⊑ refines`는 결정 → 요구·관심사의 링크이며 v4 6.8·7.3의 기여 명시다. `supersedes`는
시간축이라 세 족 밖이다. **링크는 개체다**(`agt:Link`). 링크는 양 끝·타입·**조건**·**증거 기록**을
갖는다. 조건은 `when`이며 ODD 속성·가정 위의 CEL이다. 증거 기록은 `agt:Evidence`이며 종류·참조·극성
±를 가진 항목 목록이다. 확정 전 후보는 `agt:CandidateLink`, 판정된 것은 `agt:ConfirmedLink`다.
상태(`candidate`/`confirmed`/`suspect`/`invalid`)는 저장값이 아니라 **조건 평가와 증거 기록 규칙의
결과**다. **수치 신뢰도는 없다.** 선호는 지지 증거의 종류 서열에서 파생된다. 서열은
구축 > 실행 > 동시 편집 > 공동 커버 > 임베딩 > 세션 > 제안이다. `assumes`와 스코프 conditional은
`when`의 특수형이다. 증거 기록 규칙 둘은 verify 질의다. 하나는 구축(+)·실행(+) 없는 확정이고, 다른
하나는 (−)가 있는 확정이다 (`tools/verify-queries/`). (노트 9.11절, 2026-09-10)

조회 알고리즘은 앵커 → 이웃 확장 → 우선순위 → 예산 패킹이며 [`p0-workset-anchor-neighbourhood`](../../decision/p0-workset-anchor-neighbourhood/conclusion.md)에 있다.
복원 경로는 [`p10-link-by-construction`](../../decision/p10-link-by-construction/conclusion.md)·[`p9-candidate-generation-limits`](../../decision/p9-candidate-generation-limits/conclusion.md)에 있다.
LEDGER·LARGER 대응표 원안은 출처 문서 `id:doc-dependency-graph-design`(2026-09-04, 반영 완료 2026-09-12 — 위치는 `kg/base-kg.ttl`의 `prov:atLocation`)에 있다.
**어휘는 갖춰졌고 링크 개체는 전부 구축 기록 증거를 갖는다(수는 `bazel build //kg:metrics` 3단계 절이 낸다 — 2026-09-11의 472는 2026-10-01에 1,277이었다).**
