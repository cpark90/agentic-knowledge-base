---
id: https://agentic-knowledge-base.dev/id/chunk-d0156
type: decision
level: concrete
title_ko: 카탈로그로 IRI를 파일로 해석해 union을 조립한다
title: Assemble the union by resolving IRIs through a catalog
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 여러 저장소에 나뉜 그래프는 **import 선언 + 카탈로그**(문서 IRI →
로컬 파일)로 하나의 union으로 조립한다. root 문서에서 import를 따라간 폐포가
곧 union이며, 디렉토리 glob도 submodule도 조립 수단으로 쓰지 않는다.

**근거** (harness-functional docs/federation-design.md D1)
- IRI를 **위치 독립**으로 유지하는 값싼 방법이다. 실제 재배치에서 데이터
  파일과 root가 저장소를 통째로 옮겼지만 IRI는 하나도 바뀌지 않았다 —
  카탈로그의 경로만 고쳤다. 경로를 하드코딩했다면 그 이동이 전부 IRI 변경이
  되어 그것을 참조하던 간선이 깨진다.
- 새 데이터 저장소를 연합에 넣는 비용이 두 줄이다: 카탈로그에 IRI→경로 한 줄,
  조립하는 root의 import에 한 줄. **도구 코드는 바뀌지 않는다** — 그것이
  카탈로그 기반 연합의 요점이다.
- 검증 전용 shape 파일은 import 대상에서 제외한다. 데이터 그래프에 섞이면
  검사 대상과 검사 규칙이 한 그래프가 되어 무엇을 검사한 것인지 흐려진다.
- 카탈로그나 root가 없으면 디렉토리 스캔으로 **폴백**한다 — 부분 체크아웃에서도
  도구가 죽지 않고 로드된다.

**대안**
- 디렉토리 glob·submodule 기각: 위치가 곧 정체성이 되어 파일 이동이 IRI 변경이
  된다. 배치를 사람이 읽기 좋게 바꾸는 일이 그래프 파괴가 되면 배치는 굳는다.
