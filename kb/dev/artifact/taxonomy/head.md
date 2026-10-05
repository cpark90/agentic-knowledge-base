---
id: https://agentic-knowledge-base.dev/id/chunk/205f5607-e950-444d-b697-1bf3f4449223
type: artifact
level: executable
title_ko: 모듈 머리 exit-config (tools/taxonomy.py)
title: module head exit-config in tools/taxonomy.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/5cd36157-e133-4ff0-bb51-ba6848ba0fbd
---
**모듈 머리** — `tools/taxonomy.py` 의 모듈 머리 `exit-config` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)

AGT = Namespace("https://agentic-knowledge-base.dev/agt/")
KEYS = {AGT.StaticElement: "static_element", AGT.EnvironmentalCondition: "environmental_condition", AGT.DynamicElement: "dynamic_element"}
```
<!-- 인용 끝 -->
