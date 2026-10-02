---
id: https://agentic-knowledge-base.dev/id/chunk/1a52fdec-22af-4925-98d0-b91f50c202b5
type: artifact
level: executable
title_ko: 함수 break_experiment (tools/assume_check.py)
title: function break_experiment in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/93d9eb93-7d34-4ebf-b871-041a219b6017, https://agentic-knowledge-base.dev/id/chunk/b573f0b1-8e42-4b97-bec6-397c246cd5b9]
part_of: https://agentic-knowledge-base.dev/id/composite/aa693393-615e-4f00-ada2-34df72e2832e
---
**함수** — `break_experiment(root, asms, impact)` 다. 인위 파괴(`--break`)의 검증 실험 — 계산된 직접 영향 집합과 파일 스캔의 실제 의존 집합을 견준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def break_experiment(root: Path, asms: list[dict], impact: dict) -> dict:
    """인위 파괴(`--break`)의 검증 실험 — 계산된 직접 영향 집합과 파일 스캔의 실제 의존 집합을 견준다.

    14.1 정정본 4단계의 연결 조건이다: 그래프로 센 것과 파일로 센 것이 같아야 전파를 믿을 수 있다.
    """
    computed = set().union(*(impact[x["iri"]][0] for x in asms if x["status"] == "invalidated")) if asms else set()
    actual, unparsable = set(), []
    for x in asms:
        if x["status"] == "invalidated":
            found, bad = actual_dependents(root, str(x["iri"]))
            actual |= found
            unparsable += bad
    tp = len(computed & actual)
    check = {"computed": len(computed), "actual": len(actual), "equal": computed == actual, "unparsable": unparsable,
             "precision": f"{tp}/{len(computed)}", "recall": f"{tp}/{len(actual)}",
             "only_computed": sorted(local(x) for x in computed - actual), "only_actual": sorted(local(x) for x in actual - computed)}
    return check
```
<!-- 인용 끝 -->
