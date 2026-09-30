---
id: https://agentic-knowledge-base.dev/id/chunk/8c320bc2-87f7-43f5-9492-fe4086b13e7c
type: artifact
level: executable
title_ko: 함수 parse_map (tools/chunk2kg.py)
title: function parse_map in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `parse_map(text)` 다. 인라인 맵 {k: v, k: v} — 값에 콜론이 없다는 전제.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_map(text: str) -> dict:
    """인라인 맵 {k: v, k: v} — 값에 콜론이 없다는 전제. 값이 `[...]` 면 목록으로 읽는다(`ordered`)."""
    out = {}
    for part in split_outside_brackets(text.strip().strip("{}")):
        if not part.strip():
            continue
        k, _, v = part.partition(":")
        v = v.strip()
        out[k.strip()] = parse_value(v) if v.startswith("[") else v.strip("'\"")
    return out
```
<!-- 인용 끝 -->
