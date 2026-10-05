---
id: https://agentic-knowledge-base.dev/id/chunk/030c7af0-5dd1-4541-87a2-47f630beb3cd
type: artifact
level: executable
title_ko: 함수 composite_declarers (tools/metrics.py)
title: function composite_declarers in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0]
part_of: https://agentic-knowledge-base.dev/id/composite/ff0be03b-b931-485c-bbb4-98c897dd6133
---
**함수** — `composite_declarers(bodies)` 다. 복합체 IRI → 선언 청크 IRI.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def composite_declarers(bodies) -> dict:
    """복합체 IRI → 선언 청크 IRI. 청크 파일의 frontmatter 에서 `id:` 와 `composite.id` 를 읽는다."""
    out = {}
    for b_ in bodies:
        if not b_.endswith(".md"):
            continue
        text = Path(b_).read_text(encoding="utf-8")
        lines = text.splitlines()
        head = "\n".join(lines[:kb_lib.frontmatter_end(lines)])
        mi, mc = _FM_ID.search(head), _FM_COMPOSITE.search(head)
        if mi and mc:
            out[URIRef(mc.group(1))] = URIRef(mi.group(1))
    return out
```
<!-- 인용 끝 -->
