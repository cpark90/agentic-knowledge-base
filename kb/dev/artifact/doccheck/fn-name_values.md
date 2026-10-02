---
id: https://agentic-knowledge-base.dev/id/chunk/9ad037aa-26ed-4502-92a5-7bc7dd0855a3
type: artifact
level: executable
title_ko: 함수 name_values (tools/doccheck.py)
title: function name_values in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/dbdeebe3-848d-4908-81dc-0c291b07bbe2]
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
---
**함수** — `name_values(line, name)` 다. 한 줄에서 이름 뒤 창의 수치 토큰 → [(원문, 키)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def name_values(line: str, name: re.Pattern) -> list[tuple[str, tuple]]:
    """한 줄에서 이름 뒤 창의 수치 토큰 → [(원문, 키)]. 이름에 붙지 않은 수치와 날짜·절 번호·식별자는 뺀다."""
    out = []
    for m in name.finditer(line):
        window = NOISE.sub(" ", line[m.end():m.end() + WINDOW])
        cut = CELL_END.search(window)
        window = window[:cut.start()] if cut else window
        for tok in NUM_TOKEN.finditer(window):
            gap = window[:tok.start()]
            if ADJACENT.fullmatch(gap):
                out.append((tok.group(0).strip(), num_key(tok)))
    return out
```
<!-- 인용 끝 -->
