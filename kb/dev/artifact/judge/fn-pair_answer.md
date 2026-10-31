---
id: https://agentic-knowledge-base.dev/id/chunk/1dcbf356-b12e-4bc2-b68a-0d4dc08ff69d
type: artifact
level: executable
title_ko: 함수 pair_answer (tools/judge.py)
title: function pair_answer in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/9e72d875-7a97-411f-a264-49bd2a07e2d5]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `pair_answer(data, used, question, fp)` 다. 응답 집합에서 이 (질문, 쌍 해시값)의 응답 하나 — 쌍 모드는 해시값 없는 응답을 순서로 소비하지 않는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_answer(data: dict, used: set, question: str, fp: str) -> dict | None:
    """응답 집합에서 이 (질문, 쌍 해시값)의 응답 하나 — 쌍 모드는 해시값 없는 응답을 순서로 소비하지 않는다. 없으면 None 이다."""
    for i, r in enumerate(data["responses"]):
        if i in used or r.get("question") not in (question, f"agt:{question}", str(AGT[question])) or r.get("fingerprint") != fp:
            continue
        used.add(i)
        ans = normalize(r, str(data.get("judge", kb_lib.EMPTY_UNDECIDED)))
        ans["value"] = ans["value"].strip().lower()
        if ans["value"] not in kb_lib.JUDGE_NOUL_POLARITY:
            raise JudgeError(f"판정자 {data.get('judge')} · 쌍 {fp[:12]}…: noul 값은 "
                             f"{' · '.join(kb_lib.JUDGE_NOUL_POLARITY)} 가운데 하나다 — 실제 {ans['value']!r}")
        return ans
    return None
```
<!-- 인용 끝 -->
