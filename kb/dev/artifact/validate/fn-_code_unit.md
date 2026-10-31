---
id: https://agentic-knowledge-base.dev/id/chunk/b526b631-d6a6-4bd8-9e43-b754fabfae9b
type: artifact
level: executable
title_ko: 함수 _code_unit (tools/validate.py)
title: function _code_unit in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0]
part_of: https://agentic-knowledge-base.dev/id/composite/650f6771-cd62-485d-85c3-a08e4df10c41
---
**함수** — `_code_unit(path)` 다. 단위 지식 파일 → (frontmatter, 언어, 인용 코드).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _code_unit(path: str) -> tuple[dict, str | None, str]:
    """단위 지식 파일 → (frontmatter, 언어, 인용 코드). 인용 코드(파이썬·SPARQL 펜스)가 없으면 언어가 None 이다.

    frontmatter 는 최상위 `키: 값` 줄을 chunk2kg.parse_value 로 읽는다 — 값 어휘(수준·지식 종류)의 판정은 chunk 게이트의 몫이다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    end = kb_lib.frontmatter_end(lines)
    meta = {}
    for raw in lines[1:end - 1] if end else []:
        m = _FM_KEY.match(raw)
        if m:
            meta[m.group(1)] = chunk2kg.parse_value(raw.partition(":")[2].strip())
    lang, code = None, []
    for ln in lines[end:]:
        if lang is None:
            m = _CODE_FENCE.match(ln.strip())
            if m:
                lang = m.group(1)
            continue
        if ln.strip() == "```":
            break
        code.append(ln)
    return meta, lang, "\n".join(code)
```
<!-- 인용 끝 -->
