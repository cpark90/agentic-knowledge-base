---
id: https://agentic-knowledge-base.dev/id/chunk/e5e73fb0-c433-4d73-af9c-7c61ec8e4187
type: artifact
level: executable
title_ko: 함수 frontmatter (tools/channel_lint.py)
title: function frontmatter in tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T11:29:42Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6
---
**함수** — `frontmatter(text)` 다. `---` 블록의 key: value 를 읽는다(`#` 뒤 주석 제거).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def frontmatter(text: str) -> dict | None:
    """`---` 블록의 key: value 를 읽는다(`#` 뒤 주석 제거). 블록이 없으면 None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    meta = {}
    for raw in lines[1:]:
        if raw.strip() == "---":
            return meta
        if ":" in raw and not raw.lstrip().startswith("#"):
            key, _, val = raw.partition(":")
            meta[key.strip()] = re.split(r"\s+#", val, 1)[0].strip()
    return None
```
<!-- 인용 끝 -->
