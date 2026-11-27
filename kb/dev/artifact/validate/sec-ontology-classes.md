---
id: https://agentic-knowledge-base.dev/id/chunk/9c8ff20b-21b5-413e-9f98-4759ec0b498d
type: artifact
level: executable
title_ko: 절 ontology-classes (tools/validate.py)
title: section ontology-classes in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64
composite: {id: https://agentic-knowledge-base.dev/id/composite/c74d5f7e-91df-4b58-b373-e0724cc08a64, title_ko: 절 복합체 ontology-classes (tools/validate.py), title: section composite ontology-classes in tools/validate.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/9c8ff20b-21b5-413e-9f98-4759ec0b498d, https://agentic-knowledge-base.dev/id/chunk/785609a5-d625-4486-b3dc-b0429b1de31c, https://agentic-knowledge-base.dev/id/chunk/03af6d80-e46c-44f7-acd5-12d186d9bb75, https://agentic-knowledge-base.dev/id/chunk/6caa6876-675f-4e0a-a42e-115c6f7e71d5, https://agentic-knowledge-base.dev/id/chunk/da2d5667-a0ed-4a3d-bfa8-6a83213f1d3f, https://agentic-knowledge-base.dev/id/chunk/2ef143c2-3056-410b-90b7-4bf908e80b8b, https://agentic-knowledge-base.dev/id/chunk/19b5263d-b450-496e-a214-49f3f4b0c0be, https://agentic-knowledge-base.dev/id/chunk/ff39b4c5-f9a7-40e5-bda5-e1cab86106d8], part_of: https://agentic-knowledge-base.dev/id/composite/4d158385-e139-4042-8477-a87c3deeefe2}
---
**절** — `tools/validate.py` 의 절 `ontology-classes` 다. 분류 계층

**정의** — `ontology_classes` · `subclass_components` · `check_cyclic_hierarchy` · `told_superclasses` · `probe_unsatisfiable` · `check_unsatisfiable_class` · `check_unintended_equivalence` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 분류 계층 ────────────────────
# 셋째 단계의 계층 검사 셋(유저 결정 Q179-a) — 순환, 불만족, 의도치 않은 동치다. 대상은 온톨로지 파일(--ontology)이 `owl:Class` 로
# 선언한 이름 IRI 이고 빈 노드(제약·교집합 같은 익명 클래스)와 owl:Thing·owl:Nothing 은 뺀다. 한 결함에 한 줄이다.
```
<!-- 인용 끝 -->
