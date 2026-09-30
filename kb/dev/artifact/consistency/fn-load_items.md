---
id: https://agentic-knowledge-base.dev/id/chunk/73948788-1cde-4993-859e-695091f31e4f
type: artifact
level: executable
title_ko: 함수 load_items (tools/consistency.py)
title: function load_items in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/c10c407c-9993-4ba9-a09f-bfdc6e910b5e
---
**함수** — `load_items(paths)` 다. 청크 경로 → 살아 있는 항목 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_items(paths):
    """청크 경로 → 살아 있는 항목 목록. 파싱 실패는 ValueError 로 올라가 main 이 CONFIG 로 바꾼다."""
    items = []
    for p in paths:
        if not p.endswith(".md"):
            continue
        meta, n = parse_chunk(p)
        if meta.get("status") not in LIVE:
            continue
        items.append({"path": p, "id": meta["id"], "type": meta["type"], "level": meta["level"],
                      "title_ko": str(meta.get("title_ko", "")), "title": str(meta.get("title", "")),
                      "hash": meta["_content_hash"], "body": body_of(p), "lines": n,
                      "co": set(meta.get("coUpdatesWith", []) or []), "slots": meta.get("_body_slots", [])})
    return items
```
<!-- 인용 끝 -->
