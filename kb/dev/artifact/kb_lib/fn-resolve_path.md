---
id: https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1
type: artifact
level: executable
title_ko: 함수 resolve_path (tools/kb_lib.py)
title: function resolve_path in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
---
**함수** — `resolve_path(path, root)` 다. 워크스페이스 상대 경로를 runfiles(현재 디렉토리) → bazel-bin → 소스 순으로 찾는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve_path(path: str, root: Path) -> Path | None:
    """워크스페이스 상대 경로를 runfiles(현재 디렉토리) → bazel-bin → 소스 순으로 찾는다. 없으면 None (호출자가 EXIT_CONFIG)."""
    for cand in (Path(path), root / "bazel-bin" / path, root / path):
        if cand.is_file():
            return cand
    return None
```
<!-- 인용 끝 -->
