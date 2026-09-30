---
id: https://agentic-knowledge-base.dev/id/chunk/af9d2631-9208-4af1-a217-fd12cb8b6b83
type: artifact
level: executable
title_ko: 함수 answer_section (tools/channel_lint.py)
title: function answer_section in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T11:29:42Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6
---
**함수** — `answer_section(text)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def answer_section(text: str) -> str:
    m = re.search(r"^## 답\b.*$", text, re.M)
    return text[m.start():] if m else text
```
<!-- 인용 끝 -->
