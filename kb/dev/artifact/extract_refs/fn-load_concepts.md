---
id: https://agentic-knowledge-base.dev/id/chunk/387e5197-3f50-4685-a292-423f00120e05
type: artifact
level: executable
title_ko: 함수 load_concepts (tools/extract_refs.py)
title: function load_concepts in tools/extract_refs.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract-refs}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-19T14:57:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/444fc7bd-680b-4c09-aec8-0e5de0cc1175
---
**함수** — `load_concepts(paths)` 다. 온톨로지 union이 정의하는 agt: 용어(클래스·속성·개체)의 로컬 이름 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_concepts(paths: list[str]) -> set[str]:
    """온톨로지 union이 정의하는 agt: 용어(클래스·속성·개체)의 로컬 이름 집합.

    rdflib·kb_lib 는 --ontology 를 줄 때만 필요하다 — 없으면 이 함수는 호출되지 않는다.
    """
    try:
        from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path에 있다
    except ImportError:
        import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    merged, _ = kb_lib.load_merged(paths)
    return {str(t)[len(AGT):] for t in kb_lib.defined_terms(merged)}
```
<!-- 인용 끝 -->
