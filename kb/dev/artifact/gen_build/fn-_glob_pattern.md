---
id: https://agentic-knowledge-base.dev/id/chunk/13aadb6d-6816-4906-8368-5b13dc8dd3f2
type: artifact
level: executable
title_ko: 함수 _glob_pattern (tools/gen_build.py)
title: function _glob_pattern in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6f567db9-617b-4afe-bc62-3ae6f78e6dce
---
**함수** — `_glob_pattern(pat)` 다. Bazel glob 패턴 → 정규식.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _glob_pattern(pat: str):
    """Bazel glob 패턴 → 정규식. `*` 는 경로 조각 하나 안, `**` 는 조각 여럿을 건넌다."""
    out, i = "", 0
    while i < len(pat):
        if pat.startswith("**/", i):
            out, i = out + "(?:.*/)?", i + 3
        elif pat.startswith("**", i):
            out, i = out + ".*", i + 2
        elif pat[i] == "*":
            out, i = out + "[^/]*", i + 1
        else:
            out, i = out + re.escape(pat[i]), i + 1
    return re.compile(out + r"\Z")
```
<!-- 인용 끝 -->
