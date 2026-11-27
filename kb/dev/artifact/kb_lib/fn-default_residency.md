---
id: https://agentic-knowledge-base.dev/id/chunk/c72423ba-8082-4594-8317-046edbd135ed
type: artifact
level: executable
title_ko: 함수 default_residency (tools/kb_lib.py)
title: function default_residency in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04fe68bc-58a1-45bd-ac00-78d263cbba81, https://agentic-knowledge-base.dev/id/chunk/8ed1af77-96cb-4d77-ae1e-028946b9ebb8]
part_of: https://agentic-knowledge-base.dev/id/composite/be71ea80-0460-47d3-b2be-8acda0b879fb
---
**함수** — `default_residency()` 다. `--residency` 의 기본값 — 이 모듈의 `defs/kb.bzl` 이다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def default_residency() -> str:
    """`--residency` 의 기본값 — 이 모듈의 `defs/kb.bzl` 이다 (task 0327 손질 6). `gates_bzl_path` 와 같은 탐색을 쓴다."""
    try:
        return str(gates_bzl_path())
    except FileNotFoundError:
        return str(workspace_root() / "defs" / "kb.bzl")
```
<!-- 인용 끝 -->
