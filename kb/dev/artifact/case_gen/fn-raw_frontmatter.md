---
id: https://agentic-knowledge-base.dev/id/chunk/d4776922-4147-4da3-a80b-caafc1acc6ac
type: artifact
level: executable
title_ko: 함수 raw_frontmatter (tools/case_gen.py)
title: function raw_frontmatter in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/10ce940e-ae6b-4b2e-8d0e-3bb5448ae88e
---
**함수** — `raw_frontmatter(text)` 다. frontmatter 의 키 → 원문 값.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def raw_frontmatter(text: str) -> dict[str, str]:
    """frontmatter 의 키 → 원문 값. 생성 케이스가 시나리오의 `sources`·`assumes` 를 바이트 그대로 옮기는 자리다."""
    lines = text.splitlines()
    end = lines[1:].index("---") + 1
    out = {}
    for raw in lines[1:end]:
        key, _, val = raw.partition(":")
        out[key.strip()] = val.strip()
    return out
```
<!-- 인용 끝 -->
