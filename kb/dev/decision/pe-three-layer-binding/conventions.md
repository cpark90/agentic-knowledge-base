---
id: https://agentic-knowledge-base.dev/id/chunk/fedbcbff-d6a0-4214-a758-d215f37bba66
type: decision
level: concrete
title_ko: 규범 문서 규약 — 청크의 물리 형식은 OKF, 어휘·제약은 온톨로지, 의존·검사·뷰는 Bazel이 맡는다
title: Normative-document conventions — OKF carries physical form, the ontology carries vocabulary and constraints, Bazel carries dependencies, checks and projections
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T02:19:04+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/22ffbbd9-3eba-4e36-aeaf-8e5ff96113aa
---
**규약** — `pe-three-layer-binding`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] frontmatter 필수 키는 `id`, `type`, `level`, `title_ko`, `title`, `status`, `generated`다(OKF v0.2 사상, 노트 E.2). 선택 키는 `verified`, `sources`, `assumes`, 요구에만 쓰는 `pattern`(EARS — `ubiquitous`·`event-driven`·`state-driven`·`unwanted-behaviour`·`optional`·`complex`), 그리고 복원 링크의 표시 `restored`(같은 청크의 링크 대상 IRI 목록 — 증거가 `proposal`이 된다, [`p10-restored-link-marking`](../p10-restored-link-marking/conclusion.md)), 분할 조각의 `specializationOf`(원 청크 IRI 하나 — 같은 plane, [`p10-split-keeps-work-identity`](../p10-split-keeps-work-identity/conclusion.md)), 위험에서 파생된 항목의 `exposes`(그 항목이 노출하려는 결함 요인 개체의 `agt:` IRI 목록 — `agt:exposesFactor`로 나가고 링크 키가 아니다, 게이트 `shacl`(exposes-factor))이다. `type`·`status`·`generated`·`verified`는 **OKF v0.2 필드명**이다. 이 저장소의 `chunks/`는 OKF 번들이다. 값 어휘의 원본은 둘로 갈린다(2026-09-27). `PLANES`·`LEVELS`·`STATES`는 **`defs/kb.bzl`**이 원본이고 `tools/chunk2kg.py`는 그것을 리터럴로 읽어 파생한다 — Starlark는 파일을 읽지 못해 분석 시점 판정을 지키려면 표가 거기 있어야 한다. `PLANE_CLASS`·`REQUIRED`는 `chunk2kg.py`가 원본이며 `PLANE_CLASS`의 키 집합이 `PLANES`와 다르면 로드 시점에 죽는다. 폴백은 없다 — `defs/kb.bzl`을 입력으로 받지 못한 액션은 `EXIT_CONFIG`다.
규약: [지킴] 예약 파일명 `index.md`·`log.md`를 쓰지 않는다(OKF).
