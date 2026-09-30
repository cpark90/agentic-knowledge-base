---
id: https://agentic-knowledge-base.dev/id/chunk/06e23e71-6409-4041-9dfb-d07cc209dc10
type: artifact
level: executable
title_ko: 함수 resolve (tools/doccheck.py)
title: function resolve in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/41567349-5994-4e9e-aec7-ac6603e2e6f5
---
**함수** — `resolve(doc, dest_path)` 다. 문서 기준 상대 경로 → 루트 기준 경로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve(doc: Path, dest_path: str) -> str | None:
    """문서 기준 상대 경로 → 루트 기준 경로. 루트 밖이면 None."""
    base = "" if dest_path.startswith("/") else doc.parent.as_posix()
    joined = os.path.normpath(os.path.join(base, dest_path.lstrip("/")))
    if joined == "." or joined.startswith(".."):
        return None if joined.startswith("..") else ""
    return joined
```
<!-- 인용 끝 -->
