---
id: https://agentic-knowledge-base.dev/id/chunk/0b2c0543-8f0e-4ad8-a18a-eb3da5ff4767
type: artifact
level: executable
title_ko: 함수 _gendoc_graph_triples (tools/kb_lib.py)
title: function _gendoc_graph_triples in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1]
part_of: https://agentic-knowledge-base.dev/id/composite/6b2ef1c0-06f1-44c5-9b0f-6ba8a1fedb8d
---
**함수** — `_gendoc_graph_triples(path)` 다. 그래프 파일 하나의 트리플 집합 — 경로 그대로, 없으면 워크스페이스 루트 기준으로 찾는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_graph_triples(path: str):
    """그래프 파일 하나의 트리플 집합 — 경로 그대로, 없으면 워크스페이스 루트 기준으로 찾는다. 못 읽으면 None.

    빈 노드는 파싱마다 새 노드다. 생성기의 union 적재(`load_union` · `metrics`)도 파일마다 따로 파싱하므로 두 셈이 같다.
    """
    f = Path(path) if Path(path).is_file() else resolve_path(str(path), Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY") or "."))
    if f is None:
        return None
    key = str(f.resolve())
    if key not in _GENDOC_TRIPLES:
        g = Graph()
        try:
            g.parse(str(f), format="turtle")
        except Exception:  # noqa: BLE001 — 머리 블록은 셈을 못 해도 나간다. 표기는 GENDOC_UNION_UNREAD 이고 G4 가 판정한다
            return None
        _GENDOC_TRIPLES[key] = frozenset(g)
    return _GENDOC_TRIPLES[key]
```
<!-- 인용 끝 -->
