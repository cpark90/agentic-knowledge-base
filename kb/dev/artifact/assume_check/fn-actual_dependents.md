---
id: https://agentic-knowledge-base.dev/id/chunk/93d9eb93-7d34-4ebf-b871-041a219b6017
type: artifact
level: executable
title_ko: 함수 actual_dependents (tools/assume_check.py)
title: function actual_dependents in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `actual_dependents(root, assumption)` 다. 실제 의존 집합 — 청크 파일의 frontmatter `assumes` 를 그래프와 독립적으로 스캔한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def actual_dependents(root: Path, assumption: str) -> tuple[set, list[str]]:
    """실제 의존 집합 — 청크 파일의 frontmatter `assumes` 를 그래프와 독립적으로 스캔한다 (살아 있는 청크만)."""
    found, unparsable = set(), []
    for d in CHUNK_DIRS:
        for p in sorted((root / d).rglob("*.md")):
            try:
                meta = parse_chunk(str(p))[0]
            except ValueError as e:
                if "frontmatter가 없다" not in str(e):  # frontmatter 없는 md(README)는 청크가 아니다
                    unparsable.append(str(e))
                continue
            if meta.get("status") != "deprecated" and assumption in (meta.get("assumes") or []):
                found.add(URIRef(meta["id"]))
    return found, unparsable
```
<!-- 인용 끝 -->
