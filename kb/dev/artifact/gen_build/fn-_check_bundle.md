---
id: https://agentic-knowledge-base.dev/id/chunk/816a1348-352c-462d-bbb0-ad267befb0d9
type: artifact
level: executable
title_ko: 함수 _check_bundle (tools/gen_build.py)
title: function _check_bundle in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/569c6e75-e264-4981-bf0b-bba156b541c8
---
**함수** — `_check_bundle(comp_iri, dlab, labs, items, pkg, member_labs, child_comps, decl)` 다. 복합체 하나의 생성 시점 거부 — 패키지 밖 부분·부분 수·동질성·선언된 순서.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _check_bundle(comp_iri, dlab, labs, items, pkg, member_labs, child_comps, decl):
    """복합체 하나의 생성 시점 거부 — 패키지 밖 부분·부분 수·동질성·선언된 순서. 직접 부분 IRI 를 선언된 순서로 돌려준다.

    부분은 둘이다 — 청크(최상위 `part_of`)와 다른 복합체(선언 청크의 `composite.part_of`, p4-composite-as-part-of).
    동질성은 청크 부분으로 판정한다: 복합체 부분의 plane·level 은 그 부분의 부분에서 나오고 묶음 전체가 한 쌍이므로 같은 판정이다.
    """
    for l in labs:
        if items[l]["pkg"] != pkg:
            raise GenBuildError(f"{items[l]['pkg']}/{items[l]['src']}: 복합체 {comp_iri} 의 선언은 {pkg} 에 있다 — 부분과 선언은 같은 "
                                f"패키지여야 한다 (묶음 = 액션의 입력 집합, defs/kb.bzl kb_composite)")
    chunk_parts = sorted(member_labs)
    chunk_iris = [items[l]["meta"]["id"] for l in chunk_parts]
    n = len(chunk_iris) + len(child_comps)
    if n < 2:
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 부분이 {n}개다 — 복합체는 부분 둘 이상의 "
                            f"묶음이고 부분 하나면 청크다 (4.5절)")
    if n > MAX_PARTS:
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 직접 부분이 {n}개다 — 최대 {MAX_PARTS}개(7±2, 4.5절)")
    order = (items[dlab]["meta"].get("composite") or {}).get(ORDERED_KEY)
    if order is None and pkg == SCENARIO_PKG and any(
            Path(items[l]["src"]).stem.endswith("-" + suf) for l in chunk_parts for suf in SCENARIO_ROLE_SUFFIXES):
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 에 composite.{ORDERED_KEY} 가 없다 — 시나리오는 "
                            f"자극 → 요인 → 배제 자극의 읽기 순서를 가지므로(p8-scenario-authoring) 선언 없는 시나리오 묶음은 거짓 "
                            f"무순서다. 선언 청크(`-{SCENARIO_ROLE_SUFFIXES[0]}`)의 composite: 에 "
                            f"`{ORDERED_KEY}: [<자극 IRI>, <요인 IRI>, <배제 자극 IRI>]` 를 적는다 (p4-composite-order-is-declared)")
    part_iris = chunk_iris + sorted(child_comps)
    if order is not None:
        if sorted(order) != sorted(part_iris):
            raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 composite.{ORDERED_KEY} 가 부분 집합과 다르다 — "
                                f"선언 {sorted(order)} · 부분 {sorted(part_iris)}. 순서 목록은 부분 전부를 "
                                f"빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared)")
        part_iris = sorted(part_iris, key=order.index)
    planes = sorted({items[l]["meta"]["type"] for l in chunk_parts})
    levels = sorted({items[l]["meta"]["level"] for l in chunk_parts})
    if len(planes) > 1 or len(levels) > 1:
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 부분이 이질이다 — plane {planes} · level {levels}. "
                            f"부분의 plane·level 은 서로 같다 (동질성 4.5절). 수준 혼합은 결정 복합체의 예외뿐이다 "
                            f"(p7-decision-spans-three-levels)")
    return part_iris
```
<!-- 인용 끝 -->
