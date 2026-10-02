---
id: https://agentic-knowledge-base.dev/id/chunk/9d1171df-d5e6-4602-9c49-05605607011c
type: artifact
level: executable
title_ko: 함수 check_writer (tools/validate.py)
title: function check_writer in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2c101d4c-b9a7-473c-8c02-5f4de0bbec74, https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4, https://agentic-knowledge-base.dev/id/chunk/b20316b8-e52e-4c0b-8208-f80ef26cec99]
part_of: https://agentic-knowledge-base.dev/id/composite/7624f877-e0d3-45fd-b51d-91d72c7cf025
---
**함수** — `check_writer(merged)` 다. 생성자의 쓰기 권한 (AGENTS 표 · kg/catalog-kg.ttl agt:writesIn·agt:writes) — write plane 경계를 규약에서 기계 검사로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_writer(merged: Graph) -> list[str]:
    """생성자의 쓰기 권한 (AGENTS 표 · kg/catalog-kg.ttl agt:writesIn·agt:writes) — write plane 경계를 규약에서 기계 검사로.

    generated.by 가 `<역할>/<모델>` 이면 그 역할이 청크의 KB 와 plane 을 쓸 수 있어야 한다. KB 는 청크의 assertionLocation 으로
    가른다(kb_lib.kb_of — kb/vv/ 아래면 V&V KB, 아니면 개발 KB) 그리고 역할의 KB 는 agt:writesIn(없으면 kb/dev)이다 (p8-vv-roles,
    2026-09-19). 못 쓰는 역할(hci)이 만든 청크는 같은 KB·plane 의 쓰기 권한이 있는 역할의 verified(인수)가 있어야 통과한다.
    역할이 아닌 생성자(`claude/…`·`process:…`)는 검사하지 않는다.
    """
    AGT = kb_lib.AGT
    gate = kb_lib.WRITER_GATE
    roles = {str(r).split("/")[-1].replace(kb_lib.ROLE_ID_PREFIX, ""): r for r in merged.subjects(RDF.type, AGT.Role)}

    def can_write(role: URIRef, kb: str, plane_cls: URIRef) -> bool:
        return kb in _writes_in(merged, role) and (role, AGT.writes, plane_cls) in merged

    errors, unattributed = [], 0
    for chunk, by in merged.subject_objects(AGT.generatedBy):
        producer = str(by).split("/")[0]
        if producer not in roles:
            unattributed += 1
            continue
        plane_cls = next((c for c in merged.objects(chunk, RDF.type) if str(c).endswith("Chunk")), None)
        if plane_cls is None:
            continue
        where = _chunk_location(merged, chunk)
        kb = kb_lib.kb_of(where)
        if can_write(roles[producer], kb, plane_cls):
            continue
        endorsed = any(str(v).split("/")[0] in roles and can_write(roles[str(v).split("/")[0]], kb, plane_cls)
                       for v in merged.objects(chunk, AGT.verifiedBy))
        if not endorsed:
            errors.append(f"[{gate}] {where}: 생성자 {by} 의 역할 {producer} 는 KB {kb} 의 {str(plane_cls).split('/')[-1]} 쓰기 권한이 없다 "
                          f"(agt:writesIn · agt:writes) — 담당 역할의 verified(인수) 또는 되돌림 (AGENTS 표 · 11.2절)")
    if unattributed:
        print(f"info [{gate}] 역할 없는 생성자의 청크 {unattributed}개 — 검사 대상 아님 (2026-09-11 이전 표기 · process:)")
    return errors
```
<!-- 인용 끝 -->
