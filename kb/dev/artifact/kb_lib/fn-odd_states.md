---
id: https://agentic-knowledge-base.dev/id/chunk/9a2cd33a-ee49-4782-81c9-519aaf5a1621
type: artifact
level: executable
title_ko: 함수 odd_states (tools/kb_lib.py)
title: function odd_states in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/749019ce-0d81-4c5f-b549-f44c1b0d4e55
---
**함수** — `odd_states(cond_rows)` 다. odd_check.judge_all 의 행들 → when_eval 이 읽는 상태 맵.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def odd_states(cond_rows: list) -> dict:
    """odd_check.judge_all 의 행들 → when_eval 이 읽는 상태 맵. 한 조건을 네 이름으로 넣는다 — ODD 속성명 ·
    조건 슬러그 · `id:` 축약 · 조건 IRI 전체. 판정 자체는 odd_check 가 하고 여기서 다시 하지 않는다."""
    states: dict = {}
    for r in cond_rows:
        iri = str(r.get("iri") or "")
        slug = iri.split("/")[-1] if iri else ""
        for key in (r.get("name"), slug, ("id:" + slug) if slug else "", iri):
            if key:
                states[key] = r["state"]
    return states
```
<!-- 인용 끝 -->
