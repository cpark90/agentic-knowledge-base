---
id: https://agentic-knowledge-base.dev/id/chunk/68e14740-74c0-4de0-bac0-18d8d243e398
type: artifact
level: executable
title_ko: 함수 check_keep (tools/case_gen.py)
title: function check_keep in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5bd41470-a6c2-4f8a-aa2a-49cc2598fb88]
part_of: https://agentic-knowledge-base.dev/id/composite/c1361b91-dc50-48d4-bb3e-7e5d11c04516
---
**함수** — `check_keep(where, keep, odd)` 다. `keep` 의 형식 — 변수마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_keep(where: str, keep, odd: set[str]) -> list[str]:
    """`keep` 의 형식 — 변수마다 ODD 참조 하나와 keep 하나(`range` 또는 `values`)."""
    if not isinstance(keep, dict) or not keep:
        return [f"{where}: `keep` 은 비어 있지 않은 `변수: 명세` 매핑이다"]
    errs = []
    for name, v in keep.items():
        at = f"{where}: 변수 `{name}`"
        if not isinstance(name, str) or not VAR_NAME.fullmatch(name):
            errs.append(f"{at} 의 이름이 식별자가 아니다 — 소문자·숫자·`_`")
            continue
        if not isinstance(v, dict):
            errs.append(f"{at} 의 명세가 매핑이 아니다 — 키는 {' · '.join(VAR_KEYS)} 다")
            continue
        errs += [f"{at} 의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(VAR_KEYS)} 다" for k in v if k not in VAR_KEYS]
        ref = v.get("odd")
        if ref != ODD_OUTSIDE and ref not in odd:
            errs.append(f"{at} 의 `odd` {ref!r} 가 ODD 속성이 아니다 — 시나리오의 변수는 ODD 속성에서 온다(`id:cond-…`). "
                        f"ODD 밖이면 `{ODD_OUTSIDE}` 로 적어 커버리지에서 뺀다 (p8-scenario-authoring)")
        if ("range" in v) == ("values" in v):
            errs.append(f"{at} 는 `range` 와 `values` 중 하나를 keep 으로 갖는다")
        elif "range" in v:
            bad = check_interval(at, "range", v["range"]) + (check_interval(at, "domain", v["domain"]) if "domain" in v else [])
            errs += bad
            if "reject" in v:
                errs.append(f"{at}: `reject` 는 열거 변수의 것이다 — 범위 변수의 keep 밖은 `domain` 이 정한다")
            if "domain" in v and not bad:
                if not (v["domain"][0] <= v["range"][0] and v["range"][1] <= v["domain"][1]):
                    errs.append(f"{at}: `domain` {v['domain']} 가 `range` {v['range']} 를 품지 않는다")
        else:
            vals, rej = v.get("values"), v.get("reject", [])
            if not isinstance(vals, list) or not vals or not isinstance(rej, list):
                errs.append(f"{at}: `values` 는 비어 있지 않은 목록이고 `reject` 는 목록이다")
            elif set(map(str, vals)) & set(map(str, rej)) or len(set(map(str, vals + rej))) != len(vals + rej):
                errs.append(f"{at}: `values`·`reject` 에 같은 값이 둘 있다 — 값 하나는 keep 안이거나 밖이다")
            if "domain" in v:
                errs.append(f"{at}: `domain` 은 범위 변수의 것이다 — 열거 변수의 keep 밖은 `reject` 다")
    return errs
```
<!-- 인용 끝 -->
