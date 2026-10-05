---
id: https://agentic-knowledge-base.dev/id/chunk/fd4532a7-1052-47c8-bc62-5eb12384ea3a
type: artifact
level: executable
title_ko: 함수 assignments (tools/case_gen.py)
title: function assignments in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1da98819-3151-461b-b68f-fcb080f3fbee, https://agentic-knowledge-base.dev/id/chunk/1f54d1f6-5634-49e6-abcf-060e526dcd88, https://agentic-knowledge-base.dev/id/chunk/6807ef1c-074c-48b5-a2e8-31e44223ab17, https://agentic-knowledge-base.dev/id/chunk/eb42f99d-692f-408e-b9bc-496776333330]
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `assignments(spec)` 다. cover → [{rule, values, tags, run}] — 항목 순서, 규칙 안 순서대로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def assignments(spec: dict) -> list[dict]:
    """cover → [{rule, values, tags, run}] — 항목 순서, 규칙 안 순서대로. 등가분할의 대표값만 seed 의 난수로 고른다."""
    keep, rng, base = spec["keep"], random.Random(spec["seed"]), baseline(spec["keep"])
    out = []
    for e in spec["cover"]:
        rule = e["rule"]
        if rule == "equivalence":
            for v in e["vars"]:
                for cls in classes(keep[v]):
                    pick = rng.randint(cls[0], cls[1]) if "range" in keep[v] else rng.choice(cls)
                    out.append({"rule": rule, "values": {**base, v: pick}})
        elif rule == "boundary":
            out += [{"rule": rule, "values": {**base, v: x}} for v in e["vars"] for x in boundary_values(keep[v])]
        elif rule == "pairwise":
            out += [{"rule": rule, "values": {**base, **row}} for row in pairwise_rows(keep, e["vars"])]
        elif rule == "factor":
            out += [{"rule": rule, "values": {**base, e["var"]: val}, "factor": tag} for tag, val in e["factors"].items()]
        else:
            out.append({"rule": rule, "values": {**base, **e["values"]}, "run": e["run"]})
    return out
```
<!-- 인용 끝 -->
