---
id: https://agentic-knowledge-base.dev/id/chunk/170cd5f1-d8ad-4bcc-b8d8-f89887a75a0c
type: artifact
level: executable
title_ko: 함수 run_rows (tools/run_evidence.py)
title: function run_rows in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:30:15Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/78c6c89d-58c3-43c8-8570-d8bfbac1700f
---
**함수** — `run_rows(body)` 다. 실행 기록 본문의 케이스 표 → [(케이스 슬러그, 판정, 건너뛴 명령 수)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def run_rows(body: str) -> list[tuple[str, str, int]]:
    """실행 기록 본문의 케이스 표 → [(케이스 슬러그, 판정, 건너뛴 명령 수)]. 헤더의 정의처는 kb_lib.RUN_CASE_TABLE_HEADER."""
    rows, inside = [], False
    for ln in body.splitlines():
        s = ln.strip()
        if not inside:
            inside = s == kb_lib.RUN_CASE_TABLE_HEADER
            continue
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.strip("|").split("|")]
        m = _SLUG.match(cells[0]) if cells else None
        if len(cells) < 3 or not m or cells[2] not in kb_lib.RUN_VERDICTS:
            continue
        skipped = _SKIPPED.search(cells[1])
        rows.append((m.group(1), cells[2], int(skipped.group(1)) if skipped else 0))
    return rows
```
<!-- 인용 끝 -->
