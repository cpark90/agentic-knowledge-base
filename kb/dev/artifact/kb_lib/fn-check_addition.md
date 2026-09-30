---
id: https://agentic-knowledge-base.dev/id/chunk/764328d8-e7e9-4fdf-9e87-e04f59d61a65
type: artifact
level: executable
title_ko: 함수 check_addition (tools/kb_lib.py)
title: function check_addition in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/76e74bc8-5ade-4a57-8804-6270a72fd693, https://agentic-knowledge-base.dev/id/chunk/9a10d17d-c778-4340-b082-b27d4e75e275, https://agentic-knowledge-base.dev/id/chunk/df94eed1-fa2e-4203-9b68-c415799b6b9a]
part_of: https://agentic-knowledge-base.dev/id/composite/2a5c7bf9-6e66-4ad7-80de-c8a96b80bb4a
---
**함수** — `check_addition(text)` 다. 첨가 → (메타 문장, 채움 문구, 빈 값 이상 표기).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_addition(text: str) -> tuple[list, list, list]:
    """첨가 → (메타 문장, 채움 문구, 빈 값 이상 표기). 각 원소는 (줄 번호, 표현, 인용).

    보고용이다 — 판정은 사람 몫이고 게이트가 아니다. 산문 판정은 prose_segments 안에서만 한다(코드·따옴표는
    산문이 아니다). 표의 단독 대시 셀은 산문 조각에 남지 않으므로 표 블록을 따로 훑는다.
    """
    meta: list[tuple[int, str, str]] = []
    filler: list[tuple[int, str, str]] = []
    empty: list[tuple[int, str, str]] = []
    for ln, seg in prose_segments(text):
        for rx, out in ((PROSE_META, meta), (PROSE_FILLER, filler), (EMPTY_VALUE_REJECTED, empty)):
            for m in rx.finditer(seg):
                out.append((ln, m.group(0).strip(), _around(seg, m.start(), m.end())))
    for block in _gendoc_tables(list(md_lines(text.split("\n")))):
        for ln, line in block[2:]:  # 헤더·구분 행 뒤의 값 행만 본다 — `|---|` 는 구분 행이다
            if any(EMPTY_DASH_CELL.fullmatch(c) for c in _gendoc_cells(line)):
                empty.append((ln, "단독 대시 셀", line.strip()))
    return meta, filler, empty
```
<!-- 인용 끝 -->
