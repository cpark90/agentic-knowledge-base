---
id: https://agentic-knowledge-base.dev/id/chunk/53b29448-345d-4abe-b57a-44a8f6ed1d5d
type: artifact
level: executable
title_ko: 함수 load_bodies (tools/weave.py)
title: function load_bodies in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/1a6c538a-b92e-4130-b298-48a8fe030574
---
**함수** — `load_bodies(paths)` 다. 청크 파일들 → {IRI: 본문} — frontmatter 는 chunk2kg 의 파서로 읽고 본문은 그 아래 전부.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_bodies(paths: list[str]) -> dict:
    """청크 파일들 → {IRI: 본문} — frontmatter 는 chunk2kg 의 파서로 읽고 본문은 그 아래 전부."""
    out = {}
    for p in paths:
        if not p.endswith(".md"):
            continue
        meta, _ = parse_chunk(p)
        out[meta["id"]] = kb_lib.chunk_body(Path(p).read_text(encoding="utf-8"))
    return out
```
<!-- 인용 끝 -->
