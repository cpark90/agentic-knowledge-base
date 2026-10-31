---
id: https://agentic-knowledge-base.dev/id/chunk/07748717-33f2-409f-8b8d-9c1a2fc37bc4
type: artifact
level: executable
title_ko: 함수 judge_log_rows (tools/kb_lib.py)
title: function judge_log_rows in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/37d74334-40cf-4370-ba39-2a78da325338, https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e]
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `judge_log_rows(text)` 다. 판정 로그 파일의 글 → 판정 표의 행들 [{열 이름: 칸}].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_log_rows(text: str) -> list[dict]:
    """판정 로그 파일의 글 → 판정 표의 행들 [{열 이름: 칸}]. 칸의 역따옴표는 벗긴다. 표가 없으면 빈 목록이다.

    `judge_log_graph`(shape 검사)와 `run_evidence`(판정 증거)가 이 한 읽기를 쓴다. 쌍 판정 행의 `대상` 칸은 `parse_pair_target` 이 푼다.
    표 머리는 기록 시각(frontmatter `generated.at`)으로 가린다 — `RECORD_HEADER_SINCE` 이전 로그는 `JUDGE_LOG_TABLE_HEADER_OLD` 만,
    이후 로그와 시각을 읽지 못한 로그는 `JUDGE_LOG_TABLE_HEADER` 만 받는다. 행의 열 이름은 어느 쪽이든 새 머리의 것이다."""
    cols = [c.strip() for c in JUDGE_LOG_TABLE_HEADER.split("|")[1:-1]]
    m = re.search(r"^generated:\s*\{[^}]*?\bat:\s*([^,}\s]+)", text, re.MULTILINE)
    header = JUDGE_LOG_TABLE_HEADER_OLD if record_header_old(m.group(1) if m else None) else JUDGE_LOG_TABLE_HEADER
    lines = chunk_body(text).split("\n")
    start = next((i for i, l in enumerate(lines) if l.strip() == header), None)
    rows = []
    for line in lines[start + 2:] if start is not None else []:
        if not line.strip().startswith("|"):
            break
        cells = [c.strip().strip("`").strip() for c in line.strip().split("|")[1:-1]]
        if len(cells) == len(cols):
            rows.append(dict(zip(cols, cells)))
    return rows
```
<!-- 인용 끝 -->
