---
id: https://agentic-knowledge-base.dev/id/chunk/1f76c401-7790-442a-8a89-cbeb275631a6
type: artifact
level: executable
title_ko: 함수 index_worktree (tools/revalidate.py)
title: function index_worktree in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/e7c83ee2-f6d7-442d-98f1-d053996cdfd4]
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
    index, incoming, unparsable = {}, defaultdict(list), []
    for d in CHUNK_DIRS:
        for p in sorted((root / d).rglob("*.md")):
            rel = str(p.relative_to(root))
            try:
                meta = parse_chunk(str(p))[0]
            except ValueError as e:
                unparsable.append(f"{rel}: {e}")
                continue
            index[meta["id"]] = (rel, meta)
    for iri, (rel, meta) in index.items():
        for k, t in links_of(meta):
            incoming[t].append((k, iri))
    composite_parts = defaultdict(list)
    for iri, (rel, meta) in index.items():
        if meta.get("part_of"):
            composite_parts[meta["part_of"]].append(iri)
    # 호출부 — 대상 정의 IRI → 그것을 `uses` 로 가리키는 출발점들. 링크 키가 아니므로 links_of 와 섞지 않는다:
    # 그래야 `링크(양방향)` 열이 링크 개체의 수를 계속 뜻하고 `호출부` 열이 코드 파손의 상한을 따로 뜻한다
    callers = defaultdict(list)
    for iri, (rel, meta) in index.items():
        for t in meta.get(USES_KEY) or []:
            if t != iri:
                callers[t].append(iri)
    return index, incoming, composite_parts, callers, unparsable
```
<!-- 인용 끝 -->
