---
id: https://agentic-knowledge-base.dev/id/chunk/e177d79e-6e9e-494e-a9f6-6a3fe42a641c
type: artifact
level: executable
title_ko: 함수 registry_path (tools/extract.py)
title: function registry_path in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**함수** — `registry_path(reg)` 다. 등록부 사이드카의 경로 — 소스 옆이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def registry_path(reg: dict) -> str:
    """등록부 사이드카의 경로 — 소스 옆이다."""
    return Path(reg["source"]).with_suffix(kb_lib.EXTRACT_REGISTRY_SUFFIX).as_posix()
```
<!-- 인용 끝 -->
