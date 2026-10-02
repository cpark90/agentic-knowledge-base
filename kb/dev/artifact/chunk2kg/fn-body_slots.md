---
id: https://agentic-knowledge-base.dev/id/chunk/848f96db-27ef-4fda-84af-e59077e7dc0c
type: artifact
level: executable
title_ko: 함수 body_slots (tools/chunk2kg.py)
title: function body_slots in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a88529ad-7941-47a8-a7ae-eb1866d89efc]
part_of: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a
---
**함수** — `body_slots(body)` 다. 본문이 쓴 슬롯 표지 — 등록된 표지(BODY_SLOT_MARKERS) 가운데 굵은 span 으로 나타난 것, 첫 등장 순서.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_slots(body: list[str]) -> list[str]:
    """본문이 쓴 슬롯 표지 — 등록된 표지(BODY_SLOT_MARKERS) 가운데 굵은 span 으로 나타난 것, 첫 등장 순서.

    표지는 **자리**로 판정한다(2026-09-29, BODY_SLOT_SPAN 주석) — 굵은 span 이 그 줄의 필드 자리
    (`_body_slot_at_field_head`: 줄 머리·불릿 다음·앞선 필드의 ` · ` 다음)에 있어야 슬롯이다. 문장 중간·표
    셀·목록 항목 전체를 감싼 굵기는 강조이지 표지가 아니다.

    표지 안의 한정어는 같은 표지로 본다. "**대안 없음**"·"**자극(분석)**" 이 그 예이고 DECISION_ROLE_MARKER 와 같은
    규칙이다 — 그것은 "대안 없음을 기록하라"는 규칙의 이행이지 표지 누락이 아니다. 한정어는 짧아야 한다
    (BODY_SLOT_QUALIFIER_MAX, 마침표 없음) — 길거나 마침표가 있으면 한정어가 아니라 표지 낱말로 시작하는
    별개의 문장이다("요인 분류가 환경 배정을 결정한다."가 그 예 — 표지가 아니다).
    """
    seen: list[str] = []
    fence: str | None = None
    for line in body:
        m = BODY_FENCE.match(line)
        if fence:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        if m:
            fence = m.group(1)
            continue
        kw = BODY_SLOT_KEYWORD.match(line)
        if kw and kw.group(1) not in seen:
            seen.append(kw.group(1))
        for span in BODY_SLOT_SPAN.finditer(line):
            cand = span.group(1).strip()
            for mark in BODY_SLOT_MARKERS:
                if not cand.startswith(mark):
                    continue
                if not _body_slot_at_field_head(line, span.start()):
                    break
                qualifier = cand[len(mark):]
                if len(qualifier) > BODY_SLOT_QUALIFIER_MAX or "." in qualifier:
                    break
                if mark not in seen:
                    seen.append(mark)
                break
    return seen
```
<!-- 인용 끝 -->
