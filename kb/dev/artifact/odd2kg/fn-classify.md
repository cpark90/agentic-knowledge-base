---
id: https://agentic-knowledge-base.dev/id/chunk/4884310b-8897-44ad-945d-5f70435d9635
type: artifact
level: executable
title_ko: 함수 classify (tools/odd2kg.py)
title: function classify in tools/odd2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
part_of: https://agentic-knowledge-base.dev/id/composite/f9e4439a-33de-4e81-bb1a-e3ffec0bf77d
---
**함수** — `classify(expr, decl)` 다. (식 종류, 사람이 읽는 값) — OpenODD 식 5종 + unknown.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def classify(expr, decl):
    """(식 종류, 사람이 읽는 값) — OpenODD 식 5종 + unknown."""
    if expr == "unknown":
        return "unknown", "unknown"
    s = str(expr)
    if isinstance(decl, list):  # 범주 속성
        if s not in decl:
            raise ValueError(f"리터럴 {s!r} 이 선언된 목록 {decl} 에 없다")
        return "Equal", s
    m = NUM.match(s)
    if m:
        return ("LowerBound" if m.group(1).startswith(">") else "UpperBound"), s.strip()
    m = RANGE.match(s)
    if m:
        return "Range", s.strip()
    raise ValueError(f"OpenODD 식이 아니다: {s!r} (리터럴 / '< n unit' / '> n unit' / '[a .. b] unit' / unknown)")
```
<!-- 인용 끝 -->
