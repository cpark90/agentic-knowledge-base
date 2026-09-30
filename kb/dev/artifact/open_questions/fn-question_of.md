---
id: https://agentic-knowledge-base.dev/id/chunk/1d3aee1d-549c-4ef9-be65-508014ca8f93
type: artifact
level: executable
title_ko: 함수 question_of (tools/open_questions.py)
title: function question_of in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `question_of(body)` 다. 본문 → (질문, 상세 문서 경로).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def question_of(body: str) -> tuple[str, str]:
    """본문 → (질문, 상세 문서 경로). 슬롯 줄이 없으면 ('', '')."""
    for line in body.split("\n"):
        m = SLOT_LINE.match(line.strip())
        if not m:
            continue
        text = m.group(1).strip()
        d = DETAIL.search(text)
        return (text[:d.start()].strip().rstrip(".").strip() if d else text), (d.group(1) if d else "")
    return "", ""
```
<!-- 인용 끝 -->
