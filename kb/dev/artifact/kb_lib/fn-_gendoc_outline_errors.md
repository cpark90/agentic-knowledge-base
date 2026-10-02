---
id: https://agentic-knowledge-base.dev/id/chunk/532a2677-5c0a-4466-b71b-87289153985f
type: artifact
level: executable
title_ko: 함수 _gendoc_outline_errors (tools/kb_lib.py)
title: function _gendoc_outline_errors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/76e74bc8-5ade-4a57-8804-6270a72fd693, https://agentic-knowledge-base.dev/id/chunk/df94eed1-fa2e-4203-9b68-c415799b6b9a]
part_of: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09
---
**함수** — `_gendoc_outline_errors(rows, quoted)` 다. G8·G9·G10·G14 — 제목 계층과 표의 형태.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_outline_errors(rows: list, quoted: set) -> list[tuple[int, str]]:
    """G8·G9·G10·G14 — 제목 계층과 표의 형태. 둘 다 문서의 뼈대이고 행 목록만으로 판정된다."""
    errors: list[tuple[int, str]] = []
    # G8 · G9 — 제목 계층은 한 단계씩, h1 은 문서당 하나 (MD001 · MD025 · MD041)
    prev_level = 0
    for ln, line in rows:
        m = MD_HEADING.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if level == 1 and prev_level:
            errors.append((ln, f"G9 문서당 h1 은 하나다 (MD025) — `{m.group(2).strip()[:40]}`"))
        elif prev_level and level > prev_level + 1:
            errors.append((ln, f"G8 제목 계층은 한 단계씩 내려간다 (MD001) — h{prev_level} 다음에 h{level} 이 왔다"))
        prev_level = level

    # G10 — 표는 헤더 행을 갖고 열 수가 같고 앞뒤에 빈 줄이 있다 (MD055 · MD056 · MD058)
    by_ln = dict(rows)
    for block in _gendoc_tables(rows):
        ln0, first_line = block[0]
        if ln0 in quoted:
            continue
        if len(block) < 2 or not re.fullmatch(r"\|[\s:|-]+\|", block[1][1].strip()):
            errors.append((ln0, "G10 표에 헤더 행과 구분 행(`|---|`)이 없다 (MD055)"))
            continue
        width = len(_gendoc_cells(first_line))
        for ln, line in block[1:]:
            if len(_gendoc_cells(line)) != width:
                errors.append((ln, f"G10 표의 열 수가 헤더와 다르다 (MD056) — 헤더 {width}, 이 행 {len(_gendoc_cells(line))}"))
        before, after = by_ln.get(ln0 - 1), by_ln.get(block[-1][0] + 1)
        if before is not None and before.strip():
            errors.append((ln0, "G10 표 앞에 빈 줄이 있어야 한다 (MD058)"))
        if after is not None and after.strip():
            errors.append((block[-1][0] + 1, "G10 표 뒤에 빈 줄이 있어야 한다 (MD058)"))
        # G14 — 빈 셀은 없음으로 적는다
        for ln, line in block[2:]:
            for c in _gendoc_cells(line):
                if _GENDOC_EMPTY_CELL.fullmatch(c):
                    errors.append((ln, f"G14 빈 표 셀 — 비우거나 대시를 쓰지 않고 `{NONE_MARK}` 으로 적는다 (Microsoft Writing Style Guide, Tables)"))
                    break
    return errors
```
<!-- 인용 끝 -->
