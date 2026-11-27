---
id: https://agentic-knowledge-base.dev/id/chunk/daf683a0-9d84-4163-9eb0-2ea99d87494d
type: artifact
level: executable
title_ko: 함수 _questions_unresolved (tools/weave.py)
title: function _questions_unresolved in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721, https://agentic-knowledge-base.dev/id/chunk/f04f26e1-a284-4a1d-a16a-a9ba90bde65e]
part_of: https://agentic-knowledge-base.dev/id/composite/6896fd95-4986-48dd-8016-d2446ce98fc7
---
**함수** — `_questions_unresolved(ix)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _questions_unresolved(ix: QuestionIndex) -> list[str]:
    body = ["## 풀리지 않는 번호 — 본문이 인용했는데 질문지에 없는 것", ""]
    if not ix.unresolved and not ix.dups:
        return body + ["본문과 유저 결정 증거가 인용한 번호와 옛 질문지 가운데 질문지로 풀리지 않는 것은 없다.", ""]
    body += ["| 인용 | 인용처 | 사유 |", "|---|---|---|"]
    body += [f"| `{raw}` | {_cell(where if where.startswith('유저') else f'`{where}`')} | {why} |" for raw, where, why in sorted(set(ix.unresolved))]
    body += [f"| `Q{n}` | `{a}` · `{b}` | 두 질문지에 같은 번호가 있다 — 앞 질문지의 것만 표에 싣는다 |" for n, a, b in ix.dups]
    return body + [""]
```
<!-- 인용 끝 -->
