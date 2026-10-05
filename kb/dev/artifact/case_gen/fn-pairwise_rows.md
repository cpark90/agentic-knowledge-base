---
id: https://agentic-knowledge-base.dev/id/chunk/eb42f99d-692f-408e-b9bc-496776333330
type: artifact
level: executable
title_ko: 함수 pairwise_rows (tools/case_gen.py)
title: function pairwise_rows in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `pairwise_rows(keep, vs)` 다. t=2 조합 — 값 곱을 순서대로 훑어 아직 덮이지 않은 쌍을 덮는 행만 고른다(결정론적 탐욕).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pairwise_rows(keep: dict, vs: list[str]) -> list[dict]:
    """t=2 조합 — 값 곱을 순서대로 훑어 아직 덮이지 않은 쌍을 덮는 행만 고른다(결정론적 탐욕). 모든 쌍이 덮인다."""
    domains = [list(keep[v]["values"]) + list(keep[v].get("reject", [])) for v in vs]
    need = {(i, a, j, b) for i, j in itertools.combinations(range(len(vs)), 2) for a in map(str, domains[i]) for b in map(str, domains[j])}
    rows = []
    for combo in itertools.product(*domains):
        pairs = {(i, str(combo[i]), j, str(combo[j])) for i, j in itertools.combinations(range(len(vs)), 2)}
        if pairs & need:
            need -= pairs
            rows.append(dict(zip(vs, combo)))
        if not need:
            break
    return rows
```
<!-- 인용 끝 -->
