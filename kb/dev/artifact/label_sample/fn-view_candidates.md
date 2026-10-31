---
id: https://agentic-knowledge-base.dev/id/chunk/46efd740-da05-4865-b292-1d80e216e5b3
type: artifact
level: executable
title_ko: 함수 view_candidates (tools/label_sample.py)
title: function view_candidates in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9341c57d-c9c7-4528-a0a4-3db8f66d0ce7
---
**함수** — `view_candidates(view)` 다. 링크 후보 뷰의 후보 표들(사람 확인 큐·판정 불일치·판정 없음) → 행 [{열 이름: 칸}].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def view_candidates(view: Path) -> list[dict]:
    """링크 후보 뷰의 후보 표들(사람 확인 큐·판정 불일치·판정 없음) → 행 [{열 이름: 칸}]. 열은 kb_lib.LINK_CANDIDATE_COLUMNS 다."""
    header = "| " + " | ".join(kb_lib.LINK_CANDIDATE_COLUMNS) + " |"
    rows, inside = [], False
    for ln in view.read_text(encoding="utf-8").splitlines():
        s = ln.strip()
        if s == header:
            inside = True
            continue
        if inside and s.startswith("|---"):
            continue
        if inside and s.startswith("|"):
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", s)[1:-1]]
            if len(cells) == len(kb_lib.LINK_CANDIDATE_COLUMNS) and cells[0].isdigit():
                rows.append(dict(zip(kb_lib.LINK_CANDIDATE_COLUMNS, (c.strip("`") for c in cells))))
            continue
        inside = False
    return rows
```
<!-- 인용 끝 -->
