---
id: https://agentic-knowledge-base.dev/id/chunk/4401cc9a-d248-44ec-8285-6a183e9e3b21
type: artifact
level: executable
title_ko: 함수 esc (tools/odd2kg.py)
title: function esc in tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d
---
**함수** — `esc(s)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def esc(s) -> str:
    return str(s).replace("\\", "\\\\").replace('"', '\\"')
```
<!-- 인용 끝 -->
