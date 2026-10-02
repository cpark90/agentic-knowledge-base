---
id: https://agentic-knowledge-base.dev/id/chunk/4d7ba4f8-3559-4026-8352-97c8b9835a2b
type: artifact
level: executable
title_ko: 함수 link_objects (tools/revalidate.py)
title: function link_objects in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68
---
**함수** — `link_objects(index, iris)` 다. 본문이 바뀐 청크(iris)를 양 끝 중 하나로 갖는 링크 개체 → [(링크 IRI, 종류, 출발, 도착, 방향)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def link_objects(index: dict, iris: set) -> list:
    """본문이 바뀐 청크(iris)를 양 끝 중 하나로 갖는 링크 개체 → [(링크 IRI, 종류, 출발, 도착, 방향)].

    IRI 계산은 chunk2kg 와 같다 — 양 끝을 specializationOf 사슬의 뿌리 uuid(work-id)로 올린 뒤 sha256(출발|종류|도착)[:12] 다.
    사슬이 순환하면 그 링크는 건너뛴다 (판정은 validate check_specialization 이 한다).
    """
    spec = {iri: m[SPECIALIZATION_KEY] for iri, (_rel, m) in index.items() if m.get(SPECIALIZATION_KEY)}
    out = []
    for frm, (_rel, meta) in sorted(index.items()):
        for key in OBJECT_LINK_KEYS:
            for to in meta.get(key) or []:
                if frm not in iris and to not in iris:
                    continue
                try:
                    h = link_hash(work_id(frm, spec), key, work_id(to, spec))
                except SpecializationError:
                    continue
                out.append((f"{ID_BASE}link/{h}", key, frm, to, "출발" if frm in iris else "도착"))
    return out
```
<!-- 인용 끝 -->
