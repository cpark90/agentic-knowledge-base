---
id: https://agentic-knowledge-base.dev/id/chunk/770131c5-53ed-4b85-b077-050f12836f80
type: artifact
level: executable
title_ko: 함수 generate (tools/case_gen.py)
title: function generate in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2ac44f3c-c4f0-43b6-a92b-686fa3406caf, https://agentic-knowledge-base.dev/id/chunk/68e14740-74c0-4de0-bac0-18d8d243e398, https://agentic-knowledge-base.dev/id/chunk/9f9f8d64-532f-44a2-8c09-1d523d9644e0, https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a, https://agentic-knowledge-base.dev/id/chunk/d1084eaf-333b-4dbd-ba82-e2d17786590c, https://agentic-knowledge-base.dev/id/chunk/eb325ac3-9126-44e4-977b-2da002c1b35a, https://agentic-knowledge-base.dev/id/chunk/fd4532a7-1052-47c8-bc62-5eb12384ea3a]
part_of: https://agentic-knowledge-base.dev/id/composite/d35350bd-7f95-4059-82b7-88108831c060
---
**함수** — `generate(sc, root, odd)` 다. 시나리오 하나 → {케이스 파일 이름: 텍스트}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def generate(sc: dict, root: Path, odd: set[str]) -> dict[str, str]:
    """시나리오 하나 → {케이스 파일 이름: 텍스트}. 같은 값 배정은 케이스 하나이고 근거 태그를 모은다."""
    spec, where = sc["spec"], str(sc["path"])
    if not isinstance(spec, dict):
        raise CaseGenError(f"{where}: 입력 펜스는 매핑이다 — 키는 {' · '.join(INPUT_KEYS)} 다")
    errs = []
    for k in spec:
        if k == "cases":
            errs.append(f"{where}: `cases` 는 케이스를 손으로 적은 목록이다 — {UNSAMPLED}. 값은 `cover` 의 규칙이 낸다 (p8-case-generation)")
        elif k not in INPUT_KEYS:
            errs.append(f"{where}: 입력 펜스의 키 `{k}` 는 규약 밖이다 — 키는 {' · '.join(INPUT_KEYS)} 다")
    if not isinstance(spec.get("seed"), int) or isinstance(spec.get("seed"), bool):
        errs.append(f"{where}: `seed` 는 정수다 — 규칙과 seed 가 케이스의 provenance 에 남아야 재생성이 된다")
    kerrs = check_keep(where, spec.get("keep"), odd)
    errs += kerrs
    if not kerrs:
        errs += check_cover(where, spec.get("cover"), spec["keep"], root)
        errs += check_case_template(where, spec.get("case"), spec["keep"])
    if errs:
        raise CaseGenError("\n".join(errs))
    merged: dict[str, dict] = {}
    for a in assignments(spec):
        key = json.dumps(a["values"], sort_keys=True, ensure_ascii=False)
        m = merged.setdefault(key, {"rule": a["rule"], "values": a["values"], "tags": [], "factors": [], "runs": []})
        for t in [RULE_TAGS[a["rule"]]] + ([ORIGIN_OBSERVED] if a["rule"] == "observed" else []):
            if t not in m["tags"]:
                m["tags"].append(t)
        m["factors"] += [a["factor"]] if "factor" in a else []
        m["runs"] += [a["run"]] if "run" in a else []
    out, counts = {}, {}
    for a in merged.values():
        counts[a["rule"]] = counts.get(a["rule"], 0) + 1
        name = f"{sc['slug']}-{a['rule']}-{counts[a['rule']]}.md"
        out[name] = render(sc, a, spec["case"], name)
        errs += [f"{where}: 생성 케이스 `{name}` — {e}" for e in runner_errors(out[name])]
    if errs:
        raise CaseGenError("\n".join(errs))
    return out
```
<!-- 인용 끝 -->
