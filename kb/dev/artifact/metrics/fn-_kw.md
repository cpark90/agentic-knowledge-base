---
id: https://agentic-knowledge-base.dev/id/chunk/213f1d8d-a21d-4794-a6f1-f88e4a849f3d
type: artifact
level: executable
title_ko: 함수 _kw (tools/metrics.py)
title: function _kw in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a599c470-8ce8-4e70-a475-1067401bb55c
---
**함수** — `_kw(call, key)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _kw(call, key):
    return next((k.value for k in call.keywords if k.arg == key), None)
```
<!-- 인용 끝 -->
