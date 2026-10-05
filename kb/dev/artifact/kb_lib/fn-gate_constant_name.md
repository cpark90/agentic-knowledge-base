---
id: https://agentic-knowledge-base.dev/id/chunk/e9c220ba-d7c1-4597-a620-d9ad84df3644
type: artifact
level: executable
title_ko: 함수 gate_constant_name (tools/kb_lib.py)
title: function gate_constant_name in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884
---
**함수** — `gate_constant_name(gate_id)` 다. 게이트 id → 파생 상수 이름 — `chunk` → `CHUNK_GATE` · `judge-log` → `JUDGE_LOG_GATE`.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gate_constant_name(gate_id: str) -> str:
    """게이트 id → 파생 상수 이름 — `chunk` → `CHUNK_GATE` · `judge-log` → `JUDGE_LOG_GATE`."""
    return gate_id.replace("-", "_").upper() + "_GATE"
```
<!-- 인용 끝 -->
