---
id: https://agentic-knowledge-base.dev/id/chunk/4a08e226-4f1f-4a70-a989-365d02ec3724
type: decision
level: concrete
title_ko: 규범 문서 규약 — 개체 IRI는 frontmatter에서 서는 단위 지식·복합체가 uuid4 경로이고 그 밖의 개체가 종류 접두사 슬러그다
title: Normative-document conventions — Entity IRIs are uuid4 paths for chunks and composites declared in frontmatter, and kind-prefixed slugs for every other entity
former_title_ko: ["규범 문서 규약 — 개체 IRI는 frontmatter에서 서는 지식 항목·복합체가 uuid4 경로이고 그 밖의 개체가 종류 접두사 슬러그다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:09:31+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c9bb4d82-ac37-467d-8661-6982d1684108
---
**규약** — `p0-entity-iri-forms`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 개체 IRI의 꼴은 개체가 어디서 서는가로 정한다. 단위 지식 파일의 frontmatter에서 서는 단위 지식·복합체는 불투명 uuid4 경로인 `id/chunk/<uuid4>`와 `id/composite/<uuid4>`이고, 그 밖의 개체는 `id:` 네임스페이스의 `<kind>-<slug>` 소문자 케밥이다. 접두사 표는 [`docs/rules.md` §개체 IRI 접두사](../../../../docs/rules.md#개체-iri-접두사)에 있다. 표에 없는 접두사가 그래프에 나타나면 그 접두사 자체가 드리프트 신호다.
규약: 지식, v3 이후 | `id/chunk/<uuid4>`, 불투명 영속 IRI | 생성물 `chunks-kg.ttl`
규약: 지식, 묘비(지운 v1 결정) | `id:chunk-d<번호>`이고 새로 만들지 않는다 | 생성 `chunks-kg.ttl`의 묘비로 남고 `supersedes`의 끝점이다
규약: 복합체, v3 이후 | `id/composite/<uuid4>` | 생성물 또는 `composite-kg.ttl`
규약: 가정 · 출처 문서 | `asm-` · `doc-` | `base-kg.ttl`
규약: 손으로 쓴 복합체 | `comp-` | `composite-kg.ttl`
규약: ODD · 조건 | `odd-` · `cond-` | `project-odd.ttl`
규약: 하네스, 역할, 적용 범위, 채널 | `h-` · `role-` · `scope-` · `chan-` | `catalog-kg.ttl`
규약: 시나리오 | `scn-` | 아직 없음
규약: 게이트 | `gate-` | 생성되는 `bazel-bin/kg/gates-kg.ttl`이다. 원본은 `defs/kb.bzl`의 `GATES`이고 손으로 쓰지 않는다(2026-10-02)
규약: 투영인 뷰 · skill | `view-` · `skill-` | 생성되는 `bazel-bin/kg/projections-kg.ttl`이다. 원본은 `defs/kb.bzl`의 `VIEWS`와 `tools/kb_lib.py`의 `SKILLS`이고, `prov:wasDerivedFrom`이 원본 코드 단위 지식을 가리킨다. 층은 없다(Q9-a, 2026-10-03)
규약: 실행 기록 | `id/chunk/<uuid4>`. `memory` 지식 종류의 단위 지식이고, 파일은 `kb/vv/run/run-<시각>.md`, 프로세스는 `process:vv_run`이다 | 생성물 `chunks-kg.ttl`
