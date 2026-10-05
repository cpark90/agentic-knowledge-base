---
id: https://agentic-knowledge-base.dev/id/chunk/b03385a6-0433-4102-a7ab-1753e57cb89a
type: artifact
level: executable
title_ko: 함수 parse_convention_targets (tools/chunk2kg.py)
title: function parse_convention_targets in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c5e6231f-44b9-4294-805c-08d03635fc72
---
**함수** — `parse_convention_targets(where, pairs, errors)` 다. `--convention-target slug=IRI` 들 → {slug: IRI}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_convention_targets(where: str, pairs: list, errors: list) -> dict:
    """`--convention-target slug=IRI` 들 → {slug: IRI}. 꼴 밖의 인자는 `errors` 에 더한다 (p12-norm-documents-from-section-chunks)."""
    out = {}
    for pair in pairs:
        slug, sep, iri = pair.partition("=")
        if not sep or not NORM_SLUG.match(slug) or not iri:
            errors.append(f"{where}: --convention-target {pair!r} 는 `slug=IRI` 꼴이다")
        else:
            out[slug] = iri
    return out
```
<!-- 인용 끝 -->
