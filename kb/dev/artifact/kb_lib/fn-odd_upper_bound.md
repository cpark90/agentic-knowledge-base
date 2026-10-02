---
id: https://agentic-knowledge-base.dev/id/chunk/29b60ef2-eb29-4888-b4c0-c2e627041d68
type: artifact
level: executable
title_ko: 함수 odd_upper_bound (tools/kb_lib.py)
title: function odd_upper_bound in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5804ea44-62d7-4b14-9187-5a7bb71425e1
---
**함수** — `odd_upper_bound(value)` 다. agt:conditionValue 문자열의 정수 상한.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def odd_upper_bound(value: str) -> int | None:
    """agt:conditionValue 문자열의 정수 상한. 식이 상한을 갖지 않거나 정수가 아니면 None — 호출자가 EXIT_CONFIG 로 다룬다."""
    m = _ODD_RANGE.search(value)
    if m:
        hi = m.group(2)
    else:
        m = _ODD_UPPER.search(value)
        if not m:
            return None
        hi = m.group(2)
    if not re.fullmatch(r"-?\d+", hi):
        return None
    n = int(hi)
    return n - 1 if (not _ODD_RANGE.search(value) and m.group(1) == "<") else n
```
<!-- 인용 끝 -->
