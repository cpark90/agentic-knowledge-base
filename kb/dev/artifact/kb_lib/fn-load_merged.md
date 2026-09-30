---
id: https://agentic-knowledge-base.dev/id/chunk/01fd5990-0c31-4b71-8dcd-ee095148db30
type: artifact
level: executable
title_ko: 함수 load_merged (tools/kb_lib.py)
title: function load_merged in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/f25447a7-4301-4ae4-b0a6-d22f459cd775]
part_of: https://agentic-knowledge-base.dev/id/composite/7aee7ddf-f82b-4788-88ce-b27bd5290481
---
**함수** — `load_merged(paths)` 다. 파일별 그래프와 병합 그래프를 함께 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_merged(paths: list[str]) -> tuple[Graph, dict[str, Graph]]:
    """파일별 그래프와 병합 그래프를 함께 돌려준다.

    모듈 경계 검사(2.3절)는 파일별 그래프가, SHACL·추론은 병합 그래프가 필요하다.
    """
    per_file: dict[str, Graph] = {}
    merged = Graph()
    for p in paths:
        g = load_graph(p)
        per_file[p] = g
        merged += g
    return merged, per_file
```
<!-- 인용 끝 -->
