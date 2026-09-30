---
id: https://agentic-knowledge-base.dev/id/chunk/7848189e-1a29-4f71-9bab-09f2623ff65f
type: artifact
level: executable
title_ko: 함수 check_residency (tools/validate.py)
title: function check_residency in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_residency(shapes, bzl_path, shape_paths)` 다. 수준 허용표의 단일 정의처 — shape 가 `defs/kb.bzl` 의 `RESIDENCY` 와 같은 표인가 (M1 단일 정의처, 2026-09-26).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_residency(shapes: Graph, bzl_path: str, shape_paths: list[str]) -> list[str]:
    """수준 허용표의 단일 정의처 — shape 가 `defs/kb.bzl` 의 `RESIDENCY` 와 같은 표인가 (M1 단일 정의처, 2026-09-26).

    같은 규칙을 두 곳에 적는 것을 막는다. 원본은 Starlark 쪽 리터럴이다 — Starlark 는 파일을 읽지 못하므로
    분석 시점 판정이 쓰는 표가 원본이어야 하고, shape 는 그것의 RDF 표현이다. plane 은 shape 의
    `sh:targetClass` 지역명 `<X>Chunk` 에서 읽는다(metrics 와 같은 규칙). 표에서 모든 수준을 허용하는 plane
    (annotation)은 구간 제약이 없어야 한다 — 주석은 대상에서 수준을 물려받고 그 판정은 verify 질의가 한다.
    첫 실행(2026-09-26, plane 7 · 구간 제약 6): FAIL 0.
    """
    from rdflib.collection import Collection
    from rdflib.namespace import SH

    gate = kb_lib.RESIDENCY_GATE
    where = ", ".join(shape_paths) or bzl_path
    try:
        _planes, levels, table = kb_lib.load_residency(bzl_path)
    except (OSError, ValueError) as e:
        raise ConfigFailure(f"[{gate}] {bzl_path}: 수준 허용표를 읽을 수 없다 — {e}") from e
    declared = {p: set(v) for p, v in table.items() if set(v) != set(levels)}
    found: dict[str, set[str]] = {}
    for shape, cls in shapes.subject_objects(SH.targetClass):
        plane = str(cls).split("/")[-1]
        if not plane.endswith("Chunk"):
            continue
        plane = plane[: -len("Chunk")].lower()
        for prop in shapes.objects(shape, SH.property):
            if (prop, SH.path, kb_lib.AGT.hasLevel) not in shapes:
                continue
            for lst in shapes.objects(prop, SH["in"]):
                found.setdefault(plane, set()).update(str(v).split("/")[-1] for v in Collection(shapes, lst))
    errors = []
    for plane in sorted(set(declared) | set(found)):
        want, have = declared.get(plane), found.get(plane)
        if want is None:
            errors.append(f"[{gate}] {where}: shape 가 plane {plane} 의 수준 구간을 {sorted(have)} 로 제한하는데 {bzl_path} 의 RESIDENCY 에는 그 제한이 없다 — 표의 원본은 {bzl_path} 다")
        elif have is None:
            errors.append(f"[{gate}] {where}: {bzl_path} 의 RESIDENCY 는 plane {plane} 을 {sorted(want)} 로 제한하는데 shape 에 대응 구간이 없다 — `agt:{plane.capitalize()}Chunk` 의 `agt:hasLevel` 에 `sh:in` 을 단다")
        elif want != have:
            errors.append(f"[{gate}] {where}: plane {plane} 의 수준 구간이 갈린다 — {bzl_path} 는 {sorted(want)}, shape 는 {sorted(have)} 다. 원본은 {bzl_path} 이므로 shape 를 맞춘다")
    return errors
```
<!-- 인용 끝 -->
