---
id: https://agentic-knowledge-base.dev/id/chunk/0bc1d5ff-d788-47b3-a1b4-43a27654be04
type: artifact
level: executable
title_ko: 함수 check_standard_vocab (tools/validate.py)
title: function check_standard_vocab in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/2bbdac5b-e7f6-4ca1-b5fd-04c0513178d1
---
**함수** — `check_standard_vocab(graphs, terms, namespaces)` 다. (--standard-vocab) 표준 어휘 네임스페이스의 용어는 등록 원문에 정의돼 있어야 한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_standard_vocab(graphs: dict[str, Graph], terms: set[URIRef], namespaces: set[str]) -> list[str]:
    """(--standard-vocab) 표준 어휘 네임스페이스의 용어는 등록 원문에 정의돼 있어야 한다.

    check_vocab 은 접두사(WELL_KNOWN_PREFIXES)만 보므로 prov:wasDerivedfrom 같은 오타가 통과한다.
    원문이 있으면 술어뿐 아니라 주어·목적어 자리(타입, subPropertyOf 대상)의 용어까지 실재를 본다.
    """
    errors = []
    for path, g in graphs.items():
        seen: set[URIRef] = set()
        for s, p, o in g:
            for node in (s, p, o):
                if isinstance(node, URIRef) and node not in seen:
                    seen.add(node)
                    if _namespace(node) in namespaces and node not in terms:
                        errors.append(f"[vocab] {path}: 표준 어휘 원문에 정의되지 않은 용어 {node} (--standard-vocab 기준)")
    return errors
```
<!-- 인용 끝 -->
