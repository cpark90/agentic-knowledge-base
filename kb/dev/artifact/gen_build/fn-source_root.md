---
id: https://agentic-knowledge-base.dev/id/chunk/535d310e-db77-40f1-a678-68d3de7d9727
type: artifact
level: executable
title_ko: 함수 source_root (tools/gen_build.py)
title: function source_root in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6f567db9-617b-4afe-bc62-3ae6f78e6dce
---
**함수** — `source_root(root)` 다. `bazel test` 의 runfiles 에서 소스 트리의 뿌리 — 입력 defs/kb.bzl 의 심볼릭 링크를 따라간다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def source_root(root: Path) -> Path:
    """`bazel test` 의 runfiles 에서 소스 트리의 뿌리 — 입력 defs/kb.bzl 의 심볼릭 링크를 따라간다. 트리에서는 root 자신이다.

    게이트 입력 검사는 선언되지 않은 파일을 찾는 검사라 선언된 입력만 있는 runfiles 로는 판정할 수 없다.
    """
    return Path(os.path.realpath(root / "defs" / "kb.bzl")).parents[1]
```
<!-- 인용 끝 -->
