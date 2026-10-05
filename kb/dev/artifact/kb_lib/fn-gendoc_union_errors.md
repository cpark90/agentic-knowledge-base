---
id: https://agentic-knowledge-base.dev/id/chunk/d5a80e19-21cd-4de4-b68c-641a875cd7de
type: artifact
level: executable
title_ko: 함수 gendoc_union_errors (tools/kb_lib.py)
title: function gendoc_union_errors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6b2ef1c0-06f1-44c5-9b0f-6ba8a1fedb8d
---
**함수** — `gendoc_union_errors(value)` 다. G4 — 머리 `입력` 줄의 `트리플 <n> (union: …)` 에서 증분의 합이 총수와 같은지.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_union_errors(value: str) -> list[str]:
    """G4 — 머리 `입력` 줄의 `트리플 <n> (union: …)` 에서 증분의 합이 총수와 같은지. 근거 문장들(없으면 빈 목록).

    union 표기가 없는 줄은 판정하지 않는다 — 표기의 유무는 게이트 밖이다(p12-generated-document-input-section).
    """
    m = GENDOC_UNION_RE.search(value)
    if not m or m.group(2).strip() == NONE_MARK:
        return []
    total, body = int(m.group(1)), m.group(2)
    members = [x.strip() for x in body.split("\u00b7")]
    bad = [x for x in members if not GENDOC_UNION_PART_RE.fullmatch(x)]
    if bad:
        return [f"G4 union 구성원에 증분이 없다 ({' · '.join(bad)}) — `<구성원> +<증분>` 꼴이다. kb_lib.gendoc_union 을 쓴다"]
    s = sum(int(GENDOC_UNION_PART_RE.fullmatch(x).group(2)) for x in members)
    if s != total:
        return [f"G4 union 증분의 합 {s} 가 트리플 총수 {total} 와 다르다 — 구성원 증분은 선언 순서대로 앞 구성원들의 합집합에 더한 수다"]
    return []
```
<!-- 인용 끝 -->
