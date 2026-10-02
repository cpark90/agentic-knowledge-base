---
id: https://agentic-knowledge-base.dev/id/chunk/e7c83ee2-f6d7-442d-98f1-d053996cdfd4
type: artifact
level: executable
title_ko: 함수 links_of (tools/revalidate.py)
title: function links_of in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68
---
**함수** — `links_of(meta)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def links_of(meta: dict) -> list:
    out = [(k, t) for k in LINK_KEYS for t in (meta.get(k) or [])]
    if meta.get("part_of"):
        out.append(("part_of", meta["part_of"]))
    return out
```
<!-- 인용 끝 -->
