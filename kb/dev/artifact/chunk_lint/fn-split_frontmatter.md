---
id: https://agentic-knowledge-base.dev/id/chunk/b61b3d07-041e-43c2-bb5d-cf3239db7602
type: artifact
level: executable
title_ko: 함수 split_frontmatter (tools/chunk_lint.py)
title: function split_frontmatter in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118
---
**함수** — `split_frontmatter(text)` 다. (frontmatter 의 type·status, 본문 줄들, 본문 첫 줄의 파일 줄 번호).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def split_frontmatter(text: str) -> tuple[dict[str, str], list[str], int]:
    """(frontmatter 의 type·status, 본문 줄들, 본문 첫 줄의 파일 줄 번호). frontmatter 가 없으면 본문은 전체다."""
    lines = text.splitlines()
    fields: dict[str, str] = {}
    if not lines or lines[0].strip() != "---":
        return fields, lines, 1
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return fields, lines, 1
    for raw in lines[1:end]:
        m = _FM_FIELD.match(raw)
        if m:
            fields[m.group(1)] = m.group(2)
        m = _FM_GENERATED_BY.match(raw)
        if m:
            fields["generated.by"] = m.group(1)
    return fields, lines[end + 1 :], end + 2
```
<!-- 인용 끝 -->
