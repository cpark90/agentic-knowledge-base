---
id: https://agentic-knowledge-base.dev/id/chunk/1d7270dd-9f02-4949-a1ab-2681afc73834
type: artifact
level: executable
title_ko: 함수 _audit_verified (tools/weave.py)
title: function _audit_verified in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4600b6bb-eddb-4832-9854-1c587f7929d9, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_verified(m, g, live)` 다. `verified` 주체 종류별 단위 지식 수와 검증 뒤 수정 (agt:TrustShape 가 게이트에서 강제하는 것).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_verified(m: Model, g, live: set) -> list[str]:
    """`verified` 주체 종류별 단위 지식 수와 검증 뒤 수정 (agt:TrustShape 가 게이트에서 강제하는 것).

    `agt:verifiedBy` 는 지금 내용의 판정(at ≥ generated.at)만 담는다(chunk2kg) — 옛 내용의 판정은 등급에 들지 않는다.
    검증 뒤 수정은 **가장 늦은** `agt:verifiedAt` 이 생성 시각보다 이른 단위 지식이다 — verified 는 누적되는 이력이다 (Q-0064#Q159-a).
    """
    body: list[str] = []
    # 7. 검증 표시 — verified 주체 종류와 검증 뒤 수정 (trust shape)
    kinds = Counter()
    none_n, modified = 0, []
    for c in live:
        vbs = [str(v) for v in g.objects(c, AGT.verifiedBy)]
        if not vbs:
            none_n += 1
        for kind in {("human:" if v.startswith("human:") else "process:" if v.startswith("process:") else v.split("/")[0] + "/" if "/" in v else "기타") for v in vbs}:
            kinds[kind] += 1
        gen_at = as_dt(m.at(c))
        vas = [va for va in (as_dt(str(v)) for v in g.objects(c, AGT.verifiedAt)) if va]
        if gen_at and vas and gen_at > max(vas):
            modified.append(c)
    body += ["## 검증 표시 — 지금 내용을 검증한 `verified` 주체 종류별 살아 있는 단위 지식 수 (한 단위 지식이 여러 종류를 가질 수 있다)", "",
          "| 주체 종류 | 단위 지식 수 |", "|---|---|"] + [f"| `{k}` | {v} |" for k, v in sorted(kinds.items())] + [f"| 없음 (미검증) | {none_n} |", "",
          f"- 검증 뒤 수정(`prov:generatedAtTime` > 가장 늦은 `agt:verifiedAt`): **{len(modified)}** (목표 0 — `agt:TrustShape` 가 게이트에서 강제)", ""]
    return body
```
<!-- 인용 끝 -->
