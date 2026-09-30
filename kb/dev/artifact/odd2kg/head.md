---
id: https://agentic-knowledge-base.dev/id/chunk/fb4cc423-29a9-4491-a1e8-a630c1b5a123
type: artifact
level: executable
title_ko: 모듈 머리 exit-fail (tools/odd2kg.py)
title: module head exit-fail in tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/3d66b1bc-0e65-4e62-9654-fc0ddb6b7d20, https://agentic-knowledge-base.dev/id/chunk/40abcad5-6a9c-4233-99d3-0b7ceeafb06b]
part_of: https://agentic-knowledge-base.dev/id/composite/50c525bb-02f0-4c2b-a9e0-1a3b666fbd3c
---
**모듈 머리** — `tools/odd2kg.py` 의 모듈 머리 `exit-fail` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)
TAG = "odd2kg"
```
<!-- 인용 끝 -->
