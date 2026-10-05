---
id: https://agentic-knowledge-base.dev/id/chunk/9397f206-c8b3-40ab-8fb8-d286bf02749f
type: artifact
level: executable
title_ko: 함수 parse_norm_ref (tools/chunk2kg.py)
title: function parse_norm_ref in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
---
**함수** — `parse_norm_ref(where, text)` 다. 항목 문자열 `slug#k` 또는 `slug#k + slug2 + …` → ((slug, k), [링크만 하는 결정 slug…]).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_norm_ref(where: str, text) -> tuple[tuple[str, int], list[str]]:
    """항목 문자열 `slug#k` 또는 `slug#k + slug2 + …` → ((slug, k), [링크만 하는 결정 slug…]). 형식 밖이면 ValueError."""
    if not isinstance(text, str):
        raise ValueError(f"{where}: items 의 항목 {text!r} 는 `slug#k` 꼴의 문자열이어야 한다 (p12-norm-documents-from-section-chunks)")
    head, *extras = [t.strip() for t in text.split("+")]
    m = NORM_REF.match(head)
    if not m:
        raise ValueError(f"{where}: items 의 항목 {text!r} 가 `slug#k` 로 시작하지 않는다 — slug 는 결정 디렉토리 이름, "
                         f"k 는 그 결정의 conventions.md 안 `규약:` 줄의 1부터의 순번이다 (p4-convention-slot)")
    bad = [e for e in extras if not NORM_SLUG.match(e)]
    if bad:
        raise ValueError(f"{where}: items 의 항목 {text!r} 의 `+` 뒤 {bad!r} 는 결정 slug 하나여야 한다 — 둘째 결정은 링크만이다")
    return (m.group(1), int(m.group(2))), extras
```
<!-- 인용 끝 -->
