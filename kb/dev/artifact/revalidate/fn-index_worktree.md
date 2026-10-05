---
id: https://agentic-knowledge-base.dev/id/chunk/1f76c401-7790-442a-8a89-cbeb275631a6
type: artifact
level: executable
title_ko: 함수 index_worktree (tools/revalidate.py)
title: function index_worktree in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/16f66a60-7480-4e95-a2d5-253ed492fa39]
part_of: https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68
---
**함수** — `index_worktree(root)` 다. 워킹트리의 청크 색인 → (index, incoming, composite_parts, callers, unparsable).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def index_worktree(root: Path) -> tuple:
    """워킹트리의 청크 색인 → (index, incoming, composite_parts, callers, unparsable).

    색인의 열쇠는 IRI 다 — 정체성이 uuid 이고 경로는 주소이기 때문이다 (p10-split-keeps-work-identity).
    """
    # 1. 워킹트리 청크 색인 — IRI → (경로, 라벨, meta), 들어오는 링크
    return index_files([(str(p.relative_to(root)), p) for d in CHUNK_DIRS for p in sorted((root / d).rglob("*.md"))])
```
<!-- 인용 끝 -->
