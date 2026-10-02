---
id: https://agentic-knowledge-base.dev/id/chunk/5a68bc5c-e462-4ae7-851e-58acb707017a
type: artifact
level: executable
title_ko: 절 kb-dev (tools/kb_lib.py)
title: section kb-dev in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294
composite: {id: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294, title_ko: 절 복합체 kb-dev (tools/kb_lib.py), title: section composite kb-dev in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5a68bc5c-e462-4ae7-851e-58acb707017a, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99, https://agentic-knowledge-base.dev/id/chunk/f4d0d4bb-6623-435e-b230-93d98fb7ceac, https://agentic-knowledge-base.dev/id/chunk/f25447a7-4301-4ae4-b0a6-d22f459cd775, https://agentic-knowledge-base.dev/id/chunk/01fd5990-0c31-4b71-8dcd-ee095148db30, https://agentic-knowledge-base.dev/id/chunk/8d31b7a9-85c6-48b3-875b-1223f473d503, https://agentic-knowledge-base.dev/id/chunk/90abf3f7-3c52-496f-9cb4-a2af556264cb], part_of: https://agentic-knowledge-base.dev/id/composite/e7e09bb4-4c00-411e-9e5d-857406143657}
---
**절** — `tools/kb_lib.py` 의 절 `kb-dev` 다. 두 KB 의 경계와 수준 허용표와 그래프 적재 (pe-storage-layout · M1 단일 정의처 · 2.3절 정의 경계)

**정의** — `kb_of` · `load_residency` · `load_graph` · `load_merged` · `defined_terms` · `is_well_known` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 두 KB 의 경계와 수준 허용표와 그래프 적재 (pe-storage-layout · M1 단일 정의처 · 2.3절 정의 경계) ──────────
# 두 KB 의 경로 접두 (pe-storage-layout) — 역할의 agt:writesIn 값이자 청크 assertionLocation 의 KB 판정 기준 (p8-vv-roles, 2026-09-19).
# gen_build 는 rdflib 없이 돌므로 같은 접두를 자체 상수(VV_ROOT)로 갖는다 — chunk2kg 의 PLANE 상수와 같은 사유
KB_DEV = "kb/dev"
KB_VV = "kb/vv"
KB_ROOTS = (KB_DEV, KB_VV)




# 수준 허용표의 단일 정의처 — `defs/kb.bzl` 의 `LEVELS`·`RESIDENCY` 리터럴이다 (M1 단일 정의처, 2026-09-26).
# Starlark 는 파일을 읽지 못하므로 표는 Starlark 쪽에 있어야 하고, 파이썬은 그 리터럴을 읽어 파생한다.
# 파생처는 둘이다 — `tools/metrics.py` 의 거주 위반 지표와 `tools/validate.py` 의 게이트 `residency`
# (shape `residency-shapes.ttl` 이 이 표와 같은지 판정한다).
_BZL_RESIDENCY = re.compile(r"^\s*RESIDENCY\s*=\s*\{(.*?)^\}", re.M | re.S)



# 온톨로지 모듈이 "정의"로 간주되는 타입 (2.3절 경계 규칙, 2.5절 정의 완전성)
DEFINING_TYPES = (
    OWL.Class,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.NamedIndividual,
    RDFS.Class,
    RDF.Property,
)
```
<!-- 인용 끝 -->
