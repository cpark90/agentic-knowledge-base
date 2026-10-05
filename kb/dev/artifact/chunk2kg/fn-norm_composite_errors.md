---
id: https://agentic-knowledge-base.dev/id/chunk/51b67d04-6982-40f6-ae74-88b58c403ecb
type: artifact
level: executable
title_ko: 함수 norm_composite_errors (tools/chunk2kg.py)
title: function norm_composite_errors in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/15c626f2-ee68-4a3b-a918-8a5054875a54]
part_of: https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72
---
**함수** — `norm_composite_errors(composites, parsed)` 다. 규범 문서의 복합체마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def norm_composite_errors(composites: dict, parsed: list) -> list:
    """규범 문서의 복합체마다 머리 청크(선언)와 절 청크의 구분 — norm_bundle_errors 를 묶음에 돌린다.

    문서 복합체(뿌리)의 선언 청크는 머리 청크다. 묶음 복합체(`composite.part_of` 가 문서 복합체 또는 다른 묶음)는 직접 부분
    9 이하(4.5절)를 지키려고 절을 나눈 것이고 제목을 내지 않으므로, 그 선언 청크는 묶음의 첫 절 청크이며 절 키를 갖는다.
    """
    by_iri = {meta["id"]: meta for _, meta, _ in parsed}
    errors = []
    for _iri, c in sorted(composites.items()):
        decl = next((m for _, m, _ in parsed if m.get("_path") == c["path"]), None)
        if decl is not None and decl.get("type") == NORM_TYPE:
            members = [(by_iri[m], p) for m, p in c["members"] if m in by_iri]
            errors += norm_bundle_errors(None if c.get("parent") else decl, members)
    return errors
```
<!-- 인용 끝 -->
