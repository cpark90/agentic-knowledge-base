---
id: https://agentic-knowledge-base.dev/id/chunk/7b782704-6d75-4344-9b72-f812f73bbfb0
type: artifact
level: executable
title_ko: 함수 check_line_budget (tools/validate.py)
title: function check_line_budget in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_line_budget(shapes, bzl_path, shape_paths)` 다. 본문 줄 수 상한의 단일 정의처 — shape 가 `kb_lib.BODY_LINE_LIMITS` 와 같은 표인가 (게이트 `line-budget`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_line_budget(shapes: Graph, bzl_path: str, shape_paths: list[str]) -> list[str]:
    """본문 줄 수 상한의 단일 정의처 — shape 가 `kb_lib.BODY_LINE_LIMITS` 와 같은 표인가 (게이트 `line-budget`).

    `residency` 와 같은 형이다. 원본은 파이썬 쪽 표이고(게이트 chunk_lint 가 파일마다 그것으로 판정한다) shape 는
    그것의 RDF 표현이다. plane 은 shape 의 `sh:targetClass` 지역명 `<X>Chunk` 에서 읽는다. plane 목록은
    `defs/kb.bzl` 의 PLANES 이고, 표에 없는 plane 의 상한은 기본 42줄이다 (4.1절).
    `artifact` 만 값이 다르다 — 본문이 저작이 아니라 소스의 인용이기 때문이다 (p7-code-extraction-direction "예산").
    첫 실행(2026-09-30, plane 7): FAIL 0.
    """
    from rdflib.namespace import SH

    gate = kb_lib.LINE_BUDGET_GATE
    where = ", ".join(shape_paths) or bzl_path
    try:
        planes, _levels, _table = kb_lib.load_residency(bzl_path)
    except (OSError, ValueError) as e:
        raise ConfigFailure(f"[{gate}] {bzl_path}: plane 목록을 읽을 수 없다 — {e}") from e
    declared = {p: kb_lib.body_line_limit(p) for p in planes}
    found: dict[str, set[int]] = {}
    for shape, cls in shapes.subject_objects(SH.targetClass):
        plane = str(cls).split("/")[-1]
        if not plane.endswith("Chunk"):
            continue
        plane = plane[: -len("Chunk")].lower()
        for prop in shapes.objects(shape, SH.property):
            if (prop, SH.path, kb_lib.AGT.lineCount) not in shapes:
                continue
            for v in shapes.objects(prop, SH.maxInclusive):
                found.setdefault(plane, set()).add(int(v))
    errors = []
    for plane in sorted(set(declared) | set(found)):
        want, have = declared.get(plane), found.get(plane)
        if want is None:
            errors.append(f"[{gate}] {where}: shape 가 plane {plane} 의 본문 상한을 {sorted(have)} 로 두는데 그런 plane 이 {bzl_path} 의 PLANES 에 없다")
        elif not have:
            errors.append(f"[{gate}] {where}: plane {plane} 의 본문 상한 {want} 에 대응하는 shape 가 없다 — `agt:{plane.capitalize()}Chunk` 의 `agt:lineCount` 에 `sh:maxInclusive {want}` 를 단다 (표의 원본은 tools/kb_lib.py 의 BODY_LINE_LIMITS 다)")
        elif have != {want}:
            errors.append(f"[{gate}] {where}: plane {plane} 의 본문 상한이 갈린다 — tools/kb_lib.py 의 BODY_LINE_LIMITS 는 {want}, shape 는 {sorted(have)} 다. 원본은 표이므로 shape 를 맞춘다")
    return errors
```
<!-- 인용 끝 -->
