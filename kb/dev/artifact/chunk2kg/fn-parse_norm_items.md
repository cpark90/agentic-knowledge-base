---
id: https://agentic-knowledge-base.dev/id/chunk/4eb70032-9c6d-47dc-a0b0-34e02f426e80
type: artifact
level: executable
title_ko: 함수 parse_norm_items (tools/chunk2kg.py)
title: function parse_norm_items in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/9397f206-c8b3-40ab-8fb8-d286bf02749f]
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
---
**함수** — `parse_norm_items(where, items)` 다. 절 청크의 `items` → [{ref: (slug, k), links: [slug…], sub: [{ref, links}…]}].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_norm_items(where: str, items) -> list[dict]:
    """절 청크의 `items` → [{ref: (slug, k), links: [slug…], sub: [{ref, links}…]}]. 형식 밖이면 ValueError.

    판정의 단일 정의처다 — chunk2kg 의 방출(agt:projectsConvention)과 생성기(tools/gen_norms.py)가 같은 함수를 쓴다.
    """
    if not isinstance(items, list):
        raise ValueError(f"{where}: {NORM_ITEMS_KEY} 는 순서 목록 [..] 이어야 한다 — 실제 {items!r}")
    out = []
    for it in items:
        if isinstance(it, dict):
            if set(it) != {NORM_ITEM_MAIN, NORM_ITEM_SUB}:
                raise ValueError(f"{where}: 하위를 가진 항목은 {{{NORM_ITEM_MAIN}: slug#k, {NORM_ITEM_SUB}: [slug#k, …]}} 이다 — "
                                 f"실제 키 {sorted(it)}")
            ref, links = parse_norm_ref(where, it[NORM_ITEM_MAIN])
            subs = it[NORM_ITEM_SUB]
            if not isinstance(subs, list) or not subs:
                raise ValueError(f"{where}: {NORM_ITEM_SUB} 는 비지 않은 목록 [slug#k, …] 이다 — 실제 {subs!r}")
            out.append({"ref": ref, "links": links,
                        "sub": [dict(zip(("ref", "links"), parse_norm_ref(where, x))) for x in subs]})
        else:
            ref, links = parse_norm_ref(where, it)
            out.append({"ref": ref, "links": links, "sub": []})
    return out
```
<!-- 인용 끝 -->
