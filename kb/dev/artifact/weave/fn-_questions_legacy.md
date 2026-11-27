---
id: https://agentic-knowledge-base.dev/id/chunk/75937272-b60e-4d9d-8919-5253ef837ff4
type: artifact
level: executable
title_ko: 함수 _questions_legacy (tools/weave.py)
title: function _questions_legacy in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07201b14-1b46-4994-8d76-3f7334f06262, https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721, https://agentic-knowledge-base.dev/id/chunk/6dab97ca-f033-4314-aaff-01ed32eab6d5, https://agentic-knowledge-base.dev/id/chunk/f04f26e1-a284-4a1d-a16a-a9ba90bde65e]
part_of: https://agentic-knowledge-base.dev/id/composite/6896fd95-4986-48dd-8016-d2446ce98fc7
---
**함수** — `_questions_legacy(ix)` 다. 옛 질문지 파일마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _questions_legacy(ix: QuestionIndex) -> list[str]:
    """옛 질문지 파일마다 한 행 — 질문 번호가 없어 파일이 단위다. 제목은 원문이므로 인용 구역으로 감싼다."""
    rows = [f"| `{name}` | {_cell(v['title'])} | {_cell(v['status'])} | {_names_cell(ix.legacy_cites.get(name, ()))} | "
            f"{_cell(' · '.join(ix.evidence.get(name, [])))} |" for name, v in sorted(ix.legacy.items())]
    body = ["## 옛 질문지 — 질문 번호 없는 파일 단위", "",
            f"`harness/user/archive/legacy/` 의 파일 {len(rows)}개다. 인용은 본문의 `legacy/<파일 이름>.md` 꼴이다.", ""]
    table = ["| 파일 | 제목 | 상태 | 인용한 단위 지식 | 유저 결정 증거 |", "|---|---|---|---|---|"] + rows
    return body + (kb_lib.gendoc_quote("\n".join(table)) if rows else [f"옛 질문지 {kb_lib.NONE_MARK}", ""])
```
<!-- 인용 끝 -->
