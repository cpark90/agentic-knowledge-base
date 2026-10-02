---
id: https://agentic-knowledge-base.dev/id/chunk/1b996b7a-5662-4887-bb93-a7266789532c
type: artifact
level: executable
title_ko: 절 load-yaml (tools/odd2kg.py)
title: section load-yaml in tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/3d66b1bc-0e65-4e62-9654-fc0ddb6b7d20, https://agentic-knowledge-base.dev/id/chunk/40abcad5-6a9c-4233-99d3-0b7ceeafb06b]
part_of: https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d
composite: {id: https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d, title_ko: 절 복합체 load-yaml (tools/odd2kg.py), title: section composite load-yaml in tools/odd2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/1b996b7a-5662-4887-bb93-a7266789532c, https://agentic-knowledge-base.dev/id/chunk/8399b16f-1c78-445a-9ae6-89835f8bf293, https://agentic-knowledge-base.dev/id/chunk/4401cc9a-d248-44ec-8285-6a183e9e3b21, https://agentic-knowledge-base.dev/id/chunk/4884310b-8897-44ad-945d-5f70435d9635, https://agentic-knowledge-base.dev/id/chunk/9b0e4980-f708-452f-b7c1-d932d6f1a6f8], part_of: https://agentic-knowledge-base.dev/id/composite/50c525bb-02f0-4c2b-a9e0-1a3b666fbd3c}
---
**절** — `tools/odd2kg.py` 의 절 `load-yaml` 다. OpenODD 문서를 읽어 ODD 그래프를 낸다

**정의** — `load_yaml` · `esc` · `classify` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── OpenODD 문서를 읽어 ODD 그래프를 낸다 ────────────────────


CLASS = {"static_element": "agt:StaticElement", "environmental_condition": "agt:EnvironmentalCondition", "dynamic_element": "agt:DynamicElement"}
NUM = re.compile(r'^\s*(<=?|>=?)\s*([-\d.]+)\s*(\w+)?\s*$')
RANGE = re.compile(r'^\s*\[\s*([-\d.]+)\s*\.\.\s*([-\d.]+)\s*\]\s*(\w+)?\s*$')
PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 OpenODD 문서 {src} (tools/odd2kg.py).
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix id: <https://agentic-knowledge-base.dev/id/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
"""








if __name__ == "__main__":
    raise SystemExit(main())
```
<!-- 인용 끝 -->
