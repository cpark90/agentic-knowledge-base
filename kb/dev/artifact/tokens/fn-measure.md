---
id: https://agentic-knowledge-base.dev/id/chunk/84687e20-5870-4ee0-be02-862d00aafbff
type: artifact
level: executable
title_ko: 함수 measure (tools/tokens.py)
title: function measure in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T10:12:42Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee6ebd51-06bf-439a-875f-bf4afa341c35
---
**함수** — `measure(paths, root, enc)` 다. 청크마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def measure(paths: list[Path], root: Path, enc) -> list[dict]:
    """청크마다 (경로, plane, 줄 수, 토큰 수) 한 행.

    본문은 `kb_lib.body_text` 가 뗀다 — 게이트(`chunk_lint`)·방출(`chunk2kg`)과 같은 판정처 하나다. 줄 수는
    그 문자열의 줄 수이고 분포에서 줄당 토큰의 분모로만 쓰인다(크기 규칙은 토큰이다).
    """
    rows = []
    for p in paths:
        text = p.read_text(encoding="utf-8")
        body = kb_lib.body_text(p, text)
        rel = p.relative_to(root).as_posix() if p.is_absolute() else p.as_posix()
        plane = chunk_lint.split_frontmatter(text)[0].get("type", kb_lib.NONE_MARK)
        rows.append({"path": rel, "plane": plane, "lines": len(body.splitlines()),
                     "tokens": len(enc.encode(body))})
    return rows
```
<!-- 인용 끝 -->
