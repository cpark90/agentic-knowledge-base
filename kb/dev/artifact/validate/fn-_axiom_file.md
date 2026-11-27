---
id: https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe
type: artifact
level: executable
title_ko: 함수 _axiom_file (tools/validate.py)
title: function _axiom_file in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
---
**함수** — `_axiom_file(files, *triples)` 다. 공리 트리플을 담은 파일 — 어느 것도 없으면 `추론`(폐포가 낳은 공리)이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _axiom_file(files: dict[str, Graph], *triples) -> str:
    """공리 트리플을 담은 파일 — 어느 것도 없으면 `추론`(폐포가 낳은 공리)이다."""
    for path, g in files.items():
        if any(t in g for t in triples):
            return path
    return "추론"
```
<!-- 인용 끝 -->
