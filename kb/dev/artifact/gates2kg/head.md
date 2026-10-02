---
id: https://agentic-knowledge-base.dev/id/chunk/5b36dc12-5981-480b-b53b-b3d740e777b7
type: artifact
level: executable
title_ko: 모듈 머리 exit-fail (tools/gates2kg.py)
title: module head exit-fail in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T15:47:27Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5]
part_of: https://agentic-knowledge-base.dev/id/composite/4f1a7107-6da2-49a5-b29b-7bc2f257f90a
---
**모듈 머리** — `tools/gates2kg.py` 의 모듈 머리 `exit-fail` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
EXIT_FAIL = kb_lib.EXIT_FAIL
EXIT_CONFIG = kb_lib.EXIT_CONFIG
TAG = "gates2kg"
ID_BASE = str(kb_lib.ID)
TIER_INDIVIDUAL = "agt:%sTier"  # 실행 계층 → 개체 (gate-tier-ontology)
LAYER_INDIVIDUAL = "agt:%sLayer"  # 서비스 층 → 개체 (layer-ontology)
HEADER = (
    "# 게이트 그래프 — 생성물이다. 손으로 쓰지 않는다 (tools/gates2kg.py).\n"
    "# 원본은 defs/kb.bzl 의 GATES 리터럴이고 개체 하나가 게이트 하나다 (id:gate-<게이트 id>).\n"
    "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n"
    "@prefix id: <%s> .\n"
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n" % ID_BASE
)
```
<!-- 인용 끝 -->
