---
id: https://agentic-knowledge-base.dev/id/chunk/133cf34f-4423-4525-954f-2676a7e752f5
type: artifact
level: executable
title_ko: 함수 as_list (tools/run_evidence.py)
title: function as_list in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:30:15Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/78c6c89d-58c3-43c8-8570-d8bfbac1700f
---
**함수** — `as_list(v)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def as_list(v) -> list:
    return v if isinstance(v, list) else []
```
<!-- 인용 끝 -->
