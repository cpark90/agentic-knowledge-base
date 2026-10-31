---
id: https://agentic-knowledge-base.dev/id/chunk/f5f417da-b27d-431e-8ca5-1a91337fde37
type: norm
level: logical
title_ko: docs/rules.md 절 파일 형식의 이어짐 — 값 어휘의 단일 정의 위치와 head 생성 경로
title: docs/rules.md file-format section continued — the single definition of value vocabularies and the head generation path
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
continues: true
---
**값 어휘와 지식 종류별 허용 수준 표의 단일 정의 위치는 `defs/kb.bzl`이다** (2026-09-26·27). `PLANES`, `LEVELS`,
`STATES`, `RESIDENCY`를 거기에만 적고, 파이썬 쪽 도구인 `chunk2kg`와 `kb_lib`는 그 리터럴을 읽어 파생한다. 단위 지식을 파싱하는
모든 액션은 `//defs:kb.bzl`을 입력으로 받는다. 그 액션은 `kb_chunk`와 `kb_decision`의 head 액션, `kb_consistency`,
`kb_weave`, `kb_index`, `//space:design_space`, `//:build_drift_test`이고, `bazel run` 도구는 `BUILD_WORKSPACE_DIRECTORY`로
경로를 푼다. 폴백값은 두지 않는다. 값이 같아도 정의 위치가 둘이면 어느 날 하나만 고쳐지기 때문이다.
shape 파일 `residency-shapes.ttl`은 소스로 남지만, 게이트 `residency`가 원본과의 동일성을 강제한다.

`tools/chunk2kg.py`가 따로 정의하는 것은 지식 종류 이름에서 온톨로지 클래스로 가는 사상인 `PLANE_CLASS`와 필수 키 `REQUIRED`뿐이고, 그 사상의 키 집합이 `defs/kb.bzl`의 `PLANES`와 같은지는 로드할 때 단정한다. 생성 경로에서는 단위 지식
타깃인 `kb_chunk`와 `kb_decision`마다 head 조각을 내고, 그 조각을 패키지의 `:kg` 묶음으로 모은 뒤 `kb_kg_merge` 규칙의 `//kg:chunks_kg`가
합쳐 `bazel-out/.../kg/chunks-kg.ttl`을 만들며, 이 파일이 `//kg:gate_test`의 입력이 된다. 생성물은 `bazel-out`에만
존재하며 소스 트리에 같은 이름의 파일을 두지 않는다.
