---
id: https://agentic-knowledge-base.dev/id/chunk/bd2b1aa7-e859-49c0-9e44-e961059cc36f
type: decision
level: concrete
title_ko: 개체 IRI는 frontmatter에서 서는 청크·복합체가 uuid4 경로이고 그 밖의 개체가 종류 접두사 슬러그다
title: Entity IRIs are uuid4 paths for chunks and composites declared in frontmatter, and kind-prefixed slugs for every other entity
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/90fc2df7-0a74-43fe-9c8f-546c7afdf1d3, https://agentic-knowledge-base.dev/id/chunk/f87ff3b1-40e7-4a23-827b-735744f377f9]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c9bb4d82-ac37-467d-8661-6982d1684108
composite: {id: https://agentic-knowledge-base.dev/id/composite/c9bb4d82-ac37-467d-8661-6982d1684108, title_ko: 개체 IRI의 꼴, title: Entity IRI forms}
---
**결론** — 개체 IRI의 꼴은 개체가 어디서 서는가로 정한다. 청크 파일의 frontmatter에서 서는 개체는 불투명 uuid4 경로다(`p0-iri-design`). 그 밖의 개체는 `id:` 네임스페이스의 `<kind>-<slug>` 소문자 케밥이다.

| 종류 | 꼴 | 사는 곳 |
|---|---|---|
| 청크 | `id/chunk/<uuid4>` | 생성 `chunks-kg.ttl` |
| 실행 기록 | memory 청크이므로 `id/chunk/<uuid4>` | 생성 `chunks-kg.ttl` |
| 복합체 | 선언 청크의 `composite.id` = `id/composite/<uuid4>` | 생성 |
| 복합체 (손) | `comp-` | `composite-kg.ttl` |
| v1 잔류 청크 | `id:chunk-d<번호>`. 새로 만들지 않는다 | `supersedes` 대상으로만 남는다 |
| 가정 · 출처 문서 | `asm-` · `doc-` | `base-kg.ttl` |
| ODD · 조건 | `odd-` · `cond-` | 생성 `project-odd.ttl` |
| 하네스 · 역할 · 스코프 · 채널 | `h-` · `role-` · `scope-` · `chan-` | `catalog-kg.ttl` |
| 시나리오 | `scn-` (예약) | 없음 |
| 게이트 | `gate-<게이트 id>` | 생성 `gates-kg.ttl`. 원본은 `defs/kb.bzl`의 `GATES` |
| 뷰 · skill (투영) | `view-` · `skill-` | 생성 `projections-kg.ttl`. 원본은 `defs/kb.bzl`의 `VIEWS`와 `tools/kb_lib.py`의 `SKILLS`이다(Q9-a, `p0-service-is-a-three-layer-wiki`) |

- 역할과 그 스코프는 같은 슬러그를 쓴다(`role-<x>` ↔ `scope-<x>`).
- 슬러그도 지속 이름이다. 가리키는 대상의 이름이 바뀌어도 IRI를 고치지 않는다.
- 표에 없는 접두사가 그래프에 나타나면 그 자체가 드리프트 신호다.
