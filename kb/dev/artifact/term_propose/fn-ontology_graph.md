---
id: https://agentic-knowledge-base.dev/id/chunk/0f329565-00ac-4268-a110-cf18eaef3332
type: artifact
level: executable
title_ko: 함수 ontology_graph (tools/term_propose.py)
title: function ontology_graph in tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/3eff15a8-c6b8-46a9-a707-b95a948c619d
---
**함수** — `ontology_graph(repo)` 다. 승인된 T-Box — kb/ontology 아래의 TTL 전부(승인 큐·shape 제외).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def ontology_graph(repo: Path) -> Graph:
    """승인된 T-Box — kb/ontology 아래의 TTL 전부(승인 큐·shape 제외)."""
    g = Graph()
    root = repo / ONTOLOGY_DIR
    for f in sorted(root.rglob("*.ttl")):
        if f.relative_to(root).parts[0] in EXCLUDED_SUBDIRS:
            continue
        g.parse(f)
    return g
```
<!-- 인용 끝 -->
