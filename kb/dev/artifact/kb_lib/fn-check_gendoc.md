---
id: https://agentic-knowledge-base.dev/id/chunk/e95cd557-a497-404a-9265-5ebfe0776084
type: artifact
level: executable
title_ko: 함수 check_gendoc (tools/kb_lib.py)
title: function check_gendoc in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0, https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898, https://agentic-knowledge-base.dev/id/chunk/2c1b164b-eed1-4874-8bee-b8c56033e286, https://agentic-knowledge-base.dev/id/chunk/3140660f-80b6-4277-88a8-ef61335d1da5, https://agentic-knowledge-base.dev/id/chunk/532a2677-5c0a-4466-b71b-87289153985f, https://agentic-knowledge-base.dev/id/chunk/68b9e471-9de9-45d6-8c8c-4d7b5b1609b2, https://agentic-knowledge-base.dev/id/chunk/845f9424-b055-43c1-bbc8-afa6627dffe2]
part_of: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09
---
**함수** — `check_gendoc(path, text, exists)` 다. 생성 마크다운 규약 G1~G16·G18 중 기계 판정이 되는 것과 G17 후보 → (errors, g17_candidates).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_gendoc(path, text: str, exists=None) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    """생성 마크다운 규약 G1~G16·G18 중 기계 판정이 되는 것과 G17 후보 → (errors, g17_candidates).

    check_prose 와 같은 모양(게이트/보고 분리)으로 낸다 — errors 는 게이트가 `FAIL [gendoc] <파일>:<줄>: <근거>` 로
    찍는다. g17_candidates 는 보고 전용이고 게이트는 보지 않는다 — "값 대신 쓰였는가"를 기계로 못 가르기 때문이다
    (2026-09-29 오탐률 실측, GENDOC_TIME_WORD_RE 주석). exists 는 `경로 → bool` 로 링크 대상의 실재를 판정한다
    (G13). 없으면 문서 안 앵커만 본다.
    """
    errors: list[tuple[int, str]] = []
    lines = text.split("\n")
    start = frontmatter_end(lines)
    while start < len(lines) and not lines[start].strip():  # frontmatter 뒤의 빈 줄은 본문 앞이다
        start += 1
    body = lines[start:]
    while body and not body[-1].strip():
        body.pop()
    rows = list(md_lines(lines))
    quoted = gendoc_quoted_lines(lines)
    first = start + 1

    # 규칙군마다 함수 하나다 — 머리 블록 · 뼈대(제목·표) · 블록(펜스·목차·링크) · 산문(비율·목표·문체·시점).
    # 합계를 정렬해 내므로 군의 순서가 결과를 바꾸지 않는다 (판정은 군 안에서만 순서를 갖는다).
    errors += _gendoc_head_errors(body, first, rows)
    errors += _gendoc_outline_errors(rows, quoted)
    errors += _gendoc_block_errors(path, lines, start, body, first, rows, quoted, exists)
    prose_errors, g17 = _gendoc_prose_errors(path, text, rows, quoted)
    errors += prose_errors
    return sorted(errors), sorted(g17)
```
<!-- 인용 끝 -->
