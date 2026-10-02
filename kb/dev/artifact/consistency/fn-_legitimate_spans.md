---
id: https://agentic-knowledge-base.dev/id/chunk/51576407-6260-4181-9396-8dd497ea9cf8
type: artifact
level: executable
title_ko: 함수 _legitimate_spans (tools/consistency.py)
title: function _legitimate_spans in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/38dd33c9-2317-4c0a-a596-5bb97eecca1b
---
**함수** — `_legitimate_spans(line)` 다. 이 줄에서 필드 자리에 정당하게 선언된 굵은 슬롯 표지의 문자 구간 — 한 줄에 여러 필드(이해관계자 · 관심사)가 ` · ` 로 이어질 때 뒤 필드의 표지어를 "다른 슬롯이 자리 밖에서 발견됨"으로 오판하지 않게 뺀다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _legitimate_spans(line: str) -> list[tuple[int, int]]:
    """이 줄에서 필드 자리에 정당하게 선언된 굵은 슬롯 표지의 문자 구간 — 한 줄에 여러 필드(이해관계자 · 관심사)가
    ` · ` 로 이어질 때 뒤 필드의 표지어를 "다른 슬롯이 자리 밖에서 발견됨"으로 오판하지 않게 뺀다."""
    spans = []
    for span in BODY_SLOT_SPAN.finditer(line):
        cand = span.group(1).strip()
        for mark in BODY_SLOT_MARKERS:
            if not cand.startswith(mark) or not _body_slot_at_field_head(line, span.start()):
                continue
            qualifier = cand[len(mark):]
            if len(qualifier) > BODY_SLOT_QUALIFIER_MAX or "." in qualifier:
                continue
            spans.append(span.span())
            break
    return spans
```
<!-- 인용 끝 -->
