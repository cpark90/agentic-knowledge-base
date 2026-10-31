---
id: https://agentic-knowledge-base.dev/id/chunk/942e32e9-5c96-4432-8b79-c82af3a44f4f
type: artifact
level: executable
title_ko: 함수 verdict_pair_chunk (tools/judge.py)
title: function verdict_pair_chunk in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/81e5e72c-14de-43e1-ac54-19566c8df95e, https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/d536eb83-d269-4b4d-a6ed-281a4a2f54c2]
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `verdict_pair_chunk(grp, q, name, stamp)` 다. 쌍 판정의 결과 주석 하나 — 판정자들의 값·확신도와 일치를 한 주석에 담는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def verdict_pair_chunk(grp: list[dict], q: dict, name: str, stamp: str) -> str:
    """쌍 판정의 결과 주석 하나 — 판정자들의 값·확신도와 일치를 한 주석에 담는다. 주석 형식이고 `본문:` 은 판정자가 쓰지 않는다."""
    first = grp[0]
    a, b, kind = kb_lib.parse_pair_target(first["iri"])
    vals = " · ".join(f"{r['judge']} {r['value']} {kb_lib.num(r['confidence'])}" for r in grp)
    vals_en = ", ".join(f"{slug(r['judge'])} {r['value']} {kb_lib.num(r['confidence'])}" for r in grp)
    agree = first.get("agree", kb_lib.JUDGE_AGREEMENT[2])
    en_agree = {kb_lib.JUDGE_AGREEMENT[0]: "agreed", kb_lib.JUDGE_AGREEMENT[1]: "split"}.get(agree, "single")
    ko = f"판정 결과 — {q['label']}: 쌍 {first['pair_fp'][:8]} · {kind} · {vals} · {agree}"
    en = f"Judgement result — {q['label_en']}: pair {first['pair_fp'][:8]}, {kind}, {vals_en}, {en_agree}"
    head = ["---", f"id: {ID}chunk/{uuid.uuid4()}", "type: annotation", f"level: {first['level']}",
            f"title_ko: {ko}", f"title: {en}", "status: draft", f"sources: [{{resource: {ODD_IRI}}}]",
            f"assumes: [{', '.join(ASSUMPTIONS)}]", f"targets: [{a}, {b}]",
            f"generated: {{by: {GENERATOR}, at: {stamp}}}", "---"]
    said = ", ".join(f"`{r['judge']}` 는 `{r['value']}`(확신도 {kb_lib.num(r['confidence'])})" for r in grp)
    body = [f"thought (non-blocking): 질문 `agt:{name}` 에 {said}를 냈고 일치는 `{agree}` 다. 링크 종류는 `{kind}` 다.", "",
            f"대상: {a} ↔ {b}", "",
            f"본문: {kb_lib.EMPTY_NOT_APPLICABLE}", "",
            f"해소: {kb_lib.COMMENT_OPEN} — 처리는 `{first['route']}` 다. 판정자는 설명을 만들지 못하므로 본문은 "
            f"사람 또는 System 2 에이전트가 쓴다 (p8-judge-session-agreement 규칙 ⑤). 입력 해시값은 "
            f"`{first['fingerprint'][:12]}…` 이고 전체는 판정 로그에 있다. 판정은 후보를 확정하지 않는다."]
    return "\n".join(head + body) + "\n"
```
<!-- 인용 끝 -->
