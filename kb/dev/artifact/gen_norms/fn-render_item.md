---
id: https://agentic-knowledge-base.dev/id/chunk/09837757-c9d0-4b9d-ab1e-d1c73b0116ec
type: artifact
level: executable
title_ko: 함수 render_item (tools/gen_norms.py)
title: function render_item in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/082fbbdd-904c-4476-b773-8ebe8a85418e, https://agentic-knowledge-base.dev/id/chunk/516aa2b9-e91a-4519-9bdd-e579b651a443, https://agentic-knowledge-base.dev/id/chunk/8db23029-817e-4897-aa0b-a3c9b3d966e0]
part_of: https://agentic-knowledge-base.dev/id/composite/85f4907d-b39a-4898-8cf9-888cf6204fb4
---
**함수** — `render_item(x, conventions, out, indent, marker)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_item(x: dict, conventions: dict, out: str, indent: str = "", marker: str = "-") -> str:
    slug, k = x["ref"]
    strength, text = conventions[slug]["lines"][k - 1]
    text = rebase_links(text, conventions[slug]["path"], out)
    body = with_links(text, [decision_link(s, out) for s in [slug] + x["links"]])
    return f"{indent}{marker} " + (f"**[{strength}]** " if strength else "") + body
```
<!-- 인용 끝 -->
