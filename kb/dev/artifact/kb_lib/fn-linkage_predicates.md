---
id: https://agentic-knowledge-base.dev/id/chunk/c15db5ea-e132-44e3-b82c-929369970f50
type: artifact
level: executable
title_ko: 함수 linkage_predicates (tools/kb_lib.py)
title: function linkage_predicates in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/e7a31401-e48b-4980-aece-491ec241ffe6
---
**함수** — `linkage_predicates(g)` 다. 연결 성분이 보는 술어 — `LINKAGE_PREDICATES` 에 세 족(`agt:dependsOn` 아래)의 잎을 T-Box 에서 더한 집합이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def linkage_predicates(g: Graph) -> tuple:
    """연결 성분이 보는 술어 — `LINKAGE_PREDICATES` 에 세 족(`agt:dependsOn` 아래)의 잎을 T-Box 에서 더한 집합이다.

    족은 `rdfs:subPropertyOf` 로 정의되므로(p10-link-families) 고정 목록만 보면 새 잎이 성분에서 빠진다 — 실측
    2026-10-04: 절 청크의 `agt:projectsConvention`(⊑ `agt:references`)이 빠져 성분 26. 그래서 하위 속성을 전이적으로
    따라간다. T-Box 가 입력에 없으면(`agt:dependsOn` 의 하위가 없으면) 조용히 고정 목록으로 줄지 않고 죽는다.
    """
    seen, stack = set(), [AGT.dependsOn]
    while stack:
        for s in g.subjects(RDFS.subPropertyOf, stack.pop()):
            if s not in seen:
                seen.add(s); stack.append(s)
    if not seen:
        raise SystemExit("linkage_predicates: agt:dependsOn 의 하위 속성이 그래프에 없다 — 온톨로지 모듈을 입력으로 준다")
    return LINKAGE_PREDICATES + tuple(sorted(seen - set(LINKAGE_PREDICATES), key=str))
```
<!-- 인용 끝 -->
