---
id: https://agentic-knowledge-base.dev/id/chunk/9ea0c3bb-9662-498e-a0ad-c8a481ad765f
type: artifact
level: executable
title_ko: 함수 _build_of (tools/gen_build.py)
title: function _build_of in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6f567db9-617b-4afe-bc62-3ae6f78e6dce
---
**함수** — `_build_of(d)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _build_of(d: Path):
    return next((d / n for n in ("BUILD.bazel", "BUILD") if (d / n).is_file()), None)
```
<!-- 인용 끝 -->
