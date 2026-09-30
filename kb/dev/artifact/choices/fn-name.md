---
id: https://agentic-knowledge-base.dev/id/chunk/f8483d91-de06-4c00-a478-83481e91771e
type: artifact
level: executable
title_ko: 함수 name (tools/choices.py)
title: function name in tools/choices.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T16:38:13Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/6c9da832-fd4f-4fba-a0f6-33561303de46
---
**함수** — `name(g, node)` 다. 항목의 사람 이름 — 한글 라벨과 축약 IRI.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def name(g: Graph, node) -> str:
    """항목의 사람 이름 — 한글 라벨과 축약 IRI. 라벨이 인터페이스다 (p4-label-is-the-interface)."""
    return f"{kb_lib.label_of(g, node, 'ko')} `{kb_lib.compact_iri(str(node))}`"
```
<!-- 인용 끝 -->
