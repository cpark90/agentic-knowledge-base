---
id: https://agentic-knowledge-base.dev/id/chunk/679d9b66-75c4-4149-9431-e4eedce13df2
type: artifact
level: executable
title_ko: 함수 slot_regions (tools/consistency.py)
title: function slot_regions in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/38dd33c9-2317-4c0a-a596-5bb97eecca1b
---
**함수** — `slot_regions(body_text)` 다. 등록된 슬롯 표지(chunk2kg.BODY_SLOT_MARKERS 의 굵은 span·BODY_SLOT_KEYWORD 의 줄 머리 `키워드:`)로 본문을 나눈 조각의 줄 인덱스 — {표지: [줄 인덱스, …]}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def slot_regions(body_text: str) -> dict[str, list[int]]:
    """등록된 슬롯 표지(chunk2kg.BODY_SLOT_MARKERS 의 굵은 span·BODY_SLOT_KEYWORD 의 줄 머리 `키워드:`)로 본문을
    나눈 조각의 줄 인덱스 — {표지: [줄 인덱스, …]}. 두 표지 종류(굵은 span·키워드 콜론)를 다 본다 — 어느 한쪽만
    보면 `미확정:` 같은 키워드 슬롯의 줄이 앞선 굵은 슬롯의 영역으로 잘못 편입된다(측정 2026-09-30).

    자리 판정은 chunk2kg.body_slot_mark 하나(표지는 자리로 판정한다 · 한정어의 길이와 꼴)를 재사용한다 —
    판정을 고치면 방출과 이 보고가 같이 바뀐다(STYLEGUIDE §7 단일 정의 위치, 이 함수는 그 판정을 구간으로만 편다).
    """
    lines = body_text.splitlines()
    regions: dict[str, list[int]] = {}
    fence: str | None = None
    current: str | None = None
    for i, line in enumerate(lines):
        m = BODY_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            if current:
                regions[current].append(i)
            continue
        if m:
            fence = m.group(1)
            if current:
                regions[current].append(i)
            continue
        kw = BODY_SLOT_KEYWORD.match(line)
        hit = kw.group(1) if kw else None
        if not hit:
            for span in BODY_SLOT_SPAN.finditer(line):
                hit = body_slot_mark(line, span) or None
                if hit:
                    break
        if hit:
            current = hit
            regions.setdefault(current, [])
        if current:
            regions[current].append(i)
    return regions
```
<!-- 인용 끝 -->
