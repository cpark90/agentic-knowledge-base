---
id: https://agentic-knowledge-base.dev/id/chunk/4d982d54-0f5c-4d2c-bfd0-f5babb65918c
type: artifact
level: executable
title_ko: 함수 expect_of (tools/vv_run.py)
title: function expect_of in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `expect_of(spec, i)` 다. 명령 i 번째의 기대 — `expect` 가 없으면 None(종료 0 만 본다, 점진 도입).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def expect_of(spec: dict, i: int) -> dict | None:
    """명령 i 번째의 기대 — `expect` 가 없으면 None(종료 0 만 본다, 점진 도입)."""
    exp = spec.get("expect") or []
    return exp[i] if i < len(exp) and isinstance(exp[i], dict) else None
```
<!-- 인용 끝 -->
