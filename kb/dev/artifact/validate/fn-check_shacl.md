---
id: https://agentic-knowledge-base.dev/id/chunk/07104b21-b283-4e54-a921-6b9a61fb6e45
type: artifact
level: executable
title_ko: 함수 check_shacl (tools/validate.py)
title: function check_shacl in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_shacl(merged, shapes, reason, shape_paths)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_shacl(merged: Graph, shapes: Graph, reason: bool, shape_paths: list[str]) -> list[str]:
    from pyshacl import validate as shacl_validate

    conforms, _, text = shacl_validate(
        merged,
        shacl_graph=shapes,
        ont_graph=None,
        inference="rdfs" if not reason else "both",
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=False,
    )
    return [] if conforms else [f"[shacl] {', '.join(shape_paths)}: shape 부적합 — sh:message 가 수정 방향이다\n{text}"]
```
<!-- 인용 끝 -->
