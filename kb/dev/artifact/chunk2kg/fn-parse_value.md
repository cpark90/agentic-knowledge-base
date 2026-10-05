---
id: https://agentic-knowledge-base.dev/id/chunk/03312fa3-ef91-4e77-b39e-47c5554aba7e
type: artifact
level: executable
title_ko: 함수 parse_value (tools/chunk2kg.py)
title: function parse_value in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8c320bc2-87f7-43f5-9492-fe4086b13e7c, https://agentic-knowledge-base.dev/id/chunk/a13334ee-3c25-4384-bac2-a81868a47526]
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `parse_value(val)` 다. key: value 의 값 — 인라인 맵, 목록(스칼라·맵·둘의 섞임), 스칼라.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_value(val: str):
    """key: value 의 값 — 인라인 맵, 목록(스칼라·맵·둘의 섞임), 스칼라.

    목록의 원소는 `{` 로 시작하면 맵, 아니면 스칼라다. 스칼라만의 목록과 맵만의 목록은 옛 판독과 같은 값을 낸다 —
    섞인 목록은 절 키 `items`(`[a#1, {규약: b#2, 하위: [c#1]}]`)가 처음 쓴다.
    """
    if val.startswith("{") and val.endswith("}"):
        return parse_map(val)
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        out = []
        for v in split_top_level(inner):
            v = v.strip()
            if not v:
                continue
            out.append(parse_map(v) if v.startswith("{") and v.endswith("}") else v.strip("'\""))
        return out
    return val.strip("'\"")
```
<!-- 인용 끝 -->
