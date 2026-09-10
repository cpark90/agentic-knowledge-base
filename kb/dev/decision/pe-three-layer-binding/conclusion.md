---
id: https://agentic-knowledge-base.dev/id/chunk/578a6482-7bea-4b79-9206-92870d919a33
type: decision
level: concrete
title_ko: 청크의 물리 형식은 OKF, 어휘·제약은 온톨로지, 의존·검사·투영은 Bazel이 맡는다
title: OKF carries physical form, the ontology carries vocabulary and constraints, Bazel carries dependencies, checks and projections
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a, https://agentic-knowledge-base.dev/id/chunk/f389ae99-4988-4e0f-9ab7-81235bb9c5c8]
composite: {id: https://agentic-knowledge-base.dev/id/composite/22ffbbd9-3eba-4e36-aeaf-8e5ff96113aa, title_ko: 세 층 바인딩, title: Three-layer binding}
part_of: https://agentic-knowledge-base.dev/id/composite/22ffbbd9-3eba-4e36-aeaf-8e5ff96113aa
---
**결론** — 세 층 (노트 부록 E.1): **OKF v0.2** — 청크의 물리 형식. 파일 하나 = 청크 하나, 프런트매터 = head, 본문 = assertion / **온톨로지(Turtle + LinkML)** — 어휘·제약. `type`은 plane 클래스로 제한, 관계는 TIM 링크 타입으로 제한 / **Bazel** — 확정 링크 = deps, 게이트 = test, 투영 = build output, 재판정 = 증분 재실행.

OKF 필드 사상 (E.2): plane 클래스 → `type` · 라벨 → `title` + `title_ko` · provenance → `sources`(하네스가 편집 시 채움, 비면 verify 실패) · 시각 → `generated.at` · 청크 상태 → `status`(draft/stable/deprecated + 확장 suspect/invalidated) · 판정 이력 → `verified` 목록 · 판정식 → 계산 필드(`runtime: cel`) · 라벨 목록 → `index.md`(생성) · 변경 이력 → `log.md`(생성) · 확정 링크 → 확장 키 `refines`·`satisfies`·… · IRI → 확장 키 `id`(uuid).

이 저장소: OKF 사상 A안 채택(2026-09-07), `type`·`status`·`generated`·`verified` 반영. `title`·`sources`·`id` 정렬은 도입 순서 (a) (유저 결정 Q6).
