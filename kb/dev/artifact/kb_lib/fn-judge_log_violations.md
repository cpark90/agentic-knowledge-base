---
id: https://agentic-knowledge-base.dev/id/chunk/4398e3e6-d783-4d00-a75b-cd5e24700a7c
type: artifact
level: executable
title_ko: 함수 judge_log_violations (tools/kb_lib.py)
title: function judge_log_violations in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/e7ab69be-0a39-47d8-b2cd-89083d854b3f]
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `judge_log_violations(text, shapes_path)` 다. 판정 로그의 글을 `JUDGE_LOG_SHAPES` 로 검사한 위반 메시지 목록 — 빈 목록이면 통과다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_log_violations(text: str, shapes_path) -> list:
    """판정 로그의 글을 `JUDGE_LOG_SHAPES` 로 검사한 위반 메시지 목록 — 빈 목록이면 통과다 (Q-0056 Q119-a)."""
    from pyshacl import validate as shacl_validate
    from rdflib.namespace import SH
    shapes = Graph()
    shapes.parse(str(shapes_path), format="turtle")
    conforms, report, _ = shacl_validate(judge_log_graph(text), shacl_graph=shapes)
    if conforms:
        return []
    return sorted({str(msg) for msg in report.objects(None, SH.resultMessage)})
```
<!-- 인용 끝 -->
