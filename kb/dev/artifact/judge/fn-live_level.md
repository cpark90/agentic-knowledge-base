---
id: https://agentic-knowledge-base.dev/id/chunk/7942fad8-bbd8-417d-840d-f33c6f00af3b
type: artifact
level: executable
title_ko: 함수 live_level (tools/judge.py)
title: function live_level in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `live_level(into, where, iri)` 다. `into` 저장소에서 `iri` 가 살아 있는 단위 지식이면 그 수준, 아니면 None 이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def live_level(into: Path, where: dict[str, str], iri: str) -> str | None:
    """`into` 저장소에서 `iri` 가 살아 있는 단위 지식이면 그 수준, 아니면 None 이다.

    살아 있는 단위 지식은 `into/kb/` 아래 단위 지식 파일의 frontmatter `id` 가 `iri` 이고(색인 `where` — label_sample.index_items)
    status 가 `kb_lib.LIVE_STATES`(draft·stable·suspect)인 것이다. 묘비(agt:Tombstone — 대체되어 파일을 지운 옛 IRI, chunk2kg.tombstones)는
    파일이 없어 색인에 없고, invalidated·deprecated 는 기록이지 살아 있는 단위 지식이 아니다. 그래프 빌드를 입력으로 삼지 않는다 — 파일만 훑는다.
    """
    rel = where.get(iri)
    if rel is None:
        return None
    try:
        meta, _ = parse_chunk(str(into / rel))
    except (OSError, ValueError):
        return None
    if meta.get("status") not in kb_lib.LIVE_STATES:
        return None
    return meta.get("level") or None
```
<!-- 인용 끝 -->
