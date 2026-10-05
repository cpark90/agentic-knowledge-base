---
id: https://agentic-knowledge-base.dev/id/chunk/f5f417da-b27d-431e-8ca5-1a91337fde37
type: norm
level: logical
title_ko: docs/rules.md 절 파일 형식의 이어짐 — 값 어휘의 단일 정의처와 head 생성 경로
title: docs/rules.md file-format section continued — the single definition of value vocabularies and the head generation path
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
continues: true
---
**값 어휘와 수준 허용표의 단일 정의처는 `defs/kb.bzl`이다**(2026-09-26·27). `PLANES`·`LEVELS`·`STATES`·`RESIDENCY`를 거기에만
적고, 파이썬 쪽(`chunk2kg`·`kb_lib`)은 그 리터럴을 읽어 파생한다. 청크를 파싱하는 모든 액션이 `//defs:kb.bzl`을 입력으로
받는다 — `kb_chunk`·`kb_decision`의 head 액션, `kb_consistency`·`kb_weave`·`kb_index`, `//space:design_space`,
`//:build_drift_test`이고, `bazel run` 도구는 `BUILD_WORKSPACE_DIRECTORY`로 푼다. 폴백값은 두지 않는다 — 값이 같아도
정의처가 둘이면 어느 날 하나만 고쳐진다. shape(`residency-shapes.ttl`)는 소스로 남되 게이트 `residency`가 원본과의
동일성을 강제한다.

값 어휘의 원본은 `tools/chunk2kg.py`의 상수(`PLANE_CLASS`·`LEVELS`·`STATES`·`REQUIRED`)다.
생성 경로는 청크 타깃(`kb_chunk`·`kb_decision`)마다 head 조각 → 패키지 `:kg` 묶음 → `//kg:chunks_kg`(`kb_kg_merge`)
→ `bazel-out/.../kg/chunks-kg.ttl` → `//kg:gate_test`의 입력이다.
생성물은 `bazel-out`에만 존재하며 소스 트리에 같은 이름의 파일을 두지 않는다.
