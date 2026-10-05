---
id: https://agentic-knowledge-base.dev/id/chunk/7ea462e4-8c9b-4768-98eb-df193fcee568
type: artifact
level: executable
title_ko: 함수 body_of (tools/channel_lint.py)
title: function body_of in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6
---
**함수** — `body_of(text)` 다. frontmatter 를 뗀 본문.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_of(text: str) -> str:
    """frontmatter 를 뗀 본문."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end >= 0 else ""
```
<!-- 인용 끝 -->
