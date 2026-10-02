---
id: https://agentic-knowledge-base.dev/id/chunk/3140660f-80b6-4277-88a8-ef61335d1da5
type: artifact
level: executable
title_ko: 함수 _gendoc_prose_errors (tools/kb_lib.py)
title: function _gendoc_prose_errors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/76e74bc8-5ade-4a57-8804-6270a72fd693]
part_of: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09
---
**함수** — `_gendoc_prose_errors(path, text, rows, quoted)` 다. G15·G16·G18 의 위반과 G17 후보 → (errors, g17).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_prose_errors(path, text: str, rows: list, quoted: set) -> tuple[list, list]:
    """G15·G16·G18 의 위반과 G17 후보 → (errors, g17). 넷 다 산문 조각을 훑으므로 한 자리에 둔다."""
    errors: list[tuple[int, str]] = []
    # G15 — 비율은 n/d = p.p%. 분모 없는 백분율을 쓰지 않는다. 목표 표기(G16)는 값이 아니라 기준이므로 뺀다
    heading_lines = {ln for ln, line in rows if MD_HEADING.match(line)}
    for ln, seg in prose_segments(text):
        if ln in quoted or ln in heading_lines:  # 제목은 이름이지 측정이 아니다
            continue
        seg = MD_LINK_TEXT.sub(" ", seg)  # 링크 텍스트도 이름이다 — 목차의 라벨이 백분율을 담을 수 있다
        for m in _GENDOC_PCT.finditer(seg):
            before = seg[:m.start()]
            if "목표" in before[-24:]:
                continue
            if not _GENDOC_PCT_OK.search(before):
                errors.append((ln, f"G15 분모 없는 백분율 `{m.group(0)}` — `n/d = p.p%` 꼴로 적는다 (kb_lib.pct)"))
            elif "." not in m.group(1) or len(m.group(1).split(".")[1]) != RATIO_DIGITS:
                errors.append((ln, f"G15 백분율의 소수 자릿수는 {RATIO_DIGITS} 이다 — `{m.group(0)}` (kb_lib.pct)"))

    # G16 — 목표 표기는 `(목표 <값>)` 한 꼴로 통일한다. "이 수치에 목표를 붙여야 하는가"는 사람 판단으로 남기고
    # 이미 쓰인 표기가 갈렸는지만 기계 판정한다 — 콜론 변형 `(목표: …)`은 그 밖의 전부와 다른 표기다
    for ln, seg in prose_segments(text):
        if ln in quoted:
            continue
        if GENDOC_TARGET_BAD_RE.search(seg):
            errors.append((ln, f"G16 목표 표기가 `(목표 <값>)` 꼴이 아니다 — 콜론 없이 값을 바로 잇는다 (STYLEGUIDE §9): "
                                f"{seg.strip()[:80]}"))

    # G18 — 산문은 단정 서술형이다 (STYLEGUIDE §0). 인용해 옮긴 청크 본문은 원본이 같은 게이트를 이미 통과했다
    errors += [(ln, why) for ln, why in check_prose(path, text)[0] if ln not in quoted]

    # G17(보고 전용) — 시점 의존 표현 후보. 제목·표 헤더 행·인용 구역은 이름/원문이지 측정이 아니라서 뺀다
    # (G15 의 제목·링크 텍스트 제외와 같은 근거). 게이트는 이 목록을 보지 않는다
    header_row_lines = {block[0][0] for block in _gendoc_tables(rows)
                        if len(block) >= 2 and re.fullmatch(r"\|[\s:|-]+\|", block[1][1].strip())}
    g17: list[tuple[int, str]] = []
    for ln, seg in prose_segments(text):
        if ln in quoted or ln in heading_lines or ln in header_row_lines:
            continue
        seg2 = MD_LINK_TEXT.sub(" ", seg)
        for m in GENDOC_TIME_WORD_RE.finditer(seg2):
            g17.append((ln, f"G17 시점 의존 표현 후보 `{m.group(0)}` — 값 대신 쓰였는지 사람이 판단한다 (STYLEGUIDE §9): "
                            f"{seg2.strip()[:80]}"))
    return errors, g17
```
<!-- 인용 끝 -->
