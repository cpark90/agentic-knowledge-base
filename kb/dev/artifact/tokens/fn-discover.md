---
id: https://agentic-knowledge-base.dev/id/chunk/132c7aa3-afb6-446f-be54-deeaff4e3460
type: artifact
level: executable
title_ko: 함수 discover (tools/tokens.py)
title: function discover in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T11:03:13Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee6ebd51-06bf-439a-875f-bf4afa341c35
---
**함수** — `discover(root)` 다. 인자가 없을 때의 대상 — 청크 디렉토리의 frontmatter 있는 `.md` 와 저작 접미의 `.ttl` 전부다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def discover(root: Path) -> list[Path]:
    """인자가 없을 때의 대상 — 청크 디렉토리의 frontmatter 있는 `.md` 와 저작 접미의 `.ttl` 전부다 (경로 정렬).

    분모는 **게이트가 판정하는 전 청크**여야 한다 — `chunk_lint` 는 `.md` 와 `.ttl` 을 같은 상한으로 보므로
    온톨로지 모듈·shape 도 여기 든다 (2026-10-01 정정).
    """
    out = []
    for d in CHUNK_ROOTS:
        for p in sorted((root / d).rglob("*.md")):
            if p.read_text(encoding="utf-8").startswith("---\n"):
                out.append(p)
        for p in sorted((root / d).rglob("*.ttl")):
            if p.stem.endswith(TTL_CHUNK_SUFFIXES):
                out.append(p)
    return sorted(out, key=lambda p: p.as_posix())
```
<!-- 인용 끝 -->
