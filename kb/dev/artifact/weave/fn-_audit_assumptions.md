---
id: https://agentic-knowledge-base.dev/id/chunk/c7c1c9ca-af8e-4435-a2cb-faaa5761faaf
type: artifact
level: executable
title_ko: 함수 _audit_assumptions (tools/weave.py)
title: function _audit_assumptions in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f04e6f3f-7688-4b41-a333-5dd88d484ada, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/f146d0f6-736d-44dc-9acf-ad9f25562d4a
---
**함수** — `_audit_assumptions(m, asm_obs, latest_asm, asm_body)` 다. `kb/dev/memory/` 의 최신 가정 판정 관측 요약 (assume_check).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _audit_assumptions(m: Model, asm_obs: list, latest_asm, asm_body: str) -> list[str]:
    """`kb/dev/memory/` 의 최신 가정 판정 관측 요약 (assume_check)."""
    body: list[str] = []
    # 5. 가정 — 최신 assume_check 관측
    body += ["## 가정 — `kb/dev/memory/` 의 최신 가정 판정 관측 (assume_check)", ""]
    if latest_asm is None:
        body += ["가정 판정 관측 없음 — `bazel run //tools:assume_check -- --record`", ""]
    else:
        rows = observation_table(asm_body, kb_lib.ASSUME_CHECK_TABLE_HEADER)
        states = Counter(r[3] for r in rows if len(r) >= 4)
        body += [f"- {m.ko(latest_asm)} (`{m.location[latest_asm]}`, 생성 {m.at(latest_asm)}) — 가정 판정 관측 전체 {len(asm_obs)}건",
              "- 가정 " + (" · ".join(f"{k} **{v}**" for k, v in sorted(states.items())) or kb_lib.NONE_MARK + " — 본문에 가정 표가 없다"), ""]
        if rows:
            body += ["| 가정 | 판정 유형 | 등급 | 상태 |", "|---|---|---|---|"] + ["| " + " | ".join(r[:4]) + " |" for r in rows] + [""]
    return body
```
<!-- 인용 끝 -->
