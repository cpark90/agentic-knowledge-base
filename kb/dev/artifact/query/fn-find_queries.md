---
id: https://agentic-knowledge-base.dev/id/chunk/67261510-0d9f-421b-8c52-2714e157ad27
type: artifact
level: executable
title_ko: 함수 find_queries (tools/query.py)
title: function find_queries in tools/query.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-query}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1]
part_of: https://agentic-knowledge-base.dev/id/composite/804dd9bd-ceaa-4ecc-9233-ef543578feb9
---
**함수** — `find_queries(paths, root)` 다. 디렉토리 또는 .rq 파일 목록 → 정렬된 .rq 경로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def find_queries(paths: list[str], root: Path) -> list[Path]:
    """디렉토리 또는 .rq 파일 목록 → 정렬된 .rq 경로. 없는 경로는 ValueError."""
    out: list[Path] = []
    for p in paths:
        cand = Path(p) if Path(p).exists() else (kb_lib.resolve_path(p, root) or (root / p if (root / p).is_dir() else None))
        if cand is None:
            raise ValueError(f"{p}: 질의 파일·디렉토리가 없다")
        out += sorted(cand.glob("*.rq")) if cand.is_dir() else [cand]
    return out
```
<!-- 인용 끝 -->
