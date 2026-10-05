---
id: https://agentic-knowledge-base.dev/id/chunk/b8f959c8-3cb6-443b-828c-c3952f8b8020
type: artifact
level: executable
title_ko: 함수 view_slug (tools/gates2kg.py)
title: function view_slug in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1
---
**함수** — `view_slug(label)` 다. 뷰 타깃 라벨 → IRI 꼬리 — `//kb/dev:adr` → `kb-dev-adr`.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def view_slug(label: str) -> str:
    """뷰 타깃 라벨 → IRI 꼬리 — `//kb/dev:adr` → `kb-dev-adr`."""
    return label.lstrip("/").replace("/", "-").replace(":", "-").replace("_", "-")
```
<!-- 인용 끝 -->
