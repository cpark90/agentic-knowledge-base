---
id: https://agentic-knowledge-base.dev/id/chunk/6c4aaa8d-3d57-47ff-b67f-856e48d22fb0
type: artifact
level: executable
title_ko: 함수 flatten (tools/gen_norms.py)
title: function flatten in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T17:01:27Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41]
part_of: https://agentic-knowledge-base.dev/id/composite/4467fb1d-c722-4b87-a22b-5f679ceceee0
---
**함수** — `flatten(comp_iri, comps, seen)` 다. 복합체의 `composite.ordered` 를 깊이 우선으로 펼친 절 청크 IRI 목록 — 묶음 IRI 를 만나면 그 묶음의 순서로 들어간다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def flatten(comp_iri: str, comps: dict, seen: set) -> list[str]:
    """복합체의 `composite.ordered` 를 깊이 우선으로 펼친 절 청크 IRI 목록 — 묶음 IRI 를 만나면 그 묶음의 순서로 들어간다.

    문서 복합체의 직접 부분은 9 이하다(4.5절, p4-composite-as-part-of). 절이 더 많은 문서는 절을 묶음 복합체로 나누고, 묶음은
    문서 출력에 보이지 않는다 — 펼친 순서가 곧 절의 순서다. 순환(`composite.part_of` 사슬)은 GenNormsError 다.
    """
    if comp_iri in seen:
        raise GenNormsError(f"{comps[comp_iri]['_path']}: 묶음 복합체 {comp_iri} 의 composite.{PART_OF_KEY} 사슬이 순환한다 (4.5절 비순환)")
    seen.add(comp_iri)
    out = []
    for x in comps[comp_iri]["composite"][ORDERED_KEY]:
        out += flatten(x, comps, seen) if x in comps else [x]
    return out
```
<!-- 인용 끝 -->
