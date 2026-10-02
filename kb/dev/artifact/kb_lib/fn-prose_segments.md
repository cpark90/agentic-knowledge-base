---
id: https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53
type: artifact
level: executable
title_ko: 함수 prose_segments (tools/kb_lib.py)
title: function prose_segments in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/99dbbf72-57fc-4b1b-91bd-ef07be848f6e
---
**함수** — `prose_segments(text)` 다. (줄 번호, 산문 조각) — frontmatter·코드 펜스·코드 스팬·HTML 주석·따옴표 안을 뺀 나머지.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def prose_segments(text: str) -> list[tuple[int, str]]:
    """(줄 번호, 산문 조각) — frontmatter·코드 펜스·코드 스팬·HTML 주석·따옴표 안을 뺀 나머지.

    표 셀·불릿·제목은 산문으로 남긴다. 뺀 자리는 공백 하나로 메워 앞뒤 낱말이 붙지 않게 한다. 빈 조각은 내지 않는다.
    """
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        try:
            start = lines[1:].index("---") + 2
        except ValueError:
            start = 0
    out: list[tuple[int, str]] = []
    fence: str | None = None
    in_comment = False
    for i, line in enumerate(lines[start:], start=start + 1):
        if in_comment:
            if "-->" not in line:
                continue
            in_comment = False
            line = line.split("-->", 1)[1]
        m = _MD_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        while "<!--" in line:
            head, _, tail = line.partition("<!--")
            if "-->" in tail:
                line = head + " " + tail.split("-->", 1)[1]
            else:
                in_comment = True
                line = head
        line = _MD_CODE_SPAN.sub(" ", line)
        line = _MD_QUOTED.sub(" ", line)
        if line.strip():
            out.append((i, line))
    return out
```
<!-- 인용 끝 -->
