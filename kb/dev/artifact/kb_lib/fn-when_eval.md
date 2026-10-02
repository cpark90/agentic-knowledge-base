---
id: https://agentic-knowledge-base.dev/id/chunk/b76ee239-c1db-4b7d-b6f0-0f35e7ce919f
type: artifact
level: executable
title_ko: 함수 when_eval (tools/kb_lib.py)
title: function when_eval in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8b1b0dcd-b04d-42f6-a3d6-849e3fe97268]
part_of: https://agentic-knowledge-base.dev/id/composite/749019ce-0d81-4c5f-b549-f44c1b0d4e55
---
**함수** — `when_eval(expr, states)` 다. `when` 식의 판정 → (true|false|unverified, 남긴 것 목록).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def when_eval(expr: str, states: dict) -> tuple:
    """`when` 식의 판정 → (true|false|unverified, 남긴 것 목록).

    states 는 odd_states 가 만든 {이름: in|out|unverified} 다. 접는 방식은 3값 논리(Kleene)다 — 판정 불가는 참도
    거짓도 아니므로 `A && false` 는 거짓이고 `A && true` 는 판정 불가다. 남긴 것은 판정하지 못한 항·토큰의 목록이며
    범위 밖 구문(WHEN_GRAMMAR 밖)이 거기 담긴다.
    """
    toks = _when_tokens(expr or "")
    left: list = []
    if not toks:
        return WHEN_UNVERIFIED, ["빈 식"]
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def primary():
        t = peek()
        if t is None:
            left.append("식이 항 없이 끝났다")
            return None
        pos[0] += 1
        if t == ("op", "!"):
            v = primary()
            return None if v is None else (not v)
        if t == ("op", "("):
            v = disjunction()
            if peek() == ("op", ")"):
                pos[0] += 1
            else:
                left.append("괄호가 닫히지 않았다")
            return v
        if t[0] == "lit":
            return t[1]
        if t[0] == "in":
            st = states.get(t[1])
            if st is None:
                left.append(f"in({t[1]}) — ODD 조건이 아니다")
                return None
            if st == "unverified":
                left.append(f"in({t[1]}) — 판정 불가 조건")
                return None
            return st == "in"
        left.append(f"범위 밖 토큰 `{t[1]}`")
        return None

    def conjunction():
        v = primary()
        while peek() == ("op", "&&"):
            pos[0] += 1
            r = primary()
            v = False if (v is False or r is False) else (True if (v is True and r is True) else None)
        return v

    def disjunction():
        v = conjunction()
        while peek() == ("op", "||"):
            pos[0] += 1
            r = conjunction()
            v = True if (v is True or r is True) else (False if (v is False and r is False) else None)
        return v

    val = disjunction()
    if pos[0] < len(toks):
        left.append("남은 토큰 `" + " ".join(str(t[1]) for t in toks[pos[0]:]) + "`")
        val = None
    return (WHEN_TRUE if val is True else WHEN_FALSE if val is False else WHEN_UNVERIFIED), left
```
<!-- 인용 끝 -->
