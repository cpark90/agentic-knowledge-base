---
id: https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099
type: artifact
level: executable
title_ko: 함수 check_prose (tools/kb_lib.py)
title: function check_prose in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/32dfc003-5ffa-4b9f-95c1-d71ffd0a4884, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/9a10d17d-c778-4340-b082-b27d4e75e275]
part_of: https://agentic-knowledge-base.dev/id/composite/99dbbf72-57fc-4b1b-91bd-ef07be848f6e
---
**함수** — `check_prose(path, text, waivers)` 다. 산문 문체 검사 → (errors, hedges, colloquial).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_prose(path: str | Path, text: str, waivers: list[dict] | None = None):
    """산문 문체 검사 → (errors, hedges, colloquial). 각 원소는 (줄 번호, 내용).

    errors 는 게이트(경어·비격식 종결, 산문의 느낌표) — waivers.md 에 게이트 id `prose`(축 파일)로 면제된 파일이면 비운다.
    hedges(추측 표현)·colloquial(구어 후보)은 보고용이고 면제와 무관하다 — 판정은 사람 몫이다.
    """
    errors: list[tuple[int, str]] = []
    hedges: list[tuple[int, str]] = []
    colloquial: list[tuple[int, str]] = []
    for ln, seg in prose_segments(text):
        for m in PROSE_FORBIDDEN_ENDINGS.finditer(seg):
            errors.append((ln, f'경어·비격식 종결 "…{m.group(0)}" — 평서형 "…다"로 쓴다 (STYLEGUIDE §0): {_around(seg, m.start(), m.end())}'))
        for m in PROSE_EXCLAMATION.finditer(seg):
            errors.append((ln, f"산문의 느낌표 — 감탄을 쓰지 않는다 (STYLEGUIDE §0): {_around(seg, m.start(), m.end())}"))
        for m in PROSE_HEDGES.finditer(seg):
            hedges.append((ln, m.group(0).strip()))
        for m in PROSE_COLLOQUIAL.finditer(seg):
            colloquial.append((ln, m.group(0)))
    if errors and waivers and waived(waivers, PROSE_GATE, str(path), "파일"):
        errors = []
    return errors, hedges, colloquial
```
<!-- 인용 끝 -->
