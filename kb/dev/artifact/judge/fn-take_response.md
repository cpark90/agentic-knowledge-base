---
id: https://agentic-knowledge-base.dev/id/chunk/3cfd5bbf-40af-4597-b129-32f4c73b27ab
type: artifact
level: executable
title_ko: 함수 take_response (tools/judge.py)
title: function take_response in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/97e93b30-be59-4c26-b322-176b8e0f350e
---
**함수** — `take_response(data, used, q, name, fp)` 다. 응답 집합에서 이 (질문, 대조 지문)의 응답 하나를 꺼낸다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def take_response(data: dict, used: set, q: dict, name: str, fp: str) -> dict:
    """응답 집합에서 이 (질문, 대조 지문)의 응답 하나를 꺼낸다 — 지문을 적지 않은 응답은 순서로 소비한다.

    `fp`는 **대조 지문**(`kb_lib.label_fingerprint`)이다 — 세션 판정자가 실제로 본 라벨+본문의 sha256이지,
    청크 파일 바이트의 sha256(로그의 `입력 지문` 열)이 아니다. 파일 지문으로 대조하면 판정자의 응답이
    전부 안 잡힌다(2026-09-30 vnv 결함 보고 ①).
    """
    for i, r in enumerate(data["responses"]):
        if i in used or r.get("question") not in (name, q["iri"]):
            continue
        if r.get("fingerprint") and r["fingerprint"] != fp:
            continue
        used.add(i)
        return normalize(r, str(data.get("judge", kb_lib.EMPTY_UNDECIDED)))
    raise JudgeError(f"응답 집합(판정자 {data.get('judge')})에 질문 {name} · 입력 지문 {fp[:12]}… 의 응답이 없다 — "
                     "`responses` 에 항목을 더한다")
```
<!-- 인용 끝 -->
