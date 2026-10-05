---
id: https://agentic-knowledge-base.dev/id/chunk/a8f0dd40-2e94-4fef-91a8-971850c9f957
type: artifact
level: executable
title_ko: 함수 render_list (tools/gen_norms.py)
title: function render_list in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/09837757-c9d0-4b9d-ab1e-d1c73b0116ec, https://agentic-knowledge-base.dev/id/chunk/d0952dad-2a90-465f-bce8-0789223da6e8]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `render_list(s, conventions, out)` 다. 목록 묶음 — bullets 는 `-`, ordered 는 항목마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_list(s: dict, conventions: dict, out: str) -> list[str]:
    """목록 묶음 — bullets 는 `-`, ordered 는 항목마다 `1.`(목록 규칙). 하위 항목은 상위 표지의 폭만큼 들여 같은 표지로 낸다."""
    marker = "1." if form_of(s) == "ordered" else "-"
    indent = " " * (len(marker) + 1)
    lines = []
    for it in s.get("_norm_items") or []:
        lines.append(render_item(it, conventions, out, marker=marker))
        lines += [render_item(x, conventions, out, indent, marker) for x in it["sub"]]
    return lines
```
<!-- 인용 끝 -->
