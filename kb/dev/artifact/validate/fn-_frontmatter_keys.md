---
id: https://agentic-knowledge-base.dev/id/chunk/2dd75424-2fca-48ab-9dbb-17d3b0c71ea1
type: artifact
level: executable
title_ko: 함수 _frontmatter_keys (tools/validate.py)
title: function _frontmatter_keys in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/621b8722-ef63-42b3-8470-9560e072a62a
---
**함수** — `_frontmatter_keys(path)` 다. 청크 파일의 최상위 frontmatter 키 — 중첩 키(`composite.ordered` 등)는 그 부모가 대표한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _frontmatter_keys(path: str) -> set[str]:
    """청크 파일의 최상위 frontmatter 키 — 중첩 키(`composite.ordered` 등)는 그 부모가 대표한다."""
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return set()
    return {m.group(1) for m in (_FM_KEY.match(l) for l in text.split("---\n", 2)[1].splitlines()) if m}
```
<!-- 인용 끝 -->
