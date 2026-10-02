---
id: https://agentic-knowledge-base.dev/id/chunk/32847258-f1c4-4168-8add-3c90daa63de3
type: artifact
level: executable
title_ko: 함수 size_bucket (tools/metrics.py)
title: function size_bucket in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/dcc3c5a3-a8bd-4eb2-8d59-01f4ab1d6e3a
---
**함수** — `size_bucket(ratio)` 다. 상한에 대한 비율 → 칸 번호.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def size_bucket(ratio: float) -> int:
    """상한에 대한 비율 → 칸 번호. 경계 위는 다음 칸이고 마지막 칸은 9/10 초과다."""
    for i, edge in enumerate(SIZE_BANDS):
        if ratio <= edge:
            return i
    return len(SIZE_BANDS)
```
<!-- 인용 끝 -->
