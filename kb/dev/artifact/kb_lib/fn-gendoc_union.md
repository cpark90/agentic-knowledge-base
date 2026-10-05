---
id: https://agentic-knowledge-base.dev/id/chunk/63c8b052-77ba-4c50-bc59-9b1fea9e598d
type: artifact
level: executable
title_ko: 함수 gendoc_union (tools/kb_lib.py)
title: function gendoc_union in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0b2c0543-8f0e-4ad8-a18a-eb3da5ff4767, https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20]
part_of: https://agentic-knowledge-base.dev/id/composite/6b2ef1c0-06f1-44c5-9b0f-6ba8a1fedb8d
---
**함수** — `gendoc_union(paths)` 다. 머리 블록의 규모 자리에 붙는 union 구성 — `union: chunks +a · base +b · …` 꼴.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_union(paths) -> str:
    """머리 블록의 규모 자리에 붙는 union 구성 — `union: chunks +a · base +b · …` 꼴. 그래프 파일(`.ttl`)만 센다.

    구성원의 증분은 선언 순서(GENDOC_UNION_MEMBERS, 그 뒤 표에 없는 파일의 stem 순)대로 앞 구성원들의 합집합에 더한
    트리플 수다(유저 답 Q40-a). 호출자가 적재한 그래프의 총수와 증분의 합이 같다 — 게이트 `gendoc` G4 가 판정한다.
    """
    graphs = [p for p in paths if gendoc_input_name(p).endswith(".ttl")]
    groups, matched = [], set()
    for frag, label in GENDOC_UNION_MEMBERS:
        hit = [p for p in graphs if frag in gendoc_input_name(p)]
        if hit:
            groups.append((label, hit))
            matched.update(map(str, hit))
    rest: dict[str, list] = {}
    for p in graphs:
        if str(p) not in matched:
            rest.setdefault(gendoc_input_name(p).rsplit("/", 1)[-1][:-4], []).append(p)
    groups += sorted(rest.items())
    if not groups:
        return "union: " + NONE_MARK
    seen: set = set()
    parts = []
    for label, files in groups:
        before = len(seen)
        unread = False
        for p in files:
            t = _gendoc_graph_triples(p)
            if t is None:
                unread = True
            else:
                seen |= t
        parts.append(f"{label} +{GENDOC_UNION_UNREAD}" if unread else f"{label} +{len(seen) - before}")
    return "union: " + " \u00b7 ".join(parts)
```
<!-- 인용 끝 -->
