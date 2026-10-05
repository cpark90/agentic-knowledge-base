---
id: https://agentic-knowledge-base.dev/id/chunk/90fe8a83-bd07-4bb1-bd2c-fcdad7d246b7
type: artifact
level: executable
title_ko: 함수 load_bzl_scalar (tools/kb_lib.py)
title: function load_bzl_scalar in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/513aca4d-e5f0-46c8-8d13-784c71691884
---
**함수** — `load_bzl_scalar(path, name)` 다. `defs/kb.bzl` 의 문자열 스칼라 리터럴을 읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_bzl_scalar(path: str | Path, name: str) -> str:
    """`defs/kb.bzl` 의 문자열 스칼라 리터럴을 읽는다 — `GATE_LAYER` 처럼 값이 하나인 자리."""
    text = Path(path).read_text(encoding="utf-8")
    m = re.search(rf"^\s*{re.escape(name)}\s*=\s*[\"']([^\"'\n]*)[\"']", text, re.M)
    if not m:
        raise ValueError(f"{path}: {name} 값을 찾을 수 없다")
    return m.group(1)
```
<!-- 인용 끝 -->
