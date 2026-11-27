---
id: https://agentic-knowledge-base.dev/id/chunk/0b1ee795-6889-4c66-86b1-2a77ac3ee4d6
type: artifact
level: executable
title_ko: 함수 front_fields (tools/weave.py)
title: function front_fields in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `front_fields(text)` 다. frontmatter 의 최상위 `키: 값` 줄 — 질문지는 단위 지식이 아니어서 chunk2kg 파서의 대상이 아니다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def front_fields(text: str) -> dict:
    """frontmatter 의 최상위 `키: 값` 줄 — 질문지는 단위 지식이 아니어서 chunk2kg 파서의 대상이 아니다. 값 뒤의 `# 주석` 은 뗀다."""
    lines = text.splitlines()
    out: dict = {}
    if not lines or lines[0].strip() != "---":
        return out
    for ln in lines[1:]:
        if ln.strip() == "---":
            break
        k, sep, v = ln.partition(":")
        if sep and k and not k[0].isspace():
            out[k.strip()] = re.sub(r"\s+#.*$", "", v).strip()
    return out
```
<!-- 인용 끝 -->
