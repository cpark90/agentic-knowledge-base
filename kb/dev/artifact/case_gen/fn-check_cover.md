---
id: https://agentic-knowledge-base.dev/id/chunk/9f9f8d64-532f-44a2-8c09-1d523d9644e0
type: artifact
level: executable
title_ko: 함수 check_cover (tools/case_gen.py)
title: function check_cover in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:09:24Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/9f708a60-c62b-47ce-8e23-c140b412416d]
part_of: https://agentic-knowledge-base.dev/id/composite/c1361b91-dc50-48d4-bb3e-7e5d11c04516
---
**함수** — `check_cover(where, cover, keep, root)` 다. `cover` 의 형식 — 항목마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_cover(where: str, cover, keep: dict, root: Path) -> list[str]:
    """`cover` 의 형식 — 항목마다 근거 규칙 하나. 규칙 없는 항목과 손으로 적은 값은 표본 근거가 없다."""
    if not isinstance(cover, list) or not cover:
        return [f"{where}: `cover` 는 비어 있지 않은 목록이다 — {UNSAMPLED}(근거 규칙 없이 만들 케이스가 없다)"]
    errs = []
    for i, e in enumerate(cover, start=1):
        at = f"{where}: `cover` {i}번째 항목"
        if not isinstance(e, dict) or e.get("rule") not in RULE_TAGS:
            got = e.get("rule") if isinstance(e, dict) else e
            errs.append(f"{at}에 근거 규칙이 없다(`rule` {got!r}) — {UNSAMPLED}. 규칙은 {' · '.join(RULE_TAGS)} 다 (p8-case-generation)")
            continue
        rule = e["rule"]
        for k in e:
            if k == "values" and rule != "observed":
                errs.append(f"{at}({rule}) 가 값을 손으로 적었다 — {UNSAMPLED}. 손으로 고른 값은 관측 재현(`observed` + `run`)만 받는다")
            elif k != "rule" and k not in RULE_KEYS[rule]:
                errs.append(f"{at}({rule}) 의 키 `{k}` 는 규약 밖이다 — 키는 rule · {' · '.join(RULE_KEYS[rule])} 다")
        errs += check_rule(at, rule, e, keep, root)
    return errs
```
<!-- 인용 끝 -->
