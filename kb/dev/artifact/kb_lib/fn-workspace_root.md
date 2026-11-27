---
id: https://agentic-knowledge-base.dev/id/chunk/8ed1af77-96cb-4d77-ae1e-028946b9ebb8
type: artifact
level: executable
title_ko: 함수 workspace_root (tools/kb_lib.py)
title: function workspace_root in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/be71ea80-0460-47d3-b2be-8acda0b879fb
---
**함수** — `workspace_root()` 다. 호출 저장소의 뿌리 — `bazel run` 이 주는 `BUILD_WORKSPACE_DIRECTORY`, 없으면 현재 디렉토리다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def workspace_root() -> Path:
    """호출 저장소의 뿌리 — `bazel run` 이 주는 `BUILD_WORKSPACE_DIRECTORY`, 없으면 현재 디렉토리다 (task 0327 손질 5)."""
    return Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY") or ".")
```
<!-- 인용 끝 -->
