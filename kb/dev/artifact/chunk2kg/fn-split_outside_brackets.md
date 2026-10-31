---
id: https://agentic-knowledge-base.dev/id/chunk/71a80c9a-cb89-49ce-ae62-9d1fda16125b
type: artifact
level: executable
title_ko: 함수 split_outside_brackets (tools/chunk2kg.py)
title: function split_outside_brackets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `split_outside_brackets(text)` 다. 콤마로 나누되 `[...]` 안과 큰따옴표 안의 콤마는 세지 않는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def split_outside_brackets(text: str) -> list:
    """콤마로 나누되 `[...]` 안과 큰따옴표 안의 콤마는 세지 않는다 — 인라인 맵의 목록 값(`composite: {…, ordered: [a, b]}`)과
    콤마가 든 라벨 값(묘비 선언의 `title: "A, B"`, Q-0061#Q146)."""
    parts, depth, cur, quoted = [], 0, [], False
    for ch in text:
        if ch == '"':
            quoted = not quoted
        elif quoted:
            pass
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        if ch == "," and depth <= 0 and not quoted:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return parts
```
<!-- 인용 끝 -->
