---
id: https://agentic-knowledge-base.dev/id/chunk/f04e6f3f-7688-4b41-a333-5dd88d484ada
type: artifact
level: executable
title_ko: 함수 observation_table (tools/weave.py)
title: function observation_table in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7106ea77-25cf-4aaa-931c-4e9c1c9cd637
---
**함수** — `observation_table(body, header)` 다. 관측 본문에서 헤더 줄이 `header` 인 표의 데이터 행(셀 목록).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def observation_table(body: str, header: str) -> list[list[str]]:
    """관측 본문에서 헤더 줄이 `header` 인 표의 데이터 행(셀 목록). 표가 없으면 빈 목록 — 관측 형식은 도구(vv_run·assume_check)가 정한다."""
    rows, inside = [], False
    for ln in body.splitlines():
        s_ = ln.strip()
        if not inside:
            inside = s_ == header
            continue
        if not s_.startswith("|"):
            break
        cells = [c.strip() for c in s_.strip("|").split("|")]
        if not all(TABLE_RULE.fullmatch(c) for c in cells):
            rows.append(cells)
    return rows
```
<!-- 인용 끝 -->
