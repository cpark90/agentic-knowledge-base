---
id: https://agentic-knowledge-base.dev/id/chunk/8f15c2bb-62bb-4e9f-98dc-e86d7e0436b2
type: artifact
level: executable
title_ko: 함수 read_sheet (tools/weave.py)
title: function read_sheet in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0b1ee795-6889-4c66-86b1-2a77ac3ee4d6]
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `read_sheet(path)` 다. 질문지 하나 → (frontmatter, 질문 목록).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def read_sheet(path: str) -> tuple[dict, list[dict]]:
    """질문지 하나 → (frontmatter, 질문 목록). 질문은 번호 · 제목 · 답이고, 답은 질문 절(다음 h2 앞까지)의 첫 `답:` 줄이며 없으면 None 이다."""
    text = Path(path).read_text(encoding="utf-8")
    questions, cur = [], None
    for line in text.splitlines():
        h = QUESTION_HEADING.match(line)
        if h:
            cur = {"n": int(h.group(1)), "title": h.group(2), "answer": None}
            questions.append(cur)
        elif line.startswith("## "):
            cur = None
        elif cur is not None and cur["answer"] is None and (a := ANSWER_LINE.match(line)):
            cur["answer"] = a.group(1)
    return front_fields(text), questions
```
<!-- 인용 끝 -->
