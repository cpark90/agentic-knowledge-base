---
id: https://agentic-knowledge-base.dev/id/chunk/b10bcecd-3636-4034-ba39-50cb686eb144
type: decision
level: concrete
title_ko: 카탈로그는 IRI를 위치에서 떼어 두므로 재배치와 저장소 추가가 값싸다
title: The catalog keeps IRIs independent of location, so relocation and adding repositories stay cheap
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0156-catalog-resolved-union.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:29:30+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:29:30+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/5beca94e-efeb-4e6c-89a7-12c3fa80103e
---
**근거** — 출처는 harness-functional `docs/federation-design.md`의 D1이다.

- 카탈로그는 IRI를 **위치 독립**으로 유지하는 값싼 방법이다. 실제 재배치에서 데이터 파일과 root가 저장소를 통째로 옮겼지만 IRI는 하나도 바뀌지 않았고, 카탈로그의 경로만 고쳤다. 경로를 하드코딩했다면 그 이동이 전부 IRI 변경이 되어 그것을 참조하던 간선이 깨진다.
- 새 데이터 저장소를 연합에 넣는 비용은 두 줄이다. 카탈로그에 IRI와 경로를 잇는 한 줄을, 조립하는 root의 import에 한 줄을 더한다. **도구 코드는 바뀌지 않으며**, 이것이 카탈로그 기반 연합의 요점이다.
- 검증 전용 shape 파일은 import 대상에서 제외한다. 데이터 그래프에 섞이면 검사 대상과 검사 규칙이 한 그래프가 되어 무엇을 검사한 것인지 흐려지기 때문이다.
- 카탈로그나 root가 없으면 디렉토리 스캔으로 **폴백**한다. 그래서 부분 체크아웃에서도 도구가 죽지 않고 로드된다.
