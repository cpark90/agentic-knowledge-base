---
id: https://agentic-knowledge-base.dev/id/chunk/8bfec137-25dc-4b30-8a96-8897afc667ad
type: artifact
level: executable
title_ko: 함수 suspect_saturation (tools/kb_lib.py)
title: function suspect_saturation in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `suspect_saturation(g, extra)` 다. suspect 포화율 — 확정 링크 가운데 suspect 로 유도된 것의 비율.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def suspect_saturation(g: Graph, extra: dict | None = None) -> dict:
    """suspect 포화율 — 확정 링크 가운데 suspect 로 유도된 것의 비율. extra 는 `when` 경로의 결과다.

    포화율을 보지 않으면 트리거를 좁힌 것이 맞는지 알 수 없다 (handoff 반영 2). 반환 키:
    confirmed · by_trigger · by_when · suspect · ratio · with_when.
    """
    trig = suspect_by_trigger(g)
    when_side = dict(extra or {})
    union = set(trig) | set(when_side)
    confirmed = len(_confirmed_links(g))
    return {"confirmed": confirmed, "by_trigger": len(trig), "by_when": len(when_side), "suspect": len(union),
            "ratio": (len(union) / confirmed) if confirmed else None,
            "with_when": sum(1 for l, _k, _f, _t in _confirmed_links(g) if (l, AGT.when, None) in g)}
```
<!-- 인용 끝 -->
