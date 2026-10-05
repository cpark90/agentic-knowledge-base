---
id: https://agentic-knowledge-base.dev/id/chunk/2d62de0c-4e57-4e6c-ba4e-85fe1ebdc37f
type: artifact
level: executable
title_ko: 함수 chunk_types (tools/term_propose.py)
title: function chunk_types in tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0]
part_of: https://agentic-knowledge-base.dev/id/composite/3eff15a8-c6b8-46a9-a707-b95a948c619d
---
**함수** — `chunk_types(repo)` 다. 청크 IRI → frontmatter `type` (kb/ 아래 Markdown 청크).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def chunk_types(repo: Path) -> dict[str, str]:
    """청크 IRI → frontmatter `type` (kb/ 아래 Markdown 청크)."""
    out = {}
    for f in (repo / "kb").rglob("*.md"):
        lines = f.read_text(encoding="utf-8").splitlines()
        fm = lines[1:kb_lib.frontmatter_end(lines) - 1]
        meta = dict(ln.split(":", 1) for ln in fm if re.match(r"^(id|type):", ln))
        if "id" in meta:
            out[meta["id"].strip()] = meta.get("type", "").strip()
    return out
```
<!-- 인용 끝 -->
