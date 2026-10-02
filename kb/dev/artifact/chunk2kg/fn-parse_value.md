---
id: https://agentic-knowledge-base.dev/id/chunk/03312fa3-ef91-4e77-b39e-47c5554aba7e
type: artifact
level: executable
title_ko: 함수 parse_value (tools/chunk2kg.py)
title: function parse_value in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8c320bc2-87f7-43f5-9492-fe4086b13e7c]
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `parse_value(val)` 다. key: value 의 값 — 인라인 맵, 목록(스칼라 또는 맵), 스칼라.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_value(val: str):
    """key: value 의 값 — 인라인 맵, 목록(스칼라 또는 맵), 스칼라."""
    if val.startswith("{") and val.endswith("}"):
        return parse_map(val)
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if inner.startswith("{"):
            return [parse_map(m) for m in re.findall(r"\{[^{}]*\}", inner)]
        return [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
    return val.strip("'\"")
```
<!-- 인용 끝 -->
