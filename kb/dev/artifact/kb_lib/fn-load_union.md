---
id: https://agentic-knowledge-base.dev/id/chunk/5b372e8e-c287-4ed0-b9d6-16c0366ee0c8
type: artifact
level: executable
title_ko: 함수 load_union (tools/kb_lib.py)
title: function load_union in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/808534e8-8fca-4ace-ace9-9e4b7084233e, https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1]
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
---
**함수** — `load_union(ttls, root)` 다. TTL 들을 하나의 Graph 로 (query.py·metrics.py 와 같은 방식).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_union(ttls: list[str], root: Path) -> Graph:
    """TTL 들을 하나의 Graph 로 (query.py·metrics.py 와 같은 방식). 빈 목록이면 UNION_GRAPH_PATHS + 온톨로지 glob.

    없는 파일은 ValueError — 호출자가 EXIT_CONFIG 로 다룬다. .ttl 이 아닌 입력(청크 .md 등)은 건너뛴다.
    """
    files: list[Path] = []
    if ttls:
        for t in ttls:
            f = resolve_path(t, root)
            if f is None:
                raise ValueError(f"{t}: 그래프 파일이 없다 — bazel build //kg:chunks_kg //kg:references_kg //kb/odd:odd")
            files.append(f)
    else:
        for p in UNION_GRAPH_PATHS:
            f = resolve_path(p, root)
            if f is None:
                raise ValueError(f"{p}: 그래프 파일이 없다 — bazel build //kg:chunks_kg //kg:references_kg //kb/odd:odd")
            files.append(f)
        for pat in UNION_GRAPH_GLOBS:
            found = resolve_glob(pat, root)
            if not found:
                raise ValueError(f"{pat}: 온톨로지 모듈이 없다")
            files += found
    g = Graph()
    for f in files:
        if f.suffix == ".ttl":
            g.parse(str(f), format="turtle")
    return g
```
<!-- 인용 끝 -->
