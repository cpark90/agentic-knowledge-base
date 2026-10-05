---
id: https://agentic-knowledge-base.dev/id/chunk/a13334ee-3c25-4384-bac2-a81868a47526
type: artifact
level: executable
title_ko: 함수 split_top_level (tools/chunk2kg.py)
title: function split_top_level in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `split_top_level(text)` 다. 콤마로 나누되 `[...]`·`{...}` 안의 콤마는 세지 않는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def split_top_level(text: str) -> list:
    """콤마로 나누되 `[...]`·`{...}` 안의 콤마는 세지 않는다 — 목록의 원소가 맵이거나 맵이 목록 값을 가질 때(절 키 `items`)."""
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        if ch == "," and depth <= 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts
```
<!-- 인용 끝 -->
