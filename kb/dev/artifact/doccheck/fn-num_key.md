---
id: https://agentic-knowledge-base.dev/id/chunk/dbdeebe3-848d-4908-81dc-0c291b07bbe2
type: artifact
level: executable
title_ko: 함수 num_key (tools/doccheck.py)
title: function num_key in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `num_key(tok)` 다. 수치 토큰 → 비교 키.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def num_key(tok: re.Match) -> tuple:
    """수치 토큰 → 비교 키. 비율은 두 수, 나머지는 한 수이고 백분율 기호는 키에 넣지 않는다."""
    parts = [float(g.replace(",", "")) for g in tok.groups() if g]
    return tuple(parts)
```
<!-- 인용 끝 -->
