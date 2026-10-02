---
id: https://agentic-knowledge-base.dev/id/chunk/2b38088c-7807-429a-a6df-e08e9a052e3a
type: artifact
level: executable
title_ko: 함수 listing (tools/consistency.py)
title: function listing in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e33ee826-0842-4cdd-8e68-16823604cffa
---
**함수** — `listing(hits, limit, render)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def listing(hits, limit, render):
    out = [render(h) for h in hits[:limit]] or [f"- {kb_lib.NONE_MARK}"]
    return out + ([f"- … {len(hits) - limit}건 더"] if len(hits) > limit else [])
```
<!-- 인용 끝 -->
