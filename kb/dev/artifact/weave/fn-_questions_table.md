---
id: https://agentic-knowledge-base.dev/id/chunk/f608a299-e952-4c87-88d2-f11dd286bc42
type: artifact
level: executable
title_ko: 함수 _questions_table (tools/weave.py)
title: function _questions_table in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07201b14-1b46-4994-8d76-3f7334f06262, https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721, https://agentic-knowledge-base.dev/id/chunk/6dab97ca-f033-4314-aaff-01ed32eab6d5, https://agentic-knowledge-base.dev/id/chunk/f04f26e1-a284-4a1d-a16a-a9ba90bde65e]
part_of: https://agentic-knowledge-base.dev/id/composite/6896fd95-4986-48dd-8016-d2446ce98fc7
---
**함수** — `_questions_table(ix)` 다. 질문마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _questions_table(ix: QuestionIndex) -> list[str]:
    """질문마다 한 행 — 제목과 답은 질문지의 원문을 그대로 옮기므로 인용 구역으로 감싼다."""
    rows = []
    for n in sorted(ix.questions):
        q = ix.questions[n]
        groups = ix.cites.get(n, {})
        rows.append(f"| Q{n} | {q['sheet']}{'' if not ix.sheets[q['sheet']] else ' (열림)'} | {_cell(q['title'])} | {q['created']} | "
                    f"{_cell(q['answer'] or '')} | " + " | ".join(_names_cell(groups.get(k, ())) for k, _ in QUESTION_GROUPS)
                    + f" | {_cell(' · '.join(ix.evidence.get(n, [])))} |")
    head_ = "| 질문 | 질문지 | 제목 | 생성일 | 답 | " + " | ".join(f"인용한 {name}" for _, name in QUESTION_GROUPS) + " | 유저 결정 증거 |"
    return ["## 질문 — 질문마다 답의 반영처", "",
            "질문 번호 순이다. 제목과 답은 질문지의 원문이고, 인용처 칸은 수와 앞의 이름이다. 결정은 결정 디렉토리, 설계 공간은 파일 stem, "
            "그 밖의 단위 지식은 경로로 적는다.", ""] + kb_lib.gendoc_quote("\n".join([head_, "|" + "---|" * 9] + rows))
```
<!-- 인용 끝 -->
