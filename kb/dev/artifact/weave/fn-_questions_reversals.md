---
id: https://agentic-knowledge-base.dev/id/chunk/d5be3602-e40e-4447-a03c-0d626399f32a
type: artifact
level: executable
title_ko: 함수 _questions_reversals (tools/weave.py)
title: function _questions_reversals in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721]
part_of: https://agentic-knowledge-base.dev/id/composite/6896fd95-4986-48dd-8016-d2446ce98fc7
---
**함수** — `_questions_reversals(ix)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _questions_reversals(ix: QuestionIndex) -> list[str]:
    groups = ix.reversals()
    body = ["## 뒤집힘 — 같은 결정을 인용한 질문 둘 이상", "",
            f"같은 결정을 인용한 질문이 둘 이상인 결정 {len(groups)}개다. 질문은 질문지 생성일 순이고 같은 날은 번호 순이다. "
            "뒤의 답이 앞의 답을 바꿨는지는 묶음을 읽고 판단한다.", ""]
    if not groups:
        return body + [f"묶음 {kb_lib.NONE_MARK}", ""]
    body += ["| 결정 | 질문 수 | 질문 (생성일 순) |", "|---|---|---|"]
    for d, ns in groups:
        body.append(f"| `{d}` | {len(ns)} | " + " · ".join(f"Q{n} ({ix.questions[n]['sheet']}, {ix.questions[n]['created']})" for n in ns) + " |")
    return body + [""]
```
<!-- 인용 끝 -->
