---
id: https://agentic-knowledge-base.dev/id/chunk/fbfb8a51-e654-40e6-8ff6-044179dce904
type: decision
level: logical
title_ko: 청크는 시간 정체성을 위해 uuid를 받았고 손 개체의 슬러그는 역할·스코프 대응과 게이트 태그가 기대는 지속 이름이다
title: Chunks took uuids for temporal identity, while hand-written entity slugs are persistent names that the role-scope correspondence and gate tags rely on
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:15:25+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c9bb4d82-ac37-467d-8661-6982d1684108
---
**근거** — 청크의 uuid는 `p0-iri-design`의 지속 IRI다(노트 0.7절). 라벨이나 경로가 바뀌어도 IRI가 유지되어야 시간 정체성이 성립하고, 그래서 v3부터 uuid다(유저 결정 Q1, 2026-09-10 재도출). 초판 표(2026-09-01)에서는 청크도 `chunk-` 슬러그였다. 복합체는 선언 청크의 `composite.id`로 서므로 청크와 같은 꼴을 따른다.

손 개체의 슬러그도 지속 이름으로 쓰인다. 참조 저장소가 `harness_ontology`에서 `harness-functional`로 개명된 뒤에도 `id:doc-harness-ontology`는 유지됐다(`base-kg.ttl` 주석). 슬러그에 기대는 기계 검사는 둘이다.

- 게이트 `catalog`는 역할 `id:role-<x>`의 스코프를 `id:scope-<x>`로 찾는다. 카탈로그에 역할→스코프 술어가 없고 슬러그가 대응의 원본이다(`kb_lib.ROLE_ID_PREFIX` 주석, 2026-09-13).
- 게이트 개체는 `gates2kg`가 `GATES`에서 낸다(2026-10-02). 도구 태그 `FAIL [<id>]`의 id가 그대로 개체 이름의 슬러그다.

실측(2026-10-03)에서 v1 잔류 IRI는 126개이고 결정 결론 124개의 `supersedes` 대상으로만 나타난다. `comp-` 개체는 0건이다. 손으로 쓴 복합체 41건이 2026-09-29에 생성 경로로 옮겨졌다(`composite-kg.ttl` 배너). `scn-` 개체도 0건이다. 시나리오는 `kb/vv/scenario/`의 청크로 섰다. 실행 기록은 2026-09-19부터 `vv_run`이 쓰는 memory 청크(`kb/vv/run/run-<시각>.md`)다. 초판 표의 `run-` 접두사는 이때 빠졌다.

표 전체를 판정하는 게이트는 없다. `chunk2kg`는 IRI 중복만 거부하고 uuid의 꼴은 검사하지 않는다.

`p0-run-as-observation` 결론은 실행 기록을 `run-kg`에 저장한다고 적었다. 유저 답 Q8-a(2026-10-03)로 그 결정은 `p0-run-is-an-append-only-memory-chunk`로 대체됐고, 대체 결정은 실행 기록을 이 표의 꼴대로 `kb/vv/run/`의 memory 청크로 둔다.

미확정: 손 개체에 uuid 대신 슬러그를 남긴 이유는 기록에서 확인하지 못했다.
