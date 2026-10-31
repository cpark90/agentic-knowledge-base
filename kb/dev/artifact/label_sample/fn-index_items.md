---
id: https://agentic-knowledge-base.dev/id/chunk/db984d6d-3345-4aed-bb9c-6fb4465d7923
type: artifact
level: executable
title_ko: 함수 index_items (tools/label_sample.py)
title: function index_items in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `index_items(root)` 다. 단위 지식 IRI → 워크스페이스 상대 경로 (kb/ 아래 .md 의 frontmatter `id`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def index_items(root: Path) -> dict[str, str]:
    """단위 지식 IRI → 워크스페이스 상대 경로 (kb/ 아래 .md 의 frontmatter `id`)."""
    out = {}
    for f in sorted((root / "kb").rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        m = _ID_LINE.search(text.split("---", 2)[1])
        if m:
            out[m.group(1)] = f.relative_to(root).as_posix()
    return out
```
<!-- 인용 끝 -->
