---
id: https://agentic-knowledge-base.dev/id/chunk/a99e95b4-6c01-4945-a6eb-6efe898579e1
type: artifact
level: executable
title_ko: 함수 attach_parts (tools/chunk2kg.py)
title: function attach_parts in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72
---
**함수** — `attach_parts(composites, part_refs)` 다. 청크의 `part_of` 와 선언된 복합체의 `composite.part_of` 를 복합체의 members 에 붙인다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def attach_parts(composites: dict, part_refs: list) -> list:
    """청크의 `part_of` 와 선언된 복합체의 `composite.part_of` 를 복합체의 members 에 붙인다 — 위반 메시지 목록을 돌려준다.

    대상이 이 묶음(실행의 입력 집합) 안에 선언되지 않았거나 자기 자신이거나 사슬이 순환하면 위반이다 (4.5절 비순환,
    p4-composite-as-part-of).
    """
    errors = []
    for chunk_iri, comp_iri, path in part_refs:
        if comp_iri not in composites:
            errors.append(f"{path}: part_of 대상 복합체 {comp_iri} 가 이 묶음 안에 선언되지 않았다 — 묶음은 이 실행의 입력 집합이고 "
                          f"액션 하나가 부분 청크 전부와 선언 청크를 함께 받아야 한다 (defs/kb.bzl 의 kb_composite·kb_decision)")
        else:
            composites[comp_iri]["members"].append((chunk_iri, path))
    for comp_iri, c in sorted(composites.items()):  # 복합체가 복합체의 부분이 되는 자리 (p4-composite-as-part-of)
        parent = c.get("parent")
        if not parent:
            continue
        if parent not in composites:
            errors.append(f"{c['path']}: composite.{PART_OF_KEY} 대상 복합체 {parent} 가 이 묶음 안에 선언되지 않았다 — 중첩 복합체는 "
                          f"한 액션이 뿌리부터 잎까지 함께 받아야 한다 (defs/kb.bzl 의 kb_composite)")
        elif parent == comp_iri:
            errors.append(f"{c['path']}: composite.{PART_OF_KEY} 가 자기 자신 {parent} 이다 — 부분-전체는 비순환이다 (4.5절)")
        else:
            composites[parent]["members"].append((comp_iri, c["path"]))
    for comp_iri in sorted(composites):  # 사슬 순환 — 반대칭 공리의 생성 시점 대응 (4.5절 비순환)
        seen_chain, cur = {comp_iri}, composites[comp_iri].get("parent")
        while cur in composites:
            if cur in seen_chain:
                errors.append(f"{composites[comp_iri]['path']}: composite.{PART_OF_KEY} 사슬이 순환한다 — {comp_iri} 에서 시작해 {cur} 로 돌아온다 (4.5절 비순환)")
                break
            seen_chain.add(cur)
            cur = composites[cur].get("parent")
    return errors
```
<!-- 인용 끝 -->
