---
id: https://agentic-knowledge-base.dev/id/chunk/d467ebd7-021e-4d5f-affe-f3e483fbfa17
type: artifact
level: executable
title_ko: 함수 body_lines (tools/chunk_lint.py)
title: function body_lines in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7b250e22-fd3e-4d64-9b95-214bd55ce9d3
---
**함수** — `body_lines(path, text)` 다. 본문 줄 수.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_lines(path: Path, text: str) -> int:
    """본문 줄 수. head에 해당하는 것(md frontmatter, ttl의 @prefix·주석)은 세지 않는다."""
    lines = text.splitlines()
    if path.suffix == ".ttl":
        return sum(
            1
            for l in lines
            if l.strip() and not l.lstrip().startswith(("#", "@prefix", "@base"))
        )
    # 산문 계열: frontmatter 제거
    if lines and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
            lines = lines[end + 1 :]
        except ValueError:
            pass
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return len(lines)
```
<!-- 인용 끝 -->
