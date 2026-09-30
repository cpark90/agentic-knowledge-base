---
id: https://agentic-knowledge-base.dev/id/chunk/a9138ecc-8714-414e-a8f3-69d0c646e65d
type: artifact
level: executable
title_ko: 함수 slug (tools/kb_lib.py)
title: function slug in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
---
**함수** — `slug(text)` 다. GitHub 제목 앵커 규칙 — 소문자, 공백→'-', 문자·숫자·결합 부호·'-'·'_' 외 제거.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def slug(text: str) -> str:
    """GitHub 제목 앵커 규칙 — 소문자, 공백→'-', 문자·숫자·결합 부호·'-'·'_' 외 제거."""
    text = MD_LINK_TEXT.sub(r"\1", text)
    text = MD_HTML_TAG.sub("", text)
    out = []
    for c in text.lower():
        if c == " ":
            out.append("-")
        elif c in "-_" or c.isalnum() or unicodedata.category(c).startswith("M"):
            out.append(c)
    return "".join(out)
```
<!-- 인용 끝 -->
