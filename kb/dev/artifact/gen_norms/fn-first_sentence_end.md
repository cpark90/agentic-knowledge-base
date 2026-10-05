---
id: https://agentic-knowledge-base.dev/id/chunk/d6ddca76-30dd-4d32-aa28-9f123fb1751e
type: artifact
level: executable
title_ko: 함수 first_sentence_end (tools/gen_norms.py)
title: function first_sentence_end in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T16:28:47Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d0c409f2-67d6-42c0-b5be-319def3c320d
---
**함수** — `first_sentence_end(text)` 다. 첫 문장의 끝 마침표 위치와 그 마침표가 굵은 span 을 닫는가 — 코드 스팬·괄호 안의 마침표와 `4.5절` 은 끝이 아니다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def first_sentence_end(text: str) -> tuple[int, bool] | None:
    """첫 문장의 끝 마침표 위치와 그 마침표가 굵은 span 을 닫는가 — 코드 스팬·괄호 안의 마침표와 `4.5절` 은 끝이 아니다."""
    code, depth = False, 0
    for i, ch in enumerate(text):
        if ch == "`":
            code = not code
        elif code:
            continue
        elif ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0:
            nxt = text[i + 1:i + 2]
            if nxt == "" or nxt.isspace():
                return i, False
            if text[i + 1:i + 3] == "**" and text[i + 3:i + 4] in ("", " "):
                return i, True
    return None
```
<!-- 인용 끝 -->
