---
id: https://agentic-knowledge-base.dev/id/chunk/480b1d93-d4ad-4a70-8cea-3d25a7966d12
type: artifact
level: executable
title_ko: 함수 is_tombstone_block (tools/chunk2kg.py)
title: function is_tombstone_block in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7efb5476-c231-4b0e-9e6c-a2389a12409e
---
**함수** — `is_tombstone_block(block)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def is_tombstone_block(block: str) -> bool:
    return f"\n    a {TOMBSTONE_CLASS} ;" in block
```
<!-- 인용 끝 -->
