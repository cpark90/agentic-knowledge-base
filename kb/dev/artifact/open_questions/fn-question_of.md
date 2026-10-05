---
id: https://agentic-knowledge-base.dev/id/chunk/1d3aee1d-549c-4ef9-be65-508014ca8f93
type: artifact
level: executable
title_ko: 함수 question_of (tools/open_questions.py)
title: function question_of in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `question_of(body)` 다. 본문 → (질문, 상세 값들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def question_of(body: str) -> tuple[str, list[str]]:
    """본문 → (질문, 상세 값들). 상세 값은 공간 IRI 또는 문서 경로다. 슬롯 줄이 없으면 ('', [])."""
    for line in body.split("\n"):
        m = SLOT_LINE.match(line.strip())
        if not m:
            continue
        text = m.group(1).strip()
        d = DETAIL.search(text)
        if not d:
            return text, []
        return text[:d.start()].strip().rstrip(".").strip(), TICK.findall(d.group(1))
    return "", []
```
<!-- 인용 끝 -->
