---
id: https://agentic-knowledge-base.dev/id/chunk/6b263b93-09d3-4458-ba0b-03ba81f30852
type: artifact
level: executable
title_ko: 함수 _agt_qname (tools/validate.py)
title: function _agt_qname in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/040c4845-cfe9-495a-91c7-f98702044ca6
---
**함수** — `_agt_qname(merged, term)` 다. 병합 그래프에는 접두사가 묶여 있지 않아 qname 이 ns2: 처럼 나온다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _agt_qname(merged: Graph, term: URIRef) -> str:
    """병합 그래프에는 접두사가 묶여 있지 않아 qname 이 ns2: 처럼 나온다 — agt: 용어는 그대로 적는다."""
    return f"agt:{str(term)[len(str(AGT)):]}" if str(term).startswith(str(AGT)) else merged.qname(term)
```
<!-- 인용 끝 -->
