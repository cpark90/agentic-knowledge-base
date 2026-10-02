---
id: https://agentic-knowledge-base.dev/id/chunk/7dd416db-02ce-4e5c-ae75-13a6abdb4250
type: artifact
level: executable
title_ko: 함수 _placement_regex (tools/consistency.py)
title: function _placement_regex in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/38dd33c9-2317-4c0a-a596-5bb97eecca1b
---
**함수** — `_placement_regex(mark)` 다. 표지 낱말이 한글 음절에 붙지 않은 자리(조사가 붙지 않은 자리)에서 발견되는가의 정규식 — 캐시로 재사용한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _placement_regex(mark: str):
    """표지 낱말이 한글 음절에 붙지 않은 자리(조사가 붙지 않은 자리)에서 발견되는가의 정규식 — 캐시로 재사용한다."""
    if mark not in _PLACEMENT_RE_CACHE:
        _PLACEMENT_RE_CACHE[mark] = re.compile(r"(?<![가-힣])" + re.escape(mark) + r"(?![가-힣])")
    return _PLACEMENT_RE_CACHE[mark]
```
<!-- 인용 끝 -->
