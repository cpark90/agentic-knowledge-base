---
id: https://agentic-knowledge-base.dev/id/chunk/7c06245d-1706-4edf-8a20-61ad5b35f1cc
type: artifact
level: executable
title_ko: 함수 _check_scope_subset (tools/validate.py)
title: function _check_scope_subset in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7624f877-e0d3-45fd-b51d-91d72c7cf025
---
**함수** — `_check_scope_subset(merged, odd, files)` 다. (e) 스코프는 ODD 의 부분집합이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _check_scope_subset(merged: Graph, odd: Graph | None, files: dict[str, Graph]) -> list[str]:
    """(e) 스코프는 ODD 의 부분집합이다 (0.4절, scope-ontology agt:subsetOf·agt:includesCondition 의 정의문).

    "ODD에 없는 속성을 참조하는 스코프는 존재할 수 없다" 와 "하네스가 부여하는 스코프는 ODD 의 부분집합이다" 의 실행
    자리다. 지금까지는 `tools/metrics.py` 의 `scope_bad` 지표가 세기만 했다 (2026-09-26 게이트로 승격).
    스코프마다: agt:subsetOf 가 하나 이상이고 그 대상이 ODD 그래프의 agt:ODD 이며 · include/exclude 조건이 그 ODD 에
    agt:hasCondition 으로 등록돼 있다. 첫 실행(2026-09-26, 스코프 4 · 조건 참조 14): FAIL 0.
    """
    AGT_, gate = kb_lib.AGT, kb_lib.CATALOG_GATE
    if odd is None:
        return []
    errors: list[str] = []
    for scope in sorted(s for s in merged.subjects(RDF.type, AGT_.Scope) if isinstance(s, URIRef)):
        where, sq = _where(files, scope), _qname(merged, scope)
        odds = [o for o in merged.objects(scope, AGT_.subsetOf) if isinstance(o, URIRef)]
        if not odds:
            errors.append(f"[{gate}] {where}: 스코프 {sq} 에 agt:subsetOf 가 없다 — 어느 ODD 의 부분집합인지 밝힌다 (0.4절)")
        registered: set[URIRef] = set()
        for o in odds:
            if (o, RDF.type, AGT_.ODD) not in odd:
                errors.append(f"[{gate}] {where}: 스코프 {sq} 의 agt:subsetOf 대상 {_qname(merged, o)} 가 ODD 그래프에 agt:ODD 로 없다 — ODD 를 먼저 확장한다 (0.4절)")
            registered |= {c for c in odd.objects(o, AGT_.hasCondition) if isinstance(c, URIRef)}
        for pred in (AGT_.includesCondition, AGT_.excludesCondition):
            for c in sorted(x for x in merged.objects(scope, pred) if isinstance(x, URIRef)):
                if c not in registered:
                    errors.append(f"[{gate}] {where}: 스코프 {sq} 의 {_qname(merged, pred)} 대상 {_qname(merged, c)} 가 그 ODD 의 agt:hasCondition 목록에 없다 — ODD 밖 조건을 참조하는 스코프는 존재할 수 없다 (0.4절)")
    return errors
```
<!-- 인용 끝 -->
