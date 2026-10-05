---
id: https://agentic-knowledge-base.dev/id/chunk/5bd41470-a6c2-4f8a-aa2a-49cc2598fb88
type: artifact
level: executable
title_ko: 함수 check_interval (tools/case_gen.py)
title: function check_interval in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c1361b91-dc50-48d4-bb3e-7e5d11c04516
---
**함수** — `check_interval(at, key, iv)` 다. `[lo, hi]` 정수 구간인가.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_interval(at: str, key: str, iv) -> list[str]:
    """`[lo, hi]` 정수 구간인가."""
    if not (isinstance(iv, list) and len(iv) == 2 and all(isinstance(x, int) and not isinstance(x, bool) for x in iv) and iv[0] <= iv[1]):
        return [f"{at}: `{key}` 는 정수 구간 `[lo, hi]`(lo ≤ hi)다 — 실제 {iv!r}"]
    return []
```
<!-- 인용 끝 -->
