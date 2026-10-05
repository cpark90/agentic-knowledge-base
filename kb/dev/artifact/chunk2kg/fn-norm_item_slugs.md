---
id: https://agentic-knowledge-base.dev/id/chunk/8c16b743-c8b1-4799-9c5b-5b003686ac07
type: artifact
level: executable
title_ko: 함수 norm_item_slugs (tools/chunk2kg.py)
title: function norm_item_slugs in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
---
**함수** — `norm_item_slugs(parsed, links)` 다. 항목이 가리키는 결정 slug — 정렬, 중복 없음.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def norm_item_slugs(parsed: list[dict], links: bool = True) -> list[str]:
    """항목이 가리키는 결정 slug — 정렬, 중복 없음. `links` 가 거짓이면 줄을 싣는 결정만이다(링크만 하는 `+ slug2` 를 뺀다).

    줄을 싣는 결정이 agt:projectsConvention 의 대상이다 — 링크만 하는 결정은 그 절에 문장을 싣지 않는다.
    """
    out = set()
    for it in parsed:
        for x in [it] + it["sub"]:
            out.add(x["ref"][0])
            if links:
                out.update(x["links"])
    return sorted(out)
```
<!-- 인용 끝 -->
