---
id: https://agentic-knowledge-base.dev/id/chunk/e73edb2b-4f7b-4947-a808-37ba4d35d8d5
type: artifact
level: executable
title_ko: 함수 check_register (tools/channel_lint.py)
title: function check_register in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099]
part_of: https://agentic-knowledge-base.dev/id/composite/30c94888-c0b3-4616-8c73-db2b38068fb2
---
**함수** — `check_register(it)` 다. 경어·감탄 — 게이트 `prose` 의 판정(kb_lib.check_prose)을 그대로 건다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_register(it: dict) -> list[str]:
    """경어·감탄 — 게이트 `prose` 의 판정(kb_lib.check_prose)을 그대로 건다. 인용 블록(`>`)은 유저 원문이라 비워서 넘긴다.

    줄을 지우지 않고 비우므로 줄 번호는 파일 기준 그대로다. 면제는 게이트 `channel` 의 것만 본다(main 이 먼저 거른다).
    """
    text = "\n".join("" if ln.lstrip().startswith(">") else ln for ln in it["text"].split("\n"))
    errors, _, _ = check_prose(it["path"], text)
    return [f"{it['path']}:{ln}: {msg}" for ln, msg in errors]
```
<!-- 인용 끝 -->
