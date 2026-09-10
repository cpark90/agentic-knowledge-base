---
id: https://agentic-knowledge-base.dev/id/chunk/eb439f51-39e5-4a23-9335-c77c588a598c
type: decision
level: concrete
title_ko: plane별 청크 규칙이 provider를 주고 링크 타입이 deps이며 -space는 deps가 아니다
title: Per-plane chunk rules provide providers, link types are deps, and -space is never deps
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
composite: {id: https://agentic-knowledge-base.dev/id/composite/3e725e9e-fd83-432d-b708-ed004a01cedd, title_ko: Bazel 규칙과 테스트, title: Bazel rules and tests}
part_of: https://agentic-knowledge-base.dev/id/composite/3e725e9e-fd83-432d-b708-ed004a01cedd
---
**결론** — Bazel 규칙 (노트 부록 E.6): plane별 `*_chunk` 규칙 — provider(plane·level·해시·라벨), 링크 타입별 속성이 deps, TIM·수준 허용표·동질성은 분석 시점 검사(위반 = 빌드 실패) / `composite` — 7±2·동질성 / `odd`·`scope`·`ontology` — 속성 provider, visibility 그룹, 3계층 검사 / `space` + `space_check_test` — 후보·제약·선호, 호 일관성, ODD 경계, 확정 제안, **deps 아님** / `kg`·`tangle`·`weave`·`trace_matrix`·`vv_report` — 뷰, 출력은 소스 밖 / 게이트 테스트 7종, `bazel test //...` = 재검증 시점.

`bazel query rdeps` = 영향 분석, `deps` + level 필터 = 근거 추적, visibility = 읽기 스코프. 쓰기 스코프·대칭 관계·`suspect` 저장은 Bazel 밖 — 커밋 훅, `constraint` 타깃, 캐시 미스 정의로 대체. 판정식 실행은 `external` 태그로 격리. 이 저장소: 현재는 디렉토리 단위 `kb_chunk_kg`·`kb_gate_test`; plane 규칙은 도입 순서 (c), 3단계 (유저 결정 Q6).
