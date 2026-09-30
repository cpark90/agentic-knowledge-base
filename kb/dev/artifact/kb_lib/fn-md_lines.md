---
id: https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898
type: artifact
level: executable
title_ko: 함수 md_lines (tools/kb_lib.py)
title: function md_lines in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0]
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
---
**함수** — `md_lines(lines)` 다. (줄 번호, 줄) — 코드 펜스·frontmatter·HTML 주석 안은 산문이 아니므로 건너뛴다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def md_lines(lines: list[str]):
    """(줄 번호, 줄) — 코드 펜스·frontmatter·HTML 주석 안은 산문이 아니므로 건너뛴다."""
    fence: str | None = None
    in_comment = False
    start = frontmatter_end(lines)
    for i, line in enumerate(lines[start:], start=start + 1):
        if in_comment:
            if "-->" in line:
                in_comment = False
                line = line.split("-->", 1)[1]
            else:
                continue
        m = MD_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        if "<!--" in line:
            head, _, tail = line.partition("<!--")
            if "-->" in tail:
                line = head + tail.split("-->", 1)[1]
            else:
                in_comment = True
                line = head
        yield i, line
```
<!-- 인용 끝 -->
