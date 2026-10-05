---
id: https://agentic-knowledge-base.dev/id/chunk/9865784d-08b9-47b0-826d-a088f38dd912
type: artifact
level: executable
title_ko: 함수 check_code_part_link (tools/validate.py)
title: function check_code_part_link in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/3e0a2fd1-776d-4762-b6e5-538b8cd4987d, https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4]
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `check_code_part_link(merged)` 다. 코드 부분 청크가 `refines`·`serves`·`verifies` 의 끝점이면 거부한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_code_part_link(merged: Graph) -> list[str]:
    """코드 부분 청크가 `refines`·`serves`·`verifies` 의 끝점이면 거부한다 (게이트 `code-part-link`, 유저 결정 Q47-b).

    코드의 링크는 파일 복합체의 것이고 자리는 선언 청크인 파일 청크 하나다(p7-code-links-on-file-composite). 추출 트리
    (`kb_lib.EXTRACT_ROOT`) 안에서 복합체의 부분인 청크 — 정의 청크와 구역 청크 — 가 주어든 대상이든 그 링크의 끝에 서면
    함수 churn 과 절의 재편이 링크를 움직인다. 판정에는 부분 관계(`agt:hasDirectPart`)와 청크 위치가 함께 필요해 청크 하나만
    보는 `chunk2kg` 나 Bazel deps 만 보는 `_check_links` 는 자리가 아니다 — `cross-kb-link` 와 같이 병합 그래프를 보는 여기가
    자리다. 판정 함수는 복원 후보 생성기(link `R_CODE_PART`)와 같은 `kb_lib.code_part` 다.
    """
    gate = kb_lib.CODE_PART_LINK_GATE
    parts = set(merged.objects(None, kb_lib.AGT.hasDirectPart))
    errors = []
    for key in kb_lib.CODE_PART_LINK_KINDS:
        for s, o in sorted(merged.subject_objects(kb_lib.AGT[key]), key=lambda so: (str(so[0]), str(so[1]))):
            for node, role in ((s, "주어"), (o, "대상")):
                if kb_lib.code_part(str(next(merged.objects(node, kb_lib.AGT.assertionLocation), "")), node in parts):
                    errors.append(f"[{gate}] {_chunk_location(merged, node)}: 코드 부분 청크가 agt:{key} 의 {role}다 "
                                  f"({_chunk_location(merged, s)} → {_chunk_location(merged, o)}) — 코드의 링크는 파일 복합체의 "
                                  f"선언 청크(module.md) 하나가 갖는다 (p7-code-links-on-file-composite)")
    return errors
```
<!-- 인용 끝 -->
