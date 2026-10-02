---
id: https://agentic-knowledge-base.dev/id/chunk/71a80c9a-cb89-49ce-ae62-9d1fda16125b
type: artifact
level: executable
title_ko: 함수 split_outside_brackets (tools/chunk2kg.py)
title: function split_outside_brackets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `split_outside_brackets(text)` 다. 콤마로 나누되 `[...]` 안의 콤마는 세지 않는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def split_outside_brackets(text: str) -> list:
    """콤마로 나누되 `[...]` 안의 콤마는 세지 않는다 — 인라인 맵의 목록 값(`composite: {…, ordered: [a, b]}`)."""
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch == "[":
            depth += 1
        elif ch == "]":
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
