---
id: https://agentic-knowledge-base.dev/id/chunk/29c0f765-ca46-4758-8671-e2013c8c7e8a
type: artifact
level: executable
title_ko: 함수 verdict_chunk (tools/judge.py)
title: function verdict_chunk in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2]
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `verdict_chunk(row, q, name, stamp)` 다. 결과 주석 본문 — 주석 형식 (p7-commentary-form).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def verdict_chunk(row: dict, q: dict, name: str, stamp: str) -> str:
    """결과 주석 본문 — 주석 형식 (p7-commentary-form). `본문:` 은 판정자가 쓰지 않는다 (규칙 ④)."""
    # 라벨은 질문 라벨에 대상(`verdict_stem`)과 판정자 id 를 더해 같은 질문의 결과 주석끼리 겹치지 않게 한다.
    tail = f"{row['verdict_stem']} · 판정자 {row['judge']}"
    ko = (f"판정 결과 — {q['label']}: 대상 {tail} · 값 {row['value']} · 확신도 {kb_lib.num(row['confidence'])}")
    en = (f"Judgement result — {q['label_en']}: target {row['verdict_stem']}, judge {row['judge']}, "
          f"value {row['value']}, confidence {kb_lib.num(row['confidence'])}")
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: annotation", f"level: {row['level']}",
            f"title_ko: {ko}", f"title: {en}", "status: draft", f"sources: [{{resource: {ODD_IRI}}}]",
            f"assumes: [{', '.join(ASSUMPTIONS)}]", f"targets: [{row['iri']}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    body = [f"thought (non-blocking): 질문 `agt:{name}` 의 값은 `{row['value']}` 이고 확신도는 "
            f"{kb_lib.num(row['confidence'])} 이며 판정자는 `{row['judge']}` 다.", "",
            f"대상: {row['iri']}", "",
            f"본문: {kb_lib.EMPTY_NOT_APPLICABLE}", "",
            f"해소: {kb_lib.COMMENT_OPEN} — 처리는 `{row['route']}` 다. 판정자는 설명을 만들지 못하므로 본문은 "
            f"사람 또는 System 2 에이전트가 쓴다 (p8-judge-calibration-binding 규칙 ④). 입력 지문은 "
            f"`{row['fingerprint'][:12]}…` 이고 일치는 `{row.get('agree', kb_lib.JUDGE_AGREEMENT[2])}` 다. 전체는 판정 로그에 있다."]
    return "\n".join(head + body) + "\n"
```
<!-- 인용 끝 -->
