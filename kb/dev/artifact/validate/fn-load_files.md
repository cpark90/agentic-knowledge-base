---
id: https://agentic-knowledge-base.dev/id/chunk/56006161-22a8-4cff-9d03-2ec71941b721
type: artifact
level: executable
title_ko: 함수 load_files (tools/validate.py)
title: function load_files in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/0025c8a9-2659-465c-b2f2-517884f7bcdb
---
**함수** — `load_files(paths)` 다. 파일별 그래프와 병합 그래프 — 파싱 실패는 파일을 지목하는 SyntaxFailure 로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_files(paths: list[str]) -> tuple[Graph, dict[str, Graph]]:
    """파일별 그래프와 병합 그래프 — 파싱 실패는 파일을 지목하는 SyntaxFailure 로."""
    merged, per_file = Graph(), {}
    for p in paths:
        try:
            g = kb_lib.load_graph(p)
        except Exception as e:  # rdflib 파서·OSError 모두 — 판정 불가 입력
            raise SyntaxFailure(f"{p}: 파싱 실패 — {e}") from e
        per_file[p] = g
        merged += g
    return merged, per_file
```
<!-- 인용 끝 -->
