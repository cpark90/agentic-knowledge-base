---
id: https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0
type: artifact
level: executable
title_ko: 함수 frontmatter_end (tools/kb_lib.py)
title: function frontmatter_end in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
---
**함수** — `frontmatter_end(lines)` 다. YAML frontmatter 뒤 첫 줄의 0-기준 색인.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def frontmatter_end(lines: list[str]) -> int:
    """YAML frontmatter 뒤 첫 줄의 0-기준 색인. frontmatter 가 없으면 0 이다."""
    if lines and lines[0].strip() == "---":
        try:
            return lines[1:].index("---") + 2
        except ValueError:
            return 0
    return 0
```
<!-- 인용 끝 -->
