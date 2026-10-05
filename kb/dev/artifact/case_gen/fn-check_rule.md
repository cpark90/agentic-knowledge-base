---
id: https://agentic-knowledge-base.dev/id/chunk/9f708a60-c62b-47ce-8e23-c140b412416d
type: artifact
level: executable
title_ko: 함수 check_rule (tools/case_gen.py)
title: function check_rule in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/afe80dd3-6dab-4d6c-bc6c-51c534ca4697]
part_of: https://agentic-knowledge-base.dev/id/composite/c1361b91-dc50-48d4-bb3e-7e5d11c04516
---
**함수** — `check_rule(at, rule, e, keep, root)` 다. 규칙마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_rule(at: str, rule: str, e: dict, keep: dict, root: Path) -> list[str]:
    """규칙마다 대상 변수의 꼴."""
    errs = []
    if rule in ("equivalence", "boundary", "pairwise"):
        vs = e.get("vars")
        if not isinstance(vs, list) or not vs or any(v not in keep for v in vs):
            return [f"{at}({rule}): `vars` 는 keep 의 변수 목록이다 — 실제 {vs!r}"]
        if rule == "boundary":
            errs += [f"{at}(boundary): 변수 `{v}` 는 범위 변수가 아니다 — 경계값은 `range` 의 양 끝과 바로 안팎이다" for v in vs if "range" not in keep[v]]
        if rule == "pairwise":
            if len(vs) < 2:
                errs.append(f"{at}(pairwise): 변수가 둘 이상이어야 한다 — 조합은 변수 쌍의 값 조합이다")
            errs += [f"{at}(pairwise): 변수 `{v}` 는 열거 변수가 아니다 — 조합의 값은 `values`·`reject` 다" for v in vs if "values" not in keep[v]]
    elif rule == "factor":
        var, factors = e.get("var"), e.get("factors")
        if var not in keep or not isinstance(factors, dict) or not factors:
            return [f"{at}(factor): `var`(keep 의 변수)와 비어 있지 않은 `factors`(요인 → 값)가 있어야 한다"]
        for tag, val in factors.items():
            if not isinstance(tag, str) or not FACTOR_TAG.fullmatch(tag):
                errs.append(f"{at}(factor): 요인 {tag!r} 이 `agt:<이름>` 꼴이 아니다 — 결함 요인 어휘의 개체다")
            elif in_domain(keep[var], val) is not False:
                errs.append(f"{at}(factor): 요인 {tag} 의 값 {val!r} 가 `{var}` 의 keep 밖 정의역 값이 아니다 — 요인 주입은 keep 밖 값이다")
    else:
        run, vals = e.get("run"), e.get("values")
        if not isinstance(run, str) or not run.startswith(RUN_DIR + "/") or not (root / run).is_file():
            errs.append(f"{at}(observed): `run` {run!r} 가 실행 기록(`{RUN_DIR}/…`)이 아니거나 없다 — 관측 재현의 근거는 그 기록이다")
        if not isinstance(vals, dict) or not vals or any(k not in keep for k in vals):
            errs.append(f"{at}(observed): `values` 는 keep 변수 → 값의 비어 있지 않은 매핑이다")
        else:
            errs += [f"{at}(observed): `{k}` 의 값 {v!r} 가 정의역 밖이다" for k, v in vals.items() if in_domain(keep[k], v) is None]
    return errs
```
<!-- 인용 끝 -->
