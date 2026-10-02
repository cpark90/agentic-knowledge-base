---
id: https://agentic-knowledge-base.dev/id/chunk/07104b21-b283-4e54-a921-6b9a61fb6e45
type: artifact
level: executable
title_ko: 함수 check_shacl (tools/validate.py)
title: function check_shacl in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4]
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_shacl(merged, shapes, reason, shape_paths, waivers)` 다. pySHACL 적합성 — 위반마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_shacl(merged: Graph, shapes: Graph, reason: bool, shape_paths: list[str],
                waivers: list[dict] | None = None) -> list[str]:
    """pySHACL 적합성 — 위반마다 focus node 를 파일로 사상해 선언된 면제를 가른다.

    shape 는 약화하지 않는다. 면제의 자리는 `docs/waivers.md` 하나(게이트 id `shacl`, 축 `파일`)이고 면제된
    위반은 집계에서 빼되 `WAIVED [shacl] <파일>: <sh:resultMessage>` 줄로 남긴다 — `chunk_lint` 의 `chunk`
    면제와 같은 규약이다. focus node → 파일은 그래프의 `agt:assertionLocation` 이 정한다.
    """
    from pyshacl import validate as shacl_validate
    from rdflib.namespace import SH

    gate = SHACL
    conforms, report, text = shacl_validate(
        merged,
        shacl_graph=shapes,
        ont_graph=None,
        inference="rdfs" if not reason else "both",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=False,
    )
    if conforms:
        return []
    kept, waived_notes = 0, []
    for result in report.subjects(RDF.type, SH.ValidationResult):
        if next(report.objects(result, SH.resultSeverity), None) == SH.Info:
            continue  # allow_infos=True — 판정에 들지 않는 결과다
        focus = next(report.objects(result, SH.focusNode), None)
        where = _chunk_location(merged, focus) if isinstance(focus, URIRef) else str(focus)
        if waivers and kb_lib.waived(waivers, gate, where, "파일"):
            msg = str(next(report.objects(result, SH.resultMessage), "")).strip()
            waived_notes.append(f"WAIVED [{gate}] {where}: {msg}")
        else:
            kept += 1
    for note in sorted(waived_notes):
        print(f"{note} (waivers.md — 집계에서 뺐다)")
    if not kept:
        return []
    return [f"[{gate}] {', '.join(shape_paths)}: shape 부적합 {kept}건"
            + (f" (면제 {len(waived_notes)}건)" if waived_notes else "")
            + f" — sh:message 가 수정 방향이다\n{text}"]
```
<!-- 인용 끝 -->
