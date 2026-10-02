---
id: https://agentic-knowledge-base.dev/id/chunk/05336a2f-bef3-4bc3-9b6d-976a1e9adb9d
type: artifact
level: executable
title_ko: 함수 check_dangling (tools/validate.py)
title: function check_dangling in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/6900e30a-aaf6-462a-b290-9877e3439e9b, https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4, https://agentic-knowledge-base.dev/id/chunk/8d31b7a9-85c6-48b3-875b-1223f473d503]
part_of: https://agentic-knowledge-base.dev/id/composite/621b8722-ef63-42b3-8470-9560e072a62a
---
**함수** — `check_dangling(merged, ontology, files)` 다. 저장소 안을 가리키는 링크의 대상이 실재하는가 (참조 무결성, 8.2절).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_dangling(merged: Graph, ontology: Graph | None, files: dict[str, Graph]) -> list[str]:
    """저장소 안을 가리키는 링크의 대상이 실재하는가 (참조 무결성, 8.2절).

    인용·복합체 부분·가정·출처처럼 id: 개체를 가리키는 술어의 목적어는 그래프에
    주어로 나타나야 한다. 나타나지 않으면 끊어진 링크이고, 끊어진 링크는 실제
    구조를 오도하므로 없는 것보다 해롭다 (8.6절).

    agt:usesDefinition 은 추출기가 정의의 AST 에서 낸 같은 모듈의 정의를 가리킨다 — 링크 개체가 없으므로
    대상 실재를 판정하는 자리가 여기뿐이다 (채널 uses-definition, 유저 답 2026-09-30).

    agt:usesConcept 은 개념 IRI를 바로 가리킨다(dependency-graph-design (f)) — 대상은
    온톨로지가 정의한 agt: 용어여야 한다. 온톨로지를 안 주면 병합 그래프의 주어로 대신한다.

    경계: 이 검사는 usesDefinition·exposesFactor(shape가 대상 실재를 봄) 대상의 폐기 여부는 보지 않는다 —
    exposes 대상은 온톨로지 개체라 청크식 status가 없고, usesDefinition 대상은 artifact 청크라 폐기 대신
    추출 등록부의 개명·삭제로 정체성이 관리된다(이 저장소의 artifact 청크 status: deprecated 실측 0건).
    """
    checked = (
        kb_lib.AGT.cites,
        kb_lib.AGT.hasDirectPart,
        kb_lib.AGT.assumes,
        kb_lib.AGT.satisfies,
        kb_lib.AGT.refines,
        kb_lib.AGT.verifies,     # V&V → 개발 (7.5절)
        kb_lib.AGT.derivesFrom,  # 검증 목표 → 요구 (8.3절 functional 높이)
        kb_lib.AGT.overlapsWith,  # relatedTo 족의 약한 잎 (overlap-ontology) — 링크 키이므로 대상 실재를 여기서 본다
        kb_lib.AGT.targets,      # 주석 → 대상 (p7-commentary-form) — 링크 개체가 아니라 직접 트리플뿐이라 여기가 유일한 실재 검사다
        kb_lib.AGT.usesDefinition,  # 정의 → 같은 모듈의 정의 (references 족의 잎) — 링크 개체가 없으므로 여기가 유일한 실재 검사다
        kb_lib.PROV.specializationOf,  # 분할 조각 → 원본 (p10-split-keeps-work-identity) — 없는 원본을 특수화할 수 없다
    )
    subjects = set(merged.subjects())
    errors = []
    for pred in checked:
        for s, o in merged.subject_objects(pred):
            if isinstance(o, URIRef) and str(o).startswith(str(kb_lib.ID)) and o not in subjects:
                errors.append(f"[{DANGLING}] {_where(files, s)}: {merged.qname(s)} 의 {merged.qname(pred)} 대상이 없다: {o} (참조 무결성 8.2절)")
    concepts = kb_lib.defined_terms(ontology) if ontology is not None else subjects
    for s, o in merged.subject_objects(kb_lib.AGT.usesConcept):
        if o not in concepts:
            errors.append(f"[{DANGLING}] {_chunk_location(merged, s)} 의 agt:usesConcept 대상이 온톨로지에 정의되지 않았다: {o}")
    return errors
```
<!-- 인용 끝 -->
