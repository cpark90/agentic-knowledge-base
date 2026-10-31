---
id: https://agentic-knowledge-base.dev/id/chunk/606d3393-65a6-455c-8b56-8d0277bc535c
type: artifact
level: executable
title_ko: 함수 body_slot_mark (tools/chunk2kg.py)
title: function body_slot_mark in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a88529ad-7941-47a8-a7ae-eb1866d89efc]
part_of: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a
---
**함수** — `body_slot_mark(line, span)` 다. 굵은 span 하나가 슬롯 표지이면 그 표지 낱말, 아니면 빈 문자열 — 판정의 단일 정의 위치(`body_slots`·`decision-role`·`consistency`).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_slot_mark(line: str, span: re.Match) -> str:
    """굵은 span 하나가 슬롯 표지이면 그 표지 낱말, 아니면 빈 문자열 — 판정의 단일 정의 위치(`body_slots`·`decision-role`·`consistency`).

    셋을 모두 만족해야 표지다. ① span 이 등록된 표지 낱말(BODY_SLOT_MARKERS)로 시작한다 — 표지끼리 접두가 겹치지 않으므로
    (kb_lib.validate_body_slot_markers) 후보는 많아야 하나다. ② span 이 그 줄의 필드 머리에 있다(`_body_slot_at_field_head`).
    ③ 표지 낱말 뒤의 나머지(한정어)가 비었거나, 12자 이하·마침표 없음이고 등재된 꼴(BODY_SLOT_QUALIFIER_FORM)이다.

    한정어의 꼴은 규칙에 등재된 셋뿐이다 — 괄호(`**대안(미해결)**`·`**자극(분석)**`), 대시(`**대안 — 미확정**`), 낱말
    `없음`(`**대안 없음**`). 표지 낱말 뒤에 다른 낱말이 공백으로 붙으면 한정어가 아니라 표지 낱말을 머리로 둔 다른
    명사구다. `**자극 열**`(p8-reproducibility)·`**테스트 케이스 저장소**`(p8-testbed)가 길이·마침표 조건만으로는 표지로
    잘못 잡힌 측정(2026-10-24)이 그 근거다.
    """
    cand = span.group(1).strip()
    for mark in BODY_SLOT_MARKERS:
        if not cand.startswith(mark):
            continue
        if not _body_slot_at_field_head(line, span.start()):
            return ""
        qualifier = cand[len(mark):]
        if len(qualifier) > BODY_SLOT_QUALIFIER_MAX or "." in qualifier:
            return ""
        if qualifier and not BODY_SLOT_QUALIFIER_FORM.fullmatch(qualifier):
            return ""
        return mark
    return ""
```
<!-- 인용 끝 -->
