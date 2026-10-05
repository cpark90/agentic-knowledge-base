---
id: https://agentic-knowledge-base.dev/id/chunk/c8ca6ad0-31b7-43b9-bca5-a31871f4ee1b
type: artifact
level: executable
title_ko: 절 levels (defs/kb.bzl)
title: section levels in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9a583117-c61c-48f7-b30a-f60bddda9bfe
---
**절** — `defs/kb.bzl` 의 절 `levels` 다. 값 어휘와 수준 허용표 — 분석 시점 판정과 파이썬 파생처가 함께 읽는 단일 정의처

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 값 어휘와 수준 허용표 — 분석 시점 판정과 파이썬 파생처가 함께 읽는 단일 정의처 ──────────────────────────
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
# 5.2절 단방향 순서. `norm`(규범 문서의 절, p12-norm-documents-from-section-chunks)은 끝에 둔다 — 결정의 투영이라 어느 plane 도
# 그것을 refines 하지 않고, 그것은 위의 어느 plane 이든 refines 할 수 있다
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory", "norm"]
# 수준 허용표 (6.4절) 의 **단일 정의처**다 (M1 단일 정의처, 2026-09-26). 여기 말고 어디에도 표를 손으로 적지 않는다.
# Starlark 는 파일을 읽지 못하므로 분석 시점 판정에 쓰이는 이 표가 원본이고, 파이썬 쪽은 이 리터럴을 읽어 파생한다
# (`tools/kb_lib.py` 의 `load_residency`). 파생처는 셋이다 — 분석 시점 `_check_residency` ·
# `tools/metrics.py` 의 거주 위반 지표 · 게이트 `residency`(`kb/ontology/shapes/residency-shapes.ttl` 이 이 표와 같은지).
# 값에 주석(`#`)을 쓰지 않는다 — 파서가 주석을 지운 뒤 리터럴로 읽는다.
RESIDENCY = {
    "requirement": ["functional"],
    "decision": ["abstract", "logical", "concrete"],
    "contract": ["abstract", "logical"],
    "schema": ["logical", "concrete"],
    "artifact": ["concrete", "executable"],
    "memory": ["concrete"],
    "annotation": LEVELS,
    "norm": ["logical"],
}
STATES = ["draft", "stable", "suspect", "invalidated", "deprecated"]
```
<!-- 인용 끝 -->
