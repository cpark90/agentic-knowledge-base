---
id: https://agentic-knowledge-base.dev/id/chunk/21357a69-21e9-470e-8d6c-43908a9308d7
type: artifact
level: executable
title_ko: 함수 load_responses (tools/judge.py)
title: function load_responses in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b]
part_of: https://agentic-knowledge-base.dev/id/composite/97e93b30-be59-4c26-b322-176b8e0f350e
---
**함수** — `load_responses(path)` 다. 세션 판정자의 응답 집합 — {judge: <역할/모델 또는 세션 식별자>, responses: [{question, fingerprint, value, confidence}]}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_responses(path: Path) -> dict:
    """세션 판정자의 응답 집합 — {judge: <역할/모델 또는 세션 식별자>, responses: [{question, fingerprint, value, confidence}]}.

    `judge` 가 빠져 있으면 미확정으로 둔다 — 그 값이 판정 로그의 `판정자 식별자` 열에 그대로 실려 게이트
    `judge-log`가 빈 값 표기로 거부한다. 판정자 식별자 없는 판정을 조용히 통과시키지 않는 장치다.
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise JudgeError(f"{path}: 응답을 읽을 수 없다 — {e}")
    if not isinstance(data, dict) or not isinstance(data.get("responses"), list):
        raise JudgeError(f"{path}: 응답 집합은 `responses` 목록을 가진 객체다 — {{judge, responses: [...]}}")
    data.setdefault("judge", kb_lib.EMPTY_UNDECIDED)
    return data
```
<!-- 인용 끝 -->
