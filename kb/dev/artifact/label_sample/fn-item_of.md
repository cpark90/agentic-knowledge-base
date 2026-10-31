---
id: https://agentic-knowledge-base.dev/id/chunk/a614648d-b67b-4026-ba49-0d8fa41d0a09
type: artifact
level: executable
title_ko: 함수 item_of (tools/label_sample.py)
title: function item_of in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/38526768-723a-44ce-a114-eb98395d5c68]
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `item_of(root, path)` 다. 판정지에 보일 항목 — 경로·IRI·라벨(ko/en)·파일 단위 본문.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def item_of(root: Path, path: str) -> dict:
    """판정지에 보일 항목 — 경로·IRI·라벨(ko/en)·파일 단위 본문. 같은 경로는 한 번만 읽는다."""
    if path in _ITEMS:
        return dict(_ITEMS[path])
    meta, _ = parse_chunk(str(root / path))
    _ITEMS[path] = {"path": path, "id": meta["id"], "title_ko": str(meta.get("title_ko", "")), "title": str(meta.get("title", "")),
            "body": body_of(str(root / path))}
    return dict(_ITEMS[path])
```
<!-- 인용 끝 -->
