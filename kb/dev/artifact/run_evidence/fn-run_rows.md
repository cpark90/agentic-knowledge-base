---
id: https://agentic-knowledge-base.dev/id/chunk/170cd5f1-d8ad-4bcc-b8d8-f89887a75a0c
type: artifact
level: executable
title_ko: 함수 run_rows (tools/run_evidence.py)
title: function run_rows in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/37d74334-40cf-4370-ba39-2a78da325338]
part_of: https://agentic-knowledge-base.dev/id/composite/78c6c89d-58c3-43c8-8570-d8bfbac1700f
---
**함수** — `run_rows(body, at)` 다. 실행 기록 본문의 테스트 케이스 표 → [(테스트 케이스 슬러그, 판정, 건너뛴 명령 수)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def run_rows(body: str, at=None) -> list[tuple[str, str, int]]:
    """실행 기록 본문의 테스트 케이스 표 → [(테스트 케이스 슬러그, 판정, 건너뛴 명령 수)]. 헤더의 단일 정의 위치는 kb_lib.RUN_CASE_TABLE_HEADER.

    표 머리는 기록 시각 `at`(frontmatter `generated.at`)으로 가린다 — kb_lib.RECORD_HEADER_SINCE 이전 기록은 `RUN_CASE_TABLE_HEADER_OLD` 만,
    이후 기록과 시각을 읽지 못한 기록은 새 머리만 받는다 (Q161-a)."""
    header = kb_lib.RUN_CASE_TABLE_HEADER_OLD if kb_lib.record_header_old(at) else kb_lib.RUN_CASE_TABLE_HEADER
    rows, inside = [], False
    for ln in body.splitlines():
        s = ln.strip()
        if not inside:
            inside = s == header
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
